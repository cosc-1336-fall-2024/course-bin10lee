import unittest
from tests.homework.g_lists_and_tuples import tests_lists_and_tuples
#from tests.homework.c_decisions import tests_decisions #replace tests_in_proc_out with tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
from tests.homework.e_functions import tests_functions
suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
unittest.TextTestRunner(verbosity=2).run(suite)

