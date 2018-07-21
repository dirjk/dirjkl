import re
#import syntax.syntax as syntax
import syntax.expressions as syntax

def parse(raw):
    #first strip all the whitespace at beginning and end and inbetween
    raw = raw.strip().replace(" ","")
    # is it initializing a state?
    if re.match(syntax.init_state,raw):
        return "derp derp"
    else:
        return "PLEASE ENTER SOME VALID CODE"
    return str(raw)
