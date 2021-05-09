from functools import partial
from package.ate_lib.baseWindow import BaseWindow
import maya.cmds as mc
import csv
import os

class RangeDistanceLods(BaseWindow):

    WINDOW_NAME = "Range Distance Lods"
    WINDOW_TITLE = "Range Distance Lods"
    WIDTH = 400
    HEIGHT = 200


    def CreateCustomUI (self):
        """ """
        mc.frameLayout('Buildings', label = 'Buildings 5-10m Height:', w = self.WIDTH - 4)
        mc.rowColumnLayout('rowBuildings', numberOfColumns=4, columnWidth=[(1, 135), (2, 70), (3, 90), (4, 95)] )


        mc.text(label = 'Model Width:', parent = 'rowBuildings', align = 'left')
        mc.text(label = '20m', parent = 'rowBuildings', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'rowBuildings', align = 'left')
        mc.textField(text = '10000.0m', parent = 'rowBuildings', editable = False)

        mc.text(label = 'Model Width:', parent = 'rowBuildings', align = 'left')
        mc.text(label = '50m', parent = 'rowBuildings', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'rowBuildings', align = 'left')
        mc.textField(text = '13000.0m', parent = 'rowBuildings', editable = False)
        
        mc.text(label = 'Model Width:', parent = 'rowBuildings', align = 'left')
        mc.text(label = '80m', parent = 'rowBuildings', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'rowBuildings', align = 'left')
        mc.textField(text = '15000.0m', parent = 'rowBuildings', editable = False)

        mc.text(label = 'Model Width:', parent = 'rowBuildings', align = 'left')
        mc.text(label = '100-150m', parent = 'rowBuildings', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'rowBuildings', align = 'left')
        mc.textField(text = '20000.0m', parent = 'rowBuildings', editable = False)
        

        mc.frameLayout('Buildings', label = 'Skyscraper/Large Models:', w = self.WIDTH - 4)
        mc.rowColumnLayout('Skyscraper', numberOfColumns=4, columnWidth=[(1, 135), (2, 70), (3, 90), (4, 95)] )
        
        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '50m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        mc.textField(text = '20000.0m', parent = 'Skyscraper', editable = False)

        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '70m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        mc.textField(text = '22000.0m', parent = 'Skyscraper', editable = False)

        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '100m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        mc.textField(text = '24000.0m', parent = 'Skyscraper', editable = False)

        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '200m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        mc.textField(text = '28000.0m', parent = 'Skyscraper', editable = False)
        
        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '300m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        mc.textField(text = '32000.0m', parent = 'Skyscraper', editable = False)
        
        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '400m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        mc.textField(text = '36000.0m', parent = 'Skyscraper', editable = False)

        
        mc.frameLayout('Buildings', label = 'Bridge Lod Range Guide:', w = self.WIDTH - 4)
        mc.rowColumnLayout('Bridge', numberOfColumns=4, columnWidth=[(1, 135), (2, 70), (3, 90), (4, 95)] )
        
        mc.text(label = 'Model Length:', parent = 'Bridge', align = 'left')
        mc.text(label = '1000m', parent = 'Bridge', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Bridge', align = 'left')
        mc.textField(text = '28000.0m', parent = 'Bridge', editable = False)


        mc.frameLayout('Buildings', label = 'Pier Lod Range Guide:', w = self.WIDTH - 4)
        mc.rowColumnLayout('Pier', numberOfColumns=4, columnWidth=[(1, 135), (2, 70), (3, 90), (4, 95)] )
        
        mc.text(label = 'Model Length:', parent = 'Pier', align = 'left')
        mc.text(label = '500m', parent = 'Pier', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Pier', align = 'left')
        mc.textField(text = '24000.0m', parent = 'Pier', editable = False)

RangeDistanceLods()

