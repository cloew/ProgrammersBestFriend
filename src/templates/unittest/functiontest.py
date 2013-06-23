
class %functionToTest%(unittest.TestCase):
    """ Test cases of %functionToTest% """
    
    def  setUp(self):
        """ Build the *** for the test """
        
    def caseToTest(self):
        """ Test that ... """

# Collect all test cases in this class
testcases%FunctionToTest% = ["caseToTest"]
suite%FunctionToTest% = unittest.TestSuite(map(%functionToTest%, testcases%FunctionToTest%))

##########################################################
