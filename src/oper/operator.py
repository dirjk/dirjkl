def init_new_state(raw_string,states):
    # takes in the global states variable that contains all the states
    # takes in a raw input string from the user (that has been validated by syntax.parser)
    # updates the globabl states by initing and adding a new state according to the passed in raw string
    name = raw_string[1:].split(")")[0]
    elements = raw_string.split("<-(")[1][:-1].split(",")
    #does this state already exist?    
    if name in states.keys():
        return "ERROR: "+name+" ALREADY EXISTS AS A STATE."
    else:
        if len(elements) == 1 and len(elements[0]) == 0:
            states[name] = []
        elif len(elements) > 0:
            states[name] = [float(e) for e in elements]
        else:
            states[name] = []
    return name+" is now "+ str(states[name])