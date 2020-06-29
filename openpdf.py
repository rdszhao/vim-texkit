from tex_modules import processFind, untex
import os

name, cwd, validEntry = processFind()
print(cwd)

if validEntry:
    os.chdir(cwd)

    pdfname = untex(name) + '.pdf'
    ocmd = 'open ' + pdfname

    os.system(ocmd)
