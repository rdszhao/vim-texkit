import os
import sys
import tex_modules as tm

name, cwd, validEntry = tm.processFind()
print(cwd)

if validEntry:
    secpath = tm.makePath(cwd, 'sections')
    os.chdir(secpath)

    secnum = sys.argv[2]
    exOptions = ['l', 'n']

    if secnum in exOptions:
        secs = []
        secdir = os.walk(secpath)

        for root, dirs, files in secdir:
            for file in files:
                if tm.ext in file:
                    num = int(tm.untex(file))
                    secs.append(num)

        num = max(secs)

        if 'n' in secnum:
            os.chdir(cwd)

            with open(name, 'r') as file:
                tex = file.readlines()
                inSpot = '{' + str(num) + '}'
                newtex = []

                for line in tex:
                    if inSpot in line:
                        num += 1
                        extraLine = '\input{' + str(num) + '}\n'
                        newtex.append(line)
                        newtex.append(extraLine)
                    else:
                        newtex.append(line)

            with open(name, 'w') as out:
                out.writelines(newtex)

        secnum = str(num)

    os.chdir(secpath)
    texName = tm.texify(secnum)
    cmd = 'nvim ' + texName
    print(cmd)

    os.system(cmd)
