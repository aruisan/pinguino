# -*- coding: utf-8 -*-

import pyglet
from src.tools import getResol, setResol
from src.frame import Frame
from src.launcher import AppLauncher
from src.registro import Registro
from src.menu import Menu
from src.principal import Principal
from src.ajustes import Ajustes
from src.login import Login 
from src.ayuda import Ayuda
from src.db import DB
from src.niveles import Niveles
from src.nivel1 import Nivel1
from src.ejercicio2_n1 import Ejercicio2_n1
from src.ejercicio3_n1 import Ejercicio3_n1
from src.ejercicio1_n2 import Ejercicio1_n2
from src.ejercicio2_n2 import Ejercicio2_n2
from src.ejercicio3_n2 import Ejercicio3_n2
from src.ejercicio1_n3 import Ejercicio1_n3
from src.ejercicio2_n3 import Ejercicio2_n3
from src.ejercicio3_n3 import Ejercicio3_n3

class Shell():
    
    window = None
    sucket = None
    MW = 0
    MH = 0
    
    
    def __init__(self):
        
        pyglet.resource.path = ['./res']
        pyglet.resource.reindex()
        
        self.db = DB('localhost', 3306, 'fisica', 'qwe123iop', 'fisica')
        
        platform = pyglet.window.get_platform()
        display = platform.get_default_display()
        self.MW = display.get_screens()[0].width
        self.MH = display.get_screens()[0].height
        
        pyglet.clock.schedule(self.timer)
        self.activateSuck()
        self.window = Frame(self, 400, 400, False, visible=False)
        self.window.set_location(int((self.MW-self.window.width)/2), int((self.MH-self.window.height)/2))
        self.window.setScene(AppLauncher())
        self.window.set_visible(True)
    
    
    def timer(self,data):
        
        if(self.window != None):
            
            if(self.window.scene != None):
                
                if(self.window.scene.MODE != 'LOCAL'):
                    self.switchScene()
                
                if(self.window.scene.SIZE != 'CURRENT'):
                    
                    if(self.window.scene.SIZE == 'WIN'):
                        self.window.set_fullscreen(False)
                        self.window.set_location(int((self.MW-self.window.width)/2), int((self.MH-self.window.height)/2))
                    
                    elif (self.window.scene.SIZE == 'LD'):
                        self.changeResolution(800, 600)
                    
                    elif (self.window.scene.SIZE == 'BD'):
                        self.changeResolution(1024, 768)
                    
                    elif (self.window.scene.SIZE == 'HD'):
                        self.changeResolution(1366, 768)
                    
                    self.window.scene.SIZE = 'CURRENT'
            
            self.window.timer(data)
    
    
    def activateSuck(self):
        self.sucket = pyglet.window.Window(self.MW, self.MH, fullscreen=True)
        self.sucket.set_visible(False)
    
    
    def run(self):
        pyglet.app.run()
    
    
    def switchScene(self):
        
        preData = self.window.scene.data
        
        if(self.window.scene.NAME == 'LAUNCHER'):
            
            if(self.window.scene.MODE == 'MENU'):
                w, h = getResol('./cnf/config.ini')
                self.window.scene = None
                self.changeResolution(w, h)
                self.window.setScene(Menu(preData))
        else:
                
            if(self.window.scene.MODE == 'AJUSTES'):
                self.window.setScene(Ajustes(preData))
                
            if(self.window.scene.MODE == 'PRINCIPAL'):
                self.window.setScene(Principal(preData))
                
            if(self.window.scene.MODE == 'AYUDA'):
                self.window.setScene(Ayuda(preData))
                
            if(self.window.scene.MODE == 'MENU'):
                self.window.setScene(Menu(preData))
                
            if(self.window.scene.MODE == 'REGISTRO'):
                preData['dbcon'] = self.db
                self.window.setScene(Registro(preData))
                
            if(self.window.scene.MODE == 'LOGIN'):
                preData['dbcon'] = self.db
                self.window.setScene(Login(preData))
            
            if(self.window.scene.MODE == 'NIVELES'):
                preData['dbcon'] = self.db
                self.window.setScene(Niveles(preData))
                
            if(self.window.scene.MODE == 'NIVEL1'):
                self.window.setScene(Nivel1(preData))
                
            if(self.window.scene.MODE == 'EJERCICIO2_N1'):
                self.window.setScene(Ejercicio2_n1(preData))
                
            if(self.window.scene.MODE == 'EJERCICIO3_N1'):
                self.window.setScene(Ejercicio3_n1(preData))
                
            if(self.window.scene.MODE == 'EJERCICIO1_N2'):
                self.window.setScene(Ejercicio1_n2(preData))
                
            if(self.window.scene.MODE == 'EJERCICIO2_N2'):
                self.window.setScene(Ejercicio2_n2(preData))
    
            if(self.window.scene.MODE == 'EJERCICIO3_N2'):
                self.window.setScene(Ejercicio3_n2(preData))
            
            if(self.window.scene.MODE == 'EJERCICIO1_N3'):
                self.window.setScene(Ejercicio1_n3(preData))    
                
            if(self.window.scene.MODE == 'EJERCICIO2_N3'):
                self.window.setScene(Ejercicio2_n3(preData))   
                
            if(self.window.scene.MODE == 'EJERCICIO3_N3'):
                self.window.setScene(Ejercicio3_n3(preData))   
                
    def changeResolution(self, width, height, full = True, debug = False, logpos = True):
        
        scene = None
        if(self.window.scene != None):
            scene = self.window.scene
        
        self.window.set_fullscreen(False)
        self.window.close()
        self.window = Frame(self, width, height, full, debug, logpos)
        
        if(scene != None):
            self.window.setScene(scene)
        
        setResol('./cnf/config.ini', width, height)
    
    
    def run_close(self):
        self.sucket.close()
    
