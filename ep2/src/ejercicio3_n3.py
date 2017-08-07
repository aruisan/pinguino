# -*- coding: utf-8 -*-

import pyglet, math
from pyglet.window import key
from src.tools import createSprite,createLabel,createSpriteGif


class Ejercicio3_n3():
    
    NAME = 'EJERCICIO3_N3'
    MODE = 'LOCAL'
    SIZE = 'CURRENT'
    
    R = None
    data = None
    pics = []
    
    
    def __init__(self, data = {}):
        
        self.data = data
        
        
    def make(self, R):
        
        self.run = False
        self.run2 = False
        self.run3 = False
        self.po = None
        
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
        self.sprites['anterior_eje3_N3'] = createSprite(R.anterior_eje3_N3, self.area, self.layer5)
        self.sprites['mar_eje3_N3'] = createSprite(R.mar_eje3_N3, self.area, self.layer2)
        self.sprites['balon_eje3_N3'] = createSprite(R.balon_eje3_N3, self.area, self.layer4)
        self.sprites['nina_eje3_N3'] = createSprite(R.nina_eje3_N3, self.area, self.layer3)
        self.sprites['sol_eje3_N3'] = createSprite(R.sol_eje3_N3, self.area, self.layer4)
        self.sprites['ok_eje3_N3'] = createSprite(R.ok_eje3_N3, self.area, self.layer2)
        self.sprites['actualizar_eje3_N3'] = createSprite(R.actualizar_eje3_N3, self.area, self.layer2)
        self.sprites['casa_eje3_N3'] = createSprite(R.casa_eje3_N3, self.area, self.layer2)
        self.sprites['bombillo_eje3_N3'] = createSprite(R.bombillo_eje3_N3, self.area, self.layer5)
        self.sprites['siguiente_eje3_N3'] = createSprite(R.siguiente_eje3_N3, None, self.layer5)
        self.sprites['nina_lanzando_eje3_N3'] = createSpriteGif(R.nina_lanzando_eje3_N3, self.area, self.layer5)
        self.sprites['no_eje3_N3'] = createSpriteGif(R.no_eje3_N3, self.area, self.layer5)
        self.sprites['exe_eje3_N3'] = createSpriteGif(R.exe_eje3_N3, self.area, self.layer5)
        self.sprites['velocidad_pelota_eje3_N3'] = createSprite(R.velocidad_pelota_eje3_N3, self.area, self.layer3)
        self.sprites['altura_maxima_eje3_N3'] = createSprite(R.altura_maxima_eje3_N3, self.area, self.layer3)
        self.sprites['velocidad_pelota_campo_eje3_N3'] = createSprite(R.velocidad_pelota_campo_eje3_N3, self.area, self.layer3)
        self.sprites['res_campo_eje3_N3'] = createSprite(R.res_campo_eje3_N3, self.area, self.layer3)
     
        
        self.labels['ldescripcion'] = createLabel(R.ldescripcion_eje3_N3, self.area, self.layer4)
        self.labels['laltura_maxima'] = createLabel(R.laltura_maxima_eje3_N3, self.area, self.layer4)
        self.labels['lvelocidad_pelota'] = createLabel(R.lvelocidad_pelota_eje3_N3, self.area, self.layer4)
        
                
    def loadData(self):
        
        pass
        
    def go_timer(self, data):
        pass
                                
                                
                
    
    def go_draw(self):
        self.area.draw()
    
    
    def go_mouse_motion(self, x, y, dx, dy):
        pass
        
        
    def go_mouse_press(self, x, y, b, m):
        
        if('ir_niveles' in self.pics):
            self.MODE = 'NIVELES'
            
        if('siguiente_eje3_N3' in self.pics):
            pass
            
        if('ir_casa' in self.pics):
            self.MODE = 'MENU'
            
        if('ir_actualizar' in self.pics):
            self.make(self.R)
        
            
        if('ir_bombillo' in self.pics):
            pass
            
        if('ir_ok' in self.pics):
            pass
    
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

    def ganar(self):
       pass
