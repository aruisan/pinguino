# -*- coding: utf-8 -*-

import pyglet
from pyglet.window import key
from src.tools import createSprite,createLabel


class Login():
    
    NAME = 'LOGIN'
    MODE = 'LOCAL'
    SIZE = 'CURRENT'
    
    R = None
    data = None
    pics = []
    
    login_adv1 = 0
    
    
    def __init__(self, data = {}):
        
        self.data = data
        self.data['correo2'] = ''
        self.data['clave2'] = ''
        
        
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
        self.sprites['login'] = createSprite(R.login, self.area, self.layer2)
        self.sprites['correo2'] = createSprite(R.correo2, self.area, self.layer2)
        self.sprites['clave2'] = createSprite(R.clave2, self.area, self.layer2)        
        self.sprites['cucorreo2'] = createSprite(R.cucorreo2, self.area, self.layer2)
        self.sprites['cuclave2'] = createSprite(R.cuclave2, self.area, self.layer2)
        self.sprites['anterior3'] = createSprite(R.anterior3, self.area, self.layer2)
        self.sprites['enter'] = createSprite(R.enter, self.area, self.layer2)
        self.sprites['pointersito'] = createSprite(R.pointersito, self.area, self.layer3)
        
        self.labels['lcorreo2'] = createLabel(R.lcorreo2, self.area, self.layer4)
        self.labels['lclave2'] = createLabel(R.lclave2, self.area, self.layer4)
        
        self.plabel = 'lcorreo2'
        
        self.sprites['login_adv1'] = createSprite(R.login_adv1, None, self.layer5)        
       
               
    def loadData(self):
        
        self.labels['lcorreo2'].text = self.data['correo2']
        self.labels['lclave2'].text = '#'*len(self.data['clave2'])
        
        
    def go_timer(self, data):
        pass
    
    
    def go_draw(self):
        self.area.draw()
        
        if(self.login_adv1 == 1):
            self.login_adv1 = 2
            self.sprites['login_adv1'].batch = self.area;
    
    
    def go_mouse_motion(self, x, y, dx, dy):
        pass
        
        
    def go_mouse_press(self, x, y, b, m):
        
        if(self.login_adv1 == 0):
            if('ir_principal2' in self.pics):
                self.data={}
                self.MODE = 'PRINCIPAL' 
            if(len(self.pics) > 0):
                if(self.pics[0] in self.R.pointersito.ypos.keys()):
                    self.sprites['pointersito'].y = self.R.pointersito.ypos[self.pics[0]]
                    self.plabel = 'l'+self.pics[0][2:]
                elif(self.pics[0] == 'enter'):
                    if(self.data['dbcon'].login(self.data['correo2'], self.data['clave2'])):
                        self.MODE = 'NIVELES'
                    else:
                        self.login_adv1 = 1
        else:
                if('cerrar_login_adv1' in self.pics):
                    self.login_adv1 = 0;
                    self.sprites['login_adv1'].batch = None;
                       
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
        
        if(text != "\r"):
        
            if(len(self.labels['lcorreo2'].text) < 40 and self.plabel== 'lcorreo2'):
                self.labels['lcorreo2'].text += text 
           
            elif(len(self.labels['lclave2'].text) < 15 and self.plabel== 'lclave2'):
                self.labels['lclave2'].text += '#'     
            
            print(self.plabel)
            self.data[self.plabel[1:]] += text
        
        else:
            pos = self.R.pointersito.ylist.index(self.plabel)
            pos = pos + 1
            
            if(pos > 1):
                pos = 0
            
            self.sprites['pointersito'].y = self.R.pointersito.ypos['cu'+self.R.pointersito.ylist[pos][1:]]
            self.plabel = self.R.pointersito.ylist[pos]
    
    
    def go_text_motion(self, motion):
        if(motion == key.BACKSPACE):
            self.labels[self.plabel].text = self.labels[self.plabel].text[0:-1]
            self.data[self.plabel[1:]] = self.data[self.plabel[1:]][0:-1]
