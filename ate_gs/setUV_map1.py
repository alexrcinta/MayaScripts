
import maya.cmds as mc

def setUV_map1 ():

    selection = mc.ls(selection = True)

    for item in selection:
        # Variables
        shape = item + 'Shape'
        nodeTexture = 'TX_' + item

        mc.uvLink( uvSet = shape + '.uvSet[0].uvSetName', texture = nodeTexture )

setUV_map1()