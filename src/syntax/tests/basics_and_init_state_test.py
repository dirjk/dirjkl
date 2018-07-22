#! py
import re
import unittest
import src.syntax.expressions as expr

class TestInitStateExpressions(unittest.TestCase):
    def test_state_name(self):
        #must allow upper and lower case letters
        self.assertTrue(re.fullmatch(expr.state_name,"alllowercase"))
        self.assertTrue(re.fullmatch(expr.state_name,"ALLUPPERCASE"))
        self.assertTrue(re.fullmatch(expr.state_name,"mIxEdcaSeS"))
        #must not be an empty string
        self.assertFalse(re.fullmatch(expr.state_name,""))
        #cannot container any non-letter characters
        self.assertFalse(re.fullmatch(expr.state_name,"890909"))
        self.assertFalse(re.fullmatch(expr.state_name,"!*#)@*_&#^"))
        self.assertFalse(re.fullmatch(expr.state_name,"*2343sdf"))
        self.assertFalse(re.fullmatch(expr.state_name,"asdfsfd2343(((D(Dsdfsd"))
    def test_valid_number(self):
        #must allow integers
        self.assertTrue(re.fullmatch(expr.valid_number,"1234"))
        #must allow negative integers
        self.assertTrue(re.fullmatch(expr.valid_number,"-123"))
        #must allow floats and negative floats
        self.assertTrue(re.fullmatch(expr.valid_number,"12.345"))
        self.assertTrue(re.fullmatch(expr.valid_number,".345"))
        self.assertTrue(re.fullmatch(expr.valid_number,"-.345"))
        self.assertTrue(re.fullmatch(expr.valid_number,"-877.345"))
        self.assertTrue(re.fullmatch(expr.valid_number,"12."))
        self.assertTrue(re.fullmatch(expr.valid_number,"-12."))
        #must not contain letters or special characters
        self.assertFalse(re.fullmatch(expr.valid_number,"asd"))
        self.assertFalse(re.fullmatch(expr.valid_number,"(*&())"))
        self.assertFalse(re.fullmatch(expr.valid_number,"12,123"))
    def test_state_init_input(self):
        #allow for empty input
        self.assertTrue(re.fullmatch(expr.state_init_input,""))
        #allow for a single input
        self.assertTrue(re.fullmatch(expr.state_init_input,"1"))
        self.assertTrue(re.fullmatch(expr.state_init_input,"10"))
        self.assertTrue(re.fullmatch(expr.state_init_input,"112093848576768"))
        #must allow for a list of numbers
        self.assertTrue(re.fullmatch(expr.state_init_input,"1,2,8883,47"))
        #do not allow leading or trailing commas
        self.assertFalse(re.fullmatch(expr.state_init_input,"10,"))
        self.assertFalse(re.fullmatch(expr.state_init_input,"10,111,"))
        self.assertFalse(re.fullmatch(expr.state_init_input,",10,sdfdsfs"))
        self.assertFalse(re.fullmatch(expr.state_init_input,",10,"))
        self.assertFalse(re.fullmatch(expr.state_init_input,",10"))
        #allow for negative and floats
        self.assertTrue(re.fullmatch(expr.state_init_input,"1.0"))
        self.assertTrue(re.fullmatch(expr.state_init_input,"-1"))
        self.assertTrue(re.fullmatch(expr.state_init_input,"-1,1.0"))
        self.assertTrue(re.fullmatch(expr.state_init_input,"-1,-2.0"))

    def testValidInput(self):
        #empty initial state
        self.assertTrue(re.fullmatch(expr.init_state,"(state)<-()"))
        #some test inputs        
        self.assertTrue(re.fullmatch(expr.init_state,"(state)<-(12312354)"))
        self.assertTrue(re.fullmatch(expr.init_state,"(state)<-(123,423478,4564)"))
        self.assertTrue(re.fullmatch(expr.init_state,"(state)<-(6,5,3,5,6,7,8,9,9,8,7,6,5,4,3,3,4,5,6,6)"))
    def testStateNameFullParens(self):
        # state name must be in full parens
        self.assertFalse(re.fullmatch(expr.init_state,"state<-()"))
        self.assertFalse(re.fullmatch(expr.init_state,"(state<-()"))
        self.assertFalse(re.fullmatch(expr.init_state,"state)<-()"))
        #there must be a state name invoked
        self.assertFalse(re.fullmatch(expr.init_state,"<-()"))
    def test_state_name_only_letters(self):
        # state name must contain atleast one letter and no other characters
        self.assertFalse(re.fullmatch(expr.init_state,"()<-()"))
        self.assertFalse(re.fullmatch(expr.init_state,"(8)<-()"))
        self.assertFalse(re.fullmatch(expr.init_state,"(let*$)<-()"))
        self.assertFalse(re.fullmatch(expr.init_state,"(())<-()"))
        self.assertFalse(re.fullmatch(expr.init_state,"([])<-()"))
        self.assertFalse(re.fullmatch(expr.init_state,""))
        self.assertFalse(re.fullmatch(expr.init_state,""))
    def test_state_input_only_numbers(self):
        #state input must contain only a list of numbers
        self.assertFalse(re.fullmatch(expr.init_state,"(state))<-(1,m,3)"))
        self.assertFalse(re.fullmatch(expr.init_state,"(state))<-(m)"))
        self.assertFalse(re.fullmatch(expr.init_state,"(state))<-(***&m,898,1,2,3)"))
        self.assertFalse(re.fullmatch(expr.init_state,"(state))<-(12,&&/,l,3)"))


if __name__ == "__main__":
    unittest.main()
