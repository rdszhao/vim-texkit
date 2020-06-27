from tex_modules import processFind, untex
import os

name, cwd, validEntry = processFind()
print(cwd)

if validEntry:
    os.chdir(cwd)

    pdfname = untex(name) + '.pdf'
    ocmd = 'open ' + pdfname
    lcmd = 'latexmk -auxdir=metafiles -pvc -pdf ' + name

    os.system(ocmd)
    os.system(lcmd)
