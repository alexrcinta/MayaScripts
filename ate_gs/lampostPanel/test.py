import maya.cmds as mc

def applyMaterial(lampost):
    if mc.objExists(lampost):
    	
    	fileimage = 'D:/Desktop/Python_Master/1_PFM/depot/tree/LAMPOST/MODEL_DEPOT/LAMP_POST_08/TEX/LAMP_POST_08.rgb'
    	
        MAT  =  mc.shadingNode('lambert', name = "MAT_" + lampost[:-5], asShader = True)
        
        GS  =  mc.sets(name = 'GS_' + MAT[4:], empty = True, renderable = True, noSurfaceShader = True)
        mc.connectAttr(MAT + '.outColor', GS + '.surfaceShader')
        mc.sets(lampost, e = True, forceElement = GS)
        
        TEX = mc.shadingNode('file', name='TEX_' + lampost[:-5], asTexture=True)
        mc.connectAttr(TEX + '.outColor', MAT +'.color', force=True)
        mc.setAttr(TEX + '.fileTextureName' ,fileimage,  type = 'string')
        

applyMaterial("LAMP_POST_08" + "_lod1")