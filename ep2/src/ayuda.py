# -*- coding: utf-8 -*-

import pyglet
from pyglet.window import key
from src.tools import createSprite,createLabel,createSpriteGif


class Ayuda():
    
    NAME = 'AYUDA'
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
        self.sprites['ayuda'] = createSprite(R.ayuda, self.area, self.layer2)
        self.sprites['tabla'] = createSprite(R.tabla, self.area, self.layer2)
        self.sprites['piso'] = createSprite(R.piso, self.area, self.layer2)
        self.sprites['idea'] = createSpriteGif(R.idea, self.area, self.layer4)
        self.sprites['anterior4'] = createSprite(R.anterior4, self.area, self.layer2)
        
        
    def loadData(self):
        
        pass
        
    def go_timer(self, data):
        pass
    
    
    def go_draw(self):
        self.area.draw()
    
    
    def go_mouse_motion(self, x, y, dx, dy):
        pass
        
        
    def go_mouse_press(self, x, y, b, m):
        
        if('ir_menu' in self.pics):
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

