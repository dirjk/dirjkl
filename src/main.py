"""
This is the main entry point for actually starting up and running the intreperter.

It also maintains all the States that exist.

"""
import re
import syntax.parser as parser
run = True
states = {}

def showStates():
   for i in states.keys():
       return i,states[i]
   return 'NO STATES EXIST'     

while(run):
    raw = input("?")
    if raw == "quit" or raw == "q":
        run = False
    elif raw == "states":
        print(showStates())
    else:
        print(parser.parse(raw))