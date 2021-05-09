from package.ate_lib.paths import Paths
import csv
import os

xBBOX = []
yBBOX = []
zBBOX = []

class BboxInfo():

    FILEPATH = 'D:/Desktop/Python_Master/1_PFM/package/ate_gs/lampostPanel/bbox.csv'

    def axisX_list(self):
        bbox_file = open(self.FILEPATH, 'r')
        read = csv.reader(bbox_file) 
        for axis in read:
            x = axis[1]
            xBBOX.append(x)
        bbox_file.close()
        return xBBOX

    def axisY_list(self):
        bbox_file = open(self.FILEPATH, 'r')
        read = csv.reader(bbox_file) 
        for axis in read:
            y = axis[2]
            yBBOX.append(y)
        bbox_file.close()
        return yBBOX

    def axisZ_list(self):
        bbox_file = open(self.FILEPATH, 'r')
        read = csv.reader(bbox_file) 
        for axis in read:
            z = axis[3]
            zBBOX.append(z)
        bbox_file.close()
        return zBBOX

class MeshInfo():

    PATH = Paths()
    MODEL_DEPOT = PATH.MODEL_DEPOT
    LAMP_POST_LIST = os.listdir(MODEL_DEPOT)
    VERTEX_LAMP_POSTS_LIST = []
    TRIS_LAMP_POSTS_LIST = []

    def vertex(self):
        
        for lampost in self.LAMP_POST_LIST:
            obj_file = open(self.MODEL_DEPOT + lampost + '/GEO/' + lampost + '_lod1.obj', 'r')
            read = obj_file.readlines()
            vertex_list = []

            for mesh_info in read:
                id = mesh_info[0:2]
                if id == 'v ':
                    vertex_list.append(id)
                
            vertex_lampost_number = len(vertex_list)
            self.VERTEX_LAMP_POSTS_LIST.append(vertex_lampost_number)

        return self.VERTEX_LAMP_POSTS_LIST

    def tris(self):
        
        for lampost in self.LAMP_POST_LIST:
            obj_file = open(self.MODEL_DEPOT + lampost + '/GEO/' + lampost + '_lod1.obj', 'r')
            read = obj_file.readlines()
            tris_list = []

            for mesh_info in read:
                id = mesh_info[0:2]
                if id == 'f ':
                    tris_list.append(id)
                
            tris_lampost_number = len(tris_list)
            self.TRIS_LAMP_POSTS_LIST.append(tris_lampost_number)

        return self.TRIS_LAMP_POSTS_LIST

class TexInfo():

    FILEPATH = 'D:/Desktop/Python_Master/1_PFM/package/ate_gs/lampostPanel/bbox.csv'
    TEX_RES_LIST = []

    def resolution(self):
        texInfo_file = open(self.FILEPATH, 'r')
        read = csv.reader(texInfo_file) 
        for texinfo in read:
            resolution = texinfo[4]
            self.TEX_RES_LIST.append(resolution)
        texInfo_file.close()
        return self.TEX_RES_LIST
