import unittest
import src.oper.operator as ops

class Test_push_new_element(unittest.TestCase):
    def test_state_must_exist(self):
        input_string = "stateName()->(|4)"
        orig_states = {
            "otherState":[]
        }
        expected_states = {
            "otherState":[]
        }
        ops.push_new_element(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_push_element_to_front(self):
        input_string = "stateName()->(6|)"
        orig_states = {
            "stateName":[1.0,2.0,3.0]
        }
        expected_states = {
            "stateName":[6.0,1.0,2.0,3.0]
        }
        ops.push_new_element(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_push_element_to_back(self):
        input_string = "stateName()->(|6)"
        orig_states = {
            "stateName":[1.0,2.0,3.0]
        }
        expected_states = {
            "stateName":[1.0,2.0,3.0,6.0]
        }
        ops.push_new_element(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_push_element_at_location(self):
        input_string = "stateName()->(|6|2)"
        orig_states = {
            "stateName":[1.0,2.0,3.0,4.0]
        }
        expected_states = {
            "stateName":[1.0,2.0,6.0,3.0,4.0]
        }
        ops.push_new_element(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_push_element_at_neg_location(self):
        input_string = "stateName()->(|6|-2)"
        orig_states = {
            "stateName":[1.0,2.0,3.0,4.0]
        }
        expected_states = {
            "stateName":[1.0,2.0,3.0,6.0,4.0]
        }
        ops.push_new_element(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_push_element_at_out_of_bounds_location(self):
        # should do a wrap and insert the element at (n % length).
        input_string = "stateName()->(|6|9)"
        orig_states = {
            "stateName":[1.0,2.0,3.0,4.0]
        }
        expected_states = {
            "stateName":[1.0,2.0,3.0,4.0,6.0]
        }
        ops.push_new_element(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_push_element_at_out_of_bounds_neg_location(self):
        # should do a wrap and insert the element properly
        input_string = "stateName()->(|6|-7)"
        orig_states = {
            "stateName":[1.0,2.0,3.0,4.0]
        }
        expected_states = {
            "stateName":[1.0,2.0,3.0,6.0,4.0]
        }
        ops.push_new_element(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)