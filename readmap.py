#!/usr/bin/env python
from resources.blocks import *

class mapCell:
    def __init__(self, posx=None, posy=None, mat=None, trans=None, soli=None):
        self.mat = mat
        self.posx = posx
        self.posy = posy
        self.trans = trans
        self.soli = soli

def rMap(add):
    map = [[],[],[],[],[],[],[],[],[],[]]
    mapvar = add
    splitmap = mapvar.split('\n')
    for y in range(0,mapvar.count('\n')):
        for x in range(0,len(splitmap[y])):
            attri = blocks[splitmap[y][x]]
            mat = attri['mat']
            soli = attri['soli']
            trans = attri['trans']
            map[y].append(mapCell(x,y,mat,trans,soli))
    return map
