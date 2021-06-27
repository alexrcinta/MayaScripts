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


    def bbox():

        selection = mc.ls(selection = True)


        for node in selection:
            absolute_bbox = mc.exactWorldBoundingBox(node)
            Xmin = absolute_bbox[0]
            Ymin = absolute_bbox[1]
            Zmin = absolute_bbox[2]
            Xmax = absolute_bbox[3]
            Ymax = absolute_bbox[4]
            Zmax = absolute_bbox[5]
            

            if Xmin < 0 and Xmax >= 0:
                Bbox_X = abs(Xmin) + abs(Xmax)
            elif Xmin < 0 and Xmax < 0:
                Bbox_X = abs(Xmax) - abs(Xmin)
            elif Xmin >= 0 and Xmax >= 0:
                Bbox_X = abs(Xmax) - abs(Xmin)
                
            
            if Ymin < 0 and Ymax >= 0:
                Bbox_Y = abs(Ymin) + abs(Ymax)
            elif Ymin < 0 and Ymax < 0:
                Bbox_Y = abs(Ymax) - abs(Ymin)
            elif Ymin >= 0 and Ymax >= 0:
                Bbox_Y = abs(Ymax) - abs(Ymin)
                
            
            if Zmin < 0 and Zmax >= 0:
                Bbox_Z = abs(Zmin) + abs(Zmax)
            elif Zmin < 0 and Zmax < 0:
                Bbox_Z = abs(Zmax) - abs(Zmin)
            elif Zmin >= 0 and Zmax >= 0:
                Bbox_Z = abs(Zmax) - abs(Zmin)
            
            
            bbox = [abs(Bbox_X), abs(Bbox_Y), abs(Bbox_Z)]
        
        return node, bbox

    def rangeSelected (self, bbox):

        Bbox_X = bbox[0]
        Bbox_Y = bbox[1]
        Bbox_Z = bbox[2]

        if Bbox_Z <= 10:
            if Bbox_X <= 20:
                if Bbox_Y <= 20:
                    print('10000m'),
                    mc.textField(self.Building_10000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])
            elif Bbox_X > 20 and Bbox_X <= 50:
                if Bbox_Y > 20 and Bbox_Y <= 50:
                    print('13000m'),
                    mc.textField(self.Building_13000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])
            elif Bbox_X > 50 and Bbox_X <= 80:
                if Bbox_Y > 50 and Bbox_Y <= 80:
                    print('15000m'),
                    mc.textField(self.Building_15000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])
            elif Bbox_X > 80 and Bbox_X <= 150:
                if Bbox_Y > 80 and Bbox_Y <= 150:
                    print('20000m'),
                    mc.textField(self.Building_20000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])

        if Bbox_Z > 10:
            if Bbox_X <= 50:
                if Bbox_Y <= 50:
                    print('20000m'),
                    mc.textField(self.Skyscraper_20000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])
            elif Bbox_X > 50 and Bbox_X <= 70:
                if Bbox_Y > 50 and Bbox_Y <= 70:
                    print('22000m'),
                    mc.textField(self.Skyscraper_22000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])
            elif Bbox_X > 70 and Bbox_X <= 100:
                if Bbox_Y > 70 and Bbox_Y <= 100:
                    print('24000m'),
                    mc.textField(self.Skyscraper_24000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])
            elif Bbox_X > 100 and Bbox_X <= 200:
                if Bbox_Y > 100 and Bbox_Y <= 200:
                    print('28000m'),
                    mc.textField(self.Skyscraper_28000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])
            elif Bbox_X > 200 and Bbox_X <= 300:
                if Bbox_Y > 200 and Bbox_Y <= 300:
                    print('32000m'),
                    mc.textField(self.Skyscraper_32000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])
            elif Bbox_X > 300 and Bbox_X <= 400:
                if Bbox_Y > 300 and Bbox_Y <= 400:
                    print('36000m'),
                    mc.textField(self.Skyscraper_36000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])

        if Bbox_X >= 1000 or Bbox_Y >= 1000:
            print('28000m'),
            mc.textField(self.Bridge_28000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])

        if (Bbox_X >= 500 or Bbox_Y >= 500) and (Bbox_X < 1000 or Bbox_Y < 1000):
            print('24000m'),
            mc.textField(self.Pier_24000, edit = True, enableBackground = False, backgroundColor = [0.0, 1.0, 0.0])

    def CreateCustomUI (self):
        """ """
        mc.frameLayout('Buildings', label = 'Buildings 5-10m Height:', w = self.WIDTH - 4)
        mc.rowColumnLayout('rowBuildings', numberOfColumns=4, columnWidth=[(1, 135), (2, 70), (3, 90), (4, 95)] )

        mc.text(label = 'Model Width:', parent = 'rowBuildings', align = 'left')
        mc.text(label = '20m', parent = 'rowBuildings', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'rowBuildings', align = 'left')
        self.Building_10000 = mc.textField(text = '10000.0m', parent = 'rowBuildings', editable = False)

        mc.text(label = 'Model Width:', parent = 'rowBuildings', align = 'left')
        mc.text(label = '50m', parent = 'rowBuildings', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'rowBuildings', align = 'left')
        self.Building_13000 = mc.textField(text = '13000.0m', parent = 'rowBuildings', editable = False)
        
        mc.text(label = 'Model Width:', parent = 'rowBuildings', align = 'left')
        mc.text(label = '80m', parent = 'rowBuildings', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'rowBuildings', align = 'left')
        self.Building_15000 = mc.textField(text = '15000.0m', parent = 'rowBuildings', editable = False)

        mc.text(label = 'Model Width:', parent = 'rowBuildings', align = 'left')
        mc.text(label = '100-150m', parent = 'rowBuildings', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'rowBuildings', align = 'left')
        self.Building_20000 = mc.textField(text = '20000.0m', parent = 'rowBuildings', editable = False)
        

        mc.frameLayout('Buildings', label = 'Skyscraper/Large Models:', w = self.WIDTH - 4)
        mc.rowColumnLayout('Skyscraper', numberOfColumns=4, columnWidth=[(1, 135), (2, 70), (3, 90), (4, 95)] )
        
        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '50m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        self.Skyscraper_20000 = mc.textField(text = '20000.0m', parent = 'Skyscraper', editable = False)

        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '70m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        self.Skyscraper_22000 = mc.textField(text = '22000.0m', parent = 'Skyscraper', editable = False)

        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '100m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        self.Skyscraper_24000 = mc.textField(text = '24000.0m', parent = 'Skyscraper', editable = False)

        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '200m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        self.Skyscraper_28000 = mc.textField(text = '28000.0m', parent = 'Skyscraper', editable = False)
        
        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '300m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        self.Skyscraper_32000 = mc.textField(text = '32000.0m', parent = 'Skyscraper', editable = False)
        
        mc.text(label = 'Model Height/Width:', parent = 'Skyscraper', align = 'left')
        mc.text(label = '400m', parent = 'Skyscraper', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Skyscraper', align = 'left')
        self.Skyscraper_36000 = mc.textField(text = '36000.0m', parent = 'Skyscraper', editable = False)

        
        mc.frameLayout('Buildings', label = 'Bridge Lod Range Guide:', w = self.WIDTH - 4)
        mc.rowColumnLayout('Bridge', numberOfColumns=4, columnWidth=[(1, 135), (2, 70), (3, 90), (4, 95)] )
        
        mc.text(label = 'Model Length:', parent = 'Bridge', align = 'left')
        mc.text(label = '1000m', parent = 'Bridge', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Bridge', align = 'left')
        self.Bridge_28000 = mc.textField(text = '28000.0m', parent = 'Bridge', editable = False)


        mc.frameLayout('Buildings', label = 'Pier Lod Range Guide:', w = self.WIDTH - 4)
        mc.rowColumnLayout('Pier', numberOfColumns=4, columnWidth=[(1, 135), (2, 70), (3, 90), (4, 95)] )
        
        mc.text(label = 'Model Length:', parent = 'Pier', align = 'left')
        mc.text(label = '500m', parent = 'Pier', align = 'left')
        mc.text(label = 'Ending Range:', parent = 'Pier', align = 'left')
        self.Pier_24000 = mc.textField(text = '24000.0m', parent = 'Pier', editable = False)

    data_list = bbox()
    obj = data_list[0]
    bbox = data_list[1]

    rangeSelected(obj, bbox)
