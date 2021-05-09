import maya.cmds as mc

selection = mc.ls(selection = True)

def set2zero (selection):

    for objects in selection:
        mc.setAttr(objects + '.translateZ', 0)

    return set2zero

set2zero (selection)