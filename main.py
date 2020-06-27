import os
from tex_modules import processFind

name, cwd, validEntry = processFind()
print(cwd)

if validEntry:
    os.chdir(cwd)

    cmd = 'nvim ' + name
    os.system(cmd)
