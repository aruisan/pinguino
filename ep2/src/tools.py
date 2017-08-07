# -*- coding: utf-8 -*-

import re
import pyglet

def getResol(path):
    f = open(path, 'r')
    d = f.read()
    f.close()
    
    pw = re.compile("width=[0-9]*")
    ph = re.compile("height=[0-9]*")
    
    mw = pw.search(d).group(0)
    mh = ph.search(d).group(0)
    
    return (int(mw.split('=')[1]), int(mh.split('=')[1]))

def setResol(path, w, h):
    f = open(path, 'r')
    d = f.read()
    f.close()
    
    pw = re.compile("width=[0-9]*")
    ph = re.compile("height=[0-9]*")
    
    mw = pw.search(d).group(0)
    mh = ph.search(d).group(0)
    
    d = d.replace(mw, "width="+str(w))
    d = d.replace(mh, "height="+str(h))
    
    f = open(path, 'w')
    f.write(d)
    f.close()

def trazer(zones, x, y):
    
    res = []
    
    for k in zones.keys():
        flag = False
        
        for t in zones[k]:
            if( (t[0] <= x and x <= (t[0]+t[2])) and (t[1] <= y and y <= (t[1]+t[3])) ):
                flag = True
                break
            
        if(flag):
            res.append(k)
    
    return res
    
def createSprite(obj, batch, layer):
    
    img = pyglet.resource.image(obj.path)
    img.width = obj.w
    img.height = obj.h
    return pyglet.sprite.Sprite(img, x=obj.x, y=obj.y, batch=batch, group=layer)

def createLabel(obj, batch, layer):
    return pyglet.text.Label(obj.text, font_name=obj.fname , color=obj.color, font_size=obj.fsize, x=obj.x, y=obj.y, batch=batch, group=layer)

def createSpriteGif(obj, batch, layer):
    
    img = pyglet.resource.animation(obj.path)
    img.width = obj.w
    img.height = obj.h
    return pyglet.sprite.Sprite(img, x=obj.x, y=obj.y, batch=batch, group=layer)
