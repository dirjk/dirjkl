import re
#import syntax.syntax as syntax
import syntax.expressions as syntax
import oper.operator as ops

def parse(raw_string,states):
    #first strip all the whitespace at beginning and end and inbetween
    raw_string = raw_string.strip().replace(" ","")
    # is it initializing a state?
    if re.fullmatch(syntax.init_state,raw_string):
        return ops.init_new_state(raw_string,states)
    #is it pushing a new element?
    elif re.fullmatch(syntax.full_push_element,raw_string):
        return ops.push_new_element(raw_string,states)
    else:
        return "PLEASE ENTER SOME VALID CODE"
    return str(raw_string)
