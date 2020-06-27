from tex_modules import *

name, cwd, validEntry = processFind()

if not validEntry:
    print(cwd)

else:
    secdir = cwd + '/sections'
    cleanup(secdir)
    texMod(name, cwd)
