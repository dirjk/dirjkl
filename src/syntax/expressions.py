import re

#here we define the basic parts of the language that are used in more complex statements
state_name = r'([a-zA-Z]+)'
valid_number = r'(([-]?[\d]*)([\.]?[\d]*))'
#here we define more complex inputs
# init_state: (state_name)<-(1,2,3)
#state_init_input is a list of comma separated numbers
state_init_input = r'(()|([^,](('+valid_number + r')|((' + valid_number + r')(([,]{1}' + valid_number + r'))*([^,])))))'
# called by the user to create a new state object.
init_state = re.compile(r'^\(' + state_name + r'\)<-\(' + state_init_input + r'\)$')

# activeSate: stateName([elementName])
#activeState = r'^[\D]*\(\[[\D]*\]\)'
# updateState: ->(...) # any thing goes in the ...
#updateState = r'(->\(.*\))+$'
#fullUpdateState = activeState+updateState

#operations

# act on every element: ([ operations ])
#actOnEveryElement = r'^\(\[.*\]\)$'