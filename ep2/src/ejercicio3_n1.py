# -*- coding: utf-8 -*-

import pyglet, math, random, decimal
from pyglet.window import key
from src.tools import createSprite,createLabel, createSpriteGif


class Ejercicio3_n1():
    
    NAME = 'EJERCICIO3_N1'
    MODE = 'LOCAL'
    SIZE = 'CURRENT'
    
    R = None
    data = None
    pics = []
    
    margen1=0
    margen2=0
    
    
    def __init__(self, data = {}):
        
        self.data = data
        self.om = None
        
        
    def make(self, R):
        self.margen1 = float(random.randrange(100))/1000
        self.margen2= float(random.randrange(100))/1000
    
        if self.om == None:
            self.om = R.zones['EJERCICIO3_N1'] ['mover_mano'][:]
        else:
            R.zones['EJERCICIO3_N1'] ['mover_mano'] = self.om
        
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
        self.sprites['anterior9_eje3_N1'] = createSprite(R.anterior9_eje3_N1, self.area, self.layer2)
        self.sprites['tractor1_eje3_N1'] = createSprite(R.tractor1_eje3_N1, self.area, self.layer4)
        self.sprites['tractor2_eje3_N1'] = createSprite(R.tractor2_eje3_N1, self.area, self.layer5)
        self.sprites['tierra_eje3_N1'] = createSprite(R.tierra_eje3_N1, self.area, self.layer2)
        self.sprites['granja_eje3_N1'] = createSprite(R.granja_eje3_N1, self.area, self.layer3)
        self.sprites['molino_eje3_N1'] = createSprite(R.molino_eje3_N1, self.area, self.layer3)
        self.sprites['tiempo_campo_eje3_N1'] = createSprite(R.tiempo_campo_eje3_N1, self.area, self.layer2)
        self.sprites['car1_campo_eje3_N1'] = createSprite(R.car1_campo_eje3_N1, self.area, self.layer2)
        self.sprites['car2_campo_eje3_N1'] = createSprite(R.car2_campo_eje3_N1, self.area, self.layer2)
        self.sprites['vel_car2_campo_eje3_N1'] = createSprite(R.vel_car2_campo_eje3_N1, self.area, self.layer2)
        self.sprites['distancia_campo_eje3_N1'] = createSprite(R.distancia_campo_eje3_N1, self.area, self.layer2)
        self.sprites['res_campo_eje3_N1'] = createSprite(R.res_campo_eje3_N1, self.area, self.layer2)
        self.sprites['mano_eje3_N1'] = createSprite(R.mano_eje3_N1, self.area, self.layer2)
        self.sprites['distancia_eje3_N1'] = createSprite(R.distancia_eje3_N1, self.area, self.layer3)
        self.sprites['distanciaA_u_eje3_N1'] = createSprite(R.distanciaA_u_eje3_N1, self.area, self.layer3)
        self.sprites['distanciaB_v_eje3_N1'] = createSprite(R.distanciaB_v_eje3_N1, self.area, self.layer3)
        self.sprites['velocidad_auto_U_eje3_N1'] = createSprite(R.velocidad_auto_U_eje3_N1, self.area, self.layer3)
        self.sprites['velocidadV_eje3_N1'] = createSprite(R.velocidadV_eje3_N1, self.area, self.layer3)
        self.sprites['tiempo_eje3_N1'] = createSprite(R.tiempo_eje3_N1, self.area, self.layer3)
        self.sprites['ok_eje3_N1'] = createSprite(R.ok_eje3_N1, self.area, self.layer2)
        self.sprites['actualizar_eje3_N1'] = createSprite(R.actualizar_eje3_N1, self.area, self.layer2)
        self.sprites['casa_eje3_N1'] = createSprite(R.casa_eje3_N1, self.area, self.layer2)
        self.sprites['bombillo_eje3_N1'] = createSprite(R.bombillo_eje3_N1, self.area, self.layer2)
        self.sprites['siguiente_eje3_N1'] = createSprite(R.siguiente_eje3_N1, None, self.layer3)
        self.sprites['no_eje3_N1'] = createSpriteGif(R.no_eje3_N1, None, self.layer4)
        self.sprites['bien_eje3_N1'] = createSpriteGif(R.bien_eje3_N1, None, self.layer4)
        self.sprites['diploma_N1'] = createSprite(R.diploma_N1, None, self.layer5)
        
        
        self.labels['ldescripcion_eje3_N1'] = createLabel(R.ldescripcion_eje3_N1, self.area, self.layer4)
        self.labels['ldistancia_total_eje3_N1'] = createLabel(R.ldistancia_total_eje3_N1, self.area, self.layer4)
        self.labels['ldistancia_u_A_eje3_N1'] = createLabel(R.ldistanciaA_u_eje3_N1, self.area, self.layer4)
        self.labels['ldistancia_v_B_eje3_N1'] = createLabel(R.ldistanciaB_V_eje3_N1, self.area, self.layer4)
        self.labels['ltiempo_transcurrido_eje3_N1'] = createLabel(R.ltiempo_transcurrido_eje3_N1, self.area, self.layer4)
        self.labels['lvelocidad_auto_u_eje3_N1'] = createLabel(R.lvelocidad_auto_U_eje3_N1, self.area, self.layer4)
        self.labels['lvelocidad_v_eje3_N1'] = createLabel(R.lvelocidadV_eje3_N1, self.area, self.layer4)
        
            

        
        
        self.eje = self.data['dbcon'].getEjercicio(3)
        self.labels['ldescripcion_eje3_N1'].width=700
        self.labels['ldescripcion_eje3_N1'].multiline=True
        self.labels['ldescripcion_eje3_N1'].align = "center"
        self.labels['ldescripcion_eje3_N1'].anchor_x = "center"
        self.labels['ldescripcion_eje3_N1'].text = self.eje[1].replace("\r", "")
        self.camps = self.data['dbcon'].getCampos(self.eje[0])
        
        print(self.eje[1])
        for k in self.camps.keys():
            print(k, self.camps[k])
            if(k[0:9] == 'distancia'):
                self.labels['l'+k+"_eje3_N1"].text = str(self.camps[k] / 1000)
            elif(k[0:9] == 'velocidad'):
                self.labels['l'+k+"_eje3_N1"].text = str(math.ceil(self.camps[k] * 3.6))
        
        
        
        self.labels['ltiempo_transcurrido_eje3_N1'].text  =  str(round(float(self.camps['tiempo_transcurrido'])/3600, 2))
        
        
        rr = round(float(self.camps['velocidad_auto_u'])* 3.6, 2)
        print("*******", rr)
        self.trig = round((self.camps['max']-self.camps['min'])/50, 2)
        rmin = int( (rr - self.camps['min'])/self.trig)
        
        rmax = int( (self.camps['max']-rr)/self.trig)
        
        rtot = rmin+rmax
        
        flood = rr-(rmin*self.trig)
        
        if rtot % 2 != 0:
            rtot += 1
        
        rtot = rtot / 2
        
        self.labels['lvelocidad_auto_u_eje3_N1'].text = str(  round(flood+(rtot*self.trig),2))
        print("TRINGGGGGGGG")
        print(self.trig)
        
        
    def loadData(self):
        
        pass
        
    def go_timer(self, data):
        if(self.run):
            self.sprites['tractor1_eje3_N1'].x += 1
            self.sprites['tractor2_eje3_N1'].x -= 1
            
        #    dif = self.sprites['tractor2_eje3_N1'].x - (self.sprites['tractor1_eje3_N1'].x+self.sprites['tractor1_eje3_N1'].width) 
            if(self.po == -150):
                dif = self.sprites['tractor2_eje3_N1'].x - ((self.sprites['molino_eje3_N1'].x+self.sprites['molino_eje3_N1'].width) -self.sprites['molino_eje3_N1'].width * 1.1)
            elif(self.po == 0):
                print("ss")
                dif = self.sprites['tractor2_eje3_N1'].x - ((self.sprites['molino_eje3_N1'].x+self.sprites['molino_eje3_N1'].width) -self.sprites['molino_eje3_N1'].width * 0.6)
            else:
                dif = self.sprites['tractor2_eje3_N1'].x - ((self.sprites['molino_eje3_N1'].x+self.sprites['molino_eje3_N1'].width) -self.sprites['molino_eje3_N1'].width )
            
        
            print(self.po, dif)
            
            if( (dif-1) <= self.po and (dif+1) >= self.po ):
            #if(self.sprites['tractor1_eje3_N1'].x >= self.sprites['granja_eje3_N1'].x and self.sprites['tractor2_eje3_N1'].x <= self.sprites['molino_eje3_N1'].x ):
                if(self.po == -150):
                    self.sprites['no_eje3_N1'].batch= self.area
                elif(self.po==0):
                    self.ganar()
                    
                elif(self.po==400):
                    self.sprites['no_eje3_N1'].batch= self.area
                self.run = False
        
    
    
    def go_draw(self):
        self.area.draw()
    
    
    def go_mouse_motion(self, x, y, dx, dy):
        if self.drag != None:
            
            print(self.sprites['mano_eje3_N1'].x)
            if( (round(float(self.camps['min'])) - (round(float(self.camps['min']))*0.05) ) > round(float(self.labels['lvelocidad_auto_u_eje3_N1'].text)) or round(float(self.labels['lvelocidad_auto_u_eje3_N1'].text))  > (round(float(self.camps['max'])) + (round(float(self.camps['max']))*0.05) )):
                self.drag= None
                
                rr = round(float(self.camps['velocidad_auto_u'])* 3.6, 2)
                print("*******", rr)
                self.trig = round((self.camps['max']-self.camps['min'])/50, 2)
                rmin = int( (rr - self.camps['min'])/self.trig)
                
                rmax = int( (self.camps['max']-rr)/self.trig)
                
                rtot = rmin+rmax
                
                flood = rr-(rmin*self.trig)
                
                if rtot % 2 != 0:
                    rtot += 1
                
                rtot = rtot / 2
                
                self.labels['lvelocidad_auto_u_eje3_N1'].text = str(  round(flood+(rtot*self.trig),2))
                
                self.llx = self.R.mano_eje3_N1.x
                self.sprites['mano_eje3_N1'].x =  self.R.mano_eje3_N1.x
                self.R.zones['EJERCICIO3_N1'] ['mover_mano'] = [(self.R.mano_eje3_N1.x,self.R.mano_eje3_N1.y,self.R.mano_eje3_N1.w,self.R.mano_eje3_N1.h)]
                
                
                
            else:
                if((self.drag.x > (x-(self.drag.width // 2))) and abs(self.llx-x) >= 10):
                    #self.labels['lvelocidad_auto_u_eje3_N1'].text = str( round(float(self.labels['lvelocidad_auto_u_eje3_N1'].text) - self.trig, 2) )
                    self.labels['lvelocidad_auto_u_eje3_N1'].text = str( round(float(self.labels['lvelocidad_auto_u_eje3_N1'].text) - self.trig, 2) )
                
                    self.llx = x
                elif(self.drag.x < (x-(self.drag.width // 2)) and abs(self.llx-x) >= 10):
                    #self.labels['lvelocidad_auto_u_eje3_N1'].text = str( round(float(self.labels['lvelocidad_auto_u_eje3_N1'].text) + self.trig, 2) )
                    self.labels['lvelocidad_auto_u_eje3_N1'].text = str( round(float(self.labels['lvelocidad_auto_u_eje3_N1'].text) + self.trig, 2) )
                
                    self.llx = x
                
                self.drag.x = x-(self.drag.width // 2)
                self.R.zones['EJERCICIO3_N1'] ['mover_mano'] = [(self.drag.x, self.drag.y, self.drag.width, self.drag.height)]
                
                
        
        
    def go_mouse_press(self, x, y, b, m):
       
            
        if('siguiente_eje3_N1' in self.pics):
            self.sprites['diploma_N1'].batch= self.area 
            self.sprites['bien_eje3_N1'].batch= None 
            self.sprites['siguiente_eje3_N1'].batch= None
            self.sprites['tractor1_eje3_N1'].batch= None
            self.sprites['tractor2_eje3_N1'].batch= None
            self.sprites['tierra_eje3_N1'].batch= None
            self.sprites['granja_eje3_N1'].batch= None
            self.sprites['molino_eje3_N1'].batch= None
            self.sprites['actualizar_eje3_N1'].batch= None
            self.sprites['casa_eje3_N1'].batch= None
            self.sprites['anterior9_eje3_N1'].batch= None
            del self.R.zones['EJERCICIO3_N1'] ['ir_niveles']
            del self.R.zones['EJERCICIO3_N1'] ['ir_casa']
            del self.R.zones['EJERCICIO3_N1'] ['ir_actualizar']
            del self.R.zones['EJERCICIO3_N1'] ['ir_ok']
            self.labels['ldescripcion_eje3_N1'].text = ""
            
            
        if('terminar_nivel' in self.pics):
            self.MODE = 'NIVELES'
        if('ir_niveles' in self.pics):
            self.MODE = 'NIVELES'

        if('ir_casa' in self.pics):
            self.MODE = 'MENU'
            
        if('ir_actualizar' in self.pics):
            self.make(self.R)
        
        if('ir_ok' in self.pics):
            self.run = True
            rr = round(float(self.camps['velocidad_auto_u'])*3.6, 2)
            
            if(rr == float(self.labels['lvelocidad_auto_u_eje3_N1'].text)):
                self.po = 0
            elif(rr < float(self.labels['lvelocidad_auto_u_eje3_N1'].text)):
                self.po = -150
            else:
                self.po = 400
         
        if('ir_bombillo' in self.pics):
            pass
        if('mover_mano' in self.pics and self.drag == None):
            self.drag = self.sprites['mano_eje3_N1']
            self.llx = self.sprites['mano_eje3_N1'].x
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
    
        self.sprites['car1_campo_eje3_N1'].batch = None
        self.sprites['car2_campo_eje3_N1'].batch = None
        self.sprites['tiempo_campo_eje3_N1'].batch = None
        self.sprites['distancia_campo_eje3_N1'].batch = None
        self.sprites['mano_eje3_N1'].batch = None
        self.sprites['distancia_eje3_N1'].batch = None  
        self.sprites['distanciaA_u_eje3_N1'].batch = None
        self.sprites['vel_car2_campo_eje3_N1'].batch = None
        self.sprites['distanciaB_v_eje3_N1'].batch = None
        self.sprites['tiempo_eje3_N1'].batch = None
        
        self.sprites['velocidadV_eje3_N1'].batch = None
        self.sprites['bombillo_eje3_N1'].batch = None
        self.sprites['ok_eje3_N1'].batch = None
        self.labels['ldistancia_total_eje3_N1'].text = ""
        self.labels['ldistancia_u_A_eje3_N1'].text = ""
        self.labels['ldistancia_v_B_eje3_N1'].text = ""
        self.labels['ltiempo_transcurrido_eje3_N1'].text = ""
        self.labels['lvelocidad_v_eje3_N1'].text = ""
        self.sprites['bien_eje3_N1'].batch= self.area 
        self.sprites['siguiente_eje3_N1'].batch= self.area 
        self.R.zones['EJERCICIO3_N1'] ['siguiente_eje3_N1'] = [(self.R.siguiente_eje3_N1.x, self.R.siguiente_eje3_N1.y, self.R.siguiente_eje3_N1.w, self.R.siguiente_eje3_N1.h)]
        

    
