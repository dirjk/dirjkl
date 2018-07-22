"""
This is the main entry point for actually starting up and running the intreperter.

It also maintains all the States that exist.

"""
import re
import syntax.parser as parser
run = True
states = {}

def showStates():
    if len(states.keys()) > 0:
        print("")
        for i in states.keys():
            print(i,states[i])
        return ""
    return 'NO STATES EXIST'     

while(run):
    raw = input("?")
    if raw == "quit" or raw == "q":
        run = False
    elif raw == "states":
        print(showStates())
    else:
        print(parser.parse(raw,states))