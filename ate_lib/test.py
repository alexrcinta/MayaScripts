import maya.cmds as cmds
from functools import partial

# Something to parse ui element, it is important to make difference between ui query and functions
def optionMenuParser_string(opM_name, func, *args):
        # *args (or could be **kwargs) is here to pass maybe more arguments to a function
    string = cmds.optionMenu(opM_name, q=True, v=True) # you could even parse some flag or anything
    if args and len(args) > 1:
        # args len must be superior to 1 because maya always input True argument
        func(string, *args)
    else:
        func(string)

# A function doing something with the string
def printNewMenuItem( item ):
    print item 

window = cmds.window()
cmds.columnLayout()
# change command='' is a placeholder to input back the option menu name
mygroup = cmds.optionMenu( label='Colors', changeCommand='' )
# partial is used to put arguments in a function trhought the ui
cmds.optionMenu(mygroup, e=1, changeCommand= partial(optionMenuParser_string, mygroup, printNewMenuItem) )
cmds.menuItem( p=mygroup, label='Yellow' )
cmds.menuItem( p=mygroup, label='Purple' )
cmds.menuItem( p=mygroup, label='Orange' )
cmds.showWindow( window )


cmds.optionMenu(mygroup, q=True, v=True) # to get the name of the current value
cmds.optionMenu(mygroup, q=True, sl=True) # to get the current index
cmds.optionMenu(mygroup, e=True, sl = 3 )# to change the current value
cmds.optionMenu(mygroup, e=True, v = 'Purple' )# to change the current value