# -*- coding: utf-8 -*-

import pyglet
from pyglet.window import key
from src.tools import createSprite,createLabel


class Registro():
    
    NAME = 'REGISTRO'
    MODE = 'LOCAL'
    SIZE = 'CURRENT'
    
    R = None
    data = None
    pics = []
    
    advertencia1 = 0
    advertencia2 = 0
    
    
    def __init__(self, data = {}):
        
        self.data = data
        self.data['nombre'] = ''
        self.data['apellido'] = ''
        self.data['correo'] = ''
        self.data['clave'] = ''
        self.data['verificar'] = ''
        self.data['grado'] = ''
        self.data['rol'] = 'DOCENTE'
    
        
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
        self.sprites['registro'] = createSprite(R.registro, self.area, self.layer2)
        self.sprites['nombre'] = createSprite(R.nombre, self.area, self.layer2)
        self.sprites['apellido'] = createSprite(R.apellido, self.area, self.layer2)
        self.sprites['correo'] = createSprite(R.correo, self.area, self.layer2)
        self.sprites['clave'] = createSprite(R.clave, self.area, self.layer2)
        self.sprites['verificar'] = createSprite(R.verificar, self.area, self.layer2)
        self.sprites['grado'] = createSprite(R.grado, self.area, self.layer2)
        self.sprites['rol'] = createSprite(R.rol, self.area, self.layer2)
        self.sprites['guardar'] = createSprite(R.guardar, self.area, self.layer2)
        self.sprites['anterior'] = createSprite(R.anterior, self.area, self.layer2)
        self.sprites['cnombre'] = createSprite(R.cnombre, self.area, self.layer2)
        self.sprites['capellido'] = createSprite(R.capellido, self.area, self.layer2)
        self.sprites['ccorreo'] = createSprite(R.ccorreo, self.area, self.layer2)
        self.sprites['cclave'] = createSprite(R.cclave, self.area, self.layer2)
        self.sprites['cverificar'] = createSprite(R.cverificar, self.area, self.layer2)
        self.sprites['cgrado'] = createSprite(R.cgrado, self.area, self.layer2)
        self.sprites['crol'] = createSprite(R.crol, self.area, self.layer2)
        self.sprites['pointer'] = createSprite(R.pointer, self.area, self.layer3)
        self.sprites['flecha'] = createSprite(R.flecha, self.area, self.layer4)
        
        self.labels['lnombre'] = createLabel(R.lnombre, self.area, self.layer4)
        self.labels['lapellido'] = createLabel(R.lapellido, self.area, self.layer4)
        self.labels['lcorreo'] = createLabel(R.lcorreo, self.area, self.layer4)
        self.labels['lclave'] = createLabel(R.lclave, self.area, self.layer4)
        self.labels['lverificar'] = createLabel(R.lverificar, self.area, self.layer4)
        self.labels['lgrado'] = createLabel(R.lgrado, self.area, self.layer4)
        self.labels['lrol'] = createLabel(R.lrol, self.area, self.layer4)
        
        self.plabel = 'lnombre'
        
        self.sprites['advertencia1'] = createSprite(R.advertencia1, None, self.layer5)
        self.sprites['advertencia2'] = createSprite(R.advertencia2, None, self.layer5)
    
    
    def loadData(self):
        
        self.labels['lnombre'].text = self.data['nombre']
        self.labels['lapellido'].text = self.data['apellido']
        self.labels['lcorreo'].text = self.data['correo']
        self.labels['lclave'].text = '#'*len(self.data['clave'])
        self.labels['lverificar'].text = '#'*len(self.data['verificar'])
        self.labels['lgrado'].text = self.data['grado']
        
        if(self.data['rol'] == 'DOCENTE'):
            self.labels['lrol'].text = '                      >>  DOCENTE   <<'
        else:
            self.labels['lrol'].text = '                      >> ESTUDIANTE <<'
        
        
    def go_timer(self, data):
        pass
    
    
    def go_draw(self):
        self.area.draw()
        
        if(self.advertencia1 == 1):
            self.advertencia1 = 2
            self.sprites['advertencia1'].batch = self.area;
            
        if(self.advertencia2 == 1):
            self.advertencia2 = 2
            self.sprites['advertencia2'].batch = self.area;
    
    
    def go_mouse_motion(self, x, y, dx, dy):
        pass
        
        
    def go_mouse_press(self, x, y, b, m):
        print(self.pics)
        if(self.advertencia1 == 0):
            if(self.advertencia2 == 0):
                if(len(self.pics) > 0):
                    if(self.pics[0] in self.R.pointer.ypos.keys()):
                        self.sprites['pointer'].y = self.R.pointer.ypos[self.pics[0]]
                        self.plabel = 'l'+self.pics[0][1:]
                    elif('ir_principal2' in self.pics):
                        self.MODE = 'PRINCIPAL'
                    elif(self.pics[0] == 'guardar'):
                        
                        fc = True
                        for k in self.labels.keys():
                            if(self.labels[k].text == ''):
                                fc = False
                                break
                        
                        if(fc):
                            
                            if(self.data['clave'] == self.data['verificar']):
                                self.data['dbcon'].crearUsuario(self.data['nombre'], self.data['apellido'], self.data['correo'], self.data['clave'], self.data['rol'], self.data['grado']) 
                                self.MODE = 'PRINCIPAL'
                            else:
                                self.advertencia2 = 1
                            
                        else:
                            self.advertencia1 = 1
              
            else:
                if('cerrar_advertencia2' in self.pics):
                    self.advertencia2 = 0;
                    self.sprites['advertencia2'].batch = None;
            
        else:
            if('cerrar_advertencia1' in self.pics):
                self.advertencia1 = 0;
                self.sprites['advertencia1'].batch = None;
     
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
       
        if(self.plabel != 'lrol' and text != "\r"):
            
            if(len(self.labels['lnombre'].text) < 40 and self.plabel== 'lnombre'):
               self.labels['lnombre'].text += text 
            
            elif(len(self.labels['lapellido'].text) < 40 and self.plabel== 'lapellido'):
               self.labels['lapellido'].text += text 
            
            elif(len(self.labels['lcorreo'].text) < 40 and self.plabel== 'lcorreo'):
               self.labels['lcorreo'].text += text 
           
            elif(len(self.labels['lclave'].text) < 15 and self.plabel== 'lclave'):
               self.labels['lclave'].text += '#'     
            
            elif(len(self.labels['lverificar'].text) < 15 and self.plabel== 'lverificar'):
               self.labels['lverificar'].text += '#'
               
            elif(len(self.labels['lgrado'].text) < 15 and self.plabel== 'lgrado'):
                self.labels['lgrado'].text += text 
               
            self.data[self.plabel[1:]] += text
        
        elif(text == "\r"):
            pos = self.R.pointer.ylist.index(self.plabel)
            pos = pos + 1
            
            if(pos > 6):
                pos = 0
            
            self.sprites['pointer'].y = self.R.pointer.ypos['c'+self.R.pointer.ylist[pos][1:]]
            self.plabel = self.R.pointer.ylist[pos]
    
    
    def go_text_motion(self, motion):
        if(motion == key.BACKSPACE and self.plabel != 'lrol'):
            self.labels[self.plabel].text = self.labels[self.plabel].text[0:-1]
            self.data[self.plabel[1:]] = self.data[self.plabel[1:]][0:-1]
        
        elif(motion == key.DOWN and self.plabel == 'lrol'):
            if(self.data[self.plabel[1:]] == 'DOCENTE'):
                self.data[self.plabel[1:]] = 'ESTUDIANTE'
                self.labels[self.plabel].text = '                      >> ESTUDIANTE <<'
            else:
                self.data[self.plabel[1:]] = 'DOCENTE'
                self.labels[self.plabel].text = '                      >>  DOCENTE   <<'
