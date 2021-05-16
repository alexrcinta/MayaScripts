import maya.cmds as mc
import os

features_selected = cmds.ls(selection = True)
feature = cmds.listRelatives(features_selected, allDescendents = True, type = 'mesh')

def switcher_daynight (feature):
    
    for element in feature:
        name = element[0:-10]

        # This verify if the object name contains the "_elements" sufix.
        if name.endswith('_elements') == True: continue
        elif name.endswith('_elements_big') == True: continue
        elif name.endswith('_elements_medium') == True: continue
        elif name.endswith('_elements_small') == True: continue
        elif name.endswith('_glass') == True: continue
        else:
            pass

        tx = mc.getAttr('TX_' + name + '.fileTextureName')
        root = str(tx)
        last_level = root.rfind('/')
        path = root[0:(last_level + 1)]
        textures_files = os.listdir(path)
        file_image = root[last_level + 1::]


        # If night texture exists for any case.
        if file_image.endswith('_night.rgb') == True:
            new_tx = mc.setAttr(('TX_' + name + '.fileTextureName'), (path + name + '.rgb'), type = 'string')
        
        elif file_image.endswith('_night.rgb') == False:
            night_texture = file_image[:-4] + '_night.rgb'
            if night_texture in textures_files:
                new_tx = mc.setAttr(('TX_' + name + '.fileTextureName'), (path + name + '_night.rgb'), type = 'string')
            
            elif file_image in textures_files:
                diffuse_value = mc.getAttr('MAT_' + name + '.diffuse')
                if not diffuse_value != 0.0:
                    mc.setAttr('MAT_' + name + '.diffuse', 0.8)

                # If night texture doesn't exist for any case.
                else:
                    mc.setAttr('MAT_' + name + '.diffuse', 0.0)
                print('Cambiada noche de alpha sin exitir texura alpha night')

        print('Textures have been switched successfully.\n'),
        
    return switcher_daynight

switcher_daynight(feature)
