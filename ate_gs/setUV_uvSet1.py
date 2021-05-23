import maya.cmds as mc

selection = mc.ls(selection = True)
channelslist = []

for mesh in selection:
	shape = mesh + 'Shape'
	
	for UVchannel in range(0,10):
		uvset = mc.getAttr(shape + '.uvSet[' + str(UVchannel) + '].uvSetName')
		
		channelslist.append(uvset)

for item in selection:
    shape = item + 'Shape'
    nodeTexture = 'TX_' + item[:-5]
    try:
        uvset1 = channelslist.index('uvSet1')
        mc.uvLink( uvSet = shape + '.uvSet[' + str(uvset1) + '].uvSetName', texture = nodeTexture)
        print ('uvSet1 set successfully!'),
    except ValueError:
        print ('This mesh has not a second UV channel'),





























import maya.cmds as mc

selection = mc.ls(selection = True)
channelslist = []

for mesh in selection:
	shape = mesh + 'Shape'
	
	for UVchannel in range(0,10):
		uvset = mc.getAttr(shape + '.uvSet[' + str(UVchannel) + '].uvSetName')
		
		channelslist.append(uvset)

for item in selection:
    shape = item + 'Shape'
    nodeTexture = 'TX_' + item[:-5]
    try:
        uvset1 = channelslist.index('uvSet1')
        mc.uvLink( uvSet = shape + '.uvSet[' + str(uvset1) + '].uvSetName', texture = nodeTexture)
        print ('uvSet1 set successfully!'),
    except ValueError:
        print ('This mesh has not a second UV channel'),
