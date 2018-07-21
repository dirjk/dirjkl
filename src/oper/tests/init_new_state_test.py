import unittest
import src.oper.operator as ops

class Test_init_new_state(unittest.TestCase):
    def test_inits_new_state_with_input(self):
        input_string = "(test)<-(1,2,3)"
        orig_states = {}
        expected_states = {
            "test":[1.0,2.0,3.0]
        }
        ops.init_new_state(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_inits_new_state_with_empty_input(self):
        input_string = "(test)<-()"
        orig_states = {}
        expected_states = {
            "test":[]
        }
        ops.init_new_state(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_do_not_init_if_state_exists(self):
        input_string = "(test)<-()"
        orig_states = {
            "test":[1.4,3.56,0.0]
        }
        expected_states = {
            "test":[1.4,3.56,0.0]
        }
        ops.init_new_state(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_do_not_overwrite_if_state_exists(self):
        input_string = "(test)<-(1,2,3,4)"
        orig_states = {
            "test":[]
        }
        expected_states = {
            "test":[]
        }
        ops.init_new_state(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)
    def test_init_if_different_capitalization(self):
        input_string = "(test)<-(1,2,3,4)"
        orig_states = {
            "TEST":[]
        }
        expected_states = {
            "TEST":[],
            "test":[1.0,2.0,3.0,4.0]
        }
        ops.init_new_state(input_string,orig_states)
        self.assertDictEqual(orig_states,expected_states)