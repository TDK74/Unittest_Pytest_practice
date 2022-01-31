''' content of read_print.py '''

def read_input():
    ''' a simple read input function '''
    # for mock testing
    # my_input = input()
    my_input = 5
    return my_input

def print_input(my_input):
    ''' a simple print input function '''
    # for mock testing
    my_input = 5
    print(my_input)

def test_read_input():
    ''' a simple test read function '''
    # for mock testing
    # source: https://docs.python.org/3/library/unittest.mock.html
    # m = MagicMock()
    # p = PropertyMock(return_value=5)
    # type(m).foo = p
    # m.foo
    # foo <--> read_input() ?!
    test_input = 5
    assert read_input() == test_input

def test_print_input():
    ''' a simple test print function '''
    test_input = 5
    #test_input = None
    #assert print_input(read_input()) == test_input
    assert print_input(5) == test_input
    #assert print_input(test_input) is None
