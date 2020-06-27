import os
import sys
import tex_modules as tm

status, success = tm.preambleUpdate()
print(status)

if success:
    key = sys.argv[1]

    for root, dirs, files in os.walk(tm.workingPath):
        if key in dirs:
            cwd = tm.makePath(root, key)
            break
    else:
        print('DIR NOT FOUND')

    os.chdir(cwd)
    newdir = key + '_tex'
    makedir = 'mkdir ' + newdir
    os.system(makedir)

    os.chdir(newdir)
    dirs = ['sections', 'figures', 'metafiles']
    cmd = 'mkdir -v '

    for folder in dirs:
        mkdir = cmd + folder
        os.system(mkdir)

    cpv = 'cp -vr '
    filename = key + tm.ext
    newdir = tm.makePath(cwd, newdir)
    src = tm.templates + '/temp.tex'
    dst = tm.makePath(newdir, filename)
    cmd = cpv + src + ' ' + dst
    os.system(cmd)

    tm.linkPreamble(newdir)
