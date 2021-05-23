import maya.cmds as mc

def setUV_map1 ():

    selection = mc.ls(selection = True)

    for item in selection:
        shape = item + 'Shape'
        nodeTexture = 'TX_' + item[:-5]
        mc.uvLink( uvSet = shape + '.uvSet[0].uvSetName', texture = nodeTexture )

    print ('map1 set successfully!'),

setUV_map1()