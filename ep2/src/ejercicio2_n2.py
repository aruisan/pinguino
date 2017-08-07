# -*- coding: utf-8 -*-

import pyglet, math
from pyglet.window import key
from src.tools import createSprite,createLabel,createSpriteGif


class Ejercicio2_n2():
    
    NAME = 'EJERCICIO2_N2'
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
        self.sprites['anterior_eje2_N2'] = createSprite(R.anterior_eje2_N2, self.area, self.layer4)
        self.sprites['abismo1_eje2_N2'] = createSprite(R.abismo1_eje2_N2, self.area, self.layer3)
        self.sprites['abismo2_eje2_N2'] = createSprite(R.abismo2_eje2_N2, self.area, self.layer3)
        self.sprites['piedra_eje2_N2'] = createSprite(R.piedra_eje2_N2, self.area, self.layer4)
        self.sprites['monster_eje2_N2'] = createSprite(R.monster_eje2_N2, self.area, self.layer5)
        self.sprites['monster1_eje2_N2'] = createSprite(R.monster1_eje2_N2, None, self.layer5)
        self.sprites['monster2_eje2_N2'] = createSprite(R.monster2_eje2_N2, None, self.layer5)
        self.sprites['monster3_eje2_N2'] = createSprite(R.monster3_eje2_N2, None, self.layer5)
        self.sprites['monster4_eje2_N2'] = createSprite(R.monster4_eje2_N2, None, self.layer5)
        self.sprites['monster5_eje2_N2'] = createSprite(R.monster5_eje2_N2, self.area, self.layer5)
        self.sprites['monster6_eje2_N2'] = createSprite(R.monster6_eje2_N2, self.area, self.layer5)
        self.sprites['sombra_eje2_N2'] = createSprite(R.sombra_eje2_N2, self.area, self.layer4)
        self.sprites['rocas_eje2_N2'] = createSprite(R.rocas_eje2_N2, self.area, self.layer2)
        self.sprites['flecha_mas_eje2_N2'] = createSprite(R.flecha_mas_eje2_N2, self.area, self.layer2)
        self.sprites['flecha_menos_eje2_N2'] = createSprite(R.flecha_menos_eje2_N2, self.area, self.layer2)
        self.sprites['altura_colina_campo_eje2_N2'] = createSprite(R.altura_colina_campo_eje2_N2, self.area, self.layer2)
        self.sprites['angulo_campo_eje2_N2'] = createSprite(R.angulo_campo_eje2_N2, self.area, self.layer2)
        self.sprites['res_campo_eje2_N2'] = createSprite(R.res_campo_eje2_N2, self.area, self.layer2)
        self.sprites['altura_colina_eje2_N2'] = createSprite(R.altura_colina_eje2_N2, self.area, self.layer2)
        self.sprites['angulo_eje2_N2'] = createSprite(R.angulo_eje2_N2, self.area, self.layer2)
        self.sprites['velocidad_eje2_N2'] = createSprite(R.velocidad_eje2_N2, self.area, self.layer2)
        self.sprites['ok_eje2_N2'] = createSprite(R.ok_eje2_N2, self.area, self.layer2)
        self.sprites['actualizar_eje2_N2'] = createSprite(R.actualizar_eje2_N2, self.area, self.layer2)
        self.sprites['casa_eje2_N2'] = createSprite(R.casa_eje2_N2, self.area, self.layer2)
        self.sprites['bombillo_eje2_N2'] = createSprite(R.bombillo_eje2_N2, self.area, self.layer4)
        self.sprites['siguiente_eje2_N2'] = createSprite(R.siguiente_eje2_N2, None, self.layer4)
        self.sprites['no_eje2_N2'] = createSpriteGif(R.no_eje2_N2, None, self.layer5)
        self.sprites['exe_eje2_n2'] = createSpriteGif(R.exe_eje2_N2, None, self.layer5)
        self.sprites['explosion_eje2_n2'] = createSpriteGif(R.explosion_eje2_N2, None, self.layer5)
        
        self.labels['ldescripcion'] = createLabel(R.ldescripcion_eje2_N2, self.area, self.layer4)
        self.labels['laltura_colina'] = createLabel(R.laltura_eje2_N2, self.area, self.layer4)
        self.labels['langulo_elevacion'] = createLabel(R.langulo_elevacion_eje2_N2, self.area, self.layer4)
        self.labels['lvelocidad_auto'] = createLabel(R.lvelocidad_eje2_N2, self.area, self.layer4)
        
        self.eje = self.data['dbcon'].getEjercicio(5)
        self.labels['ldescripcion'].width=700
        self.labels['ldescripcion'].multiline=True
        self.labels['ldescripcion'].align = "center"
        self.labels['ldescripcion'].anchor_x = "center"
        self.labels['ldescripcion'].text = self.eje[1].replace("\r", "")
        self.camps = self.data['dbcon'].getCampos(self.eje[0])
        self.camps = self.data['dbcon'].getCampos(self.eje[0])
        print(self.eje[1])
        for k in self.camps.keys():
            print(k, self.camps[k])
            if(k[0:13] == 'altura_colina' ):
                self.labels['l'+k].text = str(self.camps[k])
            elif(k[0:16] == 'angulo_elevacion'):
                print("hola"+k)
                self.labels['l'+k].text = str(math.ceil(self.camps[k] ))
            
        
        rr = round(float(self.camps['velocidad_auto']), 2)
        print("*******", rr)
        self.trig = round((self.camps['max']-self.camps['min'])/50, 2)
        rmin = int( (rr - self.camps['min'])/self.trig)
        rmax = int( (self.camps['max']-rr)/self.trig)
        rtot = rmin+rmax
        
        flood = rr-(rmin*self.trig)
        
        if rtot % 2 != 0:
            rtot += 1
        
        rtot = rtot / 2
        
        self.labels['lvelocidad_auto'].text = str(round(flood+(rtot*self.trig), 2))
        
        
        
        
    def loadData(self):
        
        pass
        
    def go_timer(self, data):
        if(self.run):
            #si la trompa del carro es menor al x de la piedra, entonces corra el carro hacia adelante
            if(self.sprites['monster_eje2_N2'].x + self.sprites['monster_eje2_N2'].width < self.sprites['piedra_eje2_N2'].x ):
                self.sprites['monster_eje2_N2'].x += 1
            #cuando sean iguales los x de la trompa y la piedra
            else:
                #ingresa aca una sola vez
                if(self.run2 == False):
                    #se oculta el carro horizontal y aparece el diagonal
                    self.sprites['monster_eje2_N2'].batch= None
                    self.sprites['monster4_eje2_N2'].batch= self.area
                    self.run2= True
                #si la respuesta es menor a la respuesta correcta
                if(self.po == -150):
                    #se desplaza en diagonal hasta cuando el x del carro llegue al ultimo borde la roca
                    if(self.sprites['monster4_eje2_N2'].x < (self.sprites['piedra_eje2_N2'].x + (self.sprites['piedra_eje2_N2'].width)) ):
                        self.sprites['monster4_eje2_N2'].x += 1
                        self.sprites['monster4_eje2_N2'].y += 0.3
                    #cuando llegue al borde de la roca 
                    else:
                        #ingresa aca una sola vez, para cambiar los carros 
                        if(self.run3 == False):
                            self.sprites['monster_eje2_N2'].x = self.sprites['monster4_eje2_N2'].x 
                            self.sprites['monster_eje2_N2'].y = self.sprites['monster4_eje2_N2'].y
                            self.sprites['monster_eje2_N2'].batch= self.area
                            self.sprites['monster4_eje2_N2'].batch= None
                            self.run3= True
                        #empieza a bajar el y del carro hhorizontal hasta que llegue al y de la explosion
                        if(self.sprites['monster_eje2_N2'].y > (self.sprites['explosion_eje2_n2'].y + (self.sprites['explosion_eje2_n2'].width* 0.2))):
                            self.sprites['monster_eje2_N2'].y -= 1
                            self.sprites['monster_eje2_N2'].x += 0.15
                        else:
                            self.sprites['explosion_eje2_n2'].batch= self.area
                    
                elif(self.po == 0):
                    #se desplaza en diagonal hasta cuando el x del carro llegue al ultimo borde la roca
                    if(self.sprites['monster4_eje2_N2'].x < (self.sprites['piedra_eje2_N2'].x + (self.sprites['piedra_eje2_N2'].width)) ):
                        self.sprites['monster4_eje2_N2'].x += 1
                        self.sprites['monster4_eje2_N2'].y += 0.4
                    #cuando llegue al borde de la roca 
                    else:
                        #ingresa aca una sola vez, para cambiar los carros 
                        if(self.run3 == False):
                            self.sprites['monster_eje2_N2'].x = self.sprites['monster4_eje2_N2'].x 
                            self.sprites['monster_eje2_N2'].y = self.sprites['monster4_eje2_N2'].y
                            self.sprites['monster_eje2_N2'].batch= self.area
                            self.sprites['monster4_eje2_N2'].batch= None
                            self.run3= True
                        #empieza a bajar el y del carro hhorizontal hasta que llegue al y de la explosion
                        if(self.sprites['monster_eje2_N2'].y > (self.sprites['sombra_eje2_N2'].y )):
                            self.sprites['monster_eje2_N2'].y -= 0.45
                            self.sprites['monster_eje2_N2'].x += 1
                        elif(self.sprites['monster_eje2_N2'].x <= (self.sprites['sombra_eje2_N2'].x )):
                            self.sprites['monster_eje2_N2'].x += 1
                        else:
                            self.ganar();
                elif(self.po == 400):
                    #se desplaza en diagonal hasta cuando el x del carro llegue al ultimo borde la roca
                    if(self.sprites['monster4_eje2_N2'].x < (self.sprites['piedra_eje2_N2'].x + (self.sprites['piedra_eje2_N2'].width*1.2)) ):
                        self.sprites['monster4_eje2_N2'].x += 1
                        self.sprites['monster4_eje2_N2'].y += 0.5
                    #cuando llegue al borde de la roca 
                    else:
                        #ingresa aca una sola vez, para cambiar los carros 
                        if(self.run3 == False):
                            self.sprites['monster_eje2_N2'].x = self.sprites['monster4_eje2_N2'].x 
                            self.sprites['monster_eje2_N2'].y = self.sprites['monster4_eje2_N2'].y
                            self.sprites['monster_eje2_N2'].batch= self.area
                            self.sprites['monster4_eje2_N2'].batch= None
                            self.run3= True
                        #empieza a bajar el y del carro hhorizontal hasta que llegue al y de la explosion
                        if(self.sprites['monster_eje2_N2'].y > (self.sprites['sombra_eje2_N2'].y )):
                            self.sprites['monster_eje2_N2'].y -= 0.5
                            self.sprites['monster_eje2_N2'].x += 1.3
                        
                        else:
                            self.sprites['no_eje2_N2'].batch= self.area
                                
                                
                
    
    def go_draw(self):
        self.area.draw()
    
    
    def go_mouse_motion(self, x, y, dx, dy):
        pass
        
        
    def go_mouse_press(self, x, y, b, m):
        
        if('ir_niveles' in self.pics):
            self.MODE = 'NIVELES'
            
        if('siguiente_eje2_N2' in self.pics):
            self.MODE = 'EJERCICIO3_N2'
            
        if('ir_casa' in self.pics):
            self.MODE = 'MENU'
            
        if('ir_actualizar' in self.pics):
            self.make(self.R)
        
            
        if('ir_bombillo' in self.pics):
            pass
            
        if('ir_ok' in self.pics):
            self.run = True
            rr = round(float(self.camps['velocidad_auto']), 2)
            if(rr == float(self.labels['lvelocidad_auto'].text)):
                self.po = 0
            elif(float(self.labels['lvelocidad_auto'].text) < rr):
                self.po = -150
            else:
                self.po = 400
        
        if('mas' in self.pics):
            self.labels['lvelocidad_auto'].text = str( round(float(self.labels['lvelocidad_auto'].text) + self.trig, 2) )
        if('menos' in self.pics):
            self.labels['lvelocidad_auto'].text = str( round(float(self.labels['lvelocidad_auto'].text) - self.trig, 2) )
    
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
        self.sprites['exe_eje2_n2'].batch= self.area 
        self.sprites['siguiente_eje2_N2'].batch= self.area 
        self.R.zones['EJERCICIO2_N2'] ['siguiente_eje2_N2'] = [(self.R.siguiente_eje1_N2.x, self.R.siguiente_eje1_N2.y, self.R.siguiente_eje1_N2.w, self.R.siguiente_eje1_N2.h)]
        self.sprites['flecha_menos_eje2_N2'].batch = None
        self.sprites['flecha_mas_eje2_N2'].batch = None
        self.sprites['bombillo_eje2_N2'].batch = None
        self.sprites['altura_colina_campo_eje2_N2'].batch = None
        self.sprites['angulo_campo_eje2_N2'].batch = None
        self.sprites['altura_colina_eje2_N2'].batch = None
        self.sprites['angulo_eje2_N2'].batch = None
        self.labels['laltura_colina'].text = ""
        self.labels['langulo_elevacion'].text = ""
