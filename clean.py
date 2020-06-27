import tex_modules as tm
import os

name, cwd, validEntry = tm.processFind()

if not validEntry:
    print(cwd)

else:
    secdir = cwd + '/sections'
    tm.cleanup(secdir)
    tm.texMod(name, cwd)
