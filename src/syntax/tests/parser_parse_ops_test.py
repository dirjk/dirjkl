#! py
import re
import unittest
import src.syntax.expressions as expr
import src.syntax.parser as parser

class Test_parse_ops(unittest.TestCase):
    def test_invalid_state_load_input(self):
        result = parser.parseOps(None,"(|2)")
        self.assertEqual(result['valid'],False)
        result = parser.parseOps("",'(|2)')
        self.assertEqual(result['valid'],False)
        result = parser.parseOps("(one)",'(|2)')
        self.assertEqual(result['valid'],False)
        result = parser.parseOps("()one",'(|2)')
        self.assertEqual(result['valid'],False)
        result = parser.parseOps("one",'(|2)')
        self.assertEqual(result['valid'],False)
        result = parser.parseOps("()",'(|2)')
        self.assertEqual(result['valid'],False)
        result = parser.parseOps("one)",'(|2)')
        self.assertEqual(result['valid'],False)
        result = parser.parseOps("one(",'(|2)')
        self.assertEqual(result['valid'],False)
        result = parser.parseOps("one()",'(|2)','two')
        self.assertEqual(result['valid'],False)
    def test_full_push_element(self):
        #must allow for properly formatted input
        test_op_one = "one()"
        test_op_two = "(|4)"
        expectedResult = {
            'valid':True,
            'stateName':"one",
            'stateLoad':test_op_one,
            'stateApply':test_op_two,
            'type':"OP_TYPE_PUSH"
        }
        self.assertDictEqual(parser.parseOps(test_op_one,test_op_two),expectedResult)
        test_op_three = "(66|)"
        expectedResult['stateApply'] = test_op_three
        self.assertDictEqual(parser.parseOps(test_op_one,test_op_three),expectedResult)
        test_op_four = "(|10|3)"
        expectedResult['stateApply'] = test_op_four
        self.assertDictEqual(parser.parseOps(test_op_one,test_op_four),expectedResult)
if __name__ == "__main__":
    unittest.main()
