_pdbrc_read = None
def _pdbrc_init():
    global _pdbrc_read
    if _pdbrc_read:
        return
    # Save history across sessions
    import os, readline
    histfile = os.path.expanduser("~/.pdb-pyhist")
    try:
        readline.read_history_file(histfile)
    except IOError:
        pass
    import atexit
    atexit.register(readline.write_history_file, histfile)
    readline.set_history_length(-1)
    _pdbrc_read = True

_pdbrc_init()
del _pdbrc_init
