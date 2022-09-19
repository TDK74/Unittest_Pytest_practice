''' For testing of read_print.py '''
import sys
import unittest

from unittest import mock
from unittest.mock import MagicMock

from read_print import read_input, print_input


class TestReadPrint(unittest.TestCase):
    ''' a simple class for testing of read print '''

    def test_read_input(self):
        ''' a simple test read function '''
        with mock.patch('builtins.input', return_value='test'):
            assert read_input() == 'test'

    @mock.patch('builtins.input', lambda *args: 'test')
    def test_read_input1(self):
        ''' a simple test read function '''
        assert read_input() == 'test'

    @mock.patch('builtins.input', return_value='test')
    def test_read_input2(self, mock_input):
        ''' a simple test read function '''
        assert read_input() == 'test'
        assert mock_input.call_count == 1
        assert mock_input.called

    def test_read_input3(self):
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'test'
            assert read_input() == 'test'

    def test_read_input4(self):
        mock_input = MagicMock(return_value = 'test')
        with mock.patch('builtins.input', mock_input):
            assert read_input() == 'test'

    def test_print_input(self):
        ''' a simple test print function '''
        with mock.patch('builtins.print') as mock_print:
            print_input('test')

            mock_print.assert_called_with('test')
            mock_print.assert_called_once_with('test')
            mock_print.assert_called_once
            mock_print.assert_called

    @mock.patch('builtins.print')
    def test_print_input1(self, mock_print):
        ''' a simple test print function '''
        print_input('test')

        mock_print.assert_called_with('test')
        mock_print.assert_called_once_with('test')
        mock_print.assert_called_once
        mock_print.assert_called

    def test_print_input2(self):
        ''' a simple test print function '''
        mock_print = MagicMock(print_value = 'test')

        with mock.patch('builtins.print', mock_print):
            print_input('test')

            mock_print.assert_called_with('test')
            mock_print.assert_called_once_with('test')
            mock_print.assert_called_once()
            mock_print.assert_called

    def test_print_input3(self):
        with mock.patch('builtins.print') as mock_print:
            print_input('test')
            mock_print.return_value = 'test'
            
            mock_print.assert_called_with('test')
            mock_print.assert_called_once_with('test')
            mock_print.assert_called_once()
            mock_print.assert_called

if __name__ == '__main__':
    unittest.main(testRunner = unittest.TextTestRunner(verbosity = 5, stream = sys.stdout))
