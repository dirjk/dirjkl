import re

#here we define the basic parts of the language
state_name = r'[a-zA-Z]+'
state_init_input = r'(([\d]*)|([\d]+([,][\d]+)*))'

#here we define more complex inputs
# init_state: (state_name)<-(1,2,3)
# called by the user to create a new state object.
init_state = r'^\(' + state_name + r'\)<-\(' + state_init_input + r'\)$'

# activeSate: stateName([elementName])
#activeState = r'^[\D]*\(\[[\D]*\]\)'
# updateState: ->(...) # any thing goes in the ...
#updateState = r'(->\(.*\))+$'
#fullUpdateState = activeState+updateState

#operations

# act on every element: ([ operations ])
#actOnEveryElement = r'^\(\[.*\]\)$'