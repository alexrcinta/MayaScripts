import maya.cmds as mc

def setUV_uvSet1 ():

    selection = mc.ls(selection = True)

    for mesh in selection:
        shape = mesh + 'Shape'
        channelslist = []
        for UVchannel in range(0,10):
            uvset = mc.getAttr(shape + '.uvSet[' + str(UVchannel) + '].uvSetName')
            channelslist.append(uvset)
            nodeTexture = 'TX_' + mesh[:-5]
            try:
                uvset1 = channelslist.index('uvSet1')
                if nodeTexture.endswith('_elements') == True: continue
                elif nodeTexture.endswith('_elements_big') == True: continue
                elif nodeTexture.endswith('_elements_medium') == True: continue
                elif nodeTexture.endswith('_elements_small') == True: continue
                elif nodeTexture.endswith('_glass') == True: continue
                else:
                    mc.uvLink( uvSet = shape + '.uvSet[' + str(uvset1) + '].uvSetName', texture = nodeTexture)
                    print ('uvSet1 set successfully!'),
            except ValueError:
                print ('This mesh has not a second UV channel'),

setUV_uvSet1 ()