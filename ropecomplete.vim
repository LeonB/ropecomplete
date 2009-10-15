if !has('python')
    echo "Error: Required vim compiled with +python"
    finish
endif

"function! LoadRopeCompletion()

python << EOF
import sys
sys.path.append('./')
sys.path.append('/home/leon/Workspaces/ropecomplete/')
import ropecomplete
completer = ropecomplete.Completer()
EOF

"endfunction

"call LoadRopeCompletion()

function! ropecomplete#Complete(findstart, base)
python << EOF
findstart = int(vim.eval("a:findstart"))
base = vim.eval("a:base")
vim.command("return %s" % completer(findstart, base))
EOF
endfunction 
