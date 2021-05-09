import maya.cmds as mc

selection = mc.ls(selection = True)


def castshadow(selection):
    ''' 
    Esta tool activa y desactiva el parametro CastShadow de los elementos seleccionados.
    '''

    listaOn = []
    listaOff = []

    for i in selection:
        cs = mc.getAttr(i + '.castsShadows')

        if cs == True:
            mc.setAttr(i + '.castsShadows', False)
            listaOff.append(i)
        elif cs == False:
            mc.setAttr(i + '.castsShadows', True)
            listaOn.append(i)

    print('ON OBJECTS LIST:\n----------------------')
    for on in listaOn:
        if len(listaOn) == 0:
            print ('None')
        else:
            print(on)
    print('----------------------\n')
    print('OFF OBJECTS LIST:\n----------------------')
    for off in listaOff:
        if len(listaOff) == 0:
            print ('None')
        else:
            print(off)
    print('----------------------\n')

    return castshadow

castshadow(selection)