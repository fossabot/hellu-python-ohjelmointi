import importlib
import sys

_stdout_pointer = 0

def load_module(pkg, lang='en'):
    module_not_found = '{0} does not exist!'.format(pkg)
    other_exception = 'Running exercise {0} failed. Please make sure that you can run your code.'.format(pkg)
    exit_called = 'Make sure your program does not exit with an exit() command.'
    if lang == 'fi':
        module_not_found = 'Tehtävätiedostoa {0} ei löytynyt.'.format(pkg)
        other_exception = 'Tehtävän {0} suorittaminen epäonnistui. '.format(pkg) + 'Varmista, että saat ohjelman suoritettua loppuun.'
        exit_called = 'Varmista, että koodisi ei kutsu exit() komentoa.'
    try:
        return importlib.import_module(pkg)
    except ModuleNotFoundError:
        return AssertionError(module_not_found)
    except Exception:
        return AssertionError(other_exception)
    except SystemExit:
        return AssertionError(exit_called)

def load(pkg, method, lang='en', err=None):
    module_not_found = '{0}.{1} does not exist!'.format(pkg, method)
    if lang == 'fi':
        module_not_found = 'Tehtävätiedostoa {0}.{1} ei löytynyt.'.format(pkg, method)

    if not err:
        err = module_not_found

    def fail(*args, **kwargs):
        raise AssertionError(err)

    try:
        return getattr(importlib.import_module(pkg), method)
    except Exception:
        return fail

def reload_module(module):
    global _stdout_pointer
    if isinstance(module, AssertionError):
        raise module
    _stdout_pointer = len(sys.stdout.getvalue())
    importlib.reload(module)

def get_stdout():
    global _stdout_pointer
    return sys.stdout.getvalue()[_stdout_pointer:].strip()

def get_stderr():
    return sys.stderr.getvalue().strip()


def any_contains(needle, haystacks):
    any(map(lambda haystack: needle in haystack, haystacks))
