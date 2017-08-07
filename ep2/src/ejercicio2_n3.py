# -*- coding: utf-8 -*-

import pyglet, math
from pyglet.window import key
from src.tools import createSprite,createLabel,createSpriteGif


class Ejercicio2_n3():
    
    NAME = 'EJERCICIO2_N3'
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
        self.sprites['anterior_eje2_N3'] = createSprite(R.anterior_eje2_N3, self.area, self.layer5)
        self.sprites['pasto_eje2_N3'] = createSprite(R.pasto_eje2_N3, self.area, self.layer4)
        self.sprites['montana_eje2_N3'] = createSprite(R.montana_eje2_N3, self.area, self.layer3)
        self.sprites['arco_eje2_N3'] = createSprite(R.arco_eje2_N3, self.area, self.layer2)
        self.sprites['helicoptero_eje2_N3'] = createSprite(R.helicoptero_eje2_N3, self.area, self.layer4)
        self.sprites['pepe_eje2_N3'] = createSprite(R.pepe_eje2_N3, self.area, self.layer5)
        self.sprites['paracaidas_eje2_N3'] = createSprite(R.paracaidas_eje2_N3, self.area, self.layer5)
        self.sprites['ok_eje2_N3'] = createSprite(R.ok_eje2_N3, self.area, self.layer2)
        self.sprites['actualizar_eje2_N3'] = createSprite(R.actualizar_eje2_N3, self.area, self.layer2)
        self.sprites['casa_eje2_N3'] = createSprite(R.casa_eje2_N3, self.area, self.layer2)
        self.sprites['bombillo_eje2_N3'] = createSprite(R.bombillo_eje2_N3, self.area, self.layer5)
        self.sprites['siguiente_eje2_N3'] = createSprite(R.siguiente_eje2_N3, None, self.layer5)
        self.sprites['no_eje2_N3'] = createSpriteGif(R.no_eje2_N3, None, self.layer5)
        self.sprites['exe_eje2_N3'] = createSpriteGif(R.exe_eje2_N3, None, self.layer5)
        self.sprites['velocidad_final_eje2_N3'] = createSprite(R.velocidad_final_eje2_N3, self.area, self.layer3)
        self.sprites['velocidad_inicial_eje2_N3'] = createSprite(R.velocidad_inicial_eje2_N3, self.area, self.layer3)
        self.sprites['altura_helicoptero_eje2_N3'] = createSprite(R.altura_helicoptero_eje2_N3, self.area, self.layer3)
        self.sprites['velocidad_inicial_campo_eje2_N3'] = createSprite(R.velocidad_inicial_campo_eje2_N3, self.area, self.layer3)
        self.sprites['altura_helicoptero_campo_eje2_N3'] = createSprite(R.altura_helicoptero_campo_eje2_N3, self.area, self.layer3)
        self.sprites['res_campo_eje2_N3'] = createSprite(R.res_campo_eje2_N3, self.area, self.layer3)
     
        
        self.labels['ldescripcion'] = createLabel(R.ldescripcion_eje2_N3, self.area, self.layer4)
        self.labels['lvelocidad_inicial'] = createLabel(R.lvelocidad_inicial_eje2_N3, self.area, self.layer4)
        self.labels['laltura_helicoptero'] = createLabel(R.laltura_helicoptero_eje2_N3, self.area, self.layer4)
        self.labels['lvelocidad_final'] = createLabel(R.lvelocidad_final_eje2_N3, self.area, self.layer4)
        
                
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
            
        if('siguiente_eje2_N3' in self.pics):
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
