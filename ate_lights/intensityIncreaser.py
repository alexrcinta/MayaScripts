import maya.cmds as mc

def intensityIncreaser ():
    """ 
    EN - Intensity Increaser: rise the intensity value of the lights selection 0.1
    ES - Intensity Increaser: aumenta el valor de la intensidad de las luces selccionadas en + 0.1
    """

    # Variables
    increaser = 0.1
    lights_selected_list = []
    cancel = False
    selection = mc.ls(selection = True)
    lights_scene = mc.ls(lights = True)


    while cancel == False:
        
        # Iteracion y clasificacion de objetos
        for i in selection:
            item = i + 'Shape'
            if item in lights_scene:
                lights_selected_list.append(True)
            else:
                lights_selected_list.append(False)

        # Validacion de objetos
        if len(selection) == 0:
            mc.warning('Selecciona una o varias luces.')
        elif False in lights_selected_list:
            mc.warning('Has seleccionado algun objeto que no es una luz. Solo debes seleccionar luces.')
        else:
            # Ejecucion de la tool
            print '\n-----------------------------------------------------------'
            print 'INTENSITY LIGHTS SELECTION LIST ----- (increaser +0.1)'
            print '-----------------------------------------------------------'
            print 'LIGHT                       OLD value           NEW value'
            print '-----------------------------------------------------------'
            for light in selection:
                intensity = mc.getAttr(light + '.intensity')
                new_intensity = mc.setAttr(light + '.intensity', intensity + increaser)
                intensity_formatted = '{:.2f}'.format(intensity)
                new_intensity_formatted = '{:.2f}'.format(intensity + increaser)
                print light + ':\t\t' + intensity_formatted + '\t\t ->\t\t', new_intensity_formatted
            print '-----------------------------------------------------------\n'
            print ('Intensidad aumentada de todas las luces seleccionadas.\nListado e info de luces y valores en el Script Editor.'),

        cancel = True

intensityIncreaser()