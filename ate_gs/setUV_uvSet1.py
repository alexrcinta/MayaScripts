import maya.cmds as mc

def setUV_uvSet1 ():

    selection = mc.ls(selection = True)


    for item in selection:
        # Variables
        shape = item + 'Shape'
        nodeTexture = 'TX_' + item

        try:
            switcher = mc.uvLink( uvSet = shape + '.uvSet[1].uvSetName', texture = nodeTexture )

        except TypeError:
            print('Has selecionado alguna geometria que no tiene un segundo canal de UVs denominado uvSet1. Ver Script Editor para mas info.\n'),
            print item, 'no tiene un segundo canal de UVs denominado uvSet1.'

setUV_uvSet1()
