def init_new_state(raw_string,states):
    # takes in the global states variable that contains all the states
    # takes in a raw input string from the user (that has been validated by syntax.parser)
    # updates the globabl states by initing and adding a new state according to the passed in raw string
    name = raw_string[1:].split(")")[0]
    #does this state already exist?    
    if name in states.keys():
        return "ERROR: '"+name+"' ALREADY EXISTS AS A STATE."
    elements = raw_string.split("<-(")[1][:-1].split(",")
    if len(elements) == 1 and len(elements[0]) == 0:
        states[name] = []
    elif len(elements) > 0:
        states[name] = [float(e) for e in elements]
    else:
        states[name] = []
    return name+" is now "+ str(states[name])

def push_new_element(raw_string, states):
    # takes in the global states variable that contains all the states
    # takes in a raw input string from the user (that has been validated by syntax.parser)
    # updates the globabl states by pushing an element to the specified state.
    state_name = raw_string.split('(')[0]
    if state_name not in states.keys():
        return "ERROR: '" +state_name+ "' DOES NOT EXIST AS A STATE."
    active_state = states[state_name]
    ops = raw_string.replace("(","").replace(")","").split('->')[1:][0]
    pipe_count = ops.count("|")
    if pipe_count == 1:
        #special notation
        if ops[0] == "|":
            element = float(ops.split("|")[1])
            loc = len(active_state)
        else:
            element = float(ops.split("|")[0])
            loc = 0        
    elif pipe_count == 2:
        #regular notation
        element = float(ops.split("|")[1])
        loc = int(ops.split("|")[2])
        if loc < 0:
            #here we need to adjust for negative indexes to work as expected with python's list.insert() indexes.
            print('original loc',loc)
            alen = len(active_state)
            mod_loc = loc % -(alen + 1)
            print('mod loc',mod_loc)
            if mod_loc == 0:
                loc = mod_loc
            else:
                loc = (alen + 1) + mod_loc
            print('updated loc',loc)
    else:
        #error state:
        return "ERROR: malformed push element statement. too many pipes?"
    active_state.insert(loc,element)
    states[state_name] = active_state
    return state_name +" is now "+str(states[state_name])