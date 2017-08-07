# -*- coding: utf-8 -*-

import pyglet, math
from pyglet.window import key
from src.tools import createSprite,createLabel,createSpriteGif


class Ejercicio1_n2():
    
    NAME = 'EJERCICIO1_N2'
    MODE = 'LOCAL'
    SIZE = 'CURRENT'
    
    R = None
    data = None
    top= False
    top1= False
    pics = []
    yper=0.2
    xper=1.2
    
    
    def __init__(self, data = {}):
        
        self.data = data
        self.om = None
        
        
    def make(self, R):
        pass
        
        self.drag = None
        self.run = False
        self.top = False
        self.top1 = False
        self.po = None
        self.yper =0.2
        self.xper =1.2
        
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
        self.sprites['anterior_eje1_N2'] = createSprite(R.anterior_eje1_N2, self.area, self.layer2)
        self.sprites['pinguino_eje1_N2'] = createSprite(R.pinguino_eje1_N2, self.area, self.layer4)
        self.sprites['hielo_eje1_N2'] = createSprite(R.hielo_eje1_N2, self.area, self.layer3)
        self.sprites['rio_eje1_N2'] = createSprite(R.rio_eje1_N2, self.area, self.layer2)
        self.sprites['orca_eje1_N2'] = createSprite(R.orca_eje1_N2, None, self.layer3)
        self.sprites['nevado_eje1_N2'] = createSprite(R.nevado_eje1_N2, self.area, self.layer3)
        self.sprites['iglu_eje1_N2'] = createSprite(R.iglu_eje1_N2, self.area, self.layer4)
        self.sprites['flecha_menos_eje1_N2'] = createSprite(R.flecha_menos_eje1_N2, self.area, self.layer2)
        self.sprites['flecha_mas_eje1_N2'] = createSprite(R.flecha_mas_eje1_N2, self.area, self.layer2)
        self.sprites['ok_eje1_N2'] = createSprite(R.ok_eje1_N2, self.area, self.layer2)
        self.sprites['actualizar_eje1_N2'] = createSprite(R.actualizar_eje1_N2, self.area, self.layer2)
        self.sprites['casa_eje1_N2'] = createSprite(R.casa_eje1_N2, self.area, self.layer2)
        self.sprites['bombillo_eje1_N2'] = createSprite(R.bombillo_eje1_N2, self.area, self.layer2)
        self.sprites['siguiente_eje1_N2'] = createSprite(R.siguiente_eje1_N2, None, self.layer3)
        self.sprites['no_eje1_N2'] = createSpriteGif(R.no_eje1_N2, None, self.layer4)
        self.sprites['exe_eje1_n2'] = createSpriteGif(R.exe_eje1_N2, None, self.layer4)
        self.sprites['altura_iceberg_campo_eje1_N2'] = createSprite(R.altura_iceberg_campo_eje1_N2, self.area, self.layer2)
        self.sprites['velocidad_pingui_campo_eje1_N2'] = createSprite(R.velocidad_pingui_campo_eje1_N2, self.area, self.layer2)
        self.sprites['res_campo_eje1_N2'] = createSprite(R.res_campo_eje1_N2, self.area, self.layer2)
        self.sprites['altura_eje1_N2'] = createSprite(R.altura_eje1_N2, self.area, self.layer2)
        self.sprites['velocidad_eje1_N2'] = createSprite(R.velocidad_eje1_N2, self.area, self.layer2)
        self.sprites['alcance_horizontal_eje1_N2'] = createSprite(R.alcance_horizontal_eje1_N2, self.area, self.layer2)
        
        self.labels['ldescripcion'] = createLabel(R.ldescripcion_eje1_N2, self.area, self.layer4)
        self.labels['laltura_iceberg'] = createLabel(R.laltura_eje1_N2, self.area, self.layer4)
        self.labels['lvelocidad_pingui'] = createLabel(R.lvelocidad_eje1_N2, self.area, self.layer4)
        self.labels['lalcance_horizontal'] = createLabel(R.lalcance_horizontal_eje1_N2, self.area, self.layer4)
        
        self.eje = self.data['dbcon'].getEjercicio(4)
        self.labels['ldescripcion'].width=700
        self.labels['ldescripcion'].multiline=True
        self.labels['ldescripcion'].align = "center"
        self.labels['ldescripcion'].anchor_x = "center"
        self.labels['ldescripcion'].text = self.eje[1].replace("\r", "")
        self.camps = self.data['dbcon'].getCampos(self.eje[0])
        
        print(self.eje[1])
        for k in self.camps.keys():
            print(k, self.camps[k])
            if(k[0:14] == 'altura_iceberg' ):
                self.labels['l'+k].text = str(self.camps[k])
            elif(k[0:16] == 'velocidad_pingui'):
                print("hola"+k)
                self.labels['l'+k].text = str(math.ceil(self.camps[k] * 3.6))
            
        
        rr = round(float(self.camps['alcance_horizontal']), 2)
        print("*******", rr)
        self.trig = round((self.camps['max']-self.camps['min'])/50, 2)
        rmin = int( (rr - self.camps['min'])/self.trig)
        rmax = int( (self.camps['max']-rr)/self.trig)
        rtot = rmin+rmax
        
        flood = rr-(rmin*self.trig)
        
        if rtot % 2 != 0:
            rtot += 1
        
        rtot = rtot / 2
        
        self.labels['lalcance_horizontal'].text = str(round(flood+(rtot*self.trig), 2))
        
        
        
        
    def loadData(self):
        
        pass
        
    def go_timer(self, data):
        
        if(self.run):

            if(self.po == -150):
                
                topx1= self.sprites['hielo_eje1_N2'].x + (self.sprites['hielo_eje1_N2'].width * 2) 
                topy1= self.sprites['hielo_eje1_N2'].y + (self.sprites['hielo_eje1_N2'].height+ (self.sprites['hielo_eje1_N2'].height *0.001))
                
                topx2= self.sprites['hielo_eje1_N2'].x + (self.sprites['hielo_eje1_N2'].width * 1.1) 
                topy2= self.sprites['hielo_eje1_N2'].y + (self.sprites['hielo_eje1_N2'].height + (self.sprites['hielo_eje1_N2'].height *0.02) )
                
                topx3= self.sprites['hielo_eje1_N2'].x + (self.sprites['hielo_eje1_N2'].width * 2.5) 
                #topy3= self.sprites['hielo_eje1_N2'].y + (self.sprites['hielo_eje1_N2'].width  ) 
                topy3= self.sprites['orca_eje1_N2'].y 
                
                difx = self.sprites['orca_eje1_N2'].x + (self.sprites['orca_eje1_N2'].width /2)
                dify = self.sprites['orca_eje1_N2'].y 
                if(self.top== False):
                    
                    
                    if( self.sprites['pinguino_eje1_N2'].y < topy1 and self.top1== False):
                        self.sprites['pinguino_eje1_N2'].x += 1
                        self.sprites['pinguino_eje1_N2'].y += self.yper
                        self.yper += 0.0005
                        
                        print("top1" , self.yper)
                   
                    elif( self.sprites['pinguino_eje1_N2'].y > topy3):
                        self.sprites['pinguino_eje1_N2'].x += self.xper
                        self.sprites['pinguino_eje1_N2'].y -= self.yper
                        self.top1 =True
                        
                        self.yper +=0.01
                        
                        self.xper -=0.005
                        print("top3y", self.yper)
                        print("top3x", self.xper)
                    else:
                        self.top= True
                else:
                    
                    if( self.sprites['pinguino_eje1_N2'].y > dify):
                        self.sprites['pinguino_eje1_N2'].y -= 0.9
                    
                    
                    
            elif(self.po == 0):
                
                topx1= self.sprites['hielo_eje1_N2'].x + (self.sprites['hielo_eje1_N2'].width * 2) 
                topy1= self.sprites['hielo_eje1_N2'].y + (self.sprites['hielo_eje1_N2'].height+ (self.sprites['hielo_eje1_N2'].height *0.001))
                
                topx2= self.sprites['hielo_eje1_N2'].x + (self.sprites['hielo_eje1_N2'].width * 1.1) 
                topy2= self.sprites['hielo_eje1_N2'].y + (self.sprites['hielo_eje1_N2'].height + (self.sprites['hielo_eje1_N2'].height *0.02) )
                
                topx3= self.sprites['hielo_eje1_N2'].x + (self.sprites['hielo_eje1_N2'].width * 2.5) 
                #topy3= self.sprites['hielo_eje1_N2'].y + (self.sprites['hielo_eje1_N2'].width  ) 
                topy3= self.sprites['iglu_eje1_N2'].y 
                
                difx = self.sprites['iglu_eje1_N2'].x + (self.sprites['iglu_eje1_N2'].width /2)
                dify = self.sprites['iglu_eje1_N2'].y 
                if(self.top== False):
                    
                    
                    if( self.sprites['pinguino_eje1_N2'].y < topy1 and self.top1== False):
                        self.sprites['pinguino_eje1_N2'].x += 1
                        self.sprites['pinguino_eje1_N2'].y += self.yper
                        self.yper += 0.0005
                        
                        print("top1" , self.yper)
                   
                    elif( self.sprites['pinguino_eje1_N2'].y > topy3):
                        self.sprites['pinguino_eje1_N2'].x += self.xper
                        self.sprites['pinguino_eje1_N2'].y -= self.yper
                        self.top1 =True
                        #ld
                        if(self.sprites['iglu_eje1_N2'].x==470):
                            self.yper +=0.011
                        #bd
                        elif(self.sprites['iglu_eje1_N2'].x==612):
                            self.yper +=0.006
                        #hd
                        elif(self.sprites['iglu_eje1_N2'].x==820):
                            self.yper +=0.004
                        
                        self.xper -=0.00001
                        print("top3y", self.yper)
                        print("top3x", self.xper)
                    else:
                        self.top= True
                else:
                    
                    if( self.sprites['pinguino_eje1_N2'].y > dify):
                        self.sprites['pinguino_eje1_N2'].y -= 0.9
                    
                    
            else:
                
                topx1= self.sprites['hielo_eje1_N2'].x + (self.sprites['hielo_eje1_N2'].width * 2) 
                topy1= self.sprites['hielo_eje1_N2'].y + (self.sprites['hielo_eje1_N2'].height+ (self.sprites['hielo_eje1_N2'].height *0.001))
                
                topx2= self.sprites['hielo_eje1_N2'].x + (self.sprites['hielo_eje1_N2'].width * 1.1) 
                topy2= self.sprites['hielo_eje1_N2'].y + (self.sprites['hielo_eje1_N2'].height + (self.sprites['hielo_eje1_N2'].height *0.02) )
                
                topx3= self.sprites['hielo_eje1_N2'].x + (self.sprites['hielo_eje1_N2'].width * 2.5) 
                #topy3= self.sprites['hielo_eje1_N2'].y + (self.sprites['hielo_eje1_N2'].width  ) 
                topy3= self.sprites['iglu_eje1_N2'].y 
                
                difx = self.sprites['iglu_eje1_N2'].x + (self.sprites['iglu_eje1_N2'].width /2)
                dify = self.sprites['iglu_eje1_N2'].y -1
                if(self.top== False):
                    
                    
                    if( self.sprites['pinguino_eje1_N2'].y < topy1 and self.top1== False):
                        self.sprites['pinguino_eje1_N2'].x += 1
                        self.sprites['pinguino_eje1_N2'].y += self.yper
                        self.yper += 0.0005
                        
                        print("top1" , self.yper)
                   
                    elif( self.sprites['pinguino_eje1_N2'].y > topy3):
                        self.sprites['pinguino_eje1_N2'].x += self.xper
                        self.sprites['pinguino_eje1_N2'].y -= self.yper
                        self.top1 =True
                        
                        
                        
                        self.yper +=0.0007
                        
                        if(self.sprites['iglu_eje1_N2'].x==470):
                            self.xper -=0.001
                        #bd
                        elif(self.sprites['iglu_eje1_N2'].x==612):
                            self.xper -=0.0005
                        #hd
                        elif(self.sprites['iglu_eje1_N2'].x==820):
                            self.xper -=0.00005
                        
                        
                        
                        print("top3y", self.yper)
                        print("top3x", self.xper)
                    else:
                        self.top= True
                else:
                    
                    if( self.sprites['pinguino_eje1_N2'].y > dify):
                        self.sprites['pinguino_eje1_N2'].y -= 0.9
                    
                    
            
            
            
            #if( (dif-1) <= self.po and (dif+1) >= self.po ):
            if( self.sprites['pinguino_eje1_N2'].y <= dify ):
                if(self.po == -150):
                    self.sprites['orca_eje1_N2'].batch= self.area
                    self.sprites['pinguino_eje1_N2'].batch= None
                elif(self.po==0):
                    self.ganar()
                    
                elif(self.po==400):
                    self.sprites['no_eje1_N2'].batch= self.area
                self.run = False
            
    
            
    
    def go_draw(self):
        self.area.draw()
    
    
    def go_mouse_motion(self, x, y, dx, dy):
        pass
        
    def go_mouse_press(self, x, y, b, m):
        
        if('ir_niveles' in self.pics):
            self.MODE = 'NIVELES'
            
        if('siguiente_eje1_N2' in self.pics):
            self.MODE = 'EJERCICIO2_N2'
            
        if('ir_casa' in self.pics):
            self.MODE = 'MENU'
            
        if('ir_actualizar' in self.pics):
            self.make(self.R)
        
            
        if('ir_bombillo' in self.pics):
            pass
        if('mas' in self.pics):
            self.labels['lalcance_horizontal'].text = str( round(float(self.labels['lalcance_horizontal'].text) + self.trig, 2) )
        if('menos' in self.pics):
            self.labels['lalcance_horizontal'].text = str( round(float(self.labels['lalcance_horizontal'].text) - self.trig, 2) )
            
        if('ir_ok' in self.pics):
            self.run = True
            rr = round(float(self.camps['alcance_horizontal']), 2)
            if(rr == float(self.labels['lalcance_horizontal'].text)):
                self.po = 0
            elif(float(self.labels['lalcance_horizontal'].text) < rr):
                self.po = -150
            else:
                self.po = 400
        
        
           
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
        self.sprites['exe_eje1_n2'].batch= self.area 
        self.sprites['siguiente_eje1_N2'].batch= self.area 
        self.R.zones['EJERCICIO1_N2'] ['siguiente_eje1_N2'] = [(self.R.siguiente_eje1_N2.x, self.R.siguiente_eje1_N2.y, self.R.siguiente_eje1_N2.w, self.R.siguiente_eje1_N2.h)]
        self.sprites['flecha_menos_eje1_N2'].batch = None
        self.sprites['bombillo_eje1_N2'].batch = None
        self.sprites['flecha_mas_eje1_N2'].batch = None
        self.sprites['altura_iceberg_campo_eje1_N2'].batch = None
        self.sprites['velocidad_pingui_campo_eje1_N2'].batch = None
        self.sprites['altura_eje1_N2'].batch = None
        self.sprites['velocidad_eje1_N2'].batch = None
        self.labels['lvelocidad_pingui'].text = ""
        self.labels['laltura_iceberg'].text = ""
 
