# -*- coding: utf-8 -*-

import pyglet
from pyglet.window import key

from cnf.resol import resol as rconfig
from src.tools import trazer

class Frame(pyglet.window.Window):
    
    app = None
    scene = None
    R = None
    P = None
    L = None
    
    _view_hwnd = None
    
    
    def __init__(self, app, width, height, full = True, debug = False, logpos = True, visible=True):
        
        self.app = app
        
        super(Frame, self).__init__(width, height, fullscreen=full, visible=visible)
        self.set_mouse_visible(False)
        
        if(debug):
            self.push_handlers(pyglet.window.event.WindowEventLogger())
        
        self.R = rconfig[self.getResolution()]
        R = self.R
        
        self.area = pyglet.graphics.Batch()
        self.layer10 = pyglet.graphics.OrderedGroup(9)
        
        img = pyglet.resource.image(R.puntero.path)
        img.width = R.puntero.w
        img.height = R.puntero.h
        self.P = pyglet.sprite.Sprite(img, x=R.puntero.x, y=R.puntero.y, batch=self.area, group=self.layer10) 
        
        if(logpos):
            self.L = pyglet.text.Label('', font_name = 'monospace', color = (255, 0, 0, 255), font_size = 10, x= 10, y= 10, batch = self.area, group = self.layer10)
            
            
    def getResolution(self):
        return str(self.width)+"x"+str(self.height)
    
    
    def setScene(self, scene):
        scene.make(self.R)
        scene.loadData()
        self.scene = scene
    
    
    def timer(self, data):
        
        if(self.scene != None):
            self.scene.go_timer(data)
            
            
    def on_draw(self):
        self.clear()
        
        if(self.scene != None):
            self.scene.go_draw()
        
        self.area.draw()
    
    
    def on_mouse_motion(self, x, y, dx, dy):
        
        if(self.L != None):
            self.L.text = "("+str(self.width)+" x "+str(self.height)+"): "+str(x)+" , "+str(y)
        
        self.P.x = x
        self.P.y = y-self.R.puntero.h
        
        if(self.scene != None):
            self.scene.go_mouse_motion(x, y, dx, dy)
    
    
    def on_mouse_press(self, x, y, b, m):
        
        self.scene.pics = trazer(self.R.zones[self.scene.NAME], x, y)
        print(self.scene.pics)
        
        if(self.scene != None):
            self.scene.go_mouse_press(x, y, b, m)
    
    
    def on_key_press(self, symbol, modifiers):
        
        if(symbol != key.ESCAPE):
            if(self.scene != None):
                self.scene.go_key_press(symbol, modifiers)
        else:
            self.xclose()
    
    
    def on_text(self, text):
        
        if(self.scene != None):
            self.scene.go_text(text)
    
    
    def on_text_motion(self, motion):
        
        if(self.scene != None):
            self.scene.go_text_motion(motion)
    
    
    def on_close(self):
        self.xclose()
    
        
    def xclose(self):
        
        print("Exit!.")
        self.close()
        self.app.run_close()
    
