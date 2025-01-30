''' content of test_sysexit.py '''
import pytest

def f_n():
    ''' a simple raise SystemExit function '''
    raise SystemExit(1)

def test_mytest():
    ''' a simple test function '''
    with pytest.raises(SystemExit):
        f_n()
