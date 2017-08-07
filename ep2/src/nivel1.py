# -*- coding: utf-8 -*-

import pyglet, math
from pyglet.window import key
from src.tools import createSprite,createLabel,createSpriteGif


class Nivel1():
    
    NAME = 'NIVEL1'
    MODE = 'LOCAL'
    SIZE = 'CURRENT'
    
    R = None
    data = None
    pics = []
    
    
    def __init__(self, data = {}):
        
        self.data = data
        self.om = None
        
        
    def make(self, R):
        
        if self.om == None:
            self.om = R.zones['NIVEL1'] ['mover_mano'][:]
        else:
            R.zones['NIVEL1'] ['mover_mano'] = self.om
        
        self.drag = None
        self.run = False
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
        self.sprites['colegio'] = createSprite(R.colegio, self.area, self.layer2)
        self.sprites['parque'] = createSprite(R.parque, self.area, self.layer2)
        self.sprites['carretera'] = createSprite(R.carretera, self.area, self.layer2)
        self.sprites['carro1'] = createSprite(R.carro1, self.area, self.layer3)
        self.sprites['carro2'] = createSprite(R.carro2, self.area, self.layer3)
        self.sprites['anterior6'] = createSprite(R.anterior6, self.area, self.layer3)
        self.sprites['dis_campo'] = createSprite(R.dis_campo, self.area, self.layer2)
        self.sprites['car1_campo'] = createSprite(R.car1_campo, self.area, self.layer2)
        self.sprites['car2_campo'] = createSprite(R.car2_campo, self.area, self.layer2)
        self.sprites['vel_car1_campo'] = createSprite(R.vel_car1_campo, self.area, self.layer2)
        self.sprites['vel_car2_campo'] = createSprite(R.vel_car2_campo, self.area, self.layer2)
        self.sprites['res_campo'] = createSprite(R.res_campo, self.area, self.layer2)
        self.sprites['mano'] = createSprite(R.mano, self.area, self.layer2)
        self.sprites['distancia'] = createSprite(R.distancia, self.area, self.layer2)        
        self.sprites['distanciaA_u'] = createSprite(R.distanciaA_u, self.area, self.layer2)
        self.sprites['distanciaB_v'] = createSprite(R.distanciaB_v, self.area, self.layer2)
        self.sprites['velocidadU'] = createSprite(R.velocidadU, self.area, self.layer2)
        self.sprites['velocidadV'] = createSprite(R.velocidadV, self.area, self.layer2)
        self.sprites['resultado'] = createSprite(R.resultado, self.area, self.layer2)
        self.sprites['ok'] = createSprite(R.ok, self.area, self.layer2)
        self.sprites['actualizar'] = createSprite(R.actualizar, self.area, self.layer2)
        self.sprites['casa'] = createSprite(R.casa, self.area, self.layer2)
        self.sprites['bombillo'] = createSprite(R.bombillo, self.area, self.layer2)
        self.sprites['siguiente'] = createSprite(R.siguiente, None, self.layer3)
        self.sprites['no'] = createSpriteGif(R.no, None, self.layer5)
        self.sprites['bien'] = createSpriteGif(R.bien, None, self.layer5)
        self.sprites['explosion'] = createSpriteGif(R.explosion, None, self.layer5)
        
        self.labels['ldescripcion'] = createLabel(R.ldescripcion, self.area, self.layer4)
        self.labels['ldistancia_total'] = createLabel(R.ldistancia_total, self.area, self.layer4)
        self.labels['ldistancia_u_A'] = createLabel(R.ldistanciaA_u, self.area, self.layer4)
        self.labels['ldistancia_v_B'] = createLabel(R.ldistanciaB_V, self.area, self.layer4)
        self.labels['ltiempo'] = createLabel(R.ltiempo, self.area, self.layer4)
        self.labels['lvelocidad_u'] = createLabel(R.lvelocidadU, self.area, self.layer4)
        self.labels['lvelocidad_v'] = createLabel(R.lvelocidadV, self.area, self.layer4)
        
        
        
        
        self.eje = self.data['dbcon'].getEjercicio(1)
        self.labels['ldescripcion'].width=700
        self.labels['ldescripcion'].multiline=True
        self.labels['ldescripcion'].align = "center"
        self.labels['ldescripcion'].anchor_x = "center"
        self.labels['ldescripcion'].text = self.eje[1].replace("\r", "")
        self.camps = self.data['dbcon'].getCampos(self.eje[0])
        
        print(self.eje[1])
        for k in self.camps.keys():
            print(k, self.camps[k])
            if(k[0:9] == 'distancia'):
                self.labels['l'+k].text = str(self.camps[k] / 1000)
            elif(k[0:9] == 'velocidad'):
                self.labels['l'+k].text = str(math.ceil(self.camps[k] * 3.6))
        
        rr = round(float(self.camps['tiempo'])/3600, 2)
        print("*******", rr)
        self.trig = round((self.camps['max']-self.camps['min'])/50, 2)
        rmin = int( (rr - self.camps['min'])/self.trig)
        rmax = int( (self.camps['max']-rr)/self.trig)
        rtot = rmin+rmax
        
        flood = rr-(rmin*self.trig)
        
        if rtot % 2 != 0:
            rtot += 1
        
        rtot = rtot / 2
        
        self.labels['ltiempo'].text = str(round(flood+(rtot*self.trig), 2))
        
        
        
    def loadData(self):
        
        pass
        
    def go_timer(self, data):
        if(self.run):
            self.sprites['carro1'].x += 1
            self.sprites['carro2'].x -= 1
            
            dif = self.sprites['carro2'].x - (self.sprites['carro1'].x+self.sprites['carro1'].width) 
            
            print(self.po, dif)
            
            if( (dif-1) <= self.po and (dif+1) >= self.po ):
                if(self.po == -50):
                    self.sprites['explosion'].batch= self.area
                elif(self.po==0):
                    self.ganar()
                    
                elif(self.po==50):
                    self.sprites['no'].batch= self.area
                self.run = False
    
    
    def go_draw(self):
        self.area.draw()
    

    def go_mouse_motion(self, x, y, dx, dy):
        if self.drag != None:
            
            if( (round(float(self.camps['min'])) - (round(float(self.camps['min']))*0.05) ) > round(float(self.labels['ltiempo'].text)) or round(float(self.labels['ltiempo'].text))  > (round(float(self.camps['max'])) + (round(float(self.camps['max']))*0.05) )):
                self.drag= None
                
                rr = round(float(self.camps['tiempo'])/3600, 2)
                print("*******", rr)
                self.trig = round((self.camps['max']-self.camps['min'])/50, 2)
                rmin = int( (rr - self.camps['min'])/self.trig)
                rmax = int( (self.camps['max']-rr)/self.trig)
                rtot = rmin+rmax
                
                flood = rr-(rmin*self.trig)
                
                if rtot % 2 != 0:
                    rtot += 1
                
                rtot = rtot / 2
                
                
                self.labels['ltiempo'].text = str(  round(flood+(rtot*self.trig),2))
                
                
                self.llx = self.R.mano.x
                self.sprites['mano'].x =  self.R.mano.x
                self.R.zones['NIVEL1'] ['mover_mano'] = [(self.R.mano.x,self.R.mano.y,self.R.mano.w,self.R.mano.h)]
                
            else:
                if((self.drag.x > (x-(self.drag.width // 2))) and abs(self.llx-x) >= 10):
                    self.labels['ltiempo'].text = str( round(float(self.labels['ltiempo'].text) - self.trig, 2) )
                    self.llx = x
                elif(self.drag.x < (x-(self.drag.width // 2)) and abs(self.llx-x) >= 10):
                    self.labels['ltiempo'].text = str( round(float(self.labels['ltiempo'].text) + self.trig, 2) )
                    self.llx = x
                
                self.drag.x = x-(self.drag.width // 2)
                self.R.zones['NIVEL1'] ['mover_mano'] = [(self.drag.x, self.drag.y, self.drag.width, self.drag.height)]
        
        
    def go_mouse_press(self, x, y, b, m):
        
            
        if('siguiente' in self.pics):
            self.MODE = 'EJERCICIO2_N1'
        
        if('ir_niveles' in self.pics):
            self.MODE = 'NIVELES'
            
        if('ir_casa' in self.pics):
            self.MODE = 'MENU'
            
        if('ir_actualizar' in self.pics):
            self.make(self.R)
        
        if('ir_ok' in self.pics):
            self.run = True
            rr = round(float(self.camps['tiempo'])/3600, 2)
            if(rr == float(self.labels['ltiempo'].text)):
                self.po = 0
            elif(rr < float(self.labels['ltiempo'].text)):
                self.po = -50
            else:
                self.po = 50
         
        if('ir_bombillo' in self.pics):
            pass
        if('mover_mano' in self.pics and self.drag == None):
            self.drag = self.sprites['mano']
            self.llx = self.sprites['mano'].x
        elif(self.drag != None):
            self.drag = None
    
    
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
       
        self.sprites['dis_campo'].batch = None
        self.sprites['car1_campo'].batch = None
        self.sprites['car2_campo'].batch = None
        self.sprites['vel_car1_campo'].batch = None
        self.sprites['vel_car2_campo'].batch = None
        self.sprites['mano'].batch = None
        self.sprites['distancia'].batch = None  
        self.sprites['distanciaA_u'].batch = None
        self.sprites['distanciaB_v'].batch = None
        self.sprites['velocidadU'].batch = None
        self.sprites['velocidadV'].batch = None
        self.sprites['bombillo'].batch = None
        self.sprites['ok'].batch = None
        self.labels['ldistancia_total'].text = ""
        self.labels['ldistancia_u_A'].text = ""
        self.labels['ldistancia_v_B'].text = ""
        self.labels['lvelocidad_u'].text = ""
        self.labels['lvelocidad_v'].text = ""
        self.sprites['bien'].batch= self.area 
        self.sprites['siguiente'].batch= self.area 
        self.R.zones['NIVEL1'] ['siguiente'] = [(self.R.siguiente.x, self.R.siguiente.y, self.R.siguiente.w, self.R.siguiente.h)]
        
        



