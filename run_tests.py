import unittest
from tests.homework.h_strings import tests_strings
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.examples.b_input_process_output import tests_input_process_output
suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
from tests.homework.e_functions import tests_functions
suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)