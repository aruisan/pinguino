# -*- coding: utf-8 -*-

import pyglet
from pyglet.window import key
from src.tools import createSprite,createLabel


class Niveles():
    
    NAME = 'NIVELES'
    MODE = 'LOCAL'
    SIZE = 'CURRENT'
    
    R = None
    data = None
    pics = []
    
    
    def __init__(self, data = {}):
        
        self.data = data
        
        
    def make(self, R):
        
        self.area = pyglet.graphics.Batch()
        self.layer1 = pyglet.graphics.OrderedGroup(0)
        self.layer2 = pyglet.graphics.OrderedGroup(1)
        self.layer3 = pyglet.graphics.OrderedGroup(2)
        self.layer4 = pyglet.graphics.OrderedGroup(3)
        self.layer5 = pyglet.graphics.OrderedGroup(4)
        
        self.sprites = {}
        self.labels = {}
        self.R = R
        
        self.sprites['fondo'] = createSprite(R.fondo, self.area, self.layer1)
        self.sprites['anterior_niveles'] = createSprite(R.anterior_niveles, self.area, self.layer2)
        self.sprites['medalla_nivel1'] = createSprite(R.medalla_nivel1, None, self.layer3) 
        self.sprites['medalla_nivel2'] = createSprite(R.medalla_nivel2, None, self.layer3)
        self.sprites['medalla_nivel3'] = createSprite(R.medalla_nivel3, None, self.layer3)
        self.sprites['niveles'] = createSprite(R.niveles, self.area, self.layer2)
        self.sprites['nivel1'] = createSprite(R.nivel1, self.area, self.layer2)
        self.sprites['nivel2'] = createSprite(R.nivel2, self.area, self.layer2)
        self.sprites['nivel3'] = createSprite(R.nivel3, self.area, self.layer2)
        self.sprites['des_nivel1'] = createSprite(R.des_nivel1, self.area, self.layer2)
        self.sprites['des_nivel2'] = createSprite(R.des_nivel2, self.area, self.layer2)
        self.sprites['des_nivel3'] = createSprite(R.des_nivel3, self.area, self.layer2)
        self.sprites['rectilineo'] = createSprite(R.rectilineo, self.area, self.layer2)       
        self.sprites['curvilineo'] = createSprite(R.curvilineo, self.area, self.layer2) 
        self.sprites['especial'] = createSprite(R.especial, self.area, self.layer2) 
        
    def loadData(self):
        
        pass
        
    def go_timer(self, data):
        pass
    
    
    def go_draw(self):
        self.area.draw()
    
    
    def go_mouse_motion(self, x, y, dx, dy):
        pass
        
        
    def go_mouse_press(self, x, y, b, m):
        if('ir_nivel1' in self.pics):
            self.MODE = 'NIVEL1'
        if('ir_nivel2' in self.pics):
            self.MODE = 'EJERCICIO1_N2'
        if('ir_nivel3' in self.pics):
            self.MODE = 'NIVEL1'
        if('ir_casa' in self.pics):
            self.MODE = 'MENU'
            
        
    
    
    def go_key_press(self, symbol, modifiers):
        if(symbol == key.F1):
            self.SIZE = 'LD'
        if(symbol == key.F2):
            self.SIZE = 'BD'
        if(symbol == key.F3):
            self.SIZE = 'HD'
        elif(symbol == key.F4):
            self.SIZE = 'WIN'
            
            
    def go_text(self, text):
        pass
    
    
    def go_text_motion(self, motion):
        pass


