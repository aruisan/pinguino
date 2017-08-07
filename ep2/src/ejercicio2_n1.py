# -*- coding: utf-8 -*-

import pyglet, math
from pyglet.window import key
from src.tools import createSprite,createLabel, createSpriteGif


class Ejercicio2_n1():
    
    NAME = 'EJERCICIO2_N1'
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
            self.om = R.zones['EJERCICIO2_N1'] ['mover_mano'][:]
        else:
            R.zones['EJERCICIO2_N1'] ['mover_mano'] = self.om
        
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
        self.sprites['anterior7'] = createSprite(R.anterior7, self.area, self.layer2)
        self.sprites['barco1_eje2'] = createSprite(R.barco1_eje2, self.area, self.layer4)
        self.sprites['barco2_eje2'] = createSprite(R.barco2_eje2, self.area, self.layer5)
        self.sprites['agua_eje2'] = createSprite(R.agua_eje2, self.area, self.layer2)
        self.sprites['playa_eje2'] = createSprite(R.playa_eje2, self.area, self.layer3)
        self.sprites['faro_eje2'] = createSprite(R.faro_eje2, self.area, self.layer3)
        self.sprites['tiempo_campo'] = createSprite(R.tiempo_campo, self.area, self.layer2)
        self.sprites['car1_campo_eje2'] = createSprite(R.car1_campo_eje2, self.area, self.layer2)
        self.sprites['car2_campo_eje2'] = createSprite(R.car2_campo_eje2, self.area, self.layer2)
        self.sprites['vel_car1_campo_eje2'] = createSprite(R.vel_car1_campo_eje2, self.area, self.layer2)
        self.sprites['vel_car2_campo_eje2'] = createSprite(R.vel_car2_campo_eje2, self.area, self.layer2)
        self.sprites['res_campo_eje2'] = createSprite(R.res_campo_eje2, self.area, self.layer2)
        self.sprites['mano_eje2'] = createSprite(R.mano_eje2, self.area, self.layer2)
        self.sprites['distancia_eje2'] = createSprite(R.distancia_eje2, self.area, self.layer2)        
        self.sprites['distanciaA_u_eje2'] = createSprite(R.distanciaA_u_eje2, self.area, self.layer2)
        self.sprites['distanciaB_v_eje2'] = createSprite(R.distanciaB_v_eje2, self.area, self.layer2)
        self.sprites['velocidadU_eje2'] = createSprite(R.velocidadU_eje2, self.area, self.layer2)
        self.sprites['velocidadV_eje2'] = createSprite(R.velocidadV_eje2, self.area, self.layer2)
        self.sprites['tiempo_eje2'] = createSprite(R.tiempo_eje2, self.area, self.layer2)
        self.sprites['ok_eje2'] = createSprite(R.ok_eje2, self.area, self.layer2)
        self.sprites['actualizar_eje2'] = createSprite(R.actualizar_eje2, self.area, self.layer2)
        self.sprites['casa_eje2'] = createSprite(R.casa_eje2, self.area, self.layer2)
        self.sprites['bombillo_eje2'] = createSprite(R.bombillo_eje2, self.area, self.layer2)
        self.sprites['siguiente_eje2'] = createSprite(R.siguiente_eje2, None, self.layer3)
        self.sprites['no_eje2'] = createSpriteGif(R.no_eje2, None, self.layer4)
        self.sprites['bien_eje2'] = createSpriteGif(R.bien_eje2, None, self.layer4)
        
        
        
        self.labels['ldescripcion'] = createLabel(R.ldescripcion_eje2, self.area, self.layer4)
        self.labels['ltiempo_transcurrido'] = createLabel(R.ltiempo_total, self.area, self.layer4)
        self.labels['ldistancia_u_A'] = createLabel(R.ldistanciaA_u_eje2, self.area, self.layer4)
        self.labels['ldistancia_v_B'] = createLabel(R.ldistanciaB_V_eje2, self.area, self.layer4)
        self.labels['ldistancia_adicional'] = createLabel(R.ldistancia_eje2, self.area, self.layer4)
        self.labels['lvelocidad_u'] = createLabel(R.lvelocidadU_eje2, self.area, self.layer4)
        self.labels['lvelocidad_v'] = createLabel(R.lvelocidadV_eje2, self.area, self.layer4)
        
        self.eje = self.data['dbcon'].getEjercicio(2)
        self.labels['ldescripcion'].width=700
        self.labels['ldescripcion'].multiline=True
        self.labels['ldescripcion'].align = "center"
        self.labels['ldescripcion'].anchor_x = "center"
        self.labels['ldescripcion'].text = self.eje[1].replace("\r", "")
        self.camps = self.data['dbcon'].getCampos(self.eje[0])
        
        print(self.eje[1])
        for k in self.camps.keys():
            print(k, self.camps[k])
            if(k[0:9] == 'distancia' and k != 'distancia_adicional'):
                self.labels['l'+k].text = str(self.camps[k] / 1000)
            elif(k[0:9] == 'velocidad'):
                self.labels['l'+k].text = str(math.ceil(self.camps[k] * 3.6))
            elif(k == 'tiempo_transcurrido'):
                self.labels['l'+k].text = str(round(float(self.camps['tiempo_transcurrido'])/3600, 2))
        
        rr = round(float(self.camps['distancia_adicional'])/1000, 2)
        print("*******", rr)
        self.trig = round((self.camps['max']-self.camps['min'])/50, 2)
        rmin = int( (rr - self.camps['min'])/self.trig)
        rmax = int( (self.camps['max']-rr)/self.trig)
        rtot = rmin+rmax
        
        flood = rr-(rmin*self.trig)
        
        if rtot % 2 != 0:
            rtot += 1
        
        rtot = rtot / 2
        
        self.labels['ldistancia_adicional'].text = str(round(flood+(rtot*self.trig), 2))
                
        
    def loadData(self):
        
        pass
        
    def go_timer(self, data):
        
        if(self.run):
            self.sprites['barco1_eje2'].x += 1
            self.sprites['barco2_eje2'].x -= 1
            if(self.po == -150):
                dif = self.sprites['barco2_eje2'].x - ((self.sprites['faro_eje2'].x+self.sprites['faro_eje2'].width) -self.sprites['faro_eje2'].width * 1.1)
            elif(self.po == 0):
                print("ss")
                dif = self.sprites['barco2_eje2'].x - ((self.sprites['faro_eje2'].x+self.sprites['faro_eje2'].width) -self.sprites['faro_eje2'].width * 0.6)
            else:
                dif = self.sprites['barco2_eje2'].x - ((self.sprites['faro_eje2'].x+self.sprites['faro_eje2'].width) -self.sprites['faro_eje2'].width )
            print(self.po, dif)
            
            if( (dif-1) <= self.po and (dif+1) >= self.po ):
                if(self.po == -150):
                    self.sprites['no_eje2'].batch= self.area
                elif(self.po==0):
                    self.ganar()
                    
                elif(self.po==400):
                    self.sprites['no_eje2'].batch= self.area
                self.run = False
            
    
    def go_draw(self):
        self.area.draw()
    
    
    def go_mouse_motion(self, x, y, dx, dy):
        if self.drag != None:
            if( (round(float(self.camps['min'])) - (round(float(self.camps['min']))*0.05) ) > round(float(self.labels['ldistancia_adicional'].text)) or round(float(self.labels['ldistancia_adicional'].text))  > (round(float(self.camps['max'])) + (round(float(self.camps['max']))*0.05) )):
                self.drag= None
                
                rr = round(float(self.camps['distancia_adicional'])/1000, 2)
                print("*******", rr)
                self.trig = round((self.camps['max']-self.camps['min'])/50, 2)
                rmin = int( (rr - self.camps['min'])/self.trig)
                rmax = int( (self.camps['max']-rr)/self.trig)
                rtot = rmin+rmax
                
                flood = rr-(rmin*self.trig)
                
                if rtot % 2 != 0:
                    rtot += 1
                
                rtot = rtot / 2
                
                
                self.labels['ldistancia_adicional'].text = str(  round(flood+(rtot*self.trig),2))
                
                self.llx = self.R.mano_eje2.x
                self.sprites['mano_eje2'].x =  self.R.mano_eje2.x
                self.R.zones['EJERCICIO2_N1'] ['mover_mano'] = [(self.R.mano_eje2.x,self.R.mano_eje2.y,self.R.mano_eje2.w,self.R.mano_eje2.h)]
                
            else:
                      
                if((self.drag.x > (x-(self.drag.width // 2))) and abs(self.llx-x) >= 10):
                    self.labels['ldistancia_adicional'].text = str( round(float(self.labels['ldistancia_adicional'].text) - self.trig, 2) )
                    self.llx = x
                elif(self.drag.x < (x-(self.drag.width // 2)) and abs(self.llx-x) >= 10):
                    self.labels['ldistancia_adicional'].text = str( round(float(self.labels['ldistancia_adicional'].text) + self.trig, 2) )
                    self.llx = x
                
                self.drag.x = x-(self.drag.width // 2)
                self.R.zones['EJERCICIO2_N1'] ['mover_mano'] = [(self.drag.x, self.drag.y, self.drag.width, self.drag.height)]
            
            
    def go_mouse_press(self, x, y, b, m):
        
            
        if('siguiente_eje2' in self.pics):
            self.MODE = 'EJERCICIO3_N1'
 
        if('ir_niveles' in self.pics):
            self.MODE = 'NIVELES'

        if('ir_casa' in self.pics):
            self.MODE = 'MENU'
            
        if('ir_actualizar' in self.pics):
            self.make(self.R)
        
        if('ir_ok' in self.pics):
            self.run = True
            rr = round(float(self.camps['distancia_adicional'])/1000, 2)
            if(rr == float(self.labels['ldistancia_adicional'].text)):
                self.po = 0
            elif(rr < float(self.labels['ldistancia_adicional'].text)):
                self.po = -150
            else:
                self.po = 400
         
        if('ir_bombillo' in self.pics):
            pass
        
        if('mover_mano' in self.pics and self.drag == None):
            self.drag = self.sprites['mano_eje2']
            self.llx = self.sprites['mano_eje2'].x
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
       
        self.sprites['tiempo_campo'].batch = None
        self.sprites['tiempo_eje2'].batch = None
        self.labels['ltiempo_transcurrido'].text = ""
        self.sprites['car1_campo_eje2'].batch = None
        self.sprites['car2_campo_eje2'].batch = None
        self.sprites['vel_car1_campo_eje2'].batch = None
        self.sprites['vel_car2_campo_eje2'].batch = None
        self.sprites['mano_eje2'].batch = None
        self.sprites['distanciaA_u_eje2'].batch = None
        self.sprites['distanciaB_v_eje2'].batch = None
        self.sprites['velocidadU_eje2'].batch = None
        self.sprites['velocidadV_eje2'].batch = None
        self.sprites['bombillo_eje2'].batch = None
        self.sprites['ok_eje2'].batch = None
        self.labels['ldistancia_u_A'].text = ""
        self.labels['ldistancia_v_B'].text = ""
        self.labels['lvelocidad_u'].text = ""
        self.labels['lvelocidad_v'].text = ""
        self.sprites['bien_eje2'].batch= self.area 
        self.sprites['siguiente_eje2'].batch= self.area    
        self.R.zones['EJERCICIO2_N1'] ['siguiente_eje2'] = [(self.R.siguiente_eje2.x, self.R.siguiente_eje2.y, self.R.siguiente_eje2.w, self.R.siguiente_eje2.h)]

