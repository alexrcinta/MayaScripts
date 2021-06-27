
#Clean model buffer string.
modelClean = ""

zDisplacement = 0

#Checks for existing printer window, deletes it if it exists.
if cmds.window("vToolsPrinterWindow", exists=True):
    cmds.deleteUI("vToolsPrinterWindow")

#Creates a fresh printer window and configures it.
cmds.window("vToolsPrinterWindow", sizeable=True, title="LAMP_POST_pos Wrapper")
cmds.showWindow()
cmds.setParent("vToolsPrinterWindow")
cmds.formLayout("vToolsPrinter")
cmds.scrollField("field_printer", editable=True, h=600, w=800, text="")

#Gets a list of selected objects.
modelsList = cmds.ls(selection=True)

#Prints models to the window in HIE format.
for models in modelsList:
    #Sets up variables.
    transX = str("%.3f" %(cmds.getAttr(models + ".translateX")))
    transY = str("%.3f" %(cmds.getAttr(models + ".translateY")))
    transZ = str("%.3f" %(cmds.getAttr(models + ".translateZ")))
    rotateX = str("%.3f" %(cmds.getAttr(models + ".rotateX")))
    rotateY = str("%.3f" %(cmds.getAttr(models + ".rotateY")))
    rotateZ = str("%.3f" %(cmds.getAttr(models + ".rotateZ")))
    scaleX = str("%.3f" %(cmds.getAttr(models + ".scaleX")))
    scaleY = str("%.3f" %(cmds.getAttr(models + ".scaleY")))
    scaleZ = str("%.3f" %(cmds.getAttr(models + ".scaleZ")))
    
    #Removes namespacing characteristics if present.
    try:
        modelClean = models.split(":")[1]
    except:
        modelClean = models

    #Actual printing happens here. Complete with brackets!
    cmds.scrollField("field_printer", edit=True, insertText =
    "\tSCS " + modelClean +
    " t " + transX + " " + transY + " " + str(float(transZ)-zDisplacement) +
    " R " + rotateZ + " " + rotateX + " " + rotateY +
    " S " + scaleX + " " + scaleY + " " + scaleZ + "\n" +
    "\t{\n" + "\t\tHIE_FILE_AUTOCG ../../AIRPORT_FEATURES/" + modelClean[0:12] + "/" +  modelClean[:-4] + ".hie\n" + "\t}\n")

#Moves cursor to new window for easy select all, copy.
cmds.setFocus('field_printer')
