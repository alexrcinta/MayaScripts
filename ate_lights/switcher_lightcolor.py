import maya.cmds as mc

selection = mc.ls(selection = True)


def validation(switcher_lightcolor):
    def lights_selected (*args):
        if len(selection) == 0:
            mc.warning('No has seleccionado ninguna luz. Necesitas seleccionar al menos una.')
        else:
            shapes = mc.listRelatives(shapes=True)
            for i in shapes:
                if mc.objectType(i) != 'volumeLight':
                    mc.warning('En tu seleccion no hay LIGHTs seleccionadas. Debes  seleccionar al menos una.')
                else:
                    print('Proceso completado!'), #La coma despues del print muestra el mensaje en el commandline de la UI de maya. Sin la coma, solo aparecera en el script editor.
                    return switcher_lightcolor(selection)
                    

    return lights_selected

@validation
def switcher_lightcolor (selection):
    R_amber = 1.000
    G_amber = 0.706
    B_amber = 0.263

    for light in selection:

        light_colorB = mc.getAttr(light + '.colorB')
        light_colorB = round(light_colorB, 3)
        name = str(light)

        if light_colorB == 0.263:
            mc.setAttr(light + '.colorR', 1)
            mc.setAttr(light + '.colorG', 1)
            mc.setAttr(light + '.colorB', 1)

            new_name = name.replace('ORANGE', 'WHITE')
            mc.rename(light, new_name)

        elif light_colorB == 1:
            mc.setAttr(light + '.colorR', R_amber)
            mc.setAttr(light + '.colorG', G_amber)
            mc.setAttr(light + '.colorB', B_amber)

            new_name = name.replace('WHITE', 'ORANGE')
            mc.rename(light, new_name)
    
    return switcher_lightcolor

switcher_lightcolor(selection)