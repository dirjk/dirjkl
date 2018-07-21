#! py
import re
import unittest
import src.syntax.expressions as expr

class TestInitStateExpressions(unittest.TestCase):
    def test_state_name(self):
        #must allow upper and lower case letters
        self.assertTrue(re.match(r'^'+expr.state_name+r'$',"alllowercase"))
        self.assertTrue(re.match(r'^'+expr.state_name+r'$',"ALLUPPERCASE"))
        self.assertTrue(re.match(r'^'+expr.state_name+r'$',"mIxEdcaSeS"))
        #must not be an empty string
        self.assertFalse(re.match(r'^'+expr.state_name+r'$',""))
        #cannot container any non-letter characters
        self.assertFalse(re.match(r'^'+expr.state_name+r'$',"890909"))
        self.assertFalse(re.match(r'^'+expr.state_name+r'$',"!*#)@*_&#^"))
        self.assertFalse(re.match(r'^'+expr.state_name+r'$',"*2343sdf"))
        self.assertFalse(re.match(r'^'+expr.state_name+r'$',"asdfsfd2343(((D(Dsdfsd"))
    def test_state_init_input(self):
        #allow for empty input
        self.assertTrue(re.match(r'^'+expr.state_init_input+r'$',""))
        #allow for a single input
        self.assertTrue(re.match(r'^'+expr.state_init_input+r'$',"1"))
        self.assertTrue(re.match(r'^'+expr.state_init_input+r'$',"10"))
        self.assertTrue(re.match(r'^'+expr.state_init_input+r'$',"112093848576768"))
        #must allow for a list of numbers
        self.assertTrue(re.match(r'^'+expr.state_init_input+r'$',"1,2,8883,47"))
        #do not allow leading or trailing commas
        self.assertFalse(re.match(r'^'+expr.state_init_input+r'$',"10,"))
        self.assertFalse(re.match(r'^'+expr.state_init_input+r'$',"10,111,"))
        self.assertFalse(re.match(r'^'+expr.state_init_input+r'$',",10,sdfdsfs"))
        self.assertFalse(re.match(r'^'+expr.state_init_input+r'$',",10,"))
        self.assertFalse(re.match(r'^'+expr.state_init_input+r'$',",10"))

    def testValidInput(self):
        #empty initial state
        self.assertTrue(re.match(expr.init_state,"(state)<-()"))
        #some test inputs        
        self.assertTrue(re.match(expr.init_state,"(state)<-(12312354)"))
        self.assertTrue(re.match(expr.init_state,"(state)<-(123,423478,4564)"))
        self.assertTrue(re.match(expr.init_state,"(state)<-(6,5,3,5,6,7,8,9,9,8,7,6,5,4,3,3,4,5,6,6)"))
    def testStateNameFullParens(self):
        # state name must be in full parens
        self.assertFalse(re.match(expr.init_state,"state<-()"))
        self.assertFalse(re.match(expr.init_state,"(state<-()"))
        self.assertFalse(re.match(expr.init_state,"state)<-()"))
        #there must be a state name invoked
        self.assertFalse(re.match(expr.init_state,"<-()"))
    def test_state_name_only_letters(self):
        # state name must contain atleast one letter and no other characters
        self.assertFalse(re.match(expr.init_state,"()<-()"))
        self.assertFalse(re.match(expr.init_state,"(8)<-()"))
        self.assertFalse(re.match(expr.init_state,"(let*$)<-()"))
        self.assertFalse(re.match(expr.init_state,"(())<-()"))
        self.assertFalse(re.match(expr.init_state,"([])<-()"))
        self.assertFalse(re.match(expr.init_state,""))
        self.assertFalse(re.match(expr.init_state,""))
    def test_state_input_only_numbers(self):
        #state input must contain only a list of numbers
        self.assertFalse(re.match(expr.init_state,"(state))<-(1,m,3)"))
        self.assertFalse(re.match(expr.init_state,"(state))<-(m)"))
        self.assertFalse(re.match(expr.init_state,"(state))<-(***&m,898,1,2,3)"))
        self.assertFalse(re.match(expr.init_state,"(state))<-(12,&&/,l,3)"))


if __name__ == "__main__":
    unittest.main()
