
def window():
	#Checks for existing printer window, deletes it if it exists.
	def deleteUI(name):
		cmds.deleteUI(name)
		
	if cmds.window("vToolsPrinterWindow", exists=True):
		deleteUI("vToolsPrinterWindow")
	cmds.window("vToolsPrinterWindow", sizeable=True, title="vTools Printer")
	cmds.showWindow()
	cmds.setParent("vToolsPrinterWindow")
	cmds.formLayout("vToolsPrinter")
	cmds.scrollField("field_printer", editable=True, h=800, w=800, text="")

	
    
def scrollFieldPrint (format="", path="", alternativeText="", modelName="", translateX="", translateY="", translateZ="", rotateZ="", rotateX="", rotateY="", scaleX="", scaleY="", scaleZ=""):
	if format == "hie":
		cmds.scrollField("field_printer", edit=True, insertText = 
		" SCS " + str(modelName) + 
		" t " + str(translateX) + " " + str(translateY) + " " + str(translateZ) +
		" R " + str(rotateZ) + " " + str(rotateX) + " " + str(rotateY) +
		" S " + str(scaleX) + " " + str(scaleY) + " " + str(scaleZ) + "\n" + " {\n" +
		" HIE_FILE_AUTOCG DB/DB_HIE/" + str(path) + str(alternativeText) + "\n" + " }\n")
		#" HIE_FILE_AUTOCG DB/DB_HIE/AIRPORT_FEATURES/SUPPORT_LIGHT_red_green" + ".hie\n" + " }\n")
	else:
		cmds.scrollField("field_printer", edit=True, insertText = alternativeText)

#" HIE_FILE_AUTOCG DB/DB_HIE/" + str(path) + modelName + ".hie\n" + " }\n")

def getModelHie(translateMode="relative"):
    window()
    #Gets a list of selected objects.
    modelsList = cmds.ls(selection=True)

    #Prints models to the window in HIE format.
    for model in modelsList:
        #Sets up variables.
        if translateMode == "relative":
            translate = cmds.xform (model, query= True, translation= True)

        if translateMode =="world":
            translate = cmds.xform (model, query= True, worldSpace= True, translation= True)

        if translateMode == "pivot":
            translate = cmds.xform (model, query= True, worldSpace= True, rotatePivot= True)

        rotate = cmds.xform (model, query= True, rotation= True)
        scaleX = cmds.getAttr (model + ".scaleX")
        scaleY = cmds.getAttr (model + ".scaleY")
        scaleZ = cmds.getAttr (model + ".scaleZ")

        
        if cmds.attributeQuery ("hieName", node=model, exists = True):
            hieName = cmds.getAttr (model + ".hieName")
        else:
            hieName = model + ".hie"

        #Removes namespacing characteristics if present.
        try:
            modelClean = model.split(":")[1]
        except:
            modelClean = model

        #Actual printing happens here. #Replace modelClean for hie scepcific with "". Example "SUPPORT_LIGHT_blue"
        scrollFieldPrint(
        "hie",
        hieName[:-4] + '/',
        hieName,
        modelClean, 
        round(translate[0], 3), 
        round(translate[1], 3), 
        round(translate[2], 3), 
        round(rotate[2], 3), 
        round(rotate[0], 3),
        round(rotate[1], 3),
        round(scaleX, 3),
        round(scaleY, 3),
        round(scaleZ, 3)
        )


    #Moves cursor to new window for easy select all, copy.
    cmds.setFocus('field_printer')
	
#getModelHie accepts (), ("world") and ("pivot")
getModelHie("pivot")