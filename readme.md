TEXKIT LIB:

DEPENDENCIES: send2trash, libtmux (if using tmux)

*tmux is highly recommended to ensure a smoother experience*

These functions will only work if your .tex directories are
structured as such:

'''bash
[dir storing main texfile]
.
├── MATH010B.pdf
├── MATH010B.tex
├── metafiles
│   ├── MATH010B.aux
│   └── MATH010B.fdb_latexmk
├── preamble.tex -> /Users/raymondzhao/Documents/Projects/toolkit/tex/template/preamble.tex
└── sections
    ├── 1.tex
    ├── 2.tex
    ├── 3.tex
    ├── 4.tex
    ├── 5.tex
    └── 6.tex
'''

key being ideally sub/input files should be stored in a separate
'sections' folder to keep things clean

Also, the compile.py command is useful occasionally when I need to
compile in a pinch but the best thing to do usually is to just use
the built in latexmk continuous compilation that's built into
vimtex.
