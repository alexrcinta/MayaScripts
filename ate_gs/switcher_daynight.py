import maya.cmds as mc

selection = mc.ls(selection = True)

def switcher_daynight (selection):
    
    for element in selection:
        name = element[0:-5]
        tx = mc.getAttr('TX_' + name + '.fileTextureName')
        root = str(tx)
        last_level = root.rfind('/')
        path = root[0:(last_level + 1)]
        file_image = root[last_level + 1::]

        
        if file_image.endswith('_night.jpg') == True:
            new_tx = mc.setAttr(('TX_' + name + '.fileTextureName'), (path + name + '.jpg'), type = 'string')
        
        elif file_image.endswith('_night.jpg') == False:
            new_tx = mc.setAttr(('TX_' + name + '.fileTextureName'), (path + name + '_night.jpg'), type = 'string')
        

    return switcher_daynight
