import libtmux
import sys

subj = sys.argv[1]
name = 'tex'
sname = '[' + name + ']'

server = libtmux.Server()

if not server.has_session(name):
    print('creating session' + sname + '\n')
    session = server.new_session(
        session_name=name,
        kill_session=False,
        attach=False,
        start_directory=None,)

else:
    session = server.find_where({'session_name': name})
    print('session' + sname + ' already found\n')

numWin = 3
newWindows = session.list_windows()
shSize = len(newWindows)
winLeft = numWin - shSize

for i in range(winLeft):
    session.new_window(attach=False)

newWindows = session.list_windows()

sec = 'sec ' + subj + ' l'
main = 'texedit ' + subj
cmds = [sec, main]

for action, window in zip(cmds, newWindows):
    for pane in window.list_panes():
        pane.send_keys(action, enter=True)
