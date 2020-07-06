import os
import sys
import tex_modules as tm

name, cwd, validEntry = tm.processFind()

if validEntry:
    secpath = tm.makePath(cwd, 'sections')
    os.chdir(secpath)

    secnum = sys.argv[2]
    new = 'n'

    if new not in secnum:
        try:
            sec_int = int(secnum)
        except ValueError:
            print('invalid option')
            sec_int = -1

    if new in secnum or sec_int < 0:
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

        if sec_int < 0:
            if num > 1:
                num -= sec_int + 1

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
    os.system(cmd)
