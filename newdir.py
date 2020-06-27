from tex_modules import *

status, success = preambleUpdate()
print(status)

if success:
    key = sys.argv[1]

    for root, dirs, files in os.walk(workingPath):
        if key in dirs:
            cwd = makePath(root, key)
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
    filename = key + ext
    newdir = makePath(cwd, newdir)
    src = templates + '/temp.tex'
    dst = makePath(newdir, filename)
    cmd = cpv + src + ' ' + dst
    os.system(cmd)

    linkPreamble(newdir)
