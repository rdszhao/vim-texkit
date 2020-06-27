# tmux

function tta {
    tmux attach -t $1
}

# tex management
alias texkit="cd [repo dir]"

function texmodules {
    texkit
    nvim tex_modules.py
}

function sec {
	texkit
    python3 sub.py $1 $2
}

function texedit {
    texkit
    python3 main.py $1
}

function texcompile {
    texkit
    python3 compile.py $1
}

function texclean {
    texkit
    python3 clean.py $1
}

function newtex {
    texkit
    python3 newdir.py $1
}

function texload {
    texkit
    python3 texmux.py $1
    sleep 0.5
    tta tex
}
