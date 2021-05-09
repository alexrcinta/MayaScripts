
# This scrip reproject the UVs on your terrain mesh using the properties found on the image plane associated with said terrain. Written by VK.
# Usage: Run the script. No need to select anything. This one works on old-style edits only.

# Variable initialization.

IPxformX = 0
IPxformY = 0
IPcenterX = 0
IPcenterY = 0
IPwidth = 0
IPheight = 0
editxformX = 0
editxformY = 0

# Terrain mesh and image plane names, in case this changes or is different in the future/different machines.
terrainMeshName = "aeTerrain:Mesh"
imagePlaneName = "aeTerrainImagePlane"

# Saves the selection.
savedSelection = cmds.ls(selection = True)

# Selects the image plane node.
cmds.select(imagePlaneName)
cmds.pickWalk(direction="down")

# Extracts the attributes.
try:
    IPcenterX = cmds.getAttr(cmds.ls(selection=True)[0] + ".imageCenterX")
    IPcenterY = cmds.getAttr(cmds.ls(selection=True)[0] + ".imageCenterY")
    IPwidth = cmds.getAttr(cmds.ls(selection=True)[0] + ".width")
    IPheight = cmds.getAttr(cmds.ls(selection=True)[0] + ".height")
    
    # The translations are on the transform node, not the shape node.
    cmds.pickWalk(direction="up")
    IPxformX = cmds.getAttr(cmds.ls(selection=True)[0] + ".translateX")
    IPxformY = cmds.getAttr(cmds.ls(selection=True)[0] + ".translateY")
    
    # The main object translation should be on the main group. This selects that and gets it too, just in case the edit has been displaced. If there is no parent group, it is ignored, and remains 0.
    cmds.pickWalk(direction="up")
    if cmds.objectType(cmds.ls(selection=True)) == "transform":
        editxformX = cmds.getAttr(cmds.ls(selection=True)[0] + ".translateX")
        editxformY = cmds.getAttr(cmds.ls(selection=True)[0] + ".translateY")

except:
    print "Could not extract some attributes from '" + imagePlaneName + "'. Halting reproject. Is this an image plane?"
    cmds.select(deselect=True)

cmds.select(terrainMeshName, replace=True)

# Reprojects the UVs on the terrain mesh.
try:
    cmds.polyProjection(cmds.ls(cmds.polyListComponentConversion(toFace=True))[0],
        type="planar",
        projectionCenterX = IPcenterX + IPxformX + editxformX,
        projectionCenterY = IPcenterY + IPxformY + editxformY,
        rotateX = 0, rotateY = 0, rotateZ = 0,
        projectionScaleU = IPwidth,
        projectionScaleV = IPheight,
        insertBeforeDeformers = True)

except:
    print "Reprojection failed -- could not create a planar projection on the '" + terrainMeshName + "' object. Is it a mesh type object?"
    cmds.select(deselect=True)

# Reselects whatever was selected before the script was run.
cmds.select(savedSelection, replace = True)