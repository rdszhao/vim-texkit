import sys
import os
import re
# from send2trash import send2trash

def trash(path):
    # using os.remove is really really risky since it permanently
    # deletes. use send2trash.
    # can't currently use send2trash on my own machine since
    # there are version issues with the big sur beta
    os.remove(path)
    # send2trash(path)


def makePath(root, file):
    return root + '/' + file


ext = '.tex'
ints = re.compile(r"\d+")
workingPath = '/Users/raymondzhao/Documents'
texkit = workingPath + '/Projects/toolkit/tex'
templates = texkit + '/template'
preamble = 'preamble.tex'


def texify(name):
    return name + ext


def untex(fname):
    name, etn = fname.split('.')
    return name


def preamblePath():
    texPath = os.walk(texkit)

    for root, dirs, files in texPath:
        for file in files:

            if preamble in file:
                pname = makePath(root, file)
                return pname, True

    else:
        return 'PREAMBLE NOT FOUND', False


prbPath, prbFound = preamblePath()


def linkPreamble(path):
    dst = makePath(path, preamble)
    trash(dst)
    newlink = 'ln -s ' + prbPath + ' ' + dst

    os.system(newlink)
    print(dst)


def preamblate():
    for root, dirs, files in os.walk(workingPath):

        for file in files:

            isSub = ints.match(file)
            if ext in file and 'preamble' not in file and not isSub:

                os.chdir(root)
                with open(file, 'r') as tex:

                    texin = tex.read()
                    if 'preamble' in texin:
                        linkPreamble(root)


def preambleUpdate():
    if not prbFound:
        return prbPath, prbFound

    print('\nUPDATING PREAMBLES\n')

    for root, dirs, files in os.walk(workingPath):
        for file in files:

            if preamble in file and 'toolkit' not in root:
                linkPreamble(root)

    return '\nDONE\n', prbFound


def processFind(path=workingPath):
    filename = sys.argv[1]
    if '.' not in filename:
        filename = texify(filename)

    for root, dirs, files in os.walk(path):
        if filename in files:
            return filename, root, True

    else:
        return filename, 'lmao kill yourself', False


# behavior can be extremely squirrely if there .files for any
# reason in the same folder as the subfiles
def cleanup(path):
    os.chdir(path)
    for root, dirs, files in os.walk(path):

        print('\nREMOVING BLANK FILES')
        for file in files:
            pname = makePath(root, file)
            if os.stat(pname).st_size == 0:
                trash(pname)
                print(file)

    for root, dirs, files in os.walk(path):

        print('\nREORDERING EXISTING FILES')
        itr = 0
        for file in sorted(files):
            if ext in file:
                itr += 1
                name = str(itr) + ext

                src = makePath(root, file)
                dst = makePath(root, name)

                os.rename(src, dst)
                print(name)


def texMod(name, path):
    os.chdir(path)

    with open(name, 'r') as file:
        tex = file.readlines()
        inputs = re.compile(r'{\d+\}')
        counter = 0
        newtex = []

        for line in tex:

            if inputs.search(line) is not None:
                counter += 1

            revision = '{' + str(counter) + '}'
            newtex.append(inputs.sub(revision, line))

    with open(name, 'w') as out:
        out.writelines(newtex)
