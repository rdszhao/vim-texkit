import os
import sys
import tex_modules as tm

name, cwd, validEntry = tm.processFind()
print(cwd)

if validEntry:
    secpath = tm.makePath(cwd, 'sections')
    os.chdir(secpath)

    secnum = sys.argv[2]
    exOptions = ['l', 'n', 's']

    if secnum in exOptions:
        secs = []
        secdir = os.walk(secpath)

        for root, dirs, files in secdir:
            for file in files:
                if tm.ext in file:
                    num = int(tm.untex(file))
                    secs.append(num)

        if not secs:
            num = 0
        else:
            num = max(secs)

        if 's' in secnum:
            if num > 1:
                num -= 1

        elif 'n' in secnum:
            os.chdir(cwd)

            with open(name, 'r') as file:
                tex = file.readlines()

                if num == 0:
                    inSpot = 'maketitle'
                else:
                    inSpot = '{' + str(num) + '}'

                newtex = []

                for line in tex:
                    newtex.append(line)
                    if inSpot in line:
                        num += 1
                        extraLine = '\n\input{' + str(num) + '}\n'
                        newtex.append(extraLine)

            with open(name, 'w') as out:
                out.writelines(newtex)

        secnum = str(num)

    os.chdir(secpath)
    texName = tm.texify(secnum)
    cmd = 'nvim ' + texName
    print(cmd)

    os.system(cmd)
