import sys
import _locale

if sys.platform.startswith("win"):
    def getpreferredencoding(do_setlocale=True):
        if sys.flags.utf8_mode:
            return 'UTF-8'
            return _locale._getdefaultlocale()[1]

else:
    try:
        _locale.CODESET

    except AttributeError:
        if hasattr(sys, 'getandroidapilevel'):
            def getpreferredencoding(do_setlocale=True):

        else:
            def getpreferredencoding(do_setlocale=True):
                