import re
#import syntax.syntax as syntax
import syntax.expressions as syntax
import oper.operator as ops

def parse(raw_string,states):
    #first strip all the whitespace at beginning and end and inbetween
    raw_string = raw_string.strip().replace(" ","")
    first_char = raw_string[0]
    if first_char == '(':
        # is it initializing a state?
        if re.fullmatch(syntax.init_state,raw_string):
            return ops.init_new_state(raw_string,states)
        else:
            return "ERROR: INVALID INIT STATE CMD."
    elif first_char == '{':
        #is it initializing a chain?
        return "CHAIN INIT NOT YET IMPLEMENTED"
    elif first_char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        operations = raw_string.split('->')
        if len(operations) <=1:
            return "ERROR: MALFORMED OPERATIONS CMD: MISSING OPERATION."
        elif re.fullmatch(syntax.begin_state_change,operations[0]):
            #start parsing the operations
            parsed_ops = []
            active_state = None
            for i in range(len(operations)-2):
                op = parseOps(operations[i],operations[i+1],active_state)
                if not op['valid']:
                    return "ERROR: MALFORMED OPERATIONS CMD."
                active_state = op['stateName']
                parsed_ops.append(op)
            #TODO: here is where the new operator function will need to be called
            #that handles the new syntax parsing objects.
            #if re.fullmatch(syntax.full_push_element,raw_string):
                #is it pushing a new element?
            #    return ops.push_new_element(raw_string,states)
            if len(parsed_ops) > 0:
                return str(parsed_ops)
            else:
                return "ERROR: UNRECOGNIZED OPERATIONS CMD."
        else:
            return "ERROR: MALFORMED OPERATIONS CMD: ACTIVATE STATE."
    else:
        return "PLEASE ENTER SOME VALID CODE"
    return str(raw_string)

def parseOps(cur,nxt,active_state=None):
    # takes in two strings, cur and nxt, and checks their validity.
    # if valid, finds out the type of operation that is being attempted.
    # returns a dict the following values:
    # valid: boolean
    # stateName: string or None
    # stateLoad: cur or None
    # stateAppy: next or None
    # type: string or None
    returnThis = {
        'valid':False,
        'stateName':None,
        'stateLoad':None,
        'stateApply':None,
        'type':None
    }
    if cur == None or nxt == None:
        return returnThis
    if active_state == None:
        #if no active_state is passed in, its the first operation that is loading the state.
        if re.fullmatch(syntax.begin_state_change,cur):
            #here we figure out what the active state is supposed to be        
            state_name = cur.split('(')[0]
            if active_state != None:
                #they passed in an active state.
                if len(state_name) != 0:
                    #can't load a fresh state and pass in an active state.
                    return returnThis
                else:
                    returnThis['stateName'] = active_state
            elif state_name != None and len(state_name) > 0:
                returnThis['stateName'] = state_name
            else:
                #error condition.
                return returnThis
            #finally we save the loading state string for future use.
            returnThis['stateLoad'] = cur
        else:
            #doesn't match the regex for loading states.
            return  returnThis
    else:
        op_type = determine_ops_type(cur)
        if op_type != None:
            returnThis['stateName'] = active_state
            returnThis['stateLoad'] = cur
        else:
            #not a valid operation.
            return returnThis
    #so we've got the first part, state load, done. what about the second part?
    second_op_type = determine_ops_type(nxt)
    if second_op_type != None:
        returnThis['stateApply'] = nxt
        returnThis['type'] = second_op_type
    else:
        #error or unrecognized op type.
        #make sure to set the statename parts back to None.
        returnThis['stateLoad'] = None
        returnThis['stateName'] = None
        return returnThis
    #finally, after everything is finished, we set to valid and return.
    returnThis['valid'] = True
    return returnThis

def determine_ops_type(ops):
    #takes in a string, ops, and determines which type it is.
    #returns a string or None if no match.
    if re.fullmatch(syntax.state_change_just_push,ops):
        return 'OP_TYPE_PUSH'
    return None