''' content of test_class.py '''

class TestClass:
    ''' a simple TestClass '''

    def test_one(self):
        ''' a simple assert function '''
        x = "this"
        assert "h" in x

    def test_two(self):
        ''' a simple assert hasattr function '''
        x = "hello"
        assert hasattr(x, "check")
