import tex_modules as tm
import sys
import os

name, cwd, validEntry = tm.processFind()
print(cwd)

if validEntry:
    cwd = tm.makePath(cwd, 'sections')
    secnum = sys.argv[2]
    os.chdir(cwd)

    if secnum == 'l':
        secs = []
        secdir = os.walk(cwd)

        for root, dirs, files in secdir:
            for file in files:
                if tm.ext in file:
                    num = int(tm.untex(file))
                    secs.append(num)

        num = max(secs)
        secnum = str(num)

    texName = tm.texify(secnum)
    cmd = 'nvim ' + texName
    print(cmd)

    os.system(cmd)
