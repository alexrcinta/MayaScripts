
from package.ate_lib.paths import Paths
import os



def lampost_list ():
    path = Paths.DATABASE
    lampost_list = os.listdir(path)

    return lampost_list

def lampost (index):
    path = Paths.DATABASE
    lampost = os.listdir(path)[index]
    return lampost

lp = lampost(1)
print(lp)