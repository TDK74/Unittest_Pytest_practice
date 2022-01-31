''' content of test_sample.py '''

def func(number):
    ''' a simple add function '''
    return number + 1

def test_answer():
    ''' a simple test function '''
    assert func(3) == 5
