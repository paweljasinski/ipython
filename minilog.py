import os
import threading

def log(log):
    _lock.acquire()
    _log.write("\n----" + threading.current_thread().name + "----\n")
    _log.write(log)
    _log.flush()
    _lock.release()

_fname="c:/cygwin64/tmp/minilog-%d.log" % os.getpid()
_lock = threading.Lock()
try:
    os.remove(_fname)
except OSError:
    pass
_log=open(_fname, "a")
