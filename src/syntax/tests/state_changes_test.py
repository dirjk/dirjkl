#! py
import re
import unittest
import src.syntax.expressions as expr

class Test_state_changes(unittest.TestCase):
    def test_begin_state_changes(self):
        #must allow properly formatted input
        self.assertTrue(re.fullmatch(expr.begin_state_change,"stateName()"))
        self.assertTrue(re.fullmatch(expr.begin_state_change,"stateName()"))
        #must not allow empty input
        self.assertFalse(re.fullmatch(expr.begin_state_change,""))
        #must have a state name and parens
        self.assertFalse(re.fullmatch(expr.begin_state_change,"()"))
        self.assertFalse(re.fullmatch(expr.begin_state_change,"a"))
        self.assertFalse(re.fullmatch(expr.begin_state_change,"a("))
        self.assertFalse(re.fullmatch(expr.begin_state_change,"a)"))
        #must be properly ordered
        self.assertFalse(re.fullmatch(expr.begin_state_change,"()aa"))
        self.assertFalse(re.fullmatch(expr.begin_state_change,"a()aa()"))
        self.assertFalse(re.fullmatch(expr.begin_state_change,"()a()"))
        #must not allow numbers and such
        self.assertFalse(re.fullmatch(expr.begin_state_change,"9889()"))
    def test_push_element(self):
        #must allow properly formatted input
        self.assertTrue(re.fullmatch(expr.state_change_push,"->(|4)"))
        self.assertTrue(re.fullmatch(expr.state_change_push,"->(76|)"))
        self.assertTrue(re.fullmatch(expr.state_change_push,"->(|76|5)"))
        #must not allow missing or malformed params
        self.assertFalse(re.fullmatch(expr.state_change_push,"->()"))
        self.assertFalse(re.fullmatch(expr.state_change_push,"->(852)"))
        self.assertFalse(re.fullmatch(expr.state_change_push,"->(|)"))
        self.assertFalse(re.fullmatch(expr.state_change_push,"->(||)"))
        self.assertFalse(re.fullmatch(expr.state_change_push,"->(||435)"))
        self.assertFalse(re.fullmatch(expr.state_change_push,"->(|444|)"))
        self.assertFalse(re.fullmatch(expr.state_change_push,"->(848||)"))
    def test_full_push_element(self):
        #must allow for properly formatted input
        self.assertTrue(re.fullmatch(expr.full_push_element,"stateName()->(848|)"))
        self.assertTrue(re.fullmatch(expr.full_push_element,"stateName()->(|848)"))
        self.assertTrue(re.fullmatch(expr.full_push_element,"stateName()->(|848|3)"))



if __name__ == "__main__":
    unittest.main()
