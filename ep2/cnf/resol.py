# -*- coding: utf-8 -*-

from cnf.meta import MetaConfig, MetaData

hd = MetaConfig()
hd.NS = 'HD'
bd = MetaConfig()
bd.NS = 'BD'
ld = MetaConfig()
ld.NS = 'LD'
lu = MetaConfig()

#=====================================================================

lu.puntero = MetaData()
lu.puntero.path = 'img/cursor.png'
lu.puntero.w = 25
lu.puntero.h = 25
lu.puntero.x = 300
lu.puntero.y = 100

ld.puntero = MetaData()
ld.puntero.path = 'img/cursor.png'
ld.puntero.w = 30
ld.puntero.h = 30
ld.puntero.x = 400
ld.puntero.y = 300

bd.puntero = MetaData()
bd.puntero.path = 'img/cursor.png'
bd.puntero.w = 40
bd.puntero.h = 40
bd.puntero.x = 512
bd.puntero.y = 384

hd.puntero = MetaData()
hd.puntero.path = 'img/cursor.png'
hd.puntero.w = 50
hd.puntero.h = 50
hd.puntero.x = 683
hd.puntero.y = 384

#=====================================================================
lu.fondo = MetaData()
lu.fondo.path = 'img/fondo.png'
lu.fondo.w = 400
lu.fondo.h = 400
lu.fondo.x = 0
lu.fondo.y = 0

lu.logo = MetaData()
lu.logo.path = 'img/logo.png'
lu.logo.w = 128
lu.logo.h = 122
lu.logo.x = 136
lu.logo.y = 139

lu.titulo = MetaData()
lu.titulo.path = 'img/titulo.png'
lu.titulo.w = 350
lu.titulo.h = 100
lu.titulo.x = 25
lu.titulo.y = 250


lu.mensaje = MetaData()
lu.mensaje.text = 'PULSE "ENTER" PARA INICIAR'
lu.mensaje.color = (17, 33, 98, 255)
lu.mensaje.fname = 'Comic Sans MS'
lu.mensaje.fsize = 14
lu.mensaje.x = 60
lu.mensaje.y = 110

lu.zones = {}
lu.zones['LAUNCHER'] = {}
lu.zones['LAUNCHER'] ['logo'] = [(136, 139, 128, 122)]

#=====================================================================
# REGISTRO DE USUARIO 800X600
#=====================================================================

ld.fondo = MetaData()
ld.fondo.path = 'img/fondo.png'
ld.fondo.w = 800
ld.fondo.h = 600
ld.fondo.x = 0
ld.fondo.y = 0

ld.registro = MetaData()
ld.registro.path = 'img/registro.png'
ld.registro.w = 336
ld.registro.h = 70
ld.registro.x = 232
ld.registro.y = 530

ld.nombre = MetaData()
ld.nombre.path = 'img/nombre.png'
ld.nombre.w = 122
ld.nombre.h = 49
ld.nombre.x = 10
ld.nombre.y = 480

ld.apellido = MetaData()
ld.apellido.path = 'img/apellido.png'
ld.apellido.w = 127
ld.apellido.h = 54
ld.apellido.x = 10
ld.apellido.y = 420

ld.correo = MetaData()
ld.correo.path = 'img/correo.png'
ld.correo.w = 107
ld.correo.h = 48
ld.correo.x = 10
ld.correo.y = 360

ld.clave = MetaData()
ld.clave.path = 'img/clave.png'
ld.clave.w = 92
ld.clave.h = 49
ld.clave.x = 10
ld.clave.y = 300

ld.verificar = MetaData()
ld.verificar.path = 'img/verificar.png'
ld.verificar.w = 134
ld.verificar.h = 48
ld.verificar.x = 10
ld.verificar.y = 240

ld.grado = MetaData()
ld.grado.path = 'img/grado.png'
ld.grado.w = 100
ld.grado.h = 49
ld.grado.x = 10
ld.grado.y = 180

ld.rol = MetaData()
ld.rol.path = 'img/rol.png'
ld.rol.w = 65
ld.rol.h = 49
ld.rol.x = 10
ld.rol.y = 120

ld.guardar = MetaData()
ld.guardar.path = 'img/guardar.png'
ld.guardar.w = 149
ld.guardar.h = 89
ld.guardar.x = 641
ld.guardar.y = 10

ld.anterior = MetaData()
ld.anterior.path = 'img/anterior.png'
ld.anterior.w = 64
ld.anterior.h = 78
ld.anterior.x = 10
ld.anterior.y = 10

ld.advertencia1 = MetaData()
ld.advertencia1.path = 'img/advertencia1.png'
ld.advertencia1.w = 367
ld.advertencia1.h = 275
ld.advertencia1.x = 250
ld.advertencia1.y = 180

ld.advertencia2 = MetaData()
ld.advertencia2.path = 'img/advertencia2.png'
ld.advertencia2.w = 367
ld.advertencia2.h = 275
ld.advertencia2.x = 250
ld.advertencia2.y = 180

ld.cnombre = MetaData()
ld.cnombre.path = 'img/cuadro.png'
ld.cnombre.w = 646
ld.cnombre.h = 62
ld.cnombre.x = 144
ld.cnombre.y = 468

ld.capellido = MetaData()
ld.capellido.path = 'img/cuadro.png'
ld.capellido.w = 646
ld.capellido.h = 62
ld.capellido.x = 144
ld.capellido.y = 408

ld.ccorreo = MetaData()
ld.ccorreo.path = 'img/cuadro.png'
ld.ccorreo.w = 646
ld.ccorreo.h = 62
ld.ccorreo.x = 144
ld.ccorreo.y = 348

ld.cclave = MetaData()
ld.cclave.path = 'img/cuadro.png'
ld.cclave.w = 646
ld.cclave.h = 62
ld.cclave.x = 144
ld.cclave.y = 288

ld.cverificar = MetaData()
ld.cverificar.path = 'img/cuadro.png'
ld.cverificar.w = 646
ld.cverificar.h = 62
ld.cverificar.x = 144
ld.cverificar.y = 228

ld.cgrado = MetaData()
ld.cgrado.path = 'img/cuadro.png'
ld.cgrado.w = 646
ld.cgrado.h = 62
ld.cgrado.x = 144
ld.cgrado.y = 168

ld.crol = MetaData()
ld.crol.path = 'img/cuadro.png'
ld.crol.w = 646
ld.crol.h = 62
ld.crol.x = 144
ld.crol.y = 108

ld.flecha = MetaData()
ld.flecha.path = 'img/flecha.png'
ld.flecha.w = 17
ld.flecha.h = 17
ld.flecha.x = 743
ld.flecha.y = 138

ld.lnombre = MetaData()
ld.lnombre.text = ''
ld.lnombre.color = (0, 0, 0, 255)
ld.lnombre.fname = 'DejaVu Sans Mono'
ld.lnombre.fsize = 12
ld.lnombre.x = 156
ld.lnombre.y = 499

ld.lapellido = MetaData()
ld.lapellido.text = ''
ld.lapellido.color = (0, 0, 0, 255)
ld.lapellido.fname = 'DejaVu Sans Mono'
ld.lapellido.fsize = 12
ld.lapellido.x = 156
ld.lapellido.y = 439

ld.lcorreo = MetaData()
ld.lcorreo.text = ''
ld.lcorreo.color = (0, 0, 0, 255)
ld.lcorreo.fname = 'DejaVu Sans Mono'
ld.lcorreo.fsize = 12
ld.lcorreo.x = 156
ld.lcorreo.y = 379

ld.lclave = MetaData()
ld.lclave.text = ''
ld.lclave.color = (0, 0, 0, 255)
ld.lclave.fname = 'DejaVu Sans Mono'
ld.lclave.fsize = 12
ld.lclave.x = 156
ld.lclave.y = 319

ld.lverificar = MetaData()
ld.lverificar.text = ''
ld.lverificar.color = (0, 0, 0, 255)
ld.lverificar.fname = 'DejaVu Sans Mono'
ld.lverificar.fsize = 12
ld.lverificar.x = 156
ld.lverificar.y = 259

ld.lgrado = MetaData()
ld.lgrado.text = ''
ld.lgrado.color = (0, 0, 0, 255)
ld.lgrado.fname = 'DejaVu Sans Mono'
ld.lgrado.fsize = 12
ld.lgrado.x = 156
ld.lgrado.y = 199

ld.lrol = MetaData()
ld.lrol.text = '                      >>  DOCENTE   <<'
ld.lrol.color = (17, 33, 98, 255)
ld.lrol.fname = 'DejaVu Sans Mono'
ld.lrol.fsize = 12
ld.lrol.x = 156
ld.lrol.y = 139

ld.pointer = MetaData()
ld.pointer.path = 'img/pointer.png'
ld.pointer.w = 630
ld.pointer.h = 37
ld.pointer.x = 146
ld.pointer.y = 488
ld.pointer.ylist = ['lnombre', 'lapellido', 'lcorreo', 'lclave', 'lverificar', 'lgrado', 'lrol']
ld.pointer.ypos = {'cnombre': 488, 'capellido': 428, 'ccorreo': 368, 'cclave': 308, 'cverificar': 248, 'cgrado': 188, 'crol': 128}

ld.zones = {}
ld.zones['REGISTRO'] = {}
ld.zones['REGISTRO'] ['cnombre'] = [(144, 468, 646, 62)]
ld.zones['REGISTRO'] ['capellido'] = [(144, 408, 646, 62)]
ld.zones['REGISTRO'] ['ccorreo'] = [(144, 348, 646, 62)]
ld.zones['REGISTRO'] ['cclave'] = [(144, 288, 646, 62)]
ld.zones['REGISTRO'] ['cverificar'] = [(144, 228, 646, 62)]
ld.zones['REGISTRO'] ['cgrado'] = [(144, 168, 646, 62)]
ld.zones['REGISTRO'] ['crol'] = [(144, 108, 646, 62)]
ld.zones['REGISTRO'] ['ir_principal2'] = [(10, 10, 63, 80)]
ld.zones['REGISTRO'] ['guardar'] = [(ld.guardar.x, ld.guardar.y, ld.guardar.w, ld.guardar.h)]
ld.zones['REGISTRO'] ['cerrar_advertencia1'] = [(251, 361, 71, 94)]
ld.zones['REGISTRO'] ['cerrar_advertencia2'] = [(251, 361, 71, 94)]

#=====================================================================
# MENU 800X600
#=====================================================================

ld.menu1 = MetaData()
ld.menu1.path = 'img/menu1.png'
ld.menu1.w = 175
ld.menu1.h = 70
ld.menu1.x = 320
ld.menu1.y = 515

ld.logo1 = MetaData()
ld.logo1.path = 'img/logo.png'
ld.logo1.w = 88
ld.logo1.h = 82
ld.logo1.x = 705
ld.logo1.y = 515

ld.menu2 = MetaData()
ld.menu2.path = 'img/menu2.png'
ld.menu2.w = 351
ld.menu2.h = 351
ld.menu2.x = 230
ld.menu2.y = 100

ld.zones['MENU'] = {}
ld.zones['MENU'] ['ir_ajustes'] = [(325, 325, 100, 100)]
ld.zones['MENU'] ['ir_principal'] = [(380, 130, 135, 135)]
ld.zones['MENU'] ['ir_ayuda'] = [(515, 305, 40, 45)]
ld.zones['MENU'] ['ir_cerrar'] = [(255, 120, 70, 70)]

#=====================================================================
# PRINCIPAL 800X600
#=====================================================================

ld.iniciar = MetaData()
ld.iniciar.path = 'img/iniciar.png'
ld.iniciar.w = 200
ld.iniciar.h = 65
ld.iniciar.x = 285
ld.iniciar.y = 520

ld.ingresar = MetaData()
ld.ingresar.path = 'img/ingresar.png'
ld.ingresar.w = 122
ld.ingresar.h = 153
ld.ingresar.x = 340
ld.ingresar.y = 300


ld.nuevo = MetaData()
ld.nuevo.path = 'img/nuevo.png'
ld.nuevo.w = 196
ld.nuevo.h = 148
ld.nuevo.x = 310
ld.nuevo.y = 100

ld.anterior5 = MetaData()
ld.anterior5.path = 'img/anterior.png'
ld.anterior5.w = 64
ld.anterior5.h = 78
ld.anterior5.x = 10
ld.anterior5.y = 10

ld.zones['PRINCIPAL'] = {}
ld.zones['PRINCIPAL'] ['ir_menu'] = [(10, 10, 63, 80)]
ld.zones['PRINCIPAL'] ['ir_login'] = [(ld.ingresar.x, ld.ingresar.y, ld.ingresar.w, ld.ingresar.h)]
ld.zones['PRINCIPAL'] ['ir_registro'] = [(ld.nuevo.x, ld.nuevo.y, ld.nuevo.w, ld.nuevo.h)]

#=====================================================================
# AJUSTES 800X600
#=====================================================================

ld.ajustes= MetaData()
ld.ajustes.path = 'img/ajustes.png'
ld.ajustes.w = 190
ld.ajustes.h = 75
ld.ajustes.x = 310
ld.ajustes.y = 510

ld.sonido1 = MetaData()
ld.sonido1.path = 'img/sonido1.png'
ld.sonido1.w = 117
ld.sonido1.h = 152
ld.sonido1.x = 130
ld.sonido1.y = 340

ld.sonido2 = MetaData()
ld.sonido2.path = 'img/sonido2.png'
ld.sonido2.w = 117
ld.sonido2.h = 152
ld.sonido2.x = 130
ld.sonido2.y = 90

ld.pantalla1 = MetaData()
ld.pantalla1.path = 'img/pantalla1.png'
ld.pantalla1.w = 152
ld.pantalla1.h = 158
ld.pantalla1.x = 500
ld.pantalla1.y = 330

ld.pantalla2 = MetaData()
ld.pantalla2.path = 'img/pantalla2.png'
ld.pantalla2.w = 152
ld.pantalla2.h = 158
ld.pantalla2.x = 500
ld.pantalla2.y = 80

ld.anterior2 = MetaData()
ld.anterior2.path = 'img/anterior.png'
ld.anterior2.w = 64
ld.anterior2.h = 78
ld.anterior2.x = 10
ld.anterior2.y = 10

ld.zones['AJUSTES'] = {}
ld.zones['AJUSTES'] ['ir_menu'] = [(10, 10, 63, 80)]
ld.zones['AJUSTES'] ['pantalla1'] = [(ld.pantalla1.x, ld.pantalla1.y, ld.pantalla1.w, ld.pantalla1.h)]
ld.zones['AJUSTES'] ['pantalla2'] = [(ld.pantalla2.x, ld.pantalla2.y, ld.pantalla2.w, ld.pantalla2.h)]

#=====================================================================
# LOGIN 800X600
#=====================================================================

ld.login = MetaData()
ld.login.path = 'img/login.png'
ld.login.w = 313
ld.login.h = 63
ld.login.x = 260
ld.login.y = 520

ld.correo2 = MetaData()
ld.correo2.path = 'img/correo2.png'
ld.correo2.w = 156
ld.correo2.h = 51
ld.correo2.x = 110
ld.correo2.y = 365

ld.clave2 = MetaData()
ld.clave2.path = 'img/clave2.png'
ld.clave2.w = 133
ld.clave2.h = 54
ld.clave2.x = 120
ld.clave2.y = 215

ld.cucorreo2 = MetaData()
ld.cucorreo2.path = 'img/cuadrito.png'
ld.cucorreo2.w = 460
ld.cucorreo2.h = 62
ld.cucorreo2.x = 265
ld.cucorreo2.y = 350

ld.cuclave2 = MetaData()
ld.cuclave2.path = 'img/cuadrito.png'
ld.cuclave2.w = 460
ld.cuclave2.h = 62
ld.cuclave2.x = 265
ld.cuclave2.y = 200

ld.lcorreo2 = MetaData()
ld.lcorreo2.text = ''
ld.lcorreo2.color = (0, 0, 0, 255)
ld.lcorreo2.fname = 'DejaVu Sans Mono'
ld.lcorreo2.fsize = 12
ld.lcorreo2.x = 280
ld.lcorreo2.y = 385

ld.lclave2 = MetaData()
ld.lclave2.text = ''
ld.lclave2.color = (0, 0, 0, 255)
ld.lclave2.fname = 'DejaVu Sans Mono'
ld.lclave2.fsize = 12
ld.lclave2.x = 280
ld.lclave2.y = 235

ld.anterior3 = MetaData()
ld.anterior3.path = 'img/anterior.png'
ld.anterior3.w = 64
ld.anterior3.h = 78
ld.anterior3.x = 10
ld.anterior3.y = 10

ld.enter = MetaData()
ld.enter.path = 'img/enter.png'
ld.enter.w = 137
ld.enter.h = 80
ld.enter.x = 575
ld.enter.y = 70

ld.login_adv1 = MetaData()
ld.login_adv1.path = 'img/login_adv1.png'
ld.login_adv1.w = 367
ld.login_adv1.h = 275
ld.login_adv1.x = 250
ld.login_adv1.y = 180

ld.pointersito = MetaData()
ld.pointersito.path = 'img/pointersito.png'
ld.pointersito.w = 440
ld.pointersito.h = 37
ld.pointersito.x = 268
ld.pointersito.y = 370
ld.pointersito.ylist = ['lcorreo2', 'lclave2']
ld.pointersito.ypos = {'cucorreo2': 370, 'cuclave2': 220}

ld.zones['LOGIN'] = {}
ld.zones['LOGIN'] ['cucorreo2'] = [(ld.cucorreo2.x, ld.cucorreo2.y, ld.cucorreo2.w, ld.cucorreo2.h)]
ld.zones['LOGIN'] ['cuclave2'] = [(ld.cuclave2.x, ld.cuclave2.y, ld.cuclave2.w, ld.cuclave2.h)]
ld.zones['LOGIN'] ['ir_principal2'] = [(10, 10, 63, 80)]
ld.zones['LOGIN'] ['enter'] = [(ld.enter.x, ld.enter.y, ld.enter.w, ld.enter.h)]
ld.zones['LOGIN'] ['cerrar_login_adv1'] = [(251, 361, 71, 94)]

#=====================================================================
# AYUDA 800X600
#=====================================================================

ld.ayuda= MetaData()
ld.ayuda.path = 'img/ayuda.png'
ld.ayuda.w = 500
ld.ayuda.h = 53
ld.ayuda.x = 150
ld.ayuda.y = 520

ld.tabla = MetaData()
ld.tabla.path = 'img/tabla.png'
ld.tabla.w = 500
ld.tabla.h = 345
ld.tabla.x = 60
ld.tabla.y = 80

ld.idea = MetaData()
ld.idea.path = 'img/idea.gif'
ld.idea.w = 228
ld.idea.h = 350
ld.idea.x = 585
ld.idea.y = 90

ld.piso = MetaData()
ld.piso.path = 'img/piso.png'
ld.piso.w = 200
ld.piso.h = 100
ld.piso.x = 580
ld.piso.y = 55

ld.anterior4 = MetaData()
ld.anterior4.path = 'img/anterior.png'
ld.anterior4.w = 64
ld.anterior4.h = 78
ld.anterior4.x = 10
ld.anterior4.y = 10

ld.zones['AYUDA'] = {}
ld.zones['AYUDA'] ['ir_menu'] = [(10, 10, 63, 80)]
#=====================================================================
# NIVELES 800X600
#=====================================================================

ld.niveles = MetaData()
ld.niveles.path = 'img/niveles.png'
ld.niveles.w = 255
ld.niveles.h = 33
ld.niveles.x = 270
ld.niveles.y = 540

ld.rectilineo = MetaData()
ld.rectilineo.path = 'img/rectilineo.png'
ld.rectilineo.w = 161
ld.rectilineo.h = 60
ld.rectilineo.x = 60
ld.rectilineo.y = 410

ld.curvilineo = MetaData()
ld.curvilineo.path = 'img/curvilineo.png'
ld.curvilineo.w = 161
ld.curvilineo.h = 60
ld.curvilineo.x = 325
ld.curvilineo.y = 410

ld.especial = MetaData()
ld.especial.path = 'img/especial.png'
ld.especial.w = 161
ld.especial.h = 60
ld.especial.x = 595
ld.especial.y = 410

ld.nivel1 = MetaData()
ld.nivel1.path = 'img/nivel1.png'
ld.nivel1.w = 246
ld.nivel1.h = 138
ld.nivel1.x = 10
ld.nivel1.y = 250

ld.nivel2 = MetaData()
ld.nivel2.path = 'img/nivel1.png'
ld.nivel2.w = 246
ld.nivel2.h = 138
ld.nivel2.x = 278
ld.nivel2.y = 250

ld.nivel3 = MetaData()
ld.nivel3.path = 'img/nivel1.png'
ld.nivel3.w = 246
ld.nivel3.h = 138
ld.nivel3.x = 544
ld.nivel3.y = 250

ld.des_nivel1 = MetaData()
ld.des_nivel1.path = 'img/des_nivel1.png'
ld.des_nivel1.w = 236
ld.des_nivel1.h = 108
ld.des_nivel1.x = 10
ld.des_nivel1.y = 110

ld.des_nivel2 = MetaData()
ld.des_nivel2.path = 'img/des_nivel2.png'
ld.des_nivel2.w = 272
ld.des_nivel2.h = 108
ld.des_nivel2.x = 278
ld.des_nivel2.y = 110

ld.des_nivel3 = MetaData()
ld.des_nivel3.path = 'img/des_nivel3.png'
ld.des_nivel3.w = 224
ld.des_nivel3.h = 108
ld.des_nivel3.x = 554
ld.des_nivel3.y = 110

ld.anterior_niveles = MetaData()
ld.anterior_niveles.path = 'img/anterior.png'
ld.anterior_niveles.w = 65
ld.anterior_niveles.h = 60
ld.anterior_niveles.x = 5
ld.anterior_niveles.y = 10

ld.medalla_nivel1 = MetaData()
ld.medalla_nivel1.path = 'img/medalla.png'
ld.medalla_nivel1.w = 71
ld.medalla_nivel1.h = 107
ld.medalla_nivel1.x = 175
ld.medalla_nivel1.y = 200

ld.medalla_nivel2 = MetaData()
ld.medalla_nivel2.path = 'img/medalla.png'
ld.medalla_nivel2.w = 71
ld.medalla_nivel2.h = 107
ld.medalla_nivel2.x = 445
ld.medalla_nivel2.y = 200

ld.medalla_nivel3 = MetaData()
ld.medalla_nivel3.path = 'img/medalla.png'
ld.medalla_nivel3.w = 71
ld.medalla_nivel3.h = 107
ld.medalla_nivel3.x = 710
ld.medalla_nivel3.y = 200

ld.zones['NIVELES'] = {}
ld.zones['NIVELES'] ['ir_nivel1'] = [(ld.nivel1.x, ld.nivel1.y, ld.nivel1.w, ld.nivel1.h)]
ld.zones['NIVELES'] ['ir_nivel2'] = [(ld.nivel2.x, ld.nivel1.y, ld.nivel2.w, ld.nivel2.h)]
ld.zones['NIVELES'] ['ir_nivel3'] = [(ld.nivel3.x, ld.nivel3.y, ld.nivel3.w, ld.nivel3.h)]
ld.zones['NIVELES'] ['ir_casa'] = [(ld.anterior_niveles.x, ld.anterior_niveles.y, ld.anterior_niveles.w, ld.anterior_niveles.h)]
#=====================================================================
# NIVEL1 800x600
#=====================================================================

ld.carro1 = MetaData()
ld.carro1.path = 'img/carro1.png'
ld.carro1.w = 82
ld.carro1.h = 41
ld.carro1.x = 10
ld.carro1.y = 140

ld.carro2 = MetaData()
ld.carro2.path = 'img/carro2.png'
ld.carro2.w = 82
ld.carro2.h = 41
ld.carro2.x = 710
ld.carro2.y = 140

ld.carretera = MetaData()
ld.carretera.path = 'img/carretera.jpg'
ld.carretera.w = 800
ld.carretera.h = 40
ld.carretera.x = 0
ld.carretera.y = 130

ld.colegio = MetaData()
ld.colegio.path = 'img/colegio.png'
ld.colegio.w = 246
ld.colegio.h = 123
ld.colegio.x = 0
ld.colegio.y = 170

ld.parque = MetaData()
ld.parque.path = 'img/parque.png'
ld.parque.w = 276
ld.parque.h = 153
ld.parque.x = 524
ld.parque.y = 170

ld.casa = MetaData()
ld.casa.path = 'img/casa.png'
ld.casa.w = 37
ld.casa.h = 35
ld.casa.x = 735
ld.casa.y = 520

ld.ok = MetaData()
ld.ok.path = 'img/ok.png'
ld.ok.w = 36
ld.ok.h = 37
ld.ok.x = 735
ld.ok.y = 390

ld.actualizar = MetaData()
ld.actualizar.path = 'img/actualizar.png'
ld.actualizar.w = 37
ld.actualizar.h = 37
ld.actualizar.x = 735
ld.actualizar.y = 460

ld.bombillo= MetaData()
ld.bombillo.path = 'img/bombillo.png'
ld.bombillo.w = 31
ld.bombillo.h = 31
ld.bombillo.x = 760
ld.bombillo.y = 15

ld.anterior6 = MetaData()
ld.anterior6.path = 'img/anterior.png'
ld.anterior6.w = 65
ld.anterior6.h = 60
ld.anterior6.x = 5
ld.anterior6.y = 10

ld.dis_campo = MetaData()
ld.dis_campo.path = 'img/campo.png'
ld.dis_campo.w = 55
ld.dis_campo.h = 25
ld.dis_campo.x = 380
ld.dis_campo.y = 55

ld.car1_campo = MetaData()
ld.car1_campo.path = 'img/campo.png'
ld.car1_campo.w = 55
ld.car1_campo.h = 25
ld.car1_campo.x = 110
ld.car1_campo.y = 55

ld.car2_campo = MetaData()
ld.car2_campo.path = 'img/campo.png'
ld.car2_campo.w = 55
ld.car2_campo.h = 25
ld.car2_campo.x = 650
ld.car2_campo.y = 55

ld.vel_car1_campo = MetaData()
ld.vel_car1_campo.path = 'img/campo.png'
ld.vel_car1_campo.w = 55
ld.vel_car1_campo.h = 25
ld.vel_car1_campo.x = 280
ld.vel_car1_campo.y = 220

ld.vel_car2_campo = MetaData()
ld.vel_car2_campo.path = 'img/campo.png'
ld.vel_car2_campo.w = 55
ld.vel_car2_campo.h = 25
ld.vel_car2_campo.x = 460
ld.vel_car2_campo.y = 220

ld.res_campo = MetaData()
ld.res_campo.path = 'img/campo.png'
ld.res_campo.w = 55
ld.res_campo.h = 25
ld.res_campo.x = 380
ld.res_campo.y = 400

ld.distancia = MetaData()
ld.distancia.path = 'img/distancia.png'
ld.distancia.w = 120
ld.distancia.h = 26
ld.distancia.x = 350
ld.distancia.y = 35

ld.distanciaA_u = MetaData()
ld.distanciaA_u.path = 'img/distanciaA_u.png'
ld.distanciaA_u.w = 115
ld.distanciaA_u.h = 26
ld.distanciaA_u.x = 80
ld.distanciaA_u.y = 35

ld.distanciaB_v = MetaData()
ld.distanciaB_v.path = 'img/distanciaB_v.png'
ld.distanciaB_v.w = 113
ld.distanciaB_v.h = 26
ld.distanciaB_v.x = 620
ld.distanciaB_v.y = 35

ld.velocidadU = MetaData()
ld.velocidadU.path = 'img/velocidadU.png'
ld.velocidadU.w = 90
ld.velocidadU.h = 26
ld.velocidadU.x = 260
ld.velocidadU.y = 240

ld.velocidadV = MetaData()
ld.velocidadV.path = 'img/velocidadV.png'
ld.velocidadV.w = 88
ld.velocidadV.h = 26
ld.velocidadV.x = 440
ld.velocidadV.y = 240

ld.resultado = MetaData()
ld.resultado.path = 'img/tiempo.png'
ld.resultado.w = 66
ld.resultado.h = 25
ld.resultado.x = 375
ld.resultado.y = 420

ld.mano = MetaData()
ld.mano.path = 'img/mano.png'
ld.mano.w = 24
ld.mano.h = 28
ld.mano.x = 390
ld.mano.y = 98

ld.no = MetaData()
ld.no.path = 'img/no.gif'
ld.no.w = 162
ld.no.h = 87
ld.no.x = 260
ld.no.y = 200

ld.bien = MetaData()
ld.bien.path = 'img/bien.gif'
ld.bien.w = 177
ld.bien.h = 205
ld.bien.x = 240
ld.bien.y = 130

ld.explosion = MetaData()
ld.explosion.path = 'img/explosion.gif'
ld.explosion.w = 92
ld.explosion.h = 134
ld.explosion.x = 325
ld.explosion.y = 110

ld.siguiente = MetaData()
ld.siguiente.path = 'img/siguiente.png'
ld.siguiente.w = 150
ld.siguiente.h = 71
ld.siguiente.x = 640
ld.siguiente.y = 0

ld.ldescripcion = MetaData()
ld.ldescripcion.text = ''
ld.ldescripcion.color = (0, 0, 0, 255)
ld.ldescripcion.fname = 'DejaVu Sans Mono'
ld.ldescripcion.fsize = 10
ld.ldescripcion.x = 375
ld.ldescripcion.y = 545

ld.ldistancia_total = MetaData()
ld.ldistancia_total.text = ''
ld.ldistancia_total.color = (0, 0, 0, 255)
ld.ldistancia_total.fname = 'DejaVu Sans Mono'
ld.ldistancia_total.fsize = 10
ld.ldistancia_total.x = 385
ld.ldistancia_total.y = 67

ld.ldistanciaA_u = MetaData()
ld.ldistanciaA_u.text = ''
ld.ldistanciaA_u.color = (0, 0, 0, 255)
ld.ldistanciaA_u.fname = 'DejaVu Sans Mono'
ld.ldistanciaA_u.fsize = 10
ld.ldistanciaA_u.x = 120
ld.ldistanciaA_u.y = 67

ld.ldistanciaB_V = MetaData()
ld.ldistanciaB_V.text = ''
ld.ldistanciaB_V.color = (0, 0, 0, 255)
ld.ldistanciaB_V.fname = 'DejaVu Sans Mono'
ld.ldistanciaB_V.fsize = 10
ld.ldistanciaB_V.x = 660
ld.ldistanciaB_V.y = 67

ld.lvelocidadU = MetaData()
ld.lvelocidadU.text = ''
ld.lvelocidadU.color = (0, 0, 0, 255)
ld.lvelocidadU.fname = 'DejaVu Sans Mono'
ld.lvelocidadU.fsize = 10
ld.lvelocidadU.x = 300
ld.lvelocidadU.y = 231

ld.lvelocidadV = MetaData()
ld.lvelocidadV.text = ''
ld.lvelocidadV.color = (0, 0, 0, 255)
ld.lvelocidadV.fname = 'DejaVu Sans Mono'
ld.lvelocidadV.fsize = 10
ld.lvelocidadV.x = 480
ld.lvelocidadV.y = 231

ld.ltiempo = MetaData()
ld.ltiempo.text = ''
ld.ltiempo.color = (0, 0, 0, 255)
ld.ltiempo.fname = 'DejaVu Sans Mono'
ld.ltiempo.fsize = 10
ld.ltiempo.x = 390
ld.ltiempo.y = 410

ld.zones['NIVEL1'] = {}

ld.zones['NIVEL1'] ['mover_mano'] = [(ld.mano.x, ld.mano.y, ld.mano.w, ld.mano.h)]
ld.zones['NIVEL1'] ['ir_ok'] = [(ld.ok.x, ld.ok.y, ld.ok.w, ld.ok.h)]
ld.zones['NIVEL1'] ['ir_casa'] = [(ld.casa.x, ld.casa.y, ld.casa.w, ld.casa.h)]
ld.zones['NIVEL1'] ['ir_actualizar'] = [(ld.actualizar.x, ld.actualizar.y, ld.actualizar.w, ld.actualizar.h)]
ld.zones['NIVEL1'] ['ir_bombillo'] = [(ld.bombillo.x, ld.bombillo.y, ld.bombillo.w, ld.bombillo.h)]
ld.zones['NIVEL1'] ['ir_niveles'] = [(ld.anterior6.x, ld.anterior6.y, ld.anterior6.w, ld.anterior6.h)]

#=====================================================================
# EJERCICIO2_N1 800X600
#=====================================================================

ld.barco1_eje2 = MetaData()
ld.barco1_eje2.path = 'img/barco1.png'
ld.barco1_eje2.w = 88
ld.barco1_eje2.h = 93
ld.barco1_eje2.x = 10
ld.barco1_eje2.y = 150

ld.barco2_eje2 = MetaData()
ld.barco2_eje2.path = 'img/barco2.png'
ld.barco2_eje2.w = 88
ld.barco2_eje2.h = 80
ld.barco2_eje2.x = 702
ld.barco2_eje2.y = 135

ld.agua_eje2 = MetaData()
ld.agua_eje2.path = 'img/agua.jpg'
ld.agua_eje2.w = 800
ld.agua_eje2.h = 53
ld.agua_eje2.x = 0
ld.agua_eje2.y = 130

ld.faro_eje2 = MetaData()
ld.faro_eje2.path = 'img/faro.png'
ld.faro_eje2.w = 140
ld.faro_eje2.h = 280
ld.faro_eje2.x = 3
ld.faro_eje2.y = 170

ld.playa_eje2 = MetaData()
ld.playa_eje2.path = 'img/playa.png'
ld.playa_eje2.w = 400
ld.playa_eje2.h = 181
ld.playa_eje2.x = 400
ld.playa_eje2.y = 170

ld.anterior7 = MetaData()
ld.anterior7.path = 'img/anterior.png'
ld.anterior7.w = 65
ld.anterior7.h = 60
ld.anterior7.x = 5
ld.anterior7.y = 10

ld.tiempo_campo = MetaData()
ld.tiempo_campo.path = 'img/campo.png'
ld.tiempo_campo.w = 55
ld.tiempo_campo.h = 25
ld.tiempo_campo.x = 380
ld.tiempo_campo.y = 55

ld.car1_campo_eje2 = MetaData()
ld.car1_campo_eje2.path = 'img/campo.png'
ld.car1_campo_eje2.w = 55
ld.car1_campo_eje2.h = 25
ld.car1_campo_eje2.x = 110
ld.car1_campo_eje2.y = 55

ld.car2_campo_eje2 = MetaData()
ld.car2_campo_eje2.path = 'img/campo.png'
ld.car2_campo_eje2.w = 55
ld.car2_campo_eje2.h = 25
ld.car2_campo_eje2.x = 650
ld.car2_campo_eje2.y = 55

ld.vel_car1_campo_eje2 = MetaData()
ld.vel_car1_campo_eje2.path = 'img/campo.png'
ld.vel_car1_campo_eje2.w = 55
ld.vel_car1_campo_eje2.h = 25
ld.vel_car1_campo_eje2.x = 200
ld.vel_car1_campo_eje2.y = 320

ld.vel_car2_campo_eje2 = MetaData()
ld.vel_car2_campo_eje2.path = 'img/campo.png'
ld.vel_car2_campo_eje2.w = 55
ld.vel_car2_campo_eje2.h = 25
ld.vel_car2_campo_eje2.x = 520
ld.vel_car2_campo_eje2.y = 320

ld.res_campo_eje2 = MetaData()
ld.res_campo_eje2.path = 'img/campo.png'
ld.res_campo_eje2.w = 55
ld.res_campo_eje2.h = 25
ld.res_campo_eje2.x = 380
ld.res_campo_eje2.y = 400

ld.tiempo_eje2 = MetaData()
ld.tiempo_eje2.path = 'img/tiempo.png'
ld.tiempo_eje2.w = 65
ld.tiempo_eje2.h = 26
ld.tiempo_eje2.x = 377
ld.tiempo_eje2.y = 35

ld.distanciaA_u_eje2 = MetaData()
ld.distanciaA_u_eje2.path = 'img/distanciaA_u.png'
ld.distanciaA_u_eje2.w = 115
ld.distanciaA_u_eje2.h = 26
ld.distanciaA_u_eje2.x = 80
ld.distanciaA_u_eje2.y = 35

ld.distanciaB_v_eje2 = MetaData()
ld.distanciaB_v_eje2.path = 'img/distanciaB_v.png'
ld.distanciaB_v_eje2.w = 113
ld.distanciaB_v_eje2.h = 26
ld.distanciaB_v_eje2.x = 620
ld.distanciaB_v_eje2.y = 35

ld.velocidadU_eje2 = MetaData()
ld.velocidadU_eje2.path = 'img/velocidadU.png'
ld.velocidadU_eje2.w = 90
ld.velocidadU_eje2.h = 26
ld.velocidadU_eje2.x = 185
ld.velocidadU_eje2.y = 340

ld.velocidadV_eje2 = MetaData()
ld.velocidadV_eje2.path = 'img/velocidadV.png'
ld.velocidadV_eje2.w = 88
ld.velocidadV_eje2.h = 26
ld.velocidadV_eje2.x = 505
ld.velocidadV_eje2.y = 340

ld.distancia_eje2 = MetaData()
ld.distancia_eje2.path = 'img/distancia_eje2.png'
ld.distancia_eje2.w = 82
ld.distancia_eje2.h = 26
ld.distancia_eje2.x = 370
ld.distancia_eje2.y = 420

ld.mano_eje2 = MetaData()
ld.mano_eje2.path = 'img/mano.png'
ld.mano_eje2.w = 24
ld.mano_eje2.h = 28
ld.mano_eje2.x = 390
ld.mano_eje2.y = 98

ld.no_eje2 = MetaData()
ld.no_eje2.path = 'img/no.gif'
ld.no_eje2.w = 162
ld.no_eje2.h = 87
ld.no_eje2.x = 270
ld.no_eje2.y = 200

ld.bien_eje2 = MetaData()
ld.bien_eje2.path = 'img/bien.gif'
ld.bien_eje2.w = 177
ld.bien_eje2.h = 205
ld.bien_eje2.x = 240
ld.bien_eje2.y = 130

ld.casa_eje2 = MetaData()
ld.casa_eje2.path = 'img/casa.png'
ld.casa_eje2.w = 37
ld.casa_eje2.h = 35
ld.casa_eje2.x = 735
ld.casa_eje2.y = 520

ld.ok_eje2 = MetaData()
ld.ok_eje2.path = 'img/ok.png'
ld.ok_eje2.w = 36
ld.ok_eje2.h = 37
ld.ok_eje2.x = 735
ld.ok_eje2.y = 390

ld.actualizar_eje2 = MetaData()
ld.actualizar_eje2.path = 'img/actualizar.png'
ld.actualizar_eje2.w = 37
ld.actualizar_eje2.h = 37
ld.actualizar_eje2.x = 735
ld.actualizar_eje2.y = 460

ld.bombillo_eje2= MetaData()
ld.bombillo_eje2.path = 'img/bombillo.png'
ld.bombillo_eje2.w = 31
ld.bombillo_eje2.h = 31
ld.bombillo_eje2.x = 760
ld.bombillo_eje2.y = 15

ld.siguiente_eje2 = MetaData()
ld.siguiente_eje2.path = 'img/siguiente.png'
ld.siguiente_eje2.w = 150
ld.siguiente_eje2.h = 71
ld.siguiente_eje2.x = 640
ld.siguiente_eje2.y = 0

ld.ldescripcion_eje2 = MetaData()
ld.ldescripcion_eje2.text = ''
ld.ldescripcion_eje2.color = (0, 0, 0, 255)
ld.ldescripcion_eje2.fname = 'DejaVu Sans Mono'
ld.ldescripcion_eje2.fsize = 10
ld.ldescripcion_eje2.x = 375
ld.ldescripcion_eje2.y = 545

ld.ltiempo_total = MetaData()
ld.ltiempo_total.text = ''
ld.ltiempo_total.color = (0, 0, 0, 255)
ld.ltiempo_total.fname = 'DejaVu Sans Mono'
ld.ltiempo_total.fsize = 10
ld.ltiempo_total.x = 395
ld.ltiempo_total.y = 67

ld.ldistanciaA_u_eje2 = MetaData()
ld.ldistanciaA_u_eje2.text = ''
ld.ldistanciaA_u_eje2.color = (0, 0, 0, 255)
ld.ldistanciaA_u_eje2.fname = 'DejaVu Sans Mono'
ld.ldistanciaA_u_eje2.fsize = 10
ld.ldistanciaA_u_eje2.x = 120
ld.ldistanciaA_u_eje2.y = 67

ld.ldistanciaB_V_eje2 = MetaData()
ld.ldistanciaB_V_eje2.text = ''
ld.ldistanciaB_V_eje2.color = (0, 0, 0, 255)
ld.ldistanciaB_V_eje2.fname = 'DejaVu Sans Mono'
ld.ldistanciaB_V_eje2.fsize = 10
ld.ldistanciaB_V_eje2.x = 660
ld.ldistanciaB_V_eje2.y = 67

ld.lvelocidadU_eje2 = MetaData()
ld.lvelocidadU_eje2.text = ''
ld.lvelocidadU_eje2.color = (0, 0, 0, 255)
ld.lvelocidadU_eje2.fname = 'DejaVu Sans Mono'
ld.lvelocidadU_eje2.fsize = 10
ld.lvelocidadU_eje2.x = 220
ld.lvelocidadU_eje2.y = 331

ld.lvelocidadV_eje2 = MetaData()
ld.lvelocidadV_eje2.text = ''
ld.lvelocidadV_eje2.color = (0, 0, 0, 255)
ld.lvelocidadV_eje2.fname = 'DejaVu Sans Mono'
ld.lvelocidadV_eje2.fsize = 10
ld.lvelocidadV_eje2.x = 540
ld.lvelocidadV_eje2.y = 331

ld.ldistancia_eje2 = MetaData()
ld.ldistancia_eje2.text = ''
ld.ldistancia_eje2.color = (0, 0, 0, 255)
ld.ldistancia_eje2.fname = 'DejaVu Sans Mono'
ld.ldistancia_eje2.fsize = 10
ld.ldistancia_eje2.x = 383
ld.ldistancia_eje2.y = 410

ld.zones['EJERCICIO2_N1'] = {}

ld.zones['EJERCICIO2_N1'] ['mover_mano'] = [(ld.mano_eje2.x, ld.mano_eje2.y, ld.mano_eje2.w, ld.mano_eje2.h)]
ld.zones['EJERCICIO2_N1'] ['ir_ok'] = [(ld.ok_eje2.x, ld.ok_eje2.y, ld.ok_eje2.w, ld.ok_eje2.h)]
ld.zones['EJERCICIO2_N1'] ['ir_casa'] = [(ld.casa_eje2.x, ld.casa_eje2.y, ld.casa_eje2.w, ld.casa_eje2.h)]
ld.zones['EJERCICIO2_N1'] ['ir_actualizar'] = [(ld.actualizar_eje2.x, ld.actualizar_eje2.y, ld.actualizar_eje2.w, ld.actualizar_eje2.h)]
ld.zones['EJERCICIO2_N1'] ['ir_bombillo'] = [(ld.bombillo_eje2.x, ld.bombillo_eje2.y, ld.bombillo_eje2.w, ld.bombillo_eje2.h)]
ld.zones['EJERCICIO2_N1'] ['ir_niveles'] = [(ld.anterior7.x, ld.anterior7.y, ld.anterior7.w, ld.anterior7.h)]
#=====================================================================
# EJERCICIO3_N1 800X600
#=====================================================================

ld.anterior9_eje3_N1 = MetaData()
ld.anterior9_eje3_N1.path = 'img/anterior.png'
ld.anterior9_eje3_N1.w = 65
ld.anterior9_eje3_N1.h = 60
ld.anterior9_eje3_N1.x = 5
ld.anterior9_eje3_N1.y = 10

ld.tractor1_eje3_N1 = MetaData()
ld.tractor1_eje3_N1.path = 'img/tractor1.png'
ld.tractor1_eje3_N1.w = 88
ld.tractor1_eje3_N1.h = 61
ld.tractor1_eje3_N1.x = 10
ld.tractor1_eje3_N1.y = 150

ld.tractor2_eje3_N1 = MetaData()
ld.tractor2_eje3_N1.path = 'img/tractor2.png'
ld.tractor2_eje3_N1.w = 88
ld.tractor2_eje3_N1.h = 61
ld.tractor2_eje3_N1.x = 702
ld.tractor2_eje3_N1.y = 135

ld.tierra_eje3_N1 = MetaData()
ld.tierra_eje3_N1.path = 'img/tierra.jpg'
ld.tierra_eje3_N1.w = 800
ld.tierra_eje3_N1.h = 53
ld.tierra_eje3_N1.x = 0
ld.tierra_eje3_N1.y = 130

ld.molino_eje3_N1 = MetaData()
ld.molino_eje3_N1.path = 'img/molino.png'
ld.molino_eje3_N1.w = 197
ld.molino_eje3_N1.h = 280
ld.molino_eje3_N1.x = 3
ld.molino_eje3_N1.y = 155

ld.granja_eje3_N1 = MetaData()
ld.granja_eje3_N1.path = 'img/granja.png'
ld.granja_eje3_N1.w = 300
ld.granja_eje3_N1.h = 155
ld.granja_eje3_N1.x = 500
ld.granja_eje3_N1.y = 180

ld.tiempo_campo_eje3_N1 = MetaData()
ld.tiempo_campo_eje3_N1.path = 'img/campo.png'
ld.tiempo_campo_eje3_N1.w = 55
ld.tiempo_campo_eje3_N1.h = 25
ld.tiempo_campo_eje3_N1.x = 230
ld.tiempo_campo_eje3_N1.y = 220

ld.car1_campo_eje3_N1 = MetaData()
ld.car1_campo_eje3_N1.path = 'img/campo.png'
ld.car1_campo_eje3_N1.w = 55
ld.car1_campo_eje3_N1.h = 25
ld.car1_campo_eje3_N1.x = 110
ld.car1_campo_eje3_N1.y = 55

ld.car2_campo_eje3_N1 = MetaData()
ld.car2_campo_eje3_N1.path = 'img/campo.png'
ld.car2_campo_eje3_N1.w = 55
ld.car2_campo_eje3_N1.h = 25
ld.car2_campo_eje3_N1.x = 650
ld.car2_campo_eje3_N1.y = 55

ld.vel_car2_campo_eje3_N1 = MetaData()
ld.vel_car2_campo_eje3_N1.path = 'img/campo.png'
ld.vel_car2_campo_eje3_N1.w = 55
ld.vel_car2_campo_eje3_N1.h = 25
ld.vel_car2_campo_eje3_N1.x = 435
ld.vel_car2_campo_eje3_N1.y = 220

ld.distancia_campo_eje3_N1 = MetaData()
ld.distancia_campo_eje3_N1.path = 'img/campo.png'
ld.distancia_campo_eje3_N1.w = 55
ld.distancia_campo_eje3_N1.h = 25
ld.distancia_campo_eje3_N1.x = 380
ld.distancia_campo_eje3_N1.y = 55

ld.res_campo_eje3_N1 = MetaData()
ld.res_campo_eje3_N1.path = 'img/campo.png'
ld.res_campo_eje3_N1.w = 55
ld.res_campo_eje3_N1.h = 25
ld.res_campo_eje3_N1.x = 380
ld.res_campo_eje3_N1.y = 410

ld.mano_eje3_N1 = MetaData()
ld.mano_eje3_N1.path = 'img/mano.png'
ld.mano_eje3_N1.w = 24
ld.mano_eje3_N1.h = 28
ld.mano_eje3_N1.x = 390
ld.mano_eje3_N1.y = 98

ld.distancia_eje3_N1 = MetaData()
ld.distancia_eje3_N1.path = 'img/distancia.png'
ld.distancia_eje3_N1.w = 120
ld.distancia_eje3_N1.h = 26
ld.distancia_eje3_N1.x = 350
ld.distancia_eje3_N1.y = 35

ld.distanciaA_u_eje3_N1 = MetaData()
ld.distanciaA_u_eje3_N1.path = 'img/distanciaA_u.png'
ld.distanciaA_u_eje3_N1.w = 115
ld.distanciaA_u_eje3_N1.h = 26
ld.distanciaA_u_eje3_N1.x = 80
ld.distanciaA_u_eje3_N1.y = 35

ld.distanciaB_v_eje3_N1 = MetaData()
ld.distanciaB_v_eje3_N1.path = 'img/distanciaB_v.png'
ld.distanciaB_v_eje3_N1.w = 113
ld.distanciaB_v_eje3_N1.h = 26
ld.distanciaB_v_eje3_N1.x = 620
ld.distanciaB_v_eje3_N1.y = 35

ld.velocidad_auto_U_eje3_N1 = MetaData()
ld.velocidad_auto_U_eje3_N1.path = 'img/velocidadU.png'
ld.velocidad_auto_U_eje3_N1.w =  90
ld.velocidad_auto_U_eje3_N1.h =  26
ld.velocidad_auto_U_eje3_N1.x =  363
ld.velocidad_auto_U_eje3_N1.y =  430

ld.velocidadV_eje3_N1 = MetaData()
ld.velocidadV_eje3_N1.path = 'img/velocidadV.png'
ld.velocidadV_eje3_N1.w = 88 
ld.velocidadV_eje3_N1.h = 26
ld.velocidadV_eje3_N1.x = 420
ld.velocidadV_eje3_N1.y = 240

ld.tiempo_eje3_N1 = MetaData()
ld.tiempo_eje3_N1.path = 'img/tiempo.png'
ld.tiempo_eje3_N1.w = 66
ld.tiempo_eje3_N1.h = 25 
ld.tiempo_eje3_N1.x = 225
ld.tiempo_eje3_N1.y = 240

ld.ok_eje3_N1 = MetaData()
ld.ok_eje3_N1.path = 'img/ok.png'
ld.ok_eje3_N1.w = 36
ld.ok_eje3_N1.h = 37
ld.ok_eje3_N1.x = 735
ld.ok_eje3_N1.y = 390

ld.actualizar_eje3_N1 = MetaData()
ld.actualizar_eje3_N1.path = 'img/actualizar.png'
ld.actualizar_eje3_N1.w = 37
ld.actualizar_eje3_N1.h = 37
ld.actualizar_eje3_N1.x = 735
ld.actualizar_eje3_N1.y = 460

ld.casa_eje3_N1 = MetaData()
ld.casa_eje3_N1.path = 'img/casa.png'
ld.casa_eje3_N1.w = 37
ld.casa_eje3_N1.h = 35
ld.casa_eje3_N1.x = 735
ld.casa_eje3_N1.y = 520

ld.bombillo_eje3_N1 = MetaData()
ld.bombillo_eje3_N1.path = 'img/bombillo.png'
ld.bombillo_eje3_N1.w = 31
ld.bombillo_eje3_N1.h = 31
ld.bombillo_eje3_N1.x = 760
ld.bombillo_eje3_N1.y = 15

ld.siguiente_eje3_N1 = MetaData()
ld.siguiente_eje3_N1.path = 'img/siguiente.png'
ld.siguiente_eje3_N1.w = 150
ld.siguiente_eje3_N1.h = 71
ld.siguiente_eje3_N1.x = 640
ld.siguiente_eje3_N1.y = 0

ld.no_eje3_N1 = MetaData()
ld.no_eje3_N1.path = 'img/no.gif'
ld.no_eje3_N1.w = 162
ld.no_eje3_N1.h = 87
ld.no_eje3_N1.x = 270
ld.no_eje3_N1.y = 200

ld.bien_eje3_N1 = MetaData()
ld.bien_eje3_N1.path = 'img/bien.gif'
ld.bien_eje3_N1.w = 177
ld.bien_eje3_N1.h = 205
ld.bien_eje3_N1.x = 240
ld.bien_eje3_N1.y = 130

ld.ldescripcion_eje3_N1 = MetaData()
ld.ldescripcion_eje3_N1.text = ''
ld.ldescripcion_eje3_N1.color = (0, 0, 0, 255)
ld.ldescripcion_eje3_N1.fname = 'DejaVu Sans Mono'
ld.ldescripcion_eje3_N1.fsize = 10
ld.ldescripcion_eje3_N1.x = 375
ld.ldescripcion_eje3_N1.y = 545

ld.ldistancia_total_eje3_N1 = MetaData()
ld.ldistancia_total_eje3_N1.text = ''
ld.ldistancia_total_eje3_N1.color = (0, 0, 0, 255)
ld.ldistancia_total_eje3_N1.fname = 'DejaVu Sans Mono'
ld.ldistancia_total_eje3_N1.fsize = 10
ld.ldistancia_total_eje3_N1.x = 385 
ld.ldistancia_total_eje3_N1.y = 67

ld.ldistanciaA_u_eje3_N1 = MetaData()
ld.ldistanciaA_u_eje3_N1.text = ''
ld.ldistanciaA_u_eje3_N1.color = (0, 0, 0, 255)
ld.ldistanciaA_u_eje3_N1.fname = 'DejaVu Sans Mono'
ld.ldistanciaA_u_eje3_N1.fsize = 10
ld.ldistanciaA_u_eje3_N1.x = 120
ld.ldistanciaA_u_eje3_N1.y = 67

ld.ldistanciaB_V_eje3_N1 = MetaData()
ld.ldistanciaB_V_eje3_N1.text = ''
ld.ldistanciaB_V_eje3_N1.color = (0, 0, 0, 255)
ld.ldistanciaB_V_eje3_N1.fname = 'DejaVu Sans Mono'
ld.ldistanciaB_V_eje3_N1.fsize = 10
ld.ldistanciaB_V_eje3_N1.x = 660
ld.ldistanciaB_V_eje3_N1.y = 67

ld.lvelocidad_auto_U_eje3_N1 = MetaData()
ld.lvelocidad_auto_U_eje3_N1.text = ''
ld.lvelocidad_auto_U_eje3_N1.color = (0, 0, 0, 255)
ld.lvelocidad_auto_U_eje3_N1.fname = 'DejaVu Sans Mono'
ld.lvelocidad_auto_U_eje3_N1.fsize = 10
ld.lvelocidad_auto_U_eje3_N1.x = 383
ld.lvelocidad_auto_U_eje3_N1.y = 420

ld.lvelocidadV_eje3_N1 = MetaData()
ld.lvelocidadV_eje3_N1.text = ''
ld.lvelocidadV_eje3_N1.color = (0, 0, 0, 255)
ld.lvelocidadV_eje3_N1.fname = 'DejaVu Sans Mono'
ld.lvelocidadV_eje3_N1.fsize = 10
ld.lvelocidadV_eje3_N1.x = 450
ld.lvelocidadV_eje3_N1.y = 231

ld.ltiempo_transcurrido_eje3_N1 = MetaData()
ld.ltiempo_transcurrido_eje3_N1.text = ''
ld.ltiempo_transcurrido_eje3_N1.color = (0, 0, 0, 255)
ld.ltiempo_transcurrido_eje3_N1.fname = 'DejaVu Sans Mono'
ld.ltiempo_transcurrido_eje3_N1.fsize = 10
ld.ltiempo_transcurrido_eje3_N1.x = 245
ld.ltiempo_transcurrido_eje3_N1.y = 231

ld.diploma_N1 = MetaData()
ld.diploma_N1.path = 'img/diploma_n1.png'
ld.diploma_N1.w = 451
ld.diploma_N1.h = 350
ld.diploma_N1.x = 165
ld.diploma_N1.y = 110

ld.zones['EJERCICIO3_N1'] = {}

ld.zones['EJERCICIO3_N1'] ['mover_mano'] = [(ld.mano_eje3_N1.x, ld.mano_eje3_N1.y, ld.mano_eje3_N1.w, ld.mano_eje3_N1.h)]
ld.zones['EJERCICIO3_N1'] ['ir_ok'] = [(ld.ok_eje3_N1.x, ld.ok_eje3_N1.y, ld.ok_eje3_N1.w, ld.ok_eje3_N1.h)]
ld.zones['EJERCICIO3_N1'] ['ir_casa'] = [(ld.casa_eje3_N1.x, ld.casa_eje3_N1.y, ld.casa_eje3_N1.w, ld.casa_eje3_N1.h)]
ld.zones['EJERCICIO3_N1'] ['ir_actualizar'] = [(ld.actualizar_eje3_N1.x, ld.actualizar_eje3_N1.y, ld.actualizar_eje3_N1.w, ld.actualizar_eje3_N1.h)]
ld.zones['EJERCICIO3_N1'] ['ir_bombillo'] = [(ld.bombillo_eje3_N1.x, ld.bombillo_eje3_N1.y, ld.bombillo_eje3_N1.w, ld.bombillo_eje3_N1.h)]
ld.zones['EJERCICIO3_N1'] ['ir_niveles'] = [(ld.anterior9_eje3_N1.x, ld.anterior9_eje3_N1.y, ld.anterior9_eje3_N1.w, ld.anterior9_eje3_N1.h)]
ld.zones['EJERCICIO3_N1'] ['terminar_nivel'] = [(510, 175, 80, 70)]
#=====================================================================
# EJERCICIO1_N2 800X600
#=====================================================================

ld.anterior_eje1_N2 = MetaData()
ld.anterior_eje1_N2.path = 'img/anterior.png'
ld.anterior_eje1_N2.w = 65
ld.anterior_eje1_N2.h = 60
ld.anterior_eje1_N2.x = 5
ld.anterior_eje1_N2.y = 10

ld.pinguino_eje1_N2 = MetaData()
ld.pinguino_eje1_N2.path = 'img/pinguino.png'
ld.pinguino_eje1_N2.w = 40
ld.pinguino_eje1_N2.h = 60
ld.pinguino_eje1_N2.x = 120
ld.pinguino_eje1_N2.y = 330

ld.hielo_eje1_N2 = MetaData()
ld.hielo_eje1_N2.path = 'img/hielo.png'
ld.hielo_eje1_N2.w = 176
ld.hielo_eje1_N2.h = 251
ld.hielo_eje1_N2.x = 0
ld.hielo_eje1_N2.y = 100

ld.nevado_eje1_N2 = MetaData()
ld.nevado_eje1_N2.path = 'img/nevado.png'
ld.nevado_eje1_N2.w = 422
ld.nevado_eje1_N2.h = 157
ld.nevado_eje1_N2.x = 375
ld.nevado_eje1_N2.y = 100

ld.iglu_eje1_N2 = MetaData()
ld.iglu_eje1_N2.path = 'img/iglu.png'
ld.iglu_eje1_N2.w = 91
ld.iglu_eje1_N2.h = 61
ld.iglu_eje1_N2.x = 470
ld.iglu_eje1_N2.y = 130

ld.rio_eje1_N2 = MetaData()
ld.rio_eje1_N2.path = 'img/rio.png'
ld.rio_eje1_N2.w = 800
ld.rio_eje1_N2.h = 93
ld.rio_eje1_N2.x = 0
ld.rio_eje1_N2.y = 100

ld.orca_eje1_N2 = MetaData()
ld.orca_eje1_N2.path = 'img/orca.png'
ld.orca_eje1_N2.w = 235
ld.orca_eje1_N2.h = 134
ld.orca_eje1_N2.x = 180
ld.orca_eje1_N2.y = 150

ld.ok_eje1_N2 = MetaData()
ld.ok_eje1_N2.path = 'img/ok.png'
ld.ok_eje1_N2.w = 36
ld.ok_eje1_N2.h = 37
ld.ok_eje1_N2.x = 735
ld.ok_eje1_N2.y = 390

ld.actualizar_eje1_N2 = MetaData()
ld.actualizar_eje1_N2.path = 'img/actualizar.png'
ld.actualizar_eje1_N2.w = 37
ld.actualizar_eje1_N2.h = 37
ld.actualizar_eje1_N2.x = 735
ld.actualizar_eje1_N2.y = 460

ld.casa_eje1_N2 = MetaData()
ld.casa_eje1_N2.path = 'img/casa.png'
ld.casa_eje1_N2.w = 37
ld.casa_eje1_N2.h = 35
ld.casa_eje1_N2.x = 735
ld.casa_eje1_N2.y = 520

ld.bombillo_eje1_N2 = MetaData()
ld.bombillo_eje1_N2.path = 'img/bombillo.png'
ld.bombillo_eje1_N2.w = 31
ld.bombillo_eje1_N2.h = 31
ld.bombillo_eje1_N2.x = 760
ld.bombillo_eje1_N2.y = 15

ld.siguiente_eje1_N2 = MetaData()
ld.siguiente_eje1_N2.path = 'img/siguiente.png'
ld.siguiente_eje1_N2.w = 150
ld.siguiente_eje1_N2.h = 71
ld.siguiente_eje1_N2.x = 640
ld.siguiente_eje1_N2.y = 0

ld.no_eje1_N2 = MetaData()
ld.no_eje1_N2.path = 'img/mal.gif'
ld.no_eje1_N2.w = 162
ld.no_eje1_N2.h = 87
ld.no_eje1_N2.x = 185
ld.no_eje1_N2.y = 140

ld.exe_eje1_N2 = MetaData()
ld.exe_eje1_N2.path = 'img/banana.gif'
ld.exe_eje1_N2.w = 193
ld.exe_eje1_N2.h = 116
ld.exe_eje1_N2.x = 150
ld.exe_eje1_N2.y = 140

ld.flecha_menos_eje1_N2 = MetaData()
ld.flecha_menos_eje1_N2.path = 'img/flecha-.png'
ld.flecha_menos_eje1_N2.w = 13
ld.flecha_menos_eje1_N2.h = 18
ld.flecha_menos_eje1_N2.x = 520
ld.flecha_menos_eje1_N2.y = 405

ld.flecha_mas_eje1_N2 = MetaData()
ld.flecha_mas_eje1_N2.path = 'img/flecha+.png'
ld.flecha_mas_eje1_N2.w = 13
ld.flecha_mas_eje1_N2.h = 18
ld.flecha_mas_eje1_N2.x = 600
ld.flecha_mas_eje1_N2.y = 405

ld.altura_iceberg_campo_eje1_N2 = MetaData()
ld.altura_iceberg_campo_eje1_N2.path = 'img/campo.png'
ld.altura_iceberg_campo_eje1_N2.w = 55
ld.altura_iceberg_campo_eje1_N2.h = 25
ld.altura_iceberg_campo_eje1_N2.x = 150
ld.altura_iceberg_campo_eje1_N2.y = 55

ld.velocidad_pingui_campo_eje1_N2 = MetaData()
ld.velocidad_pingui_campo_eje1_N2.path = 'img/campo.png'
ld.velocidad_pingui_campo_eje1_N2.w = 55
ld.velocidad_pingui_campo_eje1_N2.h = 25
ld.velocidad_pingui_campo_eje1_N2.x = 595
ld.velocidad_pingui_campo_eje1_N2.y = 55

ld.res_campo_eje1_N2 = MetaData()
ld.res_campo_eje1_N2.path = 'img/campo.png'
ld.res_campo_eje1_N2.w = 55
ld.res_campo_eje1_N2.h = 25
ld.res_campo_eje1_N2.x = 540
ld.res_campo_eje1_N2.y = 400

ld.altura_eje1_N2 = MetaData()
ld.altura_eje1_N2.path = 'img/altura.png'
ld.altura_eje1_N2.w = 112
ld.altura_eje1_N2.h = 26
ld.altura_eje1_N2.x = 120
ld.altura_eje1_N2.y = 35

ld.velocidad_eje1_N2 = MetaData()
ld.velocidad_eje1_N2.path = 'img/velocidad.png'
ld.velocidad_eje1_N2.w = 142
ld.velocidad_eje1_N2.h = 26
ld.velocidad_eje1_N2.x = 555
ld.velocidad_eje1_N2.y = 35

ld.alcance_horizontal_eje1_N2 = MetaData()
ld.alcance_horizontal_eje1_N2.path = 'img/alcance.png'
ld.alcance_horizontal_eje1_N2.w = 140
ld.alcance_horizontal_eje1_N2.h = 24
ld.alcance_horizontal_eje1_N2.x = 500
ld.alcance_horizontal_eje1_N2.y = 420

ld.laltura_eje1_N2 = MetaData()
ld.laltura_eje1_N2.text = ''
ld.laltura_eje1_N2.color = (0, 0, 0, 255)
ld.laltura_eje1_N2.fname = 'DejaVu Sans Mono'
ld.laltura_eje1_N2.fsize = 10
ld.laltura_eje1_N2.x = 160
ld.laltura_eje1_N2.y = 67

ld.lvelocidad_eje1_N2 = MetaData()
ld.lvelocidad_eje1_N2.text = ''
ld.lvelocidad_eje1_N2.color = (0, 0, 0, 255)
ld.lvelocidad_eje1_N2.fname = 'DejaVu Sans Mono'
ld.lvelocidad_eje1_N2.fsize = 10
ld.lvelocidad_eje1_N2.x = 615
ld.lvelocidad_eje1_N2.y = 67

ld.lalcance_horizontal_eje1_N2 = MetaData()
ld.lalcance_horizontal_eje1_N2.text = ''
ld.lalcance_horizontal_eje1_N2.color = (0, 0, 0, 255)
ld.lalcance_horizontal_eje1_N2.fname = 'DejaVu Sans Mono'
ld.lalcance_horizontal_eje1_N2.fsize = 10
ld.lalcance_horizontal_eje1_N2.x = 550
ld.lalcance_horizontal_eje1_N2.y = 411

ld.ldescripcion_eje1_N2 = MetaData()
ld.ldescripcion_eje1_N2.text = ''
ld.ldescripcion_eje1_N2.color = (0, 0, 0, 255)
ld.ldescripcion_eje1_N2.fname = 'DejaVu Sans Mono'
ld.ldescripcion_eje1_N2.fsize = 10
ld.ldescripcion_eje1_N2.x = 385
ld.ldescripcion_eje1_N2.y = 545

ld.zones['EJERCICIO1_N2'] = {}
ld.zones['EJERCICIO1_N2'] ['ir_niveles'] = [(ld.anterior_eje1_N2.x, ld.anterior_eje1_N2.y, ld.anterior_eje1_N2.w, ld.anterior_eje1_N2.h)]
ld.zones['EJERCICIO1_N2'] ['ir_ok'] = [(ld.ok_eje1_N2.x, ld.ok_eje1_N2.y, ld.ok_eje1_N2.w, ld.ok_eje1_N2.h)]
ld.zones['EJERCICIO1_N2'] ['ir_casa'] = [(ld.casa_eje1_N2.x, ld.casa_eje1_N2.y, ld.casa_eje1_N2.w, ld.casa_eje1_N2.h)]
ld.zones['EJERCICIO1_N2'] ['ir_actualizar'] = [(ld.actualizar_eje1_N2.x, ld.actualizar_eje1_N2.y, ld.actualizar_eje1_N2.w, ld.actualizar_eje1_N2.h)]
ld.zones['EJERCICIO1_N2'] ['ir_bombillo'] = [(ld.bombillo_eje1_N2.x, ld.bombillo_eje1_N2.y, ld.bombillo_eje1_N2.w, ld.bombillo_eje1_N2.h)]
ld.zones['EJERCICIO1_N2'] ['mas'] = [(ld.flecha_mas_eje1_N2.x, ld.flecha_mas_eje1_N2.y, ld.flecha_mas_eje1_N2.w, ld.flecha_mas_eje1_N2.h)]
ld.zones['EJERCICIO1_N2'] ['menos'] = [(ld.flecha_menos_eje1_N2.x, ld.flecha_menos_eje1_N2.y, ld.flecha_menos_eje1_N2.w, ld.flecha_menos_eje1_N2.h)]

#=====================================================================
# EJERCICIO2_N2 800X600
#=====================================================================

ld.anterior_eje2_N2 = MetaData()
ld.anterior_eje2_N2.path = 'img/anterior.png'
ld.anterior_eje2_N2.w = 65
ld.anterior_eje2_N2.h = 60
ld.anterior_eje2_N2.x = 5
ld.anterior_eje2_N2.y = 5

ld.monster_eje2_N2 = MetaData()
ld.monster_eje2_N2.path = 'img/monster.png'
ld.monster_eje2_N2.w = 88
ld.monster_eje2_N2.h = 51
ld.monster_eje2_N2.x = 1
ld.monster_eje2_N2.y = 260

ld.monster1_eje2_N2 = MetaData()
ld.monster1_eje2_N2.path = 'img/monster1.png'
ld.monster1_eje2_N2.w = 88
ld.monster1_eje2_N2.h = 53
ld.monster1_eje2_N2.x = 100
ld.monster1_eje2_N2.y = 260

ld.monster2_eje2_N2 = MetaData()
ld.monster2_eje2_N2.path = 'img/monster2.png'
ld.monster2_eje2_N2.w = 88
ld.monster2_eje2_N2.h = 57
ld.monster2_eje2_N2.x = 110
ld.monster2_eje2_N2.y = 260

ld.monster3_eje2_N2 = MetaData()
ld.monster3_eje2_N2.path = 'img/monster3.png'
ld.monster3_eje2_N2.w = 90
ld.monster3_eje2_N2.h = 61
ld.monster3_eje2_N2.x = 121
ld.monster3_eje2_N2.y = 260

ld.monster4_eje2_N2 = MetaData()
ld.monster4_eje2_N2.path = 'img/monster4.png'
ld.monster4_eje2_N2.w = 90
ld.monster4_eje2_N2.h = 69
ld.monster4_eje2_N2.x = 135
ld.monster4_eje2_N2.y = 260

ld.monster5_eje2_N2 = MetaData()
ld.monster5_eje2_N2.path = 'img/monster5.png'
ld.monster5_eje2_N2.w = 88
ld.monster5_eje2_N2.h = 73
ld.monster5_eje2_N2.x = 155
ld.monster5_eje2_N2.x = 155
ld.monster5_eje2_N2.y = 263

ld.monster6_eje2_N2 = MetaData()
ld.monster6_eje2_N2.path = 'img/monster6.png'
ld.monster6_eje2_N2.w = 88
ld.monster6_eje2_N2.h = 73
ld.monster6_eje2_N2.x = 180
ld.monster6_eje2_N2.y = 273

ld.sombra_eje2_N2 = MetaData()
ld.sombra_eje2_N2.path = 'img/sombra.png'
ld.sombra_eje2_N2.w = 88
ld.sombra_eje2_N2.h = 51
ld.sombra_eje2_N2.x = 530
ld.sombra_eje2_N2.y = 258


ld.piedra_eje2_N2 = MetaData()
ld.piedra_eje2_N2.path = 'img/piedra.png'
ld.piedra_eje2_N2.w = 158
ld.piedra_eje2_N2.h = 63
ld.piedra_eje2_N2.x = 170
ld.piedra_eje2_N2.y = 239

ld.abismo1_eje2_N2 = MetaData()
ld.abismo1_eje2_N2.path = 'img/abismo1.png'
ld.abismo1_eje2_N2.w = 331
ld.abismo1_eje2_N2.h = 263
ld.abismo1_eje2_N2.x = 0
ld.abismo1_eje2_N2.y = 0

ld.abismo2_eje2_N2 = MetaData()
ld.abismo2_eje2_N2.path = 'img/abismo2.png'
ld.abismo2_eje2_N2.w = 331
ld.abismo2_eje2_N2.h = 305
ld.abismo2_eje2_N2.x = 469
ld.abismo2_eje2_N2.y = 0

ld.rocas_eje2_N2 = MetaData()
ld.rocas_eje2_N2.path = 'img/rocas.png'
ld.rocas_eje2_N2.w = 800
ld.rocas_eje2_N2.h = 40
ld.rocas_eje2_N2.x = 2
ld.rocas_eje2_N2.y = 0

ld.ok_eje2_N2 = MetaData()
ld.ok_eje2_N2.path = 'img/ok.png'
ld.ok_eje2_N2.w = 36
ld.ok_eje2_N2.h = 37
ld.ok_eje2_N2.x = 735
ld.ok_eje2_N2.y = 395

ld.actualizar_eje2_N2 = MetaData()
ld.actualizar_eje2_N2.path = 'img/actualizar.png'
ld.actualizar_eje2_N2.w = 37
ld.actualizar_eje2_N2.h = 37
ld.actualizar_eje2_N2.x = 735
ld.actualizar_eje2_N2.y = 465

ld.casa_eje2_N2 = MetaData()
ld.casa_eje2_N2.path = 'img/casa.png'
ld.casa_eje2_N2.w = 37
ld.casa_eje2_N2.h = 35
ld.casa_eje2_N2.x = 735
ld.casa_eje2_N2.y = 520

ld.bombillo_eje2_N2 = MetaData()
ld.bombillo_eje2_N2.path = 'img/bombillo.png'
ld.bombillo_eje2_N2.w = 31
ld.bombillo_eje2_N2.h = 31
ld.bombillo_eje2_N2.x = 760
ld.bombillo_eje2_N2.y = 15

ld.siguiente_eje2_N2 = MetaData()
ld.siguiente_eje2_N2.path = 'img/siguiente.png'
ld.siguiente_eje2_N2.w = 150
ld.siguiente_eje2_N2.h = 71
ld.siguiente_eje2_N2.x = 640
ld.siguiente_eje2_N2.y = 0

ld.no_eje2_N2 = MetaData()
ld.no_eje2_N2.path = 'img/mal.gif'
ld.no_eje2_N2.w = 162
ld.no_eje2_N2.h = 87
ld.no_eje2_N2.x = 250
ld.no_eje2_N2.y = 10

ld.exe_eje2_N2 = MetaData()
ld.exe_eje2_N2.path = 'img/banana.gif'
ld.exe_eje2_N2.w = 193
ld.exe_eje2_N2.h = 116
ld.exe_eje2_N2.x = 230
ld.exe_eje2_N2.y = 10

ld.explosion_eje2_N2 = MetaData()
ld.explosion_eje2_N2.path = 'img/explosion.gif'
ld.explosion_eje2_N2.w = 329
ld.explosion_eje2_N2.h = 198
ld.explosion_eje2_N2.x = 320
ld.explosion_eje2_N2.y = 8

ld.flecha_menos_eje2_N2 = MetaData()
ld.flecha_menos_eje2_N2.path = 'img/flecha-.png'
ld.flecha_menos_eje2_N2.w = 13
ld.flecha_menos_eje2_N2.h = 18
ld.flecha_menos_eje2_N2.x = 540
ld.flecha_menos_eje2_N2.y = 385

ld.flecha_mas_eje2_N2 = MetaData()
ld.flecha_mas_eje2_N2.path = 'img/flecha+.png'
ld.flecha_mas_eje2_N2.w = 13
ld.flecha_mas_eje2_N2.h = 18
ld.flecha_mas_eje2_N2.x = 620
ld.flecha_mas_eje2_N2.y = 385

ld.altura_colina_campo_eje2_N2 = MetaData()
ld.altura_colina_campo_eje2_N2.path = 'img/campo.png'
ld.altura_colina_campo_eje2_N2.w = 55
ld.altura_colina_campo_eje2_N2.h = 25
ld.altura_colina_campo_eje2_N2.x = 200
ld.altura_colina_campo_eje2_N2.y = 70

ld.angulo_campo_eje2_N2 = MetaData()
ld.angulo_campo_eje2_N2.path = 'img/campo.png'
ld.angulo_campo_eje2_N2.w = 55
ld.angulo_campo_eje2_N2.h = 25
ld.angulo_campo_eje2_N2.x = 45
ld.angulo_campo_eje2_N2.y = 350

ld.res_campo_eje2_N2 = MetaData()
ld.res_campo_eje2_N2.path = 'img/campo.png'
ld.res_campo_eje2_N2.w = 55
ld.res_campo_eje2_N2.h = 25
ld.res_campo_eje2_N2.x = 560
ld.res_campo_eje2_N2.y = 380

ld.altura_colina_eje2_N2 = MetaData()
ld.altura_colina_eje2_N2.path = 'img/alturaColina.png'
ld.altura_colina_eje2_N2.w = 108
ld.altura_colina_eje2_N2.h = 26
ld.altura_colina_eje2_N2.x = 180
ld.altura_colina_eje2_N2.y = 90

ld.angulo_eje2_N2 = MetaData()
ld.angulo_eje2_N2.path = 'img/angulo.png'
ld.angulo_eje2_N2.w = 129
ld.angulo_eje2_N2.h = 28
ld.angulo_eje2_N2.x = 10
ld.angulo_eje2_N2.y = 370

ld.velocidad_eje2_N2 = MetaData()
ld.velocidad_eje2_N2.path = 'img/velocidadAuto.png'
ld.velocidad_eje2_N2.w = 117
ld.velocidad_eje2_N2.h = 26
ld.velocidad_eje2_N2.x = 530
ld.velocidad_eje2_N2.y = 400

ld.ldescripcion_eje2_N2 = MetaData()
ld.ldescripcion_eje2_N2.text = ''
ld.ldescripcion_eje2_N2.color = (0, 0, 0, 255)
ld.ldescripcion_eje2_N2.fname = 'DejaVu Sans Mono'
ld.ldescripcion_eje2_N2.fsize = 10
ld.ldescripcion_eje2_N2.x = 380
ld.ldescripcion_eje2_N2.y = 545

ld.laltura_eje2_N2 = MetaData()
ld.laltura_eje2_N2.text = ''
ld.laltura_eje2_N2.color = (0, 0, 0, 255)
ld.laltura_eje2_N2.fname = 'DejaVu Sans Mono'
ld.laltura_eje2_N2.fsize = 10
ld.laltura_eje2_N2.x = 209
ld.laltura_eje2_N2.y = 81

ld.langulo_elevacion_eje2_N2 = MetaData()
ld.langulo_elevacion_eje2_N2.text = ''
ld.langulo_elevacion_eje2_N2.color = (0, 0, 0, 255)
ld.langulo_elevacion_eje2_N2.fname = 'DejaVu Sans Mono'
ld.langulo_elevacion_eje2_N2.fsize = 10
ld.langulo_elevacion_eje2_N2.x = 65
ld.langulo_elevacion_eje2_N2.y = 361

ld.lvelocidad_eje2_N2 = MetaData()
ld.lvelocidad_eje2_N2.text = ''
ld.lvelocidad_eje2_N2.color = (0, 0, 0, 255)
ld.lvelocidad_eje2_N2.fname = 'DejaVu Sans Mono'
ld.lvelocidad_eje2_N2.fsize = 10
ld.lvelocidad_eje2_N2.x = 562
ld.lvelocidad_eje2_N2.y = 391

ld.zones['EJERCICIO2_N2'] = {}
ld.zones['EJERCICIO2_N2'] ['ir_niveles'] = [(ld.anterior_eje2_N2.x, ld.anterior_eje2_N2.y, ld.anterior_eje2_N2.w, ld.anterior_eje2_N2.h)]
ld.zones['EJERCICIO2_N2'] ['ir_ok'] = [(ld.ok_eje2_N2.x, ld.ok_eje2_N2.y, ld.ok_eje2_N2.w, ld.ok_eje2_N2.h)]
ld.zones['EJERCICIO2_N2'] ['ir_casa'] = [(ld.casa_eje2_N2.x, ld.casa_eje2_N2.y, ld.casa_eje2_N2.w, ld.casa_eje2_N2.h)]
ld.zones['EJERCICIO2_N2'] ['ir_actualizar'] = [(ld.actualizar_eje2_N2.x, ld.actualizar_eje2_N2.y, ld.actualizar_eje2_N2.w, ld.actualizar_eje2_N2.h)]
ld.zones['EJERCICIO2_N2'] ['ir_bombillo'] = [(ld.bombillo_eje2_N2.x, ld.bombillo_eje2_N2.y, ld.bombillo_eje2_N2.w, ld.bombillo_eje2_N2.h)]
ld.zones['EJERCICIO2_N2'] ['mas'] = [(ld.flecha_mas_eje2_N2.x, ld.flecha_mas_eje2_N2.y, ld.flecha_mas_eje2_N2.w, ld.flecha_mas_eje2_N2.h)]
ld.zones['EJERCICIO2_N2'] ['menos'] = [(ld.flecha_menos_eje2_N2.x, ld.flecha_menos_eje2_N2.y, ld.flecha_menos_eje2_N2.w, ld.flecha_menos_eje2_N2.h)]

#=====================================================================
# EJERCICIO3_N2 800X600
#=====================================================================

ld.anterior_eje3_N2 = MetaData()
ld.anterior_eje3_N2.path = 'img/anterior.png'
ld.anterior_eje3_N2.w = 65
ld.anterior_eje3_N2.h = 60
ld.anterior_eje3_N2.x = 5
ld.anterior_eje3_N2.y = 5

ld.rocas_eje3_N2 = MetaData()
ld.rocas_eje3_N2.path = 'img/rocas2.png'
ld.rocas_eje3_N2.w = 800
ld.rocas_eje3_N2.h = 40
ld.rocas_eje3_N2.x = 0
ld.rocas_eje3_N2.y = 0

ld.grua_eje3_N2 = MetaData()
ld.grua_eje3_N2.path = 'img/grua.png'
ld.grua_eje3_N2.w = 387
ld.grua_eje3_N2.h = 333
ld.grua_eje3_N2.x = 100
ld.grua_eje3_N2.y = 5

ld.bola_eje3_N2 = MetaData()
ld.bola_eje3_N2.path = 'img/bola1.gif'
ld.bola_eje3_N2.w = 225
ld.bola_eje3_N2.h = 191
ld.bola_eje3_N2.x = 349
ld.bola_eje3_N2.y = 130

ld.bola1_eje3_N2 = MetaData()
ld.bola1_eje3_N2.path = 'img/bola1.png'
ld.bola1_eje3_N2.w = 53
ld.bola1_eje3_N2.h = 183
ld.bola1_eje3_N2.x = 437
ld.bola1_eje3_N2.y = 135

ld.edificio_eje3_N2 = MetaData()
ld.edificio_eje3_N2.path = 'img/edificio.png'
ld.edificio_eje3_N2.w = 188
ld.edificio_eje3_N2.h = 269
ld.edificio_eje3_N2.x = 565
ld.edificio_eje3_N2.y = 20

ld.luz_eje3_N2 = MetaData()
ld.luz_eje3_N2.path = 'img/luz1.gif'
ld.luz_eje3_N2.w = 300
ld.luz_eje3_N2.h = 340
ld.luz_eje3_N2.x = 495
ld.luz_eje3_N2.y = 0

ld.ok_eje3_N2 = MetaData()
ld.ok_eje3_N2.path = 'img/ok.png'
ld.ok_eje3_N2.w = 36
ld.ok_eje3_N2.h = 37
ld.ok_eje3_N2.x = 735
ld.ok_eje3_N2.y = 395

ld.actualizar_eje3_N2 = MetaData()
ld.actualizar_eje3_N2.path = 'img/actualizar.png'
ld.actualizar_eje3_N2.w = 37
ld.actualizar_eje3_N2.h = 37
ld.actualizar_eje3_N2.x = 735
ld.actualizar_eje3_N2.y = 465

ld.casa_eje3_N2 = MetaData()
ld.casa_eje3_N2.path = 'img/casa.png'
ld.casa_eje3_N2.w = 37
ld.casa_eje3_N2.h = 35
ld.casa_eje3_N2.x = 735
ld.casa_eje3_N2.y = 520

ld.bombillo_eje3_N2 = MetaData()
ld.bombillo_eje3_N2.path = 'img/bombillo.png'
ld.bombillo_eje3_N2.w = 31
ld.bombillo_eje3_N2.h = 31
ld.bombillo_eje3_N2.x = 760
ld.bombillo_eje3_N2.y = 10

ld.siguiente_eje3_N2 = MetaData()
ld.siguiente_eje3_N2.path = 'img/siguiente.png'
ld.siguiente_eje3_N2.w = 150
ld.siguiente_eje3_N2.h = 71
ld.siguiente_eje3_N2.x = 640
ld.siguiente_eje3_N2.y = 0

ld.no_eje3_N2 = MetaData()
ld.no_eje3_N2.path = 'img/mal.gif'
ld.no_eje3_N2.w = 162
ld.no_eje3_N2.h = 87
ld.no_eje3_N2.x = 300
ld.no_eje3_N2.y = 10

ld.exe_eje3_N2 = MetaData()
ld.exe_eje3_N2.path = 'img/banana.gif'
ld.exe_eje3_N2.w = 193
ld.exe_eje3_N2.h = 116
ld.exe_eje3_N2.x = 270
ld.exe_eje3_N2.y = 10

ld.flecha_menos_eje3_N2 = MetaData()
ld.flecha_menos_eje3_N2.path = 'img/flecha-.png'
ld.flecha_menos_eje3_N2.w = 13
ld.flecha_menos_eje3_N2.h = 18
ld.flecha_menos_eje3_N2.x = 540
ld.flecha_menos_eje3_N2.y = 385

ld.flecha_mas_eje3_N2 = MetaData()
ld.flecha_mas_eje3_N2.path = 'img/flecha+.png'
ld.flecha_mas_eje3_N2.w = 13
ld.flecha_mas_eje3_N2.h = 18
ld.flecha_mas_eje3_N2.x = 620
ld.flecha_mas_eje3_N2.y = 385

ld.longitud_cable_campo_eje3_N2 = MetaData()
ld.longitud_cable_campo_eje3_N2.path = 'img/campo.png'
ld.longitud_cable_campo_eje3_N2.w = 55
ld.longitud_cable_campo_eje3_N2.h = 25
ld.longitud_cable_campo_eje3_N2.x = 110
ld.longitud_cable_campo_eje3_N2.y = 230

ld.res_campo_eje3_N2 = MetaData()
ld.res_campo_eje3_N2.path = 'img/campo.png'
ld.res_campo_eje3_N2.w = 55
ld.res_campo_eje3_N2.h = 25
ld.res_campo_eje3_N2.x = 560
ld.res_campo_eje3_N2.y = 380

ld.longitud_eje3_N2 = MetaData()
ld.longitud_eje3_N2.path = 'img/longitud.png'
ld.longitud_eje3_N2.w = 120
ld.longitud_eje3_N2.h = 29
ld.longitud_eje3_N2.x = 80
ld.longitud_eje3_N2.y = 250

ld.periodo_eje3_N2 = MetaData()
ld.periodo_eje3_N2.path = 'img/periodo.png'
ld.periodo_eje3_N2.w = 126
ld.periodo_eje3_N2.h = 26
ld.periodo_eje3_N2.x = 530
ld.periodo_eje3_N2.y = 400

ld.ldescripcion_eje3_N2 = MetaData()
ld.ldescripcion_eje3_N2.text = ''
ld.ldescripcion_eje3_N2.color = (0, 0, 0, 255)
ld.ldescripcion_eje3_N2.fname = 'DejaVu Sans Mono'
ld.ldescripcion_eje3_N2.fsize = 10
ld.ldescripcion_eje3_N2.x = 380
ld.ldescripcion_eje3_N2.y = 545

ld.llongitud_eje3_N2 = MetaData()
ld.llongitud_eje3_N2.text = ''
ld.llongitud_eje3_N2.color = (0, 0, 0, 255)
ld.llongitud_eje3_N2.fname = 'DejaVu Sans Mono'
ld.llongitud_eje3_N2.fsize = 10
ld.llongitud_eje3_N2.x = 110
ld.llongitud_eje3_N2.y = 230

ld.lperiodo_eje3_N2 = MetaData()
ld.lperiodo_eje3_N2.text = ''
ld.lperiodo_eje3_N2.color = (0, 0, 0, 255)
ld.lperiodo_eje3_N2.fname = 'DejaVu Sans Mono'
ld.lperiodo_eje3_N2.fsize = 10
ld.lperiodo_eje3_N2.x = 560
ld.lperiodo_eje3_N2.y = 368

ld.diploma_N2 = MetaData()
ld.diploma_N2.path = 'img/diploma_n2.png'
ld.diploma_N2.w = 451
ld.diploma_N2.h = 350
ld.diploma_N2.x = 165
ld.diploma_N2.y = 110

ld.zones['EJERCICIO3_N2'] = {}
ld.zones['EJERCICIO3_N2'] ['ir_niveles'] = [(ld.anterior_eje3_N2.x, ld.anterior_eje3_N2.y, ld.anterior_eje3_N2.w, ld.anterior_eje3_N2.h)]
ld.zones['EJERCICIO3_N2'] ['ir_ok'] = [(ld.ok_eje3_N2.x, ld.ok_eje3_N2.y, ld.ok_eje3_N2.w, ld.ok_eje3_N2.h)]
ld.zones['EJERCICIO3_N2'] ['ir_casa'] = [(ld.casa_eje3_N2.x, ld.casa_eje3_N2.y, ld.casa_eje3_N2.w, ld.casa_eje3_N2.h)]
ld.zones['EJERCICIO3_N2'] ['ir_actualizar'] = [(ld.actualizar_eje3_N2.x, ld.actualizar_eje3_N2.y, ld.actualizar_eje3_N2.w, ld.actualizar_eje3_N2.h)]
ld.zones['EJERCICIO3_N2'] ['ir_bombillo'] = [(ld.bombillo_eje3_N2.x, ld.bombillo_eje3_N2.y, ld.bombillo_eje3_N2.w, ld.bombillo_eje3_N2.h)]
ld.zones['EJERCICIO3_N2'] ['mas'] = [(ld.flecha_mas_eje3_N2.x, ld.flecha_mas_eje3_N2.y, ld.flecha_mas_eje3_N2.w, ld.flecha_mas_eje3_N2.h)]
ld.zones['EJERCICIO3_N2'] ['menos'] = [(ld.flecha_menos_eje3_N2.x, ld.flecha_menos_eje3_N2.y, ld.flecha_menos_eje3_N2.w, ld.flecha_menos_eje3_N2.h)]

#=====================================================================
# EJERCICIO1_N3 800X600 
#=====================================================================

ld.anterior_eje1_N3 = MetaData()
ld.anterior_eje1_N3.path = 'img/anterior.png'
ld.anterior_eje1_N3.w = 65
ld.anterior_eje1_N3.h = 60
ld.anterior_eje1_N3.x = 0
ld.anterior_eje1_N3.y = 0

ld.suelo_eje1_N3 = MetaData()
ld.suelo_eje1_N3.path = 'img/suelo.png'
ld.suelo_eje1_N3.w = 800
ld.suelo_eje1_N3.h = 150
ld.suelo_eje1_N3.x = 0
ld.suelo_eje1_N3.y = 0

ld.arbol_eje1_N3 = MetaData()
ld.arbol_eje1_N3.path = 'img/arbol.png'
ld.arbol_eje1_N3.w = 350
ld.arbol_eje1_N3.h = 390
ld.arbol_eje1_N3.x = 0
ld.arbol_eje1_N3.y = 0

ld.manzana_eje1_N3 = MetaData()
ld.manzana_eje1_N3.path = 'img/manzana.png'
ld.manzana_eje1_N3.w = 23
ld.manzana_eje1_N3.h = 26
ld.manzana_eje1_N3.x = 201
ld.manzana_eje1_N3.y = 300

ld.nino_eje1_N3 = MetaData()
ld.nino_eje1_N3.path = 'img/nino.png'
ld.nino_eje1_N3.w = 190
ld.nino_eje1_N3.h = 100
ld.nino_eje1_N3.x = 170
ld.nino_eje1_N3.y = 0

ld.sol_eje1_N3 = MetaData()
ld.sol_eje1_N3.path = 'img/sol.png'
ld.sol_eje1_N3.w = 150
ld.sol_eje1_N3.h = 150
ld.sol_eje1_N3.x = 580
ld.sol_eje1_N3.y = 310

ld.golpe_eje1_N3 = MetaData()
ld.golpe_eje1_N3.path = 'img/golpe1.gif'
ld.golpe_eje1_N3.w = 120
ld.golpe_eje1_N3.h = 113
ld.golpe_eje1_N3.x = 110
ld.golpe_eje1_N3.y = 34

ld.ok_eje1_N3 = MetaData()
ld.ok_eje1_N3.path = 'img/ok.png'
ld.ok_eje1_N3.w = 36
ld.ok_eje1_N3.h = 37
ld.ok_eje1_N3.x = 735
ld.ok_eje1_N3.y = 395

ld.actualizar_eje1_N3 = MetaData()
ld.actualizar_eje1_N3.path = 'img/actualizar.png'
ld.actualizar_eje1_N3.w = 37
ld.actualizar_eje1_N3.h = 37
ld.actualizar_eje1_N3.x = 735
ld.actualizar_eje1_N3.y = 465

ld.casa_eje1_N3 = MetaData()
ld.casa_eje1_N3.path = 'img/casa.png'
ld.casa_eje1_N3.w = 37
ld.casa_eje1_N3.h = 35
ld.casa_eje1_N3.x = 735
ld.casa_eje1_N3.y = 520

ld.bombillo_eje1_N3 = MetaData()
ld.bombillo_eje1_N3.path = 'img/bombillo.png'
ld.bombillo_eje1_N3.w = 31
ld.bombillo_eje1_N3.h = 31
ld.bombillo_eje1_N3.x = 760
ld.bombillo_eje1_N3.y = 10

ld.siguiente_eje1_N3 = MetaData()
ld.siguiente_eje1_N3.path = 'img/siguiente.png'
ld.siguiente_eje1_N3.w = 150
ld.siguiente_eje1_N3.h = 71
ld.siguiente_eje1_N3.x = 640
ld.siguiente_eje1_N3.y = 0

ld.no_eje1_N3 = MetaData()
ld.no_eje1_N3.path = 'img/dormido.gif'
ld.no_eje1_N3.w = 162
ld.no_eje1_N3.h = 87
ld.no_eje1_N3.x = 400
ld.no_eje1_N3.y = 0

ld.exe_eje1_N3 = MetaData()
ld.exe_eje1_N3.path = 'img/gano.gif'
ld.exe_eje1_N3.w = 193
ld.exe_eje1_N3.h = 116
ld.exe_eje1_N3.x = 400
ld.exe_eje1_N3.y = 0

ld.tiempo_caida_campo_eje1_N3 = MetaData()
ld.tiempo_caida_campo_eje1_N3.path = 'img/campo.png'
ld.tiempo_caida_campo_eje1_N3.w = 55
ld.tiempo_caida_campo_eje1_N3.h = 25
ld.tiempo_caida_campo_eje1_N3.x = 500
ld.tiempo_caida_campo_eje1_N3.y = 380

ld.res_campo_eje1_N3 = MetaData()
ld.res_campo_eje1_N3.path = 'img/campo.png'
ld.res_campo_eje1_N3.w = 55
ld.res_campo_eje1_N3.h = 25
ld.res_campo_eje1_N3.x = 360
ld.res_campo_eje1_N3.y = 230

ld.distancia_recorrida_eje1_N3 = MetaData()
ld.distancia_recorrida_eje1_N3.path = 'img/distanciaRecorrida.png'
ld.distancia_recorrida_eje1_N3.w = 145
ld.distancia_recorrida_eje1_N3.h = 24
ld.distancia_recorrida_eje1_N3.x = 315
ld.distancia_recorrida_eje1_N3.y = 250

ld.tiempo_caida_eje1_N3 = MetaData()
ld.tiempo_caida_eje1_N3.path = 'img/tiempoCaida.png'
ld.tiempo_caida_eje1_N3.w = 107
ld.tiempo_caida_eje1_N3.h = 26
ld.tiempo_caida_eje1_N3.x = 475
ld.tiempo_caida_eje1_N3.y = 400

ld.ldescripcion_eje1_N3 = MetaData()
ld.ldescripcion_eje1_N3.text = ''
ld.ldescripcion_eje1_N3.color = (0, 0, 0, 255)
ld.ldescripcion_eje1_N3.fname = 'DejaVu Sans Mono'
ld.ldescripcion_eje1_N3.fsize = 10
ld.ldescripcion_eje1_N3.x = 380
ld.ldescripcion_eje1_N3.y = 545

ld.ldistancia_recorrida_eje1_N3 = MetaData()
ld.ldistancia_recorrida_eje1_N3.text = ''
ld.ldistancia_recorrida_eje1_N3.color = (0, 0, 0, 255)
ld.ldistancia_recorrida_eje1_N3.fname = 'DejaVu Sans Mono'
ld.ldistancia_recorrida_eje1_N3.fsize = 10
ld.ldistancia_recorrida_eje1_N3.x = 360
ld.ldistancia_recorrida_eje1_N3.y = 230

ld.ltiempo_caida_eje1_N3 = MetaData()
ld.ltiempo_caida_eje1_N3.text = ''
ld.ltiempo_caida_eje1_N3.color = (0, 0, 0, 255)
ld.ltiempo_caida_eje1_N3.fname = 'DejaVu Sans Mono'
ld.ltiempo_caida_eje1_N3.fsize = 10
ld.ltiempo_caida_eje1_N3.x = 500
ld.ltiempo_caida_eje1_N3.y = 368


ld.zones['EJERCICIO1_N3'] = {}
ld.zones['EJERCICIO1_N3'] ['ir_niveles'] = [(ld.anterior_eje1_N3.x, ld.anterior_eje1_N3.y, ld.anterior_eje1_N3.w, ld.anterior_eje1_N3.h)]
ld.zones['EJERCICIO1_N3'] ['ir_ok'] = [(ld.ok_eje1_N3.x, ld.ok_eje1_N3.y, ld.ok_eje1_N3.w, ld.ok_eje1_N3.h)]
ld.zones['EJERCICIO1_N3'] ['ir_casa'] = [(ld.casa_eje1_N3.x, ld.casa_eje1_N3.y, ld.casa_eje1_N3.w, ld.casa_eje1_N3.h)]
ld.zones['EJERCICIO1_N3'] ['ir_actualizar'] = [(ld.actualizar_eje1_N3.x, ld.actualizar_eje1_N3.y, ld.actualizar_eje1_N3.w, ld.actualizar_eje1_N3.h)]
ld.zones['EJERCICIO1_N3'] ['ir_bombillo'] = [(ld.bombillo_eje1_N3.x, ld.bombillo_eje1_N3.y, ld.bombillo_eje1_N3.w, ld.bombillo_eje1_N3.h)]

#=====================================================================
# EJERCICIO2_N3 800X600 
#=====================================================================

ld.anterior_eje2_N3 = MetaData()
ld.anterior_eje2_N3.path = 'img/anterior.png'
ld.anterior_eje2_N3.w = 65
ld.anterior_eje2_N3.h = 60
ld.anterior_eje2_N3.x = 0
ld.anterior_eje2_N3.y = 0

ld.pasto_eje2_N3 = MetaData()
ld.pasto_eje2_N3.path = 'img/pasto.png'
ld.pasto_eje2_N3.w = 800
ld.pasto_eje2_N3.h = 100
ld.pasto_eje2_N3.x = 0
ld.pasto_eje2_N3.y = 0

ld.montana_eje2_N3 = MetaData()
ld.montana_eje2_N3.path = 'img/montana.png'
ld.montana_eje2_N3.w = 434
ld.montana_eje2_N3.h = 357
ld.montana_eje2_N3.x = 366
ld.montana_eje2_N3.y = 0

ld.arco_eje2_N3 = MetaData()
ld.arco_eje2_N3.path = 'img/arco.png'
ld.arco_eje2_N3.w = 700
ld.arco_eje2_N3.h = 428
ld.arco_eje2_N3.x = 0
ld.arco_eje2_N3.y = 0

ld.helicoptero_eje2_N3 = MetaData()
ld.helicoptero_eje2_N3.path = 'img/helicoptero.png'
ld.helicoptero_eje2_N3.w = 250
ld.helicoptero_eje2_N3.h = 119
ld.helicoptero_eje2_N3.x = 170
ld.helicoptero_eje2_N3.y = 300

ld.pepe_eje2_N3 = MetaData()
ld.pepe_eje2_N3.path = 'img/pepe.png'
ld.pepe_eje2_N3.w = 25
ld.pepe_eje2_N3.h = 35
ld.pepe_eje2_N3.x = 312
ld.pepe_eje2_N3.y = 340

ld.paracaidas_eje2_N3 = MetaData()
ld.paracaidas_eje2_N3.path = 'img/paracaidas.png'
ld.paracaidas_eje2_N3.w = 47
ld.paracaidas_eje2_N3.h = 58
ld.paracaidas_eje2_N3.x = 300
ld.paracaidas_eje2_N3.y = 367

ld.ok_eje2_N3 = MetaData()
ld.ok_eje2_N3.path = 'img/ok.png'
ld.ok_eje2_N3.w = 36
ld.ok_eje2_N3.h = 37
ld.ok_eje2_N3.x = 735
ld.ok_eje2_N3.y = 395

ld.actualizar_eje2_N3 = MetaData()
ld.actualizar_eje2_N3.path = 'img/actualizar.png'
ld.actualizar_eje2_N3.w = 37
ld.actualizar_eje2_N3.h = 37
ld.actualizar_eje2_N3.x = 735
ld.actualizar_eje2_N3.y = 465

ld.casa_eje2_N3 = MetaData()
ld.casa_eje2_N3.path = 'img/casa.png'
ld.casa_eje2_N3.w = 37
ld.casa_eje2_N3.h = 35
ld.casa_eje2_N3.x = 735
ld.casa_eje2_N3.y = 520

ld.bombillo_eje2_N3 = MetaData()
ld.bombillo_eje2_N3.path = 'img/bombillo.png'
ld.bombillo_eje2_N3.w = 31
ld.bombillo_eje2_N3.h = 31
ld.bombillo_eje2_N3.x = 760
ld.bombillo_eje2_N3.y = 10

ld.siguiente_eje2_N3 = MetaData()
ld.siguiente_eje2_N3.path = 'img/siguiente.png'
ld.siguiente_eje2_N3.w = 150
ld.siguiente_eje2_N3.h = 71
ld.siguiente_eje2_N3.x = 640
ld.siguiente_eje2_N3.y = 0

ld.no_eje2_N3 = MetaData()
ld.no_eje2_N3.path = 'img/dormido.gif'
ld.no_eje2_N3.w = 162
ld.no_eje2_N3.h = 87
ld.no_eje2_N3.x = 140
ld.no_eje2_N3.y = 0

ld.exe_eje2_N3 = MetaData()
ld.exe_eje2_N3.path = 'img/gano.gif'
ld.exe_eje2_N3.w = 193
ld.exe_eje2_N3.h = 116
ld.exe_eje2_N3.x = 170
ld.exe_eje2_N3.y = 0

ld.velocidad_inicial_campo_eje2_N3 = MetaData()
ld.velocidad_inicial_campo_eje2_N3.path = 'img/campo.png'
ld.velocidad_inicial_campo_eje2_N3.w = 55
ld.velocidad_inicial_campo_eje2_N3.h = 25
ld.velocidad_inicial_campo_eje2_N3.x = 35
ld.velocidad_inicial_campo_eje2_N3.y = 230

ld.altura_helicoptero_campo_eje2_N3 = MetaData()
ld.altura_helicoptero_campo_eje2_N3.path = 'img/campo.png'
ld.altura_helicoptero_campo_eje2_N3.w = 55
ld.altura_helicoptero_campo_eje2_N3.h = 25
ld.altura_helicoptero_campo_eje2_N3.x = 35
ld.altura_helicoptero_campo_eje2_N3.y = 160

ld.res_campo_eje2_N3 = MetaData()
ld.res_campo_eje2_N3.path = 'img/campo.png'
ld.res_campo_eje2_N3.w = 55
ld.res_campo_eje2_N3.h = 25
ld.res_campo_eje2_N3.x = 565
ld.res_campo_eje2_N3.y = 380

ld.velocidad_final_eje2_N3 = MetaData()
ld.velocidad_final_eje2_N3.path = 'img/velocidadF.png'
ld.velocidad_final_eje2_N3.w = 118
ld.velocidad_final_eje2_N3.h = 25
ld.velocidad_final_eje2_N3.x = 535
ld.velocidad_final_eje2_N3.y = 400

ld.velocidad_inicial_eje2_N3 = MetaData()
ld.velocidad_inicial_eje2_N3.path = 'img/velocidadI.png'
ld.velocidad_inicial_eje2_N3.w = 126
ld.velocidad_inicial_eje2_N3.h = 24
ld.velocidad_inicial_eje2_N3.x = 5
ld.velocidad_inicial_eje2_N3.y = 250

ld.altura_helicoptero_eje2_N3 = MetaData()
ld.altura_helicoptero_eje2_N3.path = 'img/alturaH.png'
ld.altura_helicoptero_eje2_N3.w = 140
ld.altura_helicoptero_eje2_N3.h = 27
ld.altura_helicoptero_eje2_N3.x = 5
ld.altura_helicoptero_eje2_N3.y = 180

ld.ldescripcion_eje2_N3 = MetaData()
ld.ldescripcion_eje2_N3.text = ''
ld.ldescripcion_eje2_N3.color = (0, 0, 0, 255)
ld.ldescripcion_eje2_N3.fname = 'DejaVu Sans Mono'
ld.ldescripcion_eje2_N3.fsize = 10
ld.ldescripcion_eje2_N3.x = 380
ld.ldescripcion_eje2_N3.y = 545

ld.lvelocidad_inicial_eje2_N3 = MetaData()
ld.lvelocidad_inicial_eje2_N3.text = ''
ld.lvelocidad_inicial_eje2_N3.color = (0, 0, 0, 255)
ld.lvelocidad_inicial_eje2_N3.fname = 'DejaVu Sans Mono'
ld.lvelocidad_inicial_eje2_N3.fsize = 10
ld.lvelocidad_inicial_eje2_N3.x = 10
ld.lvelocidad_inicial_eje2_N3.y = 450

ld.lvelocidad_final_eje2_N3 = MetaData()
ld.lvelocidad_final_eje2_N3.text = ''
ld.lvelocidad_final_eje2_N3.color = (0, 0, 0, 255)
ld.lvelocidad_final_eje2_N3.fname = 'DejaVu Sans Mono'
ld.lvelocidad_final_eje2_N3.fsize = 10
ld.lvelocidad_final_eje2_N3.x = 60
ld.lvelocidad_final_eje2_N3.y = 230

ld.laltura_helicoptero_eje2_N3 = MetaData()
ld.laltura_helicoptero_eje2_N3.text = ''
ld.laltura_helicoptero_eje2_N3.color = (0, 0, 0, 255)
ld.laltura_helicoptero_eje2_N3.fname = 'DejaVu Sans Mono'
ld.laltura_helicoptero_eje2_N3.fsize = 10
ld.laltura_helicoptero_eje2_N3.x = 10
ld.laltura_helicoptero_eje2_N3.y = 230


ld.zones['EJERCICIO2_N3'] = {}
ld.zones['EJERCICIO2_N3'] ['ir_niveles'] = [(ld.anterior_eje2_N3.x, ld.anterior_eje2_N3.y, ld.anterior_eje2_N3.w, ld.anterior_eje2_N3.h)]
ld.zones['EJERCICIO2_N3'] ['ir_ok'] = [(ld.ok_eje2_N3.x, ld.ok_eje2_N3.y, ld.ok_eje2_N3.w, ld.ok_eje2_N3.h)]
ld.zones['EJERCICIO2_N3'] ['ir_casa'] = [(ld.casa_eje2_N3.x, ld.casa_eje2_N3.y, ld.casa_eje2_N3.w, ld.casa_eje2_N3.h)]
ld.zones['EJERCICIO2_N3'] ['ir_actualizar'] = [(ld.actualizar_eje2_N3.x, ld.actualizar_eje2_N3.y, ld.actualizar_eje2_N3.w, ld.actualizar_eje2_N3.h)]
ld.zones['EJERCICIO2_N3'] ['ir_bombillo'] = [(ld.bombillo_eje2_N3.x, ld.bombillo_eje2_N3.y, ld.bombillo_eje2_N3.w, ld.bombillo_eje2_N3.h)]

#=====================================================================
# EJERCICIO3_N3 800X600 
#=====================================================================

ld.anterior_eje3_N3 = MetaData()
ld.anterior_eje3_N3.path = 'img/anterior.png'
ld.anterior_eje3_N3.w = 37
ld.anterior_eje3_N3.h = 34
ld.anterior_eje3_N3.x = 735
ld.anterior_eje3_N3.y = 335

ld.mar_eje3_N3 = MetaData()
ld.mar_eje3_N3.path = 'img/mar.png'
ld.mar_eje3_N3.w = 800
ld.mar_eje3_N3.h = 176
ld.mar_eje3_N3.x = 0
ld.mar_eje3_N3.y = 0

ld.balon_eje3_N3 = MetaData()
ld.balon_eje3_N3.path = 'img/balon.png'
ld.balon_eje3_N3.w = 71
ld.balon_eje3_N3.h = 71
ld.balon_eje3_N3.x = 570
ld.balon_eje3_N3.y = 50

ld.nina_eje3_N3 = MetaData()
ld.nina_eje3_N3.path = 'img/nina.png'
ld.nina_eje3_N3.w = 211
ld.nina_eje3_N3.h = 152
ld.nina_eje3_N3.x = 588
ld.nina_eje3_N3.y = 30

ld.sol_eje3_N3 = MetaData()
ld.sol_eje3_N3.path = 'img/sol.png'
ld.sol_eje3_N3.w = 150
ld.sol_eje3_N3.h = 150
ld.sol_eje3_N3.x = 100
ld.sol_eje3_N3.y = 300

ld.nina_lanzando_eje3_N3 = MetaData()
ld.nina_lanzando_eje3_N3.path = 'img/ninalanzandopelota1.gif'
ld.nina_lanzando_eje3_N3.w = 217
ld.nina_lanzando_eje3_N3.h = 217
ld.nina_lanzando_eje3_N3.x = 570
ld.nina_lanzando_eje3_N3.y = 0

ld.ok_eje3_N3 = MetaData()
ld.ok_eje3_N3.path = 'img/ok.png'
ld.ok_eje3_N3.w = 36
ld.ok_eje3_N3.h = 37
ld.ok_eje3_N3.x = 735
ld.ok_eje3_N3.y = 400

ld.actualizar_eje3_N3 = MetaData()
ld.actualizar_eje3_N3.path = 'img/actualizar.png'
ld.actualizar_eje3_N3.w = 37
ld.actualizar_eje3_N3.h = 37
ld.actualizar_eje3_N3.x = 735
ld.actualizar_eje3_N3.y = 465

ld.casa_eje3_N3 = MetaData()
ld.casa_eje3_N3.path = 'img/casa.png'
ld.casa_eje3_N3.w = 37
ld.casa_eje3_N3.h = 35
ld.casa_eje3_N3.x = 735
ld.casa_eje3_N3.y = 520

ld.bombillo_eje3_N3 = MetaData()
ld.bombillo_eje3_N3.path = 'img/bombillo.png'
ld.bombillo_eje3_N3.w = 31
ld.bombillo_eje3_N3.h = 31
ld.bombillo_eje3_N3.x = 760
ld.bombillo_eje3_N3.y = 80

ld.siguiente_eje3_N3 = MetaData()
ld.siguiente_eje3_N3.path = 'img/siguiente.png'
ld.siguiente_eje3_N3.w = 150
ld.siguiente_eje3_N3.h = 71
ld.siguiente_eje3_N3.x = 640
ld.siguiente_eje3_N3.y = 0

ld.no_eje3_N3 = MetaData()
ld.no_eje3_N3.path = 'img/dormido.gif'
ld.no_eje3_N3.w = 162
ld.no_eje3_N3.h = 87
ld.no_eje3_N3.x = 300
ld.no_eje3_N3.y = 0

ld.exe_eje3_N3 = MetaData()
ld.exe_eje3_N3.path = 'img/gano.gif'
ld.exe_eje3_N3.w = 193
ld.exe_eje3_N3.h = 116
ld.exe_eje3_N3.x = 300
ld.exe_eje3_N3.y = 0

ld.velocidad_pelota_campo_eje3_N3 = MetaData()
ld.velocidad_pelota_campo_eje3_N3.path = 'img/campo.png'
ld.velocidad_pelota_campo_eje3_N3.w = 55
ld.velocidad_pelota_campo_eje3_N3.h = 25
ld.velocidad_pelota_campo_eje3_N3.x = 200
ld.velocidad_pelota_campo_eje3_N3.y = 180

ld.res_campo_eje3_N3 = MetaData()
ld.res_campo_eje3_N3.path = 'img/campo.png'
ld.res_campo_eje3_N3.w = 55
ld.res_campo_eje3_N3.h = 25
ld.res_campo_eje3_N3.x = 425
ld.res_campo_eje3_N3.y = 380

ld.altura_maxima_eje3_N3 = MetaData()
ld.altura_maxima_eje3_N3.path = 'img/alturaMaxima.png'
ld.altura_maxima_eje3_N3.w = 115
ld.altura_maxima_eje3_N3.h = 24
ld.altura_maxima_eje3_N3.x = 400
ld.altura_maxima_eje3_N3.y = 400

ld.velocidad_pelota_eje3_N3 = MetaData()
ld.velocidad_pelota_eje3_N3.path = 'img/velocidadPelota.png'
ld.velocidad_pelota_eje3_N3.w = 125
ld.velocidad_pelota_eje3_N3.h = 25
ld.velocidad_pelota_eje3_N3.x = 165
ld.velocidad_pelota_eje3_N3.y = 200

ld.ldescripcion_eje3_N3 = MetaData()
ld.ldescripcion_eje3_N3.text = ''
ld.ldescripcion_eje3_N3.color = (0, 0, 0, 255)
ld.ldescripcion_eje3_N3.fname = 'DejaVu Sans Mono'
ld.ldescripcion_eje3_N3.fsize = 10
ld.ldescripcion_eje3_N3.x = 380
ld.ldescripcion_eje3_N3.y = 545

ld.lvelocidad_pelota_eje3_N3 = MetaData()
ld.lvelocidad_pelota_eje3_N3.text = ''
ld.lvelocidad_pelota_eje3_N3.color = (0, 0, 0, 255)
ld.lvelocidad_pelota_eje3_N3.fname = 'DejaVu Sans Mono'
ld.lvelocidad_pelota_eje3_N3.fsize = 10
ld.lvelocidad_pelota_eje3_N3.x = 360
ld.lvelocidad_pelota_eje3_N3.y = 230

ld.laltura_maxima_eje3_N3 = MetaData()
ld.laltura_maxima_eje3_N3.text = ''
ld.laltura_maxima_eje3_N3.color = (0, 0, 0, 255)
ld.laltura_maxima_eje3_N3.fname = 'DejaVu Sans Mono'
ld.laltura_maxima_eje3_N3.fsize = 10
ld.laltura_maxima_eje3_N3.x = 500
ld.laltura_maxima_eje3_N3.y = 360


ld.zones['EJERCICIO3_N3'] = {}
ld.zones['EJERCICIO3_N3'] ['ir_niveles'] = [(ld.anterior_eje3_N3.x, ld.anterior_eje3_N3.y, ld.anterior_eje3_N3.w, ld.anterior_eje3_N3.h)]
ld.zones['EJERCICIO3_N3'] ['ir_ok'] = [(ld.ok_eje3_N3.x, ld.ok_eje3_N3.y, ld.ok_eje3_N3.w, ld.ok_eje3_N3.h)]
ld.zones['EJERCICIO3_N3'] ['ir_casa'] = [(ld.casa_eje3_N3.x, ld.casa_eje3_N3.y, ld.casa_eje3_N3.w, ld.casa_eje3_N3.h)]
ld.zones['EJERCICIO3_N3'] ['ir_actualizar'] = [(ld.actualizar_eje3_N3.x, ld.actualizar_eje3_N3.y, ld.actualizar_eje3_N3.w, ld.actualizar_eje3_N3.h)]
ld.zones['EJERCICIO3_N3'] ['ir_bombillo'] = [(ld.bombillo_eje3_N3.x, ld.bombillo_eje3_N3.y, ld.bombillo_eje3_N3.w, ld.bombillo_eje3_N3.h)]

#=====================================================================
# REGISTRO DE USUARIO 1024X768
#=====================================================================

bd.fondo = MetaData()
bd.fondo.path = 'img/fondo.png'
bd.fondo.w = 1024
bd.fondo.h = 768
bd.fondo.x = 0
bd.fondo.y = 0

bd.registro = MetaData()
bd.registro.path = 'img/registro.png'
bd.registro.w = 431
bd.registro.h = 90
bd.registro.x = 296
bd.registro.y = 660

bd.nombre = MetaData()
bd.nombre.path = 'img/nombre.png'
bd.nombre.w = 156
bd.nombre.h = 63
bd.nombre.x = 10
bd.nombre.y = 590

bd.apellido = MetaData()
bd.apellido.path = 'img/apellido.png'
bd.apellido.w = 162
bd.apellido.h = 70
bd.apellido.x = 10
bd.apellido.y = 507

bd.correo = MetaData()
bd.correo.path = 'img/correo.png'
bd.correo.w = 137
bd.correo.h = 62
bd.correo.x = 10
bd.correo.y = 440

bd.clave = MetaData()
bd.clave.path = 'img/clave.png'
bd.clave.w = 118
bd.clave.h = 63
bd.clave.x = 10
bd.clave.y = 365

bd.verificar = MetaData()
bd.verificar.path = 'img/verificar.png'
bd.verificar.w = 172
bd.verificar.h = 62
bd.verificar.x = 10
bd.verificar.y = 290

bd.grado = MetaData()
bd.grado.path = 'img/grado.png'
bd.grado.w = 128
bd.grado.h = 63
bd.grado.x = 10
bd.grado.y = 215

bd.rol = MetaData()
bd.rol.path = 'img/rol.png'
bd.rol.w = 83
bd.rol.h = 63
bd.rol.x = 10
bd.rol.y = 140

bd.guardar = MetaData()
bd.guardar.path = 'img/guardar.png'
bd.guardar.w = 191
bd.guardar.h = 114
bd.guardar.x = 820
bd.guardar.y = 10

bd.advertencia1 = MetaData()
bd.advertencia1.path = 'img/advertencia1.png'
bd.advertencia1.w = 470
bd.advertencia1.h = 353
bd.advertencia1.x = 300
bd.advertencia1.y = 220

bd.advertencia2 = MetaData()
bd.advertencia2.path = 'img/advertencia2.png'
bd.advertencia2.w = 470
bd.advertencia2.h = 353
bd.advertencia2.x = 300
bd.advertencia2.y = 220

bd.anterior = MetaData()
bd.anterior.path = 'img/anterior.png'
bd.anterior.w = 82
bd.anterior.h = 101
bd.anterior.x = 10
bd.anterior.y = 10

bd.cnombre = MetaData()
bd.cnombre.path = 'img/cuadro.png'
bd.cnombre.w = 844
bd.cnombre.h = 80
bd.cnombre.x = 170
bd.cnombre.y = 570

bd.capellido = MetaData()
bd.capellido.path = 'img/cuadro.png'
bd.capellido.w = 844
bd.capellido.h = 80
bd.capellido.x = 170
bd.capellido.y = 495

bd.ccorreo = MetaData()
bd.ccorreo.path = 'img/cuadro.png'
bd.ccorreo.w = 844
bd.ccorreo.h = 80
bd.ccorreo.x = 170
bd.ccorreo.y = 420

bd.cclave = MetaData()
bd.cclave.path = 'img/cuadro.png'
bd.cclave.w = 844
bd.cclave.h = 80
bd.cclave.x = 170
bd.cclave.y = 345

bd.cverificar = MetaData()
bd.cverificar.path = 'img/cuadro.png'
bd.cverificar.w = 844
bd.cverificar.h = 80
bd.cverificar.x = 170
bd.cverificar.y = 270

bd.cgrado = MetaData()
bd.cgrado.path = 'img/cuadro.png'
bd.cgrado.w = 844
bd.cgrado.h = 80
bd.cgrado.x = 170
bd.cgrado.y = 195

bd.crol = MetaData()
bd.crol.path = 'img/cuadro.png'
bd.crol.w = 844
bd.crol.h = 80
bd.crol.x = 170
bd.crol.y = 120

bd.flecha = MetaData()
bd.flecha.path = 'img/flecha.png'
bd.flecha.w = 22
bd.flecha.h = 22
bd.flecha.x = 950
bd.flecha.y = 155

bd.lnombre = MetaData()
bd.lnombre.text = ''
bd.lnombre.color = (0, 0, 0, 255)
bd.lnombre.fname = 'DejaVu Sans Mono'
bd.lnombre.fsize = 14
bd.lnombre.x = 190
bd.lnombre.y = 615

bd.lapellido = MetaData()
bd.lapellido.text = ''
bd.lapellido.color = (0, 0, 0, 255)
bd.lapellido.fname = 'DejaVu Sans Mono'
bd.lapellido.fsize = 14
bd.lapellido.x = 190
bd.lapellido.y = 540

bd.lcorreo = MetaData()
bd.lcorreo.text = ''
bd.lcorreo.color = (0, 0, 0, 255)
bd.lcorreo.fname = 'DejaVu Sans Mono'
bd.lcorreo.fsize = 14
bd.lcorreo.x = 190
bd.lcorreo.y = 465

bd.lclave = MetaData()
bd.lclave.text = ''
bd.lclave.color = (0, 0, 0, 255)
bd.lclave.fname = 'DejaVu Sans Mono'
bd.lclave.fsize = 14
bd.lclave.x = 190
bd.lclave.y = 390

bd.lverificar = MetaData()
bd.lverificar.text = ''
bd.lverificar.color = (0, 0, 0, 255)
bd.lverificar.fname = 'DejaVu Sans Mono'
bd.lverificar.fsize = 14
bd.lverificar.x = 190
bd.lverificar.y = 315

bd.lgrado = MetaData()
bd.lgrado.text = ''
bd.lgrado.color = (0, 0, 0, 255)
bd.lgrado.fname = 'DejaVu Sans Mono'
bd.lgrado.fsize = 14
bd.lgrado.x = 190
bd.lgrado.y = 240

bd.lrol = MetaData()
bd.lrol.text = '                      >>  DOCENTE   <<'
bd.lrol.color = (17, 33, 98, 255)
bd.lrol.fname = 'DejaVu Sans Mono'
bd.lrol.fsize = 14
bd.lrol.x = 250
bd.lrol.y = 162

bd.pointer = MetaData()
bd.pointer.path = 'img/pointer.png'
bd.pointer.w = 820
bd.pointer.h = 48
bd.pointer.x = 175
bd.pointer.y = 596
bd.pointer.ylist = ['lnombre', 'lapellido', 'lcorreo', 'lclave', 'lverificar', 'lgrado', 'lrol']
bd.pointer.ypos = {'cnombre': 596, 'capellido': 521, 'ccorreo': 446, 'cclave': 371, 'cverificar': 296, 'cgrado': 221, 'crol': 146}

bd.zones = {}
bd.zones['REGISTRO'] = {}
bd.zones['REGISTRO'] ['cnombre'] = [(bd.cnombre.x, bd.cnombre.y, bd.cnombre.w, bd.cnombre.h)]
bd.zones['REGISTRO'] ['capellido'] = [(bd.capellido.x, bd.capellido.y, bd.capellido.w, bd.capellido.h)]
bd.zones['REGISTRO'] ['ccorreo'] = [(bd.ccorreo.x, bd.ccorreo.y, bd.ccorreo.w, bd.ccorreo.h)]
bd.zones['REGISTRO'] ['cclave'] = [(bd.cclave.x, bd.cclave.y, bd.cclave.w, bd.cclave.h)]
bd.zones['REGISTRO'] ['cverificar'] = [(bd.cverificar.x, bd.cverificar.y, bd.cverificar.w, bd.cverificar.h)]
bd.zones['REGISTRO'] ['cgrado'] = [(bd.cgrado.x, bd.cgrado.y, bd.cgrado.w, bd.cgrado.h)]
bd.zones['REGISTRO'] ['crol'] = [(bd.crol.x, bd.crol.y, bd.crol.w, bd.crol.h)]
bd.zones['REGISTRO'] ['ir_principal2'] = [(10, 10, 80, 105)]
bd.zones['REGISTRO'] ['guardar'] = [(bd.guardar.x, bd.guardar.y, bd.guardar.w, bd.guardar.h)]
bd.zones['REGISTRO'] ['cerrar_advertencia1'] = [(302, 452, 91, 119)]
bd.zones['REGISTRO'] ['cerrar_advertencia2'] = [(302, 452, 91, 119)]

#=====================================================================
# MENU 1024X768
#=====================================================================

bd.menu1 = MetaData()
bd.menu1.path = 'img/menu1.png'
bd.menu1.w = 225
bd.menu1.h = 90
bd.menu1.x = 420
bd.menu1.y = 660

bd.logo1 = MetaData()
bd.logo1.path = 'img/logo.png'
bd.logo1.w = 118
bd.logo1.h = 112
bd.logo1.x = 900
bd.logo1.y = 650

bd.menu2 = MetaData()
bd.menu2.path = 'img/menu2.png'
bd.menu2.w = 449
bd.menu2.h = 449
bd.menu2.x = 290
bd.menu2.y = 120

bd.zones['MENU'] = {}
bd.zones['MENU'] ['ir_ajustes'] = [(415, 415, 125, 125)]
bd.zones['MENU'] ['ir_principal'] = [(480, 150, 170, 170)]
bd.zones['MENU'] ['ir_ayuda'] = [(650, 385, 55, 55)]
bd.zones['MENU'] ['ir_cerrar'] = [(320, 145, 90, 90)]

#=====================================================================
# PRINCIPAL 1024X768
#=====================================================================

bd.iniciar = MetaData()
bd.iniciar.path = 'img/iniciar.png'
bd.iniciar.w = 251
bd.iniciar.h = 81
bd.iniciar.x = 380
bd.iniciar.y = 660


bd.ingresar = MetaData()
bd.ingresar.path = 'img/ingresar.png'
bd.ingresar.w = 156
bd.ingresar.h = 197
bd.ingresar.x = 430
bd.ingresar.y = 400


bd.nuevo = MetaData()
bd.nuevo.path = 'img/nuevo.png'
bd.nuevo.w = 251
bd.nuevo.h = 190
bd.nuevo.x = 400
bd.nuevo.y = 130

bd.anterior5 = MetaData()
bd.anterior5.path = 'img/anterior.png'
bd.anterior5.w = 82
bd.anterior5.h = 101
bd.anterior5.x = 10
bd.anterior5.y = 10

bd.zones['PRINCIPAL'] = {}
bd.zones['PRINCIPAL'] ['ir_menu'] = [(10, 10, 80, 105)]
bd.zones['PRINCIPAL'] ['ir_registro'] = [(bd.nuevo.x, bd.nuevo.y, bd.nuevo.w, bd.nuevo.h)]
bd.zones['PRINCIPAL'] ['ir_login'] = [(bd.ingresar.x, bd.ingresar.y, bd.ingresar.w, bd.ingresar.h)]

#=====================================================================
# AJUSTES 1024X768
#=====================================================================

bd.ajustes = MetaData()
bd.ajustes.path = 'img/ajustes.png'
bd.ajustes.w = 240
bd.ajustes.h = 93
bd.ajustes.x = 390
bd.ajustes.y = 660

bd.sonido1 = MetaData()
bd.sonido1.path = 'img/sonido1.png'
bd.sonido1.w = 150
bd.sonido1.h = 150
bd.sonido1.x = 150
bd.sonido1.y = 450

bd.sonido2 = MetaData()
bd.sonido2.path = 'img/sonido2.png'
bd.sonido2.w = 150
bd.sonido2.h = 150
bd.sonido2.x = 150
bd.sonido2.y = 90

bd.pantalla1 = MetaData()
bd.pantalla1.path = 'img/pantalla1.png'
bd.pantalla1.w = 194
bd.pantalla1.h = 208
bd.pantalla1.x = 670
bd.pantalla1.y = 400

bd.pantalla2 = MetaData()
bd.pantalla2.path = 'img/pantalla2.png'
bd.pantalla2.w = 194
bd.pantalla2.h = 208
bd.pantalla2.x = 670
bd.pantalla2.y = 40

bd.anterior2 = MetaData()
bd.anterior2.path = 'img/anterior.png'
bd.anterior2.w = 82
bd.anterior2.h = 101
bd.anterior2.x = 10
bd.anterior2.y = 10

bd.zones['AJUSTES'] = {}
bd.zones['AJUSTES'] ['ir_menu'] = [(10, 10, 80, 105)]
bd.zones['AJUSTES'] ['pantalla1'] = [(bd.pantalla1.x, bd.pantalla1.y, bd.pantalla1.w, bd.pantalla1.h)]
bd.zones['AJUSTES'] ['pantalla2'] = [(bd.pantalla2.x, bd.pantalla2.y, bd.pantalla2.w, bd.pantalla2.h)]

#=====================================================================
# LOGIN 1024X768
#=====================================================================

bd.login = MetaData()
bd.login.path = 'img/login.png'
bd.login.w = 400
bd.login.h = 80
bd.login.x = 330
bd.login.y = 660

bd.correo2 = MetaData()
bd.correo2.path = 'img/correo2.png'
bd.correo2.w = 200
bd.correo2.h = 66
bd.correo2.x = 150
bd.correo2.y = 450

bd.clave2 = MetaData()
bd.clave2.path = 'img/clave2.png'
bd.clave2.w = 170
bd.clave2.h = 70
bd.clave2.x = 155
bd.clave2.y = 250

bd.lcorreo2 = MetaData()
bd.lcorreo2.text = ''
bd.lcorreo2.color = (0, 0, 0, 255)
bd.lcorreo2.fname = 'DejaVu Sans Mono'
bd.lcorreo2.fsize = 14
bd.lcorreo2.x = 370
bd.lcorreo2.y = 470

bd.lclave2 = MetaData()
bd.lclave2.text = ''
bd.lclave2.color = (0, 0, 0, 255)
bd.lclave2.fname = 'DejaVu Sans Mono'
bd.lclave2.fsize = 14
bd.lclave2.x = 370
bd.lclave2.y = 270

bd.cucorreo2 = MetaData()
bd.cucorreo2.path = 'img/cuadrito.png'
bd.cucorreo2.w = 524
bd.cucorreo2.h = 80
bd.cucorreo2.x = 350
bd.cucorreo2.y = 430

bd.cuclave2 = MetaData()
bd.cuclave2.path = 'img/cuadrito.png'
bd.cuclave2.w = 524
bd.cuclave2.h = 80
bd.cuclave2.x = 350
bd.cuclave2.y = 230

bd.anterior3 = MetaData()
bd.anterior3.path = 'img/anterior.png'
bd.anterior3.w = 82
bd.anterior3.h = 101
bd.anterior3.x = 10
bd.anterior3.y = 10

bd.enter= MetaData()
bd.enter.path = 'img/enter.png'
bd.enter.w = 180
bd.enter.h = 105
bd.enter.x = 680
bd.enter.y = 70

bd.login_adv1 = MetaData()
bd.login_adv1.path = 'img/login_adv1.png'
bd.login_adv1.w = 470
bd.login_adv1.h = 353
bd.login_adv1.x = 300
bd.login_adv1.y = 220

bd.pointersito = MetaData()
bd.pointersito.path = 'img/pointersito.png'
bd.pointersito.w = 501
bd.pointersito.h = 48
bd.pointersito.x = 354
bd.pointersito.y = 456
bd.pointersito.ylist = ['lcorreo2', 'lclave2']
bd.pointersito.ypos = {'cucorreo2': 456, 'cuclave2': 256}

bd.zones['LOGIN'] = {}
bd.zones['LOGIN'] ['cucorreo2'] = [(bd.cucorreo2.x, bd.cucorreo2.y, bd.cucorreo2.w, bd.cucorreo2.h)]
bd.zones['LOGIN'] ['cuclave2'] = [(bd.cuclave2.x, bd.cuclave2.y, bd.cuclave2.w, bd.cuclave2.h)]
bd.zones['LOGIN'] ['ir_principal2'] = [(10, 10, 80, 105)]
bd.zones['LOGIN'] ['enter'] = [(bd.enter.x, bd.enter.y, bd.enter.w, bd.enter.h)]
bd.zones['LOGIN'] ['cerrar_login_adv1'] = [(302, 452, 91, 119)]

#=====================================================================
# AYUDA 1024X768
#=====================================================================

bd.ayuda = MetaData()
bd.ayuda.path = 'img/ayuda.png'
bd.ayuda.w = 650
bd.ayuda.h = 70
bd.ayuda.x = 200
bd.ayuda.y = 660

bd.tabla = MetaData()
bd.tabla.path = 'img/tabla.png'
bd.tabla.w = 655
bd.tabla.h = 450
bd.tabla.x = 60
bd.tabla.y = 110

bd.idea = MetaData()
bd.idea.path = 'img/idea.gif'
bd.idea.w = 228
bd.idea.h = 350
bd.idea.x = 775
bd.idea.y = 150

bd.piso = MetaData()
bd.piso.path = 'img/piso.png'
bd.piso.w = 200
bd.piso.h = 100
bd.piso.x = 770
bd.piso.y = 115

bd.anterior4 = MetaData()
bd.anterior4.path = 'img/anterior.png'
bd.anterior4.w = 82
bd.anterior4.h = 101
bd.anterior4.x = 10
bd.anterior4.y = 10

bd.zones['AYUDA'] = {}
bd.zones['AYUDA'] ['ir_menu'] = [(10, 10, 80, 105)]

#=====================================================================
# NIVELES 1024X768
#=====================================================================

bd.niveles = MetaData()
bd.niveles.path = 'img/niveles.png'
bd.niveles.w = 326
bd.niveles.h = 43
bd.niveles.x = 350
bd.niveles.y = 680

bd.rectilineo = MetaData()
bd.rectilineo.path = 'img/rectilineo.png'
bd.rectilineo.w = 191
bd.rectilineo.h = 71
bd.rectilineo.x = 80
bd.rectilineo.y = 530

bd.curvilineo = MetaData()
bd.curvilineo.path = 'img/curvilineo.png'
bd.curvilineo.w = 191
bd.curvilineo.h = 71
bd.curvilineo.x = 420
bd.curvilineo.y = 530

bd.especial = MetaData()
bd.especial.path = 'img/especial.png'
bd.especial.w = 191
bd.especial.h = 71
bd.especial.x = 765
bd.especial.y = 530

bd.nivel1 = MetaData()
bd.nivel1.path = 'img/nivel1.png'
bd.nivel1.w = 300
bd.nivel1.h = 170
bd.nivel1.x = 20
bd.nivel1.y = 320

bd.nivel2 = MetaData()
bd.nivel2.path = 'img/nivel1.png'
bd.nivel2.w = 300
bd.nivel2.h = 170
bd.nivel2.x = 365
bd.nivel2.y = 320

bd.nivel3 = MetaData()
bd.nivel3.path = 'img/nivel1.png'
bd.nivel3.w = 300
bd.nivel3.h = 170
bd.nivel3.x = 704
bd.nivel3.y = 320

bd.des_nivel1 = MetaData()
bd.des_nivel1.path = 'img/des_nivel1.png'
bd.des_nivel1.w = 286
bd.des_nivel1.h = 130
bd.des_nivel1.x = 30
bd.des_nivel1.y = 150

bd.des_nivel2 = MetaData()
bd.des_nivel2.path = 'img/des_nivel2.png'
bd.des_nivel2.w = 333
bd.des_nivel2.h = 132
bd.des_nivel2.x = 375
bd.des_nivel2.y = 150

bd.des_nivel3 = MetaData()
bd.des_nivel3.path = 'img/des_nivel3.png'
bd.des_nivel3.w = 271
bd.des_nivel3.h = 130
bd.des_nivel3.x = 724
bd.des_nivel3.y = 150

bd.anterior_niveles = MetaData()
bd.anterior_niveles.path = 'img/anterior.png'
bd.anterior_niveles.w = 83
bd.anterior_niveles.h = 76
bd.anterior_niveles.x = 5
bd.anterior_niveles.y = 10

bd.medalla_nivel1 = MetaData()
bd.medalla_nivel1.path = 'img/medalla.png'
bd.medalla_nivel1.w = 75
bd.medalla_nivel1.h = 113
bd.medalla_nivel1.x = 240
bd.medalla_nivel1.y = 270

bd.medalla_nivel2 = MetaData()
bd.medalla_nivel2.path = 'img/medalla.png'
bd.medalla_nivel2.w = 75
bd.medalla_nivel2.h = 113
bd.medalla_nivel2.x = 585
bd.medalla_nivel2.y = 270

bd.medalla_nivel3 = MetaData()
bd.medalla_nivel3.path = 'img/medalla.png'
bd.medalla_nivel3.w = 75
bd.medalla_nivel3.h = 113
bd.medalla_nivel3.x = 925
bd.medalla_nivel3.y = 270

bd.zones['NIVELES'] = {}
bd.zones['NIVELES'] ['ir_nivel1'] = [(bd.nivel1.x, bd.nivel1.y, bd.nivel1.w, bd.nivel1.h)]
bd.zones['NIVELES'] ['ir_nivel2'] = [(bd.nivel2.x, bd.nivel1.y, bd.nivel2.w, bd.nivel2.h)]
bd.zones['NIVELES'] ['ir_nivel3'] = [(bd.nivel3.x, bd.nivel3.y, bd.nivel3.w, bd.nivel3.h)]
bd.zones['NIVELES'] ['ir_casa'] = [(bd.anterior_niveles.x, bd.anterior_niveles.y, bd.anterior_niveles.w, bd.anterior_niveles.h)]

#=====================================================================
# NIVEL1 1024X768
#=====================================================================

bd.carro1 = MetaData()
bd.carro1.path = 'img/carro1.png'
bd.carro1.w = 105
bd.carro1.h = 53
bd.carro1.x = 10
bd.carro1.y = 170

bd.carro2 = MetaData()
bd.carro2.path = 'img/carro2.png'
bd.carro2.w = 105
bd.carro2.h = 53
bd.carro2.x = 910
bd.carro2.y = 170

bd.carretera = MetaData()
bd.carretera.path = 'img/carretera.jpg'
bd.carretera.w = 1024
bd.carretera.h = 50
bd.carretera.x = 0
bd.carretera.y = 150

bd.colegio = MetaData()
bd.colegio.path = 'img/colegio.png'
bd.colegio.w = 300
bd.colegio.h = 150
bd.colegio.x = 0
bd.colegio.y = 200

bd.parque = MetaData()
bd.parque.path = 'img/parque.png'
bd.parque.w = 350
bd.parque.h = 195
bd.parque.x = 674
bd.parque.y = 200

bd.casa = MetaData()
bd.casa.path = 'img/casa.png'
bd.casa.w = 47
bd.casa.h = 45
bd.casa.x = 950
bd.casa.y = 680

bd.ok = MetaData()
bd.ok.path = 'img/ok.png'
bd.ok.w = 47
bd.ok.h = 49
bd.ok.x = 950
bd.ok.y = 510

bd.actualizar = MetaData()
bd.actualizar.path = 'img/actualizar.png'
bd.actualizar.w = 47
bd.actualizar.h = 47
bd.actualizar.x = 950
bd.actualizar.y = 600

bd.bombillo= MetaData()
bd.bombillo.path = 'img/bombillo.png'
bd.bombillo.w = 40
bd.bombillo.h = 40
bd.bombillo.x = 970
bd.bombillo.y = 20

bd.anterior6 = MetaData()
bd.anterior6.path = 'img/anterior.png'
bd.anterior6.w = 83
bd.anterior6.h = 76
bd.anterior6.x = 5
bd.anterior6.y = 10

bd.dis_campo = MetaData()
bd.dis_campo.path = 'img/campo.png'
bd.dis_campo.w = 75
bd.dis_campo.h = 30
bd.dis_campo.x = 475
bd.dis_campo.y = 65

bd.car1_campo = MetaData()
bd.car1_campo.path = 'img/campo.png'
bd.car1_campo.w = 75
bd.car1_campo.h = 30
bd.car1_campo.x = 120
bd.car1_campo.y = 65

bd.car2_campo = MetaData()
bd.car2_campo.path = 'img/campo.png'
bd.car2_campo.w = 75
bd.car2_campo.h = 30
bd.car2_campo.x = 850
bd.car2_campo.y = 65

bd.vel_car1_campo = MetaData()
bd.vel_car1_campo.path = 'img/campo.png'
bd.vel_car1_campo.w = 75
bd.vel_car1_campo.h = 30
bd.vel_car1_campo.x = 330
bd.vel_car1_campo.y = 255

bd.vel_car2_campo = MetaData()
bd.vel_car2_campo.path = 'img/campo.png'
bd.vel_car2_campo.w = 75
bd.vel_car2_campo.h = 30
bd.vel_car2_campo.x = 565
bd.vel_car2_campo.y = 255

bd.res_campo = MetaData()
bd.res_campo.path = 'img/campo.png'
bd.res_campo.w = 75
bd.res_campo.h = 30
bd.res_campo.x = 475
bd.res_campo.y = 540

bd.distancia = MetaData()
bd.distancia.path = 'img/distancia.png'
bd.distancia.w = 125
bd.distancia.h = 29
bd.distancia.x = 455
bd.distancia.y = 40

bd.distanciaA_u = MetaData()
bd.distanciaA_u.path = 'img/distanciaA_u.png'
bd.distanciaA_u.w = 132
bd.distanciaA_u.h = 29
bd.distanciaA_u.x = 100
bd.distanciaA_u.y = 40

bd.distanciaB_v = MetaData()
bd.distanciaB_v.path = 'img/distanciaB_v.png'
bd.distanciaB_v.w = 130
bd.distanciaB_v.h = 29
bd.distanciaB_v.x = 830
bd.distanciaB_v.y = 40

bd.velocidadU = MetaData()
bd.velocidadU.path = 'img/velocidadU.png'
bd.velocidadU.w = 100
bd.velocidadU.h = 29
bd.velocidadU.x = 320
bd.velocidadU.y = 280

bd.velocidadV = MetaData()
bd.velocidadV.path = 'img/velocidadV.png'
bd.velocidadV.w = 98
bd.velocidadV.h = 29
bd.velocidadV.x = 556
bd.velocidadV.y = 280

bd.resultado = MetaData()
bd.resultado.path = 'img/tiempo.png'
bd.resultado.w = 69
bd.resultado.h = 30
bd.resultado.x = 480
bd.resultado.y = 565

bd.mano = MetaData()
bd.mano.path = 'img/mano.png'
bd.mano.w = 31
bd.mano.h = 31
bd.mano.x = 502
bd.mano.y = 115

bd.no = MetaData()
bd.no.path = 'img/no.gif'
bd.no.w = 207
bd.no.h = 112
bd.no.x = 390
bd.no.y = 250

bd.bien = MetaData()
bd.bien.path = 'img/bien.gif'
bd.bien.w = 226
bd.bien.h = 262
bd.bien.x = 360
bd.bien.y = 150

bd.explosion = MetaData()
bd.explosion.path = 'img/explosion.gif'
bd.explosion.w = 118
bd.explosion.h = 172
bd.explosion.x = 440
bd.explosion.y = 140

bd.siguiente = MetaData()
bd.siguiente.path = 'img/siguiente.png'
bd.siguiente.w = 192
bd.siguiente.h = 91
bd.siguiente.x = 830
bd.siguiente.y = 0

bd.ldescripcion = MetaData()
bd.ldescripcion.text = ''
bd.ldescripcion.color = (0, 0, 0, 255)
bd.ldescripcion.fname = 'DejaVu Sans Mono'
bd.ldescripcion.fsize = 12
bd.ldescripcion.x = 510
bd.ldescripcion.y = 710

bd.ldistancia_total = MetaData()
bd.ldistancia_total.text = ''
bd.ldistancia_total.color = (0, 0, 0, 255)
bd.ldistancia_total.fname = 'DejaVu Sans Mono'
bd.ldistancia_total.fsize = 12
bd.ldistancia_total.x = 485
bd.ldistancia_total.y = 78

bd.ldistanciaA_u = MetaData()
bd.ldistanciaA_u.text = ''
bd.ldistanciaA_u.color = (0, 0, 0, 255)
bd.ldistanciaA_u.fname = 'DejaVu Sans Mono'
bd.ldistanciaA_u.fsize = 12
bd.ldistanciaA_u.x = 133
bd.ldistanciaA_u.y = 78

bd.ldistanciaB_V = MetaData()
bd.ldistanciaB_V.text = ''
bd.ldistanciaB_V.color = (0, 0, 0, 255)
bd.ldistanciaB_V.fname = 'DejaVu Sans Mono'
bd.ldistanciaB_V.fsize = 12
bd.ldistanciaB_V.x = 870
bd.ldistanciaB_V.y = 78

bd.lvelocidadU = MetaData()
bd.lvelocidadU.text = ''
bd.lvelocidadU.color = (0, 0, 0, 255)
bd.lvelocidadU.fname = 'DejaVu Sans Mono'
bd.lvelocidadU.fsize = 12
bd.lvelocidadU.x = 355
bd.lvelocidadU.y = 268

bd.lvelocidadV = MetaData()
bd.lvelocidadV.text = ''
bd.lvelocidadV.color = (0, 0, 0, 255)
bd.lvelocidadV.fname = 'DejaVu Sans Mono'
bd.lvelocidadV.fsize = 12
bd.lvelocidadV.x = 590
bd.lvelocidadV.y = 268

bd.ltiempo = MetaData()
bd.ltiempo.text = ''
bd.ltiempo.color = (0, 0, 0, 255)
bd.ltiempo.fname = 'DejaVu Sans Mono'
bd.ltiempo.fsize = 12
bd.ltiempo.x = 490
bd.ltiempo.y = 553

bd.zones['NIVEL1'] = {}
bd.zones['NIVEL1'] ['mover_mano'] = [(bd.mano.x, bd.mano.y, bd.mano.w, bd.mano.h)]
bd.zones['NIVEL1'] ['ir_ok'] = [(bd.ok.x, bd.ok.y, bd.ok.w, bd.ok.h)]
bd.zones['NIVEL1'] ['ir_casa'] = [(bd.casa.x, bd.casa.y, bd.casa.w, bd.casa.h)]
bd.zones['NIVEL1'] ['ir_actualizar'] = [(bd.actualizar.x, bd.actualizar.y, bd.actualizar.w, bd.actualizar.h)]
bd.zones['NIVEL1'] ['ir_bombillo'] = [(bd.bombillo.x, bd.bombillo.y, bd.bombillo.w, bd.bombillo.h)]
bd.zones['NIVEL1'] ['ir_niveles'] = [(bd.anterior6.x, bd.anterior6.y, bd.anterior6.w, bd.anterior6.h)]

#=====================================================================
# EJERCICIO2_N1 1024X768
#=====================================================================

bd.barco1_eje2 = MetaData()
bd.barco1_eje2.path = 'img/barco1.png'
bd.barco1_eje2.w = 113
bd.barco1_eje2.h = 120
bd.barco1_eje2.x = 10
bd.barco1_eje2.y = 180

bd.barco2_eje2 = MetaData()
bd.barco2_eje2.path = 'img/barco2.png'
bd.barco2_eje2.w = 113
bd.barco2_eje2.h = 102
bd.barco2_eje2.x = 901
bd.barco2_eje2.y = 155

bd.agua_eje2 = MetaData()
bd.agua_eje2.path = 'img/agua.jpg'
bd.agua_eje2.w = 1024
bd.agua_eje2.h = 63
bd.agua_eje2.x = 0
bd.agua_eje2.y = 150

bd.faro_eje2 = MetaData()
bd.faro_eje2.path = 'img/faro.png'
bd.faro_eje2.w = 200
bd.faro_eje2.h = 400
bd.faro_eje2.x = 3
bd.faro_eje2.y = 200

bd.playa_eje2 = MetaData()
bd.playa_eje2.path = 'img/playa.png'
bd.playa_eje2.w = 500
bd.playa_eje2.h = 227
bd.playa_eje2.x = 524
bd.playa_eje2.y = 200

bd.anterior7 = MetaData()
bd.anterior7.path = 'img/anterior.png'
bd.anterior7.w = 83
bd.anterior7.h = 76
bd.anterior7.x = 5
bd.anterior7.y = 10

bd.tiempo_campo = MetaData()
bd.tiempo_campo.path = 'img/campo.png'
bd.tiempo_campo.w = 75
bd.tiempo_campo.h = 30
bd.tiempo_campo.x = 475
bd.tiempo_campo.y = 65

bd.car1_campo_eje2 = MetaData()
bd.car1_campo_eje2.path = 'img/campo.png'
bd.car1_campo_eje2.w = 75
bd.car1_campo_eje2.h = 30
bd.car1_campo_eje2.x = 120
bd.car1_campo_eje2.y = 65

bd.car2_campo_eje2 = MetaData()
bd.car2_campo_eje2.path = 'img/campo.png'
bd.car2_campo_eje2.w = 75
bd.car2_campo_eje2.h = 30
bd.car2_campo_eje2.x = 850
bd.car2_campo_eje2.y = 65

bd.vel_car1_campo_eje2 = MetaData()
bd.vel_car1_campo_eje2.path = 'img/campo.png'
bd.vel_car1_campo_eje2.w = 75
bd.vel_car1_campo_eje2.h = 30
bd.vel_car1_campo_eje2.x = 240
bd.vel_car1_campo_eje2.y = 355

bd.vel_car2_campo_eje2 = MetaData()
bd.vel_car2_campo_eje2.path = 'img/campo.png'
bd.vel_car2_campo_eje2.w = 75
bd.vel_car2_campo_eje2.h = 30
bd.vel_car2_campo_eje2.x = 645
bd.vel_car2_campo_eje2.y = 355

bd.res_campo_eje2 = MetaData()
bd.res_campo_eje2.path = 'img/campo.png'
bd.res_campo_eje2.w = 75
bd.res_campo_eje2.h = 30
bd.res_campo_eje2.x = 475
bd.res_campo_eje2.y = 540

bd.tiempo_eje2 = MetaData()
bd.tiempo_eje2.path = 'img/tiempo.png'
bd.tiempo_eje2.w = 69
bd.tiempo_eje2.h = 30
bd.tiempo_eje2.x = 480
bd.tiempo_eje2.y = 40

bd.distanciaA_u_eje2 = MetaData()
bd.distanciaA_u_eje2.path = 'img/distanciaA_u.png'
bd.distanciaA_u_eje2.w = 132
bd.distanciaA_u_eje2.h = 29
bd.distanciaA_u_eje2.x = 100
bd.distanciaA_u_eje2.y = 40

bd.distanciaB_v_eje2 = MetaData()
bd.distanciaB_v_eje2.path = 'img/distanciaB_v.png'
bd.distanciaB_v_eje2.w = 130
bd.distanciaB_v_eje2.h = 29
bd.distanciaB_v_eje2.x = 830
bd.distanciaB_v_eje2.y = 40

bd.velocidadU_eje2 = MetaData()
bd.velocidadU_eje2.path = 'img/velocidadU.png'
bd.velocidadU_eje2.w = 100
bd.velocidadU_eje2.h = 29
bd.velocidadU_eje2.x = 230
bd.velocidadU_eje2.y = 380

bd.velocidadV_eje2 = MetaData()
bd.velocidadV_eje2.path = 'img/velocidadV.png'
bd.velocidadV_eje2.w = 98
bd.velocidadV_eje2.h = 29
bd.velocidadV_eje2.x = 636
bd.velocidadV_eje2.y = 380

bd.distancia_eje2 = MetaData()
bd.distancia_eje2.path = 'img/distancia_eje2.png'
bd.distancia_eje2.w = 89
bd.distancia_eje2.h = 29
bd.distancia_eje2.x = 470
bd.distancia_eje2.y = 565

bd.mano_eje2 = MetaData()
bd.mano_eje2.path = 'img/mano.png'
bd.mano_eje2.w = 31
bd.mano_eje2.h = 38
bd.mano_eje2.x = 502
bd.mano_eje2.y = 105

bd.no_eje2 = MetaData()
bd.no_eje2.path = 'img/no.gif'
bd.no_eje2.w = 207
bd.no_eje2.h = 112
bd.no_eje2.x = 390
bd.no_eje2.y = 250

bd.bien_eje2 = MetaData()
bd.bien_eje2.path = 'img/bien.gif'
bd.bien_eje2.w = 226
bd.bien_eje2.h = 262
bd.bien_eje2.x = 360
bd.bien_eje2.y = 150

bd.casa_eje2 = MetaData()
bd.casa_eje2.path = 'img/casa.png'
bd.casa_eje2.w = 47
bd.casa_eje2.h = 45
bd.casa_eje2.x = 950
bd.casa_eje2.y = 680

bd.ok_eje2 = MetaData()
bd.ok_eje2.path = 'img/ok.png'
bd.ok_eje2.w = 47
bd.ok_eje2.h = 49
bd.ok_eje2.x = 950
bd.ok_eje2.y = 510

bd.actualizar_eje2 = MetaData()
bd.actualizar_eje2.path = 'img/actualizar.png'
bd.actualizar_eje2.w = 47
bd.actualizar_eje2.h = 47
bd.actualizar_eje2.x = 950
bd.actualizar_eje2.y = 600

bd.bombillo_eje2= MetaData()
bd.bombillo_eje2.path = 'img/bombillo.png'
bd.bombillo_eje2.w = 40
bd.bombillo_eje2.h = 40
bd.bombillo_eje2.x = 970
bd.bombillo_eje2.y = 20

bd.siguiente_eje2 = MetaData()
bd.siguiente_eje2.path = 'img/siguiente.png'
bd.siguiente_eje2.w = 192
bd.siguiente_eje2.h = 91
bd.siguiente_eje2.x = 830
bd.siguiente_eje2.y = 0

bd.ldescripcion_eje2 = MetaData()
bd.ldescripcion_eje2.text = ''
bd.ldescripcion_eje2.color = (0, 0, 0, 255)
bd.ldescripcion_eje2.fname = 'DejaVu Sans Mono'
bd.ldescripcion_eje2.fsize = 12
bd.ldescripcion_eje2.x = 510
bd.ldescripcion_eje2.y = 710

bd.ltiempo_total = MetaData()
bd.ltiempo_total.text = ''
bd.ltiempo_total.color = (0, 0, 0, 255)
bd.ltiempo_total.fname = 'DejaVu Sans Mono'
bd.ltiempo_total.fsize = 12
bd.ltiempo_total.x = 495
bd.ltiempo_total.y = 78

bd.ldistanciaA_u_eje2 = MetaData()
bd.ldistanciaA_u_eje2.text = ''
bd.ldistanciaA_u_eje2.color = (0, 0, 0, 255)
bd.ldistanciaA_u_eje2.fname = 'DejaVu Sans Mono'
bd.ldistanciaA_u_eje2.fsize = 12
bd.ldistanciaA_u_eje2.x = 133
bd.ldistanciaA_u_eje2.y = 78

bd.ldistanciaB_V_eje2 = MetaData()
bd.ldistanciaB_V_eje2.text = ''
bd.ldistanciaB_V_eje2.color = (0, 0, 0, 255)
bd.ldistanciaB_V_eje2.fname = 'DejaVu Sans Mono'
bd.ldistanciaB_V_eje2.fsize = 12
bd.ldistanciaB_V_eje2.x = 870
bd.ldistanciaB_V_eje2.y = 78

bd.lvelocidadU_eje2 = MetaData()
bd.lvelocidadU_eje2.text = ''
bd.lvelocidadU_eje2.color = (0, 0, 0, 255)
bd.lvelocidadU_eje2.fname = 'DejaVu Sans Mono'
bd.lvelocidadU_eje2.fsize = 12
bd.lvelocidadU_eje2.x = 265
bd.lvelocidadU_eje2.y = 368

bd.lvelocidadV_eje2 = MetaData()
bd.lvelocidadV_eje2.text = ''
bd.lvelocidadV_eje2.color = (0, 0, 0, 255)
bd.lvelocidadV_eje2.fname = 'DejaVu Sans Mono'
bd.lvelocidadV_eje2.fsize = 12
bd.lvelocidadV_eje2.x = 670
bd.lvelocidadV_eje2.y = 368

bd.ldistancia_eje2 = MetaData()
bd.ldistancia_eje2.text = ''
bd.ldistancia_eje2.color = (0, 0, 0, 255)
bd.ldistancia_eje2.fname = 'DejaVu Sans Mono'
bd.ldistancia_eje2.fsize = 12
bd.ldistancia_eje2.x = 485
bd.ldistancia_eje2.y = 553

bd.zones['EJERCICIO2_N1'] = {}
bd.zones['EJERCICIO2_N1'] ['mover_mano'] = [(bd.mano_eje2.x, bd.mano_eje2.y, bd.mano_eje2.w, bd.mano_eje2.h)]
bd.zones['EJERCICIO2_N1'] ['ir_ok'] = [(bd.ok_eje2.x, bd.ok_eje2.y, bd.ok_eje2.w, bd.ok_eje2.h)]
bd.zones['EJERCICIO2_N1'] ['ir_casa'] = [(bd.casa_eje2.x, bd.casa_eje2.y, bd.casa_eje2.w, bd.casa_eje2.h)]
bd.zones['EJERCICIO2_N1'] ['ir_actualizar'] = [(bd.actualizar_eje2.x, bd.actualizar_eje2.y, bd.actualizar_eje2.w, bd.actualizar_eje2.h)]
bd.zones['EJERCICIO2_N1'] ['ir_bombillo'] = [(bd.bombillo_eje2.x, bd.bombillo_eje2.y, bd.bombillo_eje2.w, bd.bombillo_eje2.h)]
bd.zones['EJERCICIO2_N1'] ['ir_niveles'] = [(bd.anterior7.x, bd.anterior7.y, bd.anterior7.w, bd.anterior7.h)]

#=====================================================================
# EJERCICIO3_N1 1024X768
#=====================================================================

bd.anterior9_eje3_N1 = MetaData()
bd.anterior9_eje3_N1.path = 'img/anterior.png'
bd.anterior9_eje3_N1.w = 83
bd.anterior9_eje3_N1.h = 76
bd.anterior9_eje3_N1.x = 5
bd.anterior9_eje3_N1.y = 10

bd.tractor1_eje3_N1 = MetaData()
bd.tractor1_eje3_N1.path = 'img/tractor1.png'
bd.tractor1_eje3_N1.w = 113
bd.tractor1_eje3_N1.h = 78
bd.tractor1_eje3_N1.x = 10
bd.tractor1_eje3_N1.y = 170

bd.tractor2_eje3_N1 = MetaData()
bd.tractor2_eje3_N1.path = 'img/tractor2.png'
bd.tractor2_eje3_N1.w = 113
bd.tractor2_eje3_N1.h = 78
bd.tractor2_eje3_N1.x = 901
bd.tractor2_eje3_N1.y = 155

bd.tierra_eje3_N1 = MetaData()
bd.tierra_eje3_N1.path = 'img/tierra.jpg'
bd.tierra_eje3_N1.w = 1024
bd.tierra_eje3_N1.h = 67
bd.tierra_eje3_N1.x = 0
bd.tierra_eje3_N1.y = 150

bd.molino_eje3_N1 = MetaData()
bd.molino_eje3_N1.path = 'img/molino.png'
bd.molino_eje3_N1.w = 282
bd.molino_eje3_N1.h = 400
bd.molino_eje3_N1.x = 3
bd.molino_eje3_N1.y = 180

bd.granja_eje3_N1 = MetaData()
bd.granja_eje3_N1.path = 'img/granja.png'
bd.granja_eje3_N1.w = 400
bd.granja_eje3_N1.h = 206
bd.granja_eje3_N1.x = 624
bd.granja_eje3_N1.y = 210

bd.tiempo_campo_eje3_N1 = MetaData()
bd.tiempo_campo_eje3_N1.path = 'img/campo.png'
bd.tiempo_campo_eje3_N1.w = 75
bd.tiempo_campo_eje3_N1.h = 30
bd.tiempo_campo_eje3_N1.x = 280
bd.tiempo_campo_eje3_N1.y = 255

bd.car1_campo_eje3_N1 = MetaData()
bd.car1_campo_eje3_N1.path = 'img/campo.png'
bd.car1_campo_eje3_N1.w = 75
bd.car1_campo_eje3_N1.h = 30
bd.car1_campo_eje3_N1.x = 120
bd.car1_campo_eje3_N1.y = 65

bd.car2_campo_eje3_N1 = MetaData()
bd.car2_campo_eje3_N1.path = 'img/campo.png'
bd.car2_campo_eje3_N1.w = 75
bd.car2_campo_eje3_N1.h = 30
bd.car2_campo_eje3_N1.x = 850
bd.car2_campo_eje3_N1.y = 65

bd.vel_car2_campo_eje3_N1 = MetaData()
bd.vel_car2_campo_eje3_N1.path = 'img/campo.png'
bd.vel_car2_campo_eje3_N1.w = 75
bd.vel_car2_campo_eje3_N1.h = 30
bd.vel_car2_campo_eje3_N1.x = 515
bd.vel_car2_campo_eje3_N1.y = 255

bd.distancia_campo_eje3_N1 = MetaData()
bd.distancia_campo_eje3_N1.path = 'img/campo.png'
bd.distancia_campo_eje3_N1.w = 75
bd.distancia_campo_eje3_N1.h = 30
bd.distancia_campo_eje3_N1.x = 475
bd.distancia_campo_eje3_N1.y = 65

bd.res_campo_eje3_N1 = MetaData()
bd.res_campo_eje3_N1.path = 'img/campo.png'
bd.res_campo_eje3_N1.w = 75
bd.res_campo_eje3_N1.h = 30
bd.res_campo_eje3_N1.x = 475
bd.res_campo_eje3_N1.y = 540

bd.mano_eje3_N1 = MetaData()
bd.mano_eje3_N1.path = 'img/mano.png'
bd.mano_eje3_N1.w = 31
bd.mano_eje3_N1.h = 38
bd.mano_eje3_N1.x = 502
bd.mano_eje3_N1.y = 105

bd.distancia_eje3_N1 = MetaData()
bd.distancia_eje3_N1.path = 'img/distancia.png'
bd.distancia_eje3_N1.w = 125
bd.distancia_eje3_N1.h = 29
bd.distancia_eje3_N1.x = 455
bd.distancia_eje3_N1.y = 40

bd.distanciaA_u_eje3_N1 = MetaData()
bd.distanciaA_u_eje3_N1.path = 'img/distanciaA_u.png'
bd.distanciaA_u_eje3_N1.w = 132
bd.distanciaA_u_eje3_N1.h = 29
bd.distanciaA_u_eje3_N1.x = 100
bd.distanciaA_u_eje3_N1.y = 40

bd.distanciaB_v_eje3_N1 = MetaData()
bd.distanciaB_v_eje3_N1.path = 'img/distanciaB_v.png'
bd.distanciaB_v_eje3_N1.w = 130
bd.distanciaB_v_eje3_N1.h = 29
bd.distanciaB_v_eje3_N1.x = 830
bd.distanciaB_v_eje3_N1.y = 40

bd.velocidad_auto_U_eje3_N1 = MetaData()
bd.velocidad_auto_U_eje3_N1.path = 'img/velocidadU.png'
bd.velocidad_auto_U_eje3_N1.w =  100
bd.velocidad_auto_U_eje3_N1.h =  29
bd.velocidad_auto_U_eje3_N1.x =  465
bd.velocidad_auto_U_eje3_N1.y =  565

bd.velocidadV_eje3_N1 = MetaData()
bd.velocidadV_eje3_N1.path = 'img/velocidadV.png'
bd.velocidadV_eje3_N1.w = 98 
bd.velocidadV_eje3_N1.h = 29
bd.velocidadV_eje3_N1.x = 506
bd.velocidadV_eje3_N1.y = 280

bd.tiempo_eje3_N1 = MetaData()
bd.tiempo_eje3_N1.path = 'img/tiempo.png'
bd.tiempo_eje3_N1.w = 69
bd.tiempo_eje3_N1.h = 30 
bd.tiempo_eje3_N1.x = 285
bd.tiempo_eje3_N1.y = 280

bd.ok_eje3_N1 = MetaData()
bd.ok_eje3_N1.path = 'img/ok.png'
bd.ok_eje3_N1.w = 47
bd.ok_eje3_N1.h = 45
bd.ok_eje3_N1.x = 950
bd.ok_eje3_N1.y = 510

bd.actualizar_eje3_N1 = MetaData()
bd.actualizar_eje3_N1.path = 'img/actualizar.png'
bd.actualizar_eje3_N1.w = 47
bd.actualizar_eje3_N1.h = 47
bd.actualizar_eje3_N1.x = 950
bd.actualizar_eje3_N1.y = 600

bd.casa_eje3_N1 = MetaData()
bd.casa_eje3_N1.path = 'img/casa.png'
bd.casa_eje3_N1.w = 47
bd.casa_eje3_N1.h = 45
bd.casa_eje3_N1.x = 950
bd.casa_eje3_N1.y = 680

bd.bombillo_eje3_N1 = MetaData()
bd.bombillo_eje3_N1.path = 'img/bombillo.png'
bd.bombillo_eje3_N1.w = 40
bd.bombillo_eje3_N1.h = 40
bd.bombillo_eje3_N1.x = 970
bd.bombillo_eje3_N1.y = 20

bd.siguiente_eje3_N1 = MetaData()
bd.siguiente_eje3_N1.path = 'img/siguiente.png'
bd.siguiente_eje3_N1.w = 192
bd.siguiente_eje3_N1.h = 91
bd.siguiente_eje3_N1.x = 830
bd.siguiente_eje3_N1.y = 0

bd.no_eje3_N1 = MetaData()
bd.no_eje3_N1.path = 'img/no.gif'
bd.no_eje3_N1.w = 207
bd.no_eje3_N1.h = 112
bd.no_eje3_N1.x = 390
bd.no_eje3_N1.y = 250

bd.bien_eje3_N1 = MetaData()
bd.bien_eje3_N1.path = 'img/bien.gif'
bd.bien_eje3_N1.w = 226
bd.bien_eje3_N1.h = 262
bd.bien_eje3_N1.x = 360
bd.bien_eje3_N1.y = 150

bd.ldescripcion_eje3_N1 = MetaData()
bd.ldescripcion_eje3_N1.text = ''
bd.ldescripcion_eje3_N1.color = (0, 0, 0, 255)
bd.ldescripcion_eje3_N1.fname = 'DejaVu Sans Mono'
bd.ldescripcion_eje3_N1.fsize = 12
bd.ldescripcion_eje3_N1.x = 510
bd.ldescripcion_eje3_N1.y = 710

bd.ldistancia_total_eje3_N1 = MetaData()
bd.ldistancia_total_eje3_N1.text = ''
bd.ldistancia_total_eje3_N1.color = (0, 0, 0, 255)
bd.ldistancia_total_eje3_N1.fname = 'DejaVu Sans Mono'
bd.ldistancia_total_eje3_N1.fsize = 12
bd.ldistancia_total_eje3_N1.x = 485 
bd.ldistancia_total_eje3_N1.y = 78

bd.ldistanciaA_u_eje3_N1 = MetaData()
bd.ldistanciaA_u_eje3_N1.text = ''
bd.ldistanciaA_u_eje3_N1.color = (0, 0, 0, 255)
bd.ldistanciaA_u_eje3_N1.fname = 'DejaVu Sans Mono'
bd.ldistanciaA_u_eje3_N1.fsize = 12
bd.ldistanciaA_u_eje3_N1.x = 133
bd.ldistanciaA_u_eje3_N1.y = 78

bd.ldistanciaB_V_eje3_N1 = MetaData()
bd.ldistanciaB_V_eje3_N1.text = ''
bd.ldistanciaB_V_eje3_N1.color = (0, 0, 0, 255)
bd.ldistanciaB_V_eje3_N1.fname = 'DejaVu Sans Mono'
bd.ldistanciaB_V_eje3_N1.fsize = 12
bd.ldistanciaB_V_eje3_N1.x = 870
bd.ldistanciaB_V_eje3_N1.y = 78

bd.lvelocidad_auto_U_eje3_N1 = MetaData()
bd.lvelocidad_auto_U_eje3_N1.text = ''
bd.lvelocidad_auto_U_eje3_N1.color = (0, 0, 0, 255)
bd.lvelocidad_auto_U_eje3_N1.fname = 'DejaVu Sans Mono'
bd.lvelocidad_auto_U_eje3_N1.fsize = 12
bd.lvelocidad_auto_U_eje3_N1.x = 480
bd.lvelocidad_auto_U_eje3_N1.y = 553

bd.lvelocidadV_eje3_N1 = MetaData()
bd.lvelocidadV_eje3_N1.text = ''
bd.lvelocidadV_eje3_N1.color = (0, 0, 0, 255)
bd.lvelocidadV_eje3_N1.fname = 'DejaVu Sans Mono'
bd.lvelocidadV_eje3_N1.fsize = 12
bd.lvelocidadV_eje3_N1.x = 540
bd.lvelocidadV_eje3_N1.y = 268

bd.ltiempo_transcurrido_eje3_N1 = MetaData()
bd.ltiempo_transcurrido_eje3_N1.text = ''
bd.ltiempo_transcurrido_eje3_N1.color = (0, 0, 0, 255)
bd.ltiempo_transcurrido_eje3_N1.fname = 'DejaVu Sans Mono'
bd.ltiempo_transcurrido_eje3_N1.fsize = 12
bd.ltiempo_transcurrido_eje3_N1.x = 305
bd.ltiempo_transcurrido_eje3_N1.y = 268

bd.diploma_N1 = MetaData()
bd.diploma_N1.path = 'img/diploma_n1.png'
bd.diploma_N1.w = 562
bd.diploma_N1.h = 435
bd.diploma_N1.x = 220
bd.diploma_N1.y = 170

bd.zones['EJERCICIO3_N1'] = {}

bd.zones['EJERCICIO3_N1'] ['mover_mano'] = [(bd.mano_eje3_N1.x, bd.mano_eje3_N1.y, bd.mano_eje3_N1.w, bd.mano_eje3_N1.h)]
bd.zones['EJERCICIO3_N1'] ['ir_ok'] = [(bd.ok_eje3_N1.x, bd.ok_eje3_N1.y, bd.ok_eje3_N1.w, bd.ok_eje3_N1.h)]
bd.zones['EJERCICIO3_N1'] ['ir_casa'] = [(bd.casa_eje3_N1.x, bd.casa_eje3_N1.y, bd.casa_eje3_N1.w, bd.casa_eje3_N1.h)]
bd.zones['EJERCICIO3_N1'] ['ir_actualizar'] = [(bd.actualizar_eje3_N1.x, bd.actualizar_eje3_N1.y, bd.actualizar_eje3_N1.w, bd.actualizar_eje3_N1.h)]
bd.zones['EJERCICIO3_N1'] ['ir_bombillo'] = [(bd.bombillo_eje3_N1.x, bd.bombillo_eje3_N1.y, bd.bombillo_eje3_N1.w, bd.bombillo_eje3_N1.h)]
bd.zones['EJERCICIO3_N1'] ['ir_niveles'] = [(bd.anterior9_eje3_N1.x, bd.anterior9_eje3_N1.y, bd.anterior9_eje3_N1.w, bd.anterior9_eje3_N1.h)]
bd.zones['EJERCICIO3_N1'] ['terminar_nivel'] = [(650, 260, 100, 70)]
#=====================================================================
# EJERCICIO1_N2 1024X768
#=====================================================================

bd.anterior_eje1_N2 = MetaData()
bd.anterior_eje1_N2.path = 'img/anterior.png'
bd.anterior_eje1_N2.w = 83
bd.anterior_eje1_N2.h = 76
bd.anterior_eje1_N2.x = 5
bd.anterior_eje1_N2.y = 10

bd.pinguino_eje1_N2 = MetaData()
bd.pinguino_eje1_N2.path = 'img/pinguino.png'
bd.pinguino_eje1_N2.w = 45
bd.pinguino_eje1_N2.h = 68
bd.pinguino_eje1_N2.x = 140
bd.pinguino_eje1_N2.y = 395

bd.hielo_eje1_N2 = MetaData()
bd.hielo_eje1_N2.path = 'img/hielo.png'
bd.hielo_eje1_N2.w = 210
bd.hielo_eje1_N2.h = 300
bd.hielo_eje1_N2.x = 0
bd.hielo_eje1_N2.y = 120

bd.nevado_eje1_N2 = MetaData()
bd.nevado_eje1_N2.path = 'img/nevado.png'
bd.nevado_eje1_N2.w = 525
bd.nevado_eje1_N2.h = 195
bd.nevado_eje1_N2.x = 495
bd.nevado_eje1_N2.y = 120

bd.iglu_eje1_N2 = MetaData()
bd.iglu_eje1_N2.path = 'img/iglu.png'
bd.iglu_eje1_N2.w = 113
bd.iglu_eje1_N2.h = 75
bd.iglu_eje1_N2.x = 612
bd.iglu_eje1_N2.y = 157

bd.rio_eje1_N2 = MetaData()
bd.rio_eje1_N2.path = 'img/rio.png'
bd.rio_eje1_N2.w = 1024
bd.rio_eje1_N2.h = 113
bd.rio_eje1_N2.x = 0
bd.rio_eje1_N2.y = 120

bd.orca_eje1_N2 = MetaData()
bd.orca_eje1_N2.path = 'img/orca.png'
bd.orca_eje1_N2.w = 285
bd.orca_eje1_N2.h = 163
bd.orca_eje1_N2.x = 230
bd.orca_eje1_N2.y = 175

bd.ok_eje1_N2 = MetaData()
bd.ok_eje1_N2.path = 'img/ok.png'
bd.ok_eje1_N2.w = 47
bd.ok_eje1_N2.h = 49
bd.ok_eje1_N2.x = 950
bd.ok_eje1_N2.y = 510

bd.actualizar_eje1_N2 = MetaData()
bd.actualizar_eje1_N2.path = 'img/actualizar.png'
bd.actualizar_eje1_N2.w = 47
bd.actualizar_eje1_N2.h = 47
bd.actualizar_eje1_N2.x = 950
bd.actualizar_eje1_N2.y = 600

bd.casa_eje1_N2 = MetaData()
bd.casa_eje1_N2.path = 'img/casa.png'
bd.casa_eje1_N2.w = 47
bd.casa_eje1_N2.h = 45
bd.casa_eje1_N2.x = 950
bd.casa_eje1_N2.y = 680

bd.bombillo_eje1_N2 = MetaData()
bd.bombillo_eje1_N2.path = 'img/bombillo.png'
bd.bombillo_eje1_N2.w = 40
bd.bombillo_eje1_N2.h = 40
bd.bombillo_eje1_N2.x = 970
bd.bombillo_eje1_N2.y = 20

bd.siguiente_eje1_N2 = MetaData()
bd.siguiente_eje1_N2.path = 'img/siguiente.png'
bd.siguiente_eje1_N2.w = 192
bd.siguiente_eje1_N2.h = 91
bd.siguiente_eje1_N2.x = 830
bd.siguiente_eje1_N2.y = 0

bd.no_eje1_N2 = MetaData()
bd.no_eje1_N2.path = 'img/mal.gif'
bd.no_eje1_N2.w = 207
bd.no_eje1_N2.h = 112
bd.no_eje1_N2.x = 280
bd.no_eje1_N2.y = 170

bd.exe_eje1_N2 = MetaData()
bd.exe_eje1_N2.path = 'img/banana.gif'
bd.exe_eje1_N2.w = 247
bd.exe_eje1_N2.h = 149
bd.exe_eje1_N2.x = 250
bd.exe_eje1_N2.y = 170

bd.flecha_menos_eje1_N2 = MetaData()
bd.flecha_menos_eje1_N2.path = 'img/flecha-.png'
bd.flecha_menos_eje1_N2.w = 17
bd.flecha_menos_eje1_N2.h = 23
bd.flecha_menos_eje1_N2.x = 655
bd.flecha_menos_eje1_N2.y = 475

bd.flecha_mas_eje1_N2 = MetaData()
bd.flecha_mas_eje1_N2.path = 'img/flecha+.png'
bd.flecha_mas_eje1_N2.w = 17
bd.flecha_mas_eje1_N2.h = 23
bd.flecha_mas_eje1_N2.x = 760
bd.flecha_mas_eje1_N2.y = 475

bd.altura_iceberg_campo_eje1_N2 = MetaData()
bd.altura_iceberg_campo_eje1_N2.path = 'img/campo.png'
bd.altura_iceberg_campo_eje1_N2.w = 75
bd.altura_iceberg_campo_eje1_N2.h = 30
bd.altura_iceberg_campo_eje1_N2.x = 180
bd.altura_iceberg_campo_eje1_N2.y = 65

bd.velocidad_pingui_campo_eje1_N2 = MetaData()
bd.velocidad_pingui_campo_eje1_N2.path = 'img/campo.png'
bd.velocidad_pingui_campo_eje1_N2.w = 75
bd.velocidad_pingui_campo_eje1_N2.h = 30
bd.velocidad_pingui_campo_eje1_N2.x = 769
bd.velocidad_pingui_campo_eje1_N2.y = 65

bd.res_campo_eje1_N2 = MetaData()
bd.res_campo_eje1_N2.path = 'img/campo.png'
bd.res_campo_eje1_N2.w = 75
bd.res_campo_eje1_N2.h = 30
bd.res_campo_eje1_N2.x = 680
bd.res_campo_eje1_N2.y = 470

bd.altura_eje1_N2 = MetaData()
bd.altura_eje1_N2.path = 'img/altura.png'
bd.altura_eje1_N2.w = 127
bd.altura_eje1_N2.h = 29
bd.altura_eje1_N2.x = 155
bd.altura_eje1_N2.y = 40

bd.velocidad_eje1_N2 = MetaData()
bd.velocidad_eje1_N2.path = 'img/velocidad.png'
bd.velocidad_eje1_N2.w = 166
bd.velocidad_eje1_N2.h = 31
bd.velocidad_eje1_N2.x = 730
bd.velocidad_eje1_N2.y = 40

bd.alcance_horizontal_eje1_N2 = MetaData()
bd.alcance_horizontal_eje1_N2.path = 'img/alcance.png'
bd.alcance_horizontal_eje1_N2.w = 163
bd.alcance_horizontal_eje1_N2.h = 29
bd.alcance_horizontal_eje1_N2.x = 635
bd.alcance_horizontal_eje1_N2.y = 495

bd.laltura_eje1_N2 = MetaData()
bd.laltura_eje1_N2.text = ''
bd.laltura_eje1_N2.color = (0, 0, 0, 255)
bd.laltura_eje1_N2.fname = 'DejaVu Sans Mono'
bd.laltura_eje1_N2.fsize = 12
bd.laltura_eje1_N2.x = 195
bd.laltura_eje1_N2.y = 78

bd.lvelocidad_eje1_N2 = MetaData()
bd.lvelocidad_eje1_N2.text = ''
bd.lvelocidad_eje1_N2.color = (0, 0, 0, 255)
bd.lvelocidad_eje1_N2.fname = 'DejaVu Sans Mono'
bd.lvelocidad_eje1_N2.fsize = 12
bd.lvelocidad_eje1_N2.x = 795
bd.lvelocidad_eje1_N2.y = 78

bd.lalcance_horizontal_eje1_N2 = MetaData()
bd.lalcance_horizontal_eje1_N2.text = ''
bd.lalcance_horizontal_eje1_N2.color = (0, 0, 0, 255)
bd.lalcance_horizontal_eje1_N2.fname = 'DejaVu Sans Mono'
bd.lalcance_horizontal_eje1_N2.fsize = 12
bd.lalcance_horizontal_eje1_N2.x = 695
bd.lalcance_horizontal_eje1_N2.y = 482

bd.ldescripcion_eje1_N2 = MetaData()
bd.ldescripcion_eje1_N2.text = ''
bd.ldescripcion_eje1_N2.color = (0, 0, 0, 255)
bd.ldescripcion_eje1_N2.fname = 'DejaVu Sans Mono'
bd.ldescripcion_eje1_N2.fsize = 12
bd.ldescripcion_eje1_N2.x = 500
bd.ldescripcion_eje1_N2.y = 710

bd.zones['EJERCICIO1_N2'] = {}
bd.zones['EJERCICIO1_N2'] ['ir_niveles'] = [(bd.anterior_eje1_N2.x, bd.anterior_eje1_N2.y, bd.anterior_eje1_N2.w, bd.anterior_eje1_N2.h)]
bd.zones['EJERCICIO1_N2'] ['ir_ok'] = [(bd.ok_eje1_N2.x, bd.ok_eje1_N2.y, bd.ok_eje1_N2.w, bd.ok_eje1_N2.h)]
bd.zones['EJERCICIO1_N2'] ['ir_casa'] = [(bd.casa_eje1_N2.x, bd.casa_eje1_N2.y, bd.casa_eje1_N2.w, bd.casa_eje1_N2.h)]
bd.zones['EJERCICIO1_N2'] ['ir_actualizar'] = [(bd.actualizar_eje1_N2.x, bd.actualizar_eje1_N2.y, bd.actualizar_eje1_N2.w, bd.actualizar_eje1_N2.h)]
bd.zones['EJERCICIO1_N2'] ['ir_bombillo'] = [(bd.bombillo_eje1_N2.x, bd.bombillo_eje1_N2.y, bd.bombillo_eje1_N2.w, bd.bombillo_eje1_N2.h)]
bd.zones['EJERCICIO1_N2'] ['mas'] = [(bd.flecha_mas_eje1_N2.x, bd.flecha_mas_eje1_N2.y, bd.flecha_mas_eje1_N2.w, bd.flecha_mas_eje1_N2.h)]
bd.zones['EJERCICIO1_N2'] ['menos'] = [(bd.flecha_menos_eje1_N2.x, bd.flecha_menos_eje1_N2.y, bd.flecha_menos_eje1_N2.w, bd.flecha_menos_eje1_N2.h)]

#=====================================================================
# EJERCICIO2_N2 1024X768
#=====================================================================

bd.anterior_eje2_N2 = MetaData()
bd.anterior_eje2_N2.path = 'img/anterior.png'
bd.anterior_eje2_N2.w = 83
bd.anterior_eje2_N2.h = 76
bd.anterior_eje2_N2.x = 5
bd.anterior_eje2_N2.y = 5

bd.monster_eje2_N2 = MetaData()
bd.monster_eje2_N2.path = 'img/monster.png'
bd.monster_eje2_N2.w = 113
bd.monster_eje2_N2.h = 66
bd.monster_eje2_N2.x = 1
bd.monster_eje2_N2.y = 310

bd.monster1_eje2_N2 = MetaData()
bd.monster1_eje2_N2.path = 'img/monster1.png'
bd.monster1_eje2_N2.w = 113
bd.monster1_eje2_N2.h = 68
bd.monster1_eje2_N2.x = 130
bd.monster1_eje2_N2.y = 310

bd.monster2_eje2_N2 = MetaData()
bd.monster2_eje2_N2.path = 'img/monster2.png'
bd.monster2_eje2_N2.w = 113
bd.monster2_eje2_N2.h = 73
bd.monster2_eje2_N2.x = 145
bd.monster2_eje2_N2.y = 309

bd.monster3_eje2_N2 = MetaData()
bd.monster3_eje2_N2.path = 'img/monster3.png'
bd.monster3_eje2_N2.w = 115
bd.monster3_eje2_N2.h = 78
bd.monster3_eje2_N2.x = 160
bd.monster3_eje2_N2.y = 309

bd.monster4_eje2_N2 = MetaData()
bd.monster4_eje2_N2.path = 'img/monster4.png'
bd.monster4_eje2_N2.w = 115
bd.monster4_eje2_N2.h = 88
bd.monster4_eje2_N2.x = 176
bd.monster4_eje2_N2.y = 310

bd.monster5_eje2_N2 = MetaData()
bd.monster5_eje2_N2.path = 'img/monster5.png'
bd.monster5_eje2_N2.w = 113
bd.monster5_eje2_N2.h = 94
bd.monster5_eje2_N2.x = 211
bd.monster5_eje2_N2.y = 316

bd.monster6_eje2_N2 = MetaData()
bd.monster6_eje2_N2.path = 'img/monster6.png'
bd.monster6_eje2_N2.w = 113
bd.monster6_eje2_N2.h = 93
bd.monster6_eje2_N2.x = 233
bd.monster6_eje2_N2.y = 325

bd.sombra_eje2_N2 = MetaData()
bd.sombra_eje2_N2.path = 'img/sombra.png'
bd.sombra_eje2_N2.w = 113
bd.sombra_eje2_N2.h = 66
bd.sombra_eje2_N2.x = 680
bd.sombra_eje2_N2.y = 308

bd.piedra_eje2_N2 = MetaData()
bd.piedra_eje2_N2.path = 'img/piedra.png'
bd.piedra_eje2_N2.w = 187
bd.piedra_eje2_N2.h = 75
bd.piedra_eje2_N2.x = 220
bd.piedra_eje2_N2.y = 284

bd.abismo1_eje2_N2 = MetaData()
bd.abismo1_eje2_N2.path = 'img/abismo1.png'
bd.abismo1_eje2_N2.w = 409
bd.abismo1_eje2_N2.h = 313
bd.abismo1_eje2_N2.x = 0
bd.abismo1_eje2_N2.y = 0

bd.abismo2_eje2_N2 = MetaData()
bd.abismo2_eje2_N2.path = 'img/abismo2.png'
bd.abismo2_eje2_N2.w = 409
bd.abismo2_eje2_N2.h = 364
bd.abismo2_eje2_N2.x = 615
bd.abismo2_eje2_N2.y = 0

bd.rocas_eje2_N2 = MetaData()
bd.rocas_eje2_N2.path = 'img/rocas.png'
bd.rocas_eje2_N2.w = 1020
bd.rocas_eje2_N2.h = 50
bd.rocas_eje2_N2.x = 3
bd.rocas_eje2_N2.y = 0

bd.ok_eje2_N2 = MetaData()
bd.ok_eje2_N2.path = 'img/ok.png'
bd.ok_eje2_N2.w = 47
bd.ok_eje2_N2.h = 49
bd.ok_eje2_N2.x = 950
bd.ok_eje2_N2.y = 530

bd.actualizar_eje2_N2 = MetaData()
bd.actualizar_eje2_N2.path = 'img/actualizar.png'
bd.actualizar_eje2_N2.w = 47
bd.actualizar_eje2_N2.h = 47
bd.actualizar_eje2_N2.x = 950
bd.actualizar_eje2_N2.y = 610

bd.casa_eje2_N2 = MetaData()
bd.casa_eje2_N2.path = 'img/casa.png'
bd.casa_eje2_N2.w = 47
bd.casa_eje2_N2.h = 45
bd.casa_eje2_N2.x = 950
bd.casa_eje2_N2.y = 680

bd.bombillo_eje2_N2 = MetaData()
bd.bombillo_eje2_N2.path = 'img/bombillo.png'
bd.bombillo_eje2_N2.w = 40
bd.bombillo_eje2_N2.h = 40
bd.bombillo_eje2_N2.x = 970
bd.bombillo_eje2_N2.y = 20

bd.siguiente_eje2_N2 = MetaData()
bd.siguiente_eje2_N2.path = 'img/siguiente.png'
bd.siguiente_eje2_N2.w = 192
bd.siguiente_eje2_N2.h = 91
bd.siguiente_eje2_N2.x = 830
bd.siguiente_eje2_N2.y = 0

bd.no_eje2_N2 = MetaData()
bd.no_eje2_N2.path = 'img/mal.gif'
bd.no_eje2_N2.w = 207
bd.no_eje2_N2.h = 112
bd.no_eje2_N2.x = 340
bd.no_eje2_N2.y = 15

bd.exe_eje2_N2 = MetaData()
bd.exe_eje2_N2.path = 'img/banana.gif'
bd.exe_eje2_N2.w = 247
bd.exe_eje2_N2.h = 149
bd.exe_eje2_N2.x = 320
bd.exe_eje2_N2.y = 15

bd.explosion_eje2_N2 = MetaData()
bd.explosion_eje2_N2.path = 'img/explosion.gif'
bd.explosion_eje2_N2.w = 329
bd.explosion_eje2_N2.h = 198
bd.explosion_eje2_N2.x = 420
bd.explosion_eje2_N2.y = 20

bd.flecha_menos_eje2_N2 = MetaData()
bd.flecha_menos_eje2_N2.path = 'img/flecha-.png'
bd.flecha_menos_eje2_N2.w = 17
bd.flecha_menos_eje2_N2.h = 23
bd.flecha_menos_eje2_N2.x = 745
bd.flecha_menos_eje2_N2.y = 475

bd.flecha_mas_eje2_N2 = MetaData()
bd.flecha_mas_eje2_N2.path = 'img/flecha+.png'
bd.flecha_mas_eje2_N2.w = 17
bd.flecha_mas_eje2_N2.h = 23
bd.flecha_mas_eje2_N2.x = 848
bd.flecha_mas_eje2_N2.y = 475

bd.altura_colina_campo_eje2_N2 = MetaData()
bd.altura_colina_campo_eje2_N2.path = 'img/campo.png'
bd.altura_colina_campo_eje2_N2.w = 75
bd.altura_colina_campo_eje2_N2.h = 30
bd.altura_colina_campo_eje2_N2.x = 250
bd.altura_colina_campo_eje2_N2.y = 75

bd.angulo_campo_eje2_N2 = MetaData()
bd.angulo_campo_eje2_N2.path = 'img/campo.png'
bd.angulo_campo_eje2_N2.w = 75
bd.angulo_campo_eje2_N2.h = 30
bd.angulo_campo_eje2_N2.x = 45
bd.angulo_campo_eje2_N2.y = 405

bd.res_campo_eje2_N2 = MetaData()
bd.res_campo_eje2_N2.path = 'img/campo.png'
bd.res_campo_eje2_N2.w = 70
bd.res_campo_eje2_N2.h = 30
bd.res_campo_eje2_N2.x = 770
bd.res_campo_eje2_N2.y = 470

bd.altura_colina_eje2_N2 = MetaData()
bd.altura_colina_eje2_N2.path = 'img/alturaColina.png'
bd.altura_colina_eje2_N2.w = 123
bd.altura_colina_eje2_N2.h = 30
bd.altura_colina_eje2_N2.x = 230
bd.altura_colina_eje2_N2.y = 100

bd.angulo_eje2_N2 = MetaData()
bd.angulo_eje2_N2.path = 'img/angulo.png'
bd.angulo_eje2_N2.w = 150
bd.angulo_eje2_N2.h = 32
bd.angulo_eje2_N2.x = 10
bd.angulo_eje2_N2.y = 430

bd.velocidad_eje2_N2 = MetaData()
bd.velocidad_eje2_N2.path = 'img/velocidadAuto.png'
bd.velocidad_eje2_N2.w = 135
bd.velocidad_eje2_N2.h = 30
bd.velocidad_eje2_N2.x = 735
bd.velocidad_eje2_N2.y = 495

bd.ldescripcion_eje2_N2 = MetaData()
bd.ldescripcion_eje2_N2.text = ''
bd.ldescripcion_eje2_N2.color = (0, 0, 0, 255)
bd.ldescripcion_eje2_N2.fname = 'DejaVu Sans Mono'
bd.ldescripcion_eje2_N2.fsize = 12
bd.ldescripcion_eje2_N2.x = 500
bd.ldescripcion_eje2_N2.y = 700

bd.laltura_eje2_N2 = MetaData()
bd.laltura_eje2_N2.text = ''
bd.laltura_eje2_N2.color = (0, 0, 0, 255)
bd.laltura_eje2_N2.fname = 'DejaVu Sans Mono'
bd.laltura_eje2_N2.fsize = 12
bd.laltura_eje2_N2.x = 265
bd.laltura_eje2_N2.y = 88

bd.langulo_elevacion_eje2_N2 = MetaData()
bd.langulo_elevacion_eje2_N2.text = ''
bd.langulo_elevacion_eje2_N2.color = (0, 0, 0, 255)
bd.langulo_elevacion_eje2_N2.fname = 'DejaVu Sans Mono'
bd.langulo_elevacion_eje2_N2.fsize = 12
bd.langulo_elevacion_eje2_N2.x = 70
bd.langulo_elevacion_eje2_N2.y = 417

bd.lvelocidad_eje2_N2 = MetaData()
bd.lvelocidad_eje2_N2.text = ''
bd.lvelocidad_eje2_N2.color = (0, 0, 0, 255)
bd.lvelocidad_eje2_N2.fname = 'DejaVu Sans Mono'
bd.lvelocidad_eje2_N2.fsize = 12
bd.lvelocidad_eje2_N2.x = 775
bd.lvelocidad_eje2_N2.y = 482

bd.zones['EJERCICIO2_N2'] = {}
bd.zones['EJERCICIO2_N2'] ['ir_niveles'] = [(bd.anterior_eje2_N2.x, bd.anterior_eje2_N2.y, bd.anterior_eje2_N2.w, bd.anterior_eje2_N2.h)]
bd.zones['EJERCICIO2_N2'] ['ir_ok'] = [(bd.ok_eje2_N2.x, bd.ok_eje2_N2.y, bd.ok_eje2_N2.w, bd.ok_eje2_N2.h)]
bd.zones['EJERCICIO2_N2'] ['ir_casa'] = [(bd.casa_eje2_N2.x, bd.casa_eje2_N2.y, bd.casa_eje2_N2.w, bd.casa_eje2_N2.h)]
bd.zones['EJERCICIO2_N2'] ['ir_actualizar'] = [(bd.actualizar_eje2_N2.x, bd.actualizar_eje2_N2.y, bd.actualizar_eje2_N2.w, bd.actualizar_eje2_N2.h)]
bd.zones['EJERCICIO2_N2'] ['ir_bombillo'] = [(bd.bombillo_eje2_N2.x, bd.bombillo_eje2_N2.y, bd.bombillo_eje2_N2.w, bd.bombillo_eje2_N2.h)]
bd.zones['EJERCICIO2_N2'] ['mas'] = [(bd.flecha_mas_eje2_N2.x, bd.flecha_mas_eje2_N2.y, bd.flecha_mas_eje2_N2.w, bd.flecha_mas_eje2_N2.h)]
bd.zones['EJERCICIO2_N2'] ['menos'] = [(bd.flecha_menos_eje2_N2.x, bd.flecha_menos_eje2_N2.y, bd.flecha_menos_eje2_N2.w, bd.flecha_menos_eje2_N2.h)]

#=====================================================================
# EJERCICIO3_N2 1024X768
#=====================================================================

bd.anterior_eje3_N2 = MetaData()
bd.anterior_eje3_N2.path = 'img/anterior.png'
bd.anterior_eje3_N2.w = 83
bd.anterior_eje3_N2.h = 76
bd.anterior_eje3_N2.x = 5
bd.anterior_eje3_N2.y = 5

bd.rocas_eje3_N2 = MetaData()
bd.rocas_eje3_N2.path = 'img/rocas2.png'
bd.rocas_eje3_N2.w = 1024
bd.rocas_eje3_N2.h = 50
bd.rocas_eje3_N2.x = 0
bd.rocas_eje3_N2.y = 0

bd.grua_eje3_N2 = MetaData()
bd.grua_eje3_N2.path = 'img/grua.png'
bd.grua_eje3_N2.w = 500
bd.grua_eje3_N2.h = 450
bd.grua_eje3_N2.x = 120
bd.grua_eje3_N2.y = 5

bd.bola_eje3_N2 = MetaData()
bd.bola_eje3_N2.path = 'img/bola2.gif'
bd.bola_eje3_N2.w = 280
bd.bola_eje3_N2.h = 235
bd.bola_eje3_N2.x = 450
bd.bola_eje3_N2.y = 195

bd.bola1_eje3_N2 = MetaData()
bd.bola1_eje3_N2.path = 'img/bola1.png'
bd.bola1_eje3_N2.w = 70
bd.bola1_eje3_N2.h = 242
bd.bola1_eje3_N2.x = 555
bd.bola1_eje3_N2.y = 186

bd.edificio_eje3_N2 = MetaData()
bd.edificio_eje3_N2.path = 'img/edificio.png'
bd.edificio_eje3_N2.w = 240
bd.edificio_eje3_N2.h = 380
bd.edificio_eje3_N2.x = 717
bd.edificio_eje3_N2.y = 20

bd.luz_eje3_N2 = MetaData()
bd.luz_eje3_N2.path = 'img/luz2.gif'
bd.luz_eje3_N2.w = 400
bd.luz_eje3_N2.h = 430
bd.luz_eje3_N2.x = 620
bd.luz_eje3_N2.y = 0

bd.ok_eje3_N2 = MetaData()
bd.ok_eje3_N2.path = 'img/ok.png'
bd.ok_eje3_N2.w = 47
bd.ok_eje3_N2.h = 49
bd.ok_eje3_N2.x = 950
bd.ok_eje3_N2.y = 530

bd.actualizar_eje3_N2 = MetaData()
bd.actualizar_eje3_N2.path = 'img/actualizar.png'
bd.actualizar_eje3_N2.w = 47
bd.actualizar_eje3_N2.h = 47
bd.actualizar_eje3_N2.x = 950
bd.actualizar_eje3_N2.y = 610

bd.casa_eje3_N2 = MetaData()
bd.casa_eje3_N2.path = 'img/casa.png'
bd.casa_eje3_N2.w = 47
bd.casa_eje3_N2.h = 45
bd.casa_eje3_N2.x = 950
bd.casa_eje3_N2.y = 680

bd.bombillo_eje3_N2 = MetaData()
bd.bombillo_eje3_N2.path = 'img/bombillo.png'
bd.bombillo_eje3_N2.w = 40
bd.bombillo_eje3_N2.h = 40
bd.bombillo_eje3_N2.x = 970
bd.bombillo_eje3_N2.y = 10

bd.siguiente_eje3_N2 = MetaData()
bd.siguiente_eje3_N2.path = 'img/siguiente.png'
bd.siguiente_eje3_N2.w = 192
bd.siguiente_eje3_N2.h = 91
bd.siguiente_eje3_N2.x = 830
bd.siguiente_eje3_N2.y = 0

bd.no_eje3_N2 = MetaData()
bd.no_eje3_N2.path = 'img/mal.gif'
bd.no_eje3_N2.w = 207
bd.no_eje3_N2.h = 112
bd.no_eje3_N2.x = 430
bd.no_eje3_N2.y = 15

bd.exe_eje3_N2 = MetaData()
bd.exe_eje3_N2.path = 'img/banana.gif'
bd.exe_eje3_N2.w = 247
bd.exe_eje3_N2.h = 149
bd.exe_eje3_N2.x = 400
bd.exe_eje3_N2.y = 15

bd.flecha_menos_eje3_N2 = MetaData()
bd.flecha_menos_eje3_N2.path = 'img/flecha-.png'
bd.flecha_menos_eje3_N2.w = 17
bd.flecha_menos_eje3_N2.h = 23
bd.flecha_menos_eje3_N2.x = 715
bd.flecha_menos_eje3_N2.y = 475

bd.flecha_mas_eje3_N2 = MetaData()
bd.flecha_mas_eje3_N2.path = 'img/flecha+.png'
bd.flecha_mas_eje3_N2.w = 17
bd.flecha_mas_eje3_N2.h = 23
bd.flecha_mas_eje3_N2.x = 818
bd.flecha_mas_eje3_N2.y = 475

bd.longitud_cable_campo_eje3_N2 = MetaData()
bd.longitud_cable_campo_eje3_N2.path = 'img/campo.png'
bd.longitud_cable_campo_eje3_N2.w = 75
bd.longitud_cable_campo_eje3_N2.h = 30
bd.longitud_cable_campo_eje3_N2.x = 200
bd.longitud_cable_campo_eje3_N2.y = 275

bd.res_campo_eje3_N2 = MetaData()
bd.res_campo_eje3_N2.path = 'img/campo.png'
bd.res_campo_eje3_N2.w = 70
bd.res_campo_eje3_N2.h = 30
bd.res_campo_eje3_N2.x = 740
bd.res_campo_eje3_N2.y = 470

bd.longitud_eje3_N2 = MetaData()
bd.longitud_eje3_N2.path = 'img/longitud.png'
bd.longitud_eje3_N2.w = 138
bd.longitud_eje3_N2.h = 33
bd.longitud_eje3_N2.x = 175
bd.longitud_eje3_N2.y = 300

bd.periodo_eje3_N2 = MetaData()
bd.periodo_eje3_N2.path = 'img/periodo.png'
bd.periodo_eje3_N2.w = 145
bd.periodo_eje3_N2.h = 30
bd.periodo_eje3_N2.x = 705
bd.periodo_eje3_N2.y = 495

bd.ldescripcion_eje3_N2 = MetaData()
bd.ldescripcion_eje3_N2.text = ''
bd.ldescripcion_eje3_N2.color = (0, 0, 0, 255)
bd.ldescripcion_eje3_N2.fname = 'DejaVu Sans Mono'
bd.ldescripcion_eje3_N2.fsize = 12
bd.ldescripcion_eje3_N2.x = 500
bd.ldescripcion_eje3_N2.y = 700

bd.llongitud_eje3_N2 = MetaData()
bd.llongitud_eje3_N2.text = ''
bd.llongitud_eje3_N2.color = (0, 0, 0, 255)
bd.llongitud_eje3_N2.fname = 'DejaVu Sans Mono'
bd.llongitud_eje3_N2.fsize = 12
bd.llongitud_eje3_N2.x = 65
bd.llongitud_eje3_N2.y = 288

bd.lperiodo_eje3_N2 = MetaData()
bd.lperiodo_eje3_N2.text = ''
bd.lperiodo_eje3_N2.color = (0, 0, 0, 255)
bd.lperiodo_eje3_N2.fname = 'DejaVu Sans Mono'
bd.lperiodo_eje3_N2.fsize = 12
bd.lperiodo_eje3_N2.x = 745
bd.lperiodo_eje3_N2.y = 482

bd.diploma_N2 = MetaData()
bd.diploma_N2.path = 'img/diploma_n2.png'
bd.diploma_N2.w = 562
bd.diploma_N2.h = 435
bd.diploma_N2.x = 220
bd.diploma_N2.y = 170

bd.zones['EJERCICIO3_N2'] = {}
bd.zones['EJERCICIO3_N2'] ['ir_niveles'] = [(bd.anterior_eje3_N2.x, bd.anterior_eje3_N2.y, bd.anterior_eje3_N2.w, bd.anterior_eje3_N2.h)]
bd.zones['EJERCICIO3_N2'] ['ir_ok'] = [(bd.ok_eje3_N2.x, bd.ok_eje3_N2.y, bd.ok_eje3_N2.w, bd.ok_eje3_N2.h)]
bd.zones['EJERCICIO3_N2'] ['ir_casa'] = [(bd.casa_eje3_N2.x, bd.casa_eje3_N2.y, bd.casa_eje3_N2.w, bd.casa_eje3_N2.h)]
bd.zones['EJERCICIO3_N2'] ['ir_actualizar'] = [(bd.actualizar_eje3_N2.x, bd.actualizar_eje3_N2.y, bd.actualizar_eje3_N2.w, bd.actualizar_eje3_N2.h)]
bd.zones['EJERCICIO3_N2'] ['ir_bombillo'] = [(bd.bombillo_eje3_N2.x, bd.bombillo_eje3_N2.y, bd.bombillo_eje3_N2.w, bd.bombillo_eje3_N2.h)]
bd.zones['EJERCICIO3_N2'] ['mas'] = [(bd.flecha_mas_eje3_N2.x, bd.flecha_mas_eje3_N2.y, bd.flecha_mas_eje3_N2.w, bd.flecha_mas_eje3_N2.h)]
bd.zones['EJERCICIO3_N2'] ['menos'] = [(bd.flecha_menos_eje3_N2.x, bd.flecha_menos_eje3_N2.y, bd.flecha_menos_eje3_N2.w, bd.flecha_menos_eje3_N2.h)]

#=====================================================================
# EJERCICIO1_N3 1024X768 
#=====================================================================
bd.anterior_eje1_N3 = MetaData()
bd.anterior_eje1_N3.path = 'img/anterior.png'
bd.anterior_eje1_N3.w = 83
bd.anterior_eje1_N3.h = 76
bd.anterior_eje1_N3.x = 0
bd.anterior_eje1_N3.y = 0

bd.suelo_eje1_N3 = MetaData()
bd.suelo_eje1_N3.path = 'img/suelo.png'
bd.suelo_eje1_N3.w = 1024
bd.suelo_eje1_N3.h = 185
bd.suelo_eje1_N3.x = 0
bd.suelo_eje1_N3.y = 0

bd.arbol_eje1_N3 = MetaData()
bd.arbol_eje1_N3.path = 'img/arbol.png'
bd.arbol_eje1_N3.w = 450
bd.arbol_eje1_N3.h = 500
bd.arbol_eje1_N3.x = 0
bd.arbol_eje1_N3.y = 0

bd.manzana_eje1_N3 = MetaData()
bd.manzana_eje1_N3.path = 'img/manzana.png'
bd.manzana_eje1_N3.w = 30
bd.manzana_eje1_N3.h = 34
bd.manzana_eje1_N3.x = 257
bd.manzana_eje1_N3.y = 300

bd.nino_eje1_N3 = MetaData()
bd.nino_eje1_N3.path = 'img/nino.png'
bd.nino_eje1_N3.w = 250
bd.nino_eje1_N3.h = 133
bd.nino_eje1_N3.x = 220
bd.nino_eje1_N3.y = 0

bd.sol_eje1_N3 = MetaData()
bd.sol_eje1_N3.path = 'img/sol.png'
bd.sol_eje1_N3.w = 200
bd.sol_eje1_N3.h = 200
bd.sol_eje1_N3.x = 750
bd.sol_eje1_N3.y = 400

bd.golpe_eje1_N3 = MetaData()
bd.golpe_eje1_N3.path = 'img/golpe2.gif'
bd.golpe_eje1_N3.w = 160
bd.golpe_eje1_N3.h = 151
bd.golpe_eje1_N3.x = 138
bd.golpe_eje1_N3.y = 44

bd.ok_eje1_N3 = MetaData()
bd.ok_eje1_N3.path = 'img/ok.png'
bd.ok_eje1_N3.w = 47
bd.ok_eje1_N3.h = 49
bd.ok_eje1_N3.x = 950
bd.ok_eje1_N3.y = 530

bd.actualizar_eje1_N3 = MetaData()
bd.actualizar_eje1_N3.path = 'img/actualizar.png'
bd.actualizar_eje1_N3.w = 47
bd.actualizar_eje1_N3.h = 47
bd.actualizar_eje1_N3.x = 950
bd.actualizar_eje1_N3.y = 610

bd.casa_eje1_N3 = MetaData()
bd.casa_eje1_N3.path = 'img/casa.png'
bd.casa_eje1_N3.w = 47
bd.casa_eje1_N3.h = 45
bd.casa_eje1_N3.x = 950
bd.casa_eje1_N3.y = 680

bd.bombillo_eje1_N3 = MetaData()
bd.bombillo_eje1_N3.path = 'img/bombillo.png'
bd.bombillo_eje1_N3.w = 40
bd.bombillo_eje1_N3.h = 40
bd.bombillo_eje1_N3.x = 970
bd.bombillo_eje1_N3.y = 10

bd.siguiente_eje1_N3 = MetaData()
bd.siguiente_eje1_N3.path = 'img/siguiente.png'
bd.siguiente_eje1_N3.w = 192
bd.siguiente_eje1_N3.h = 91
bd.siguiente_eje1_N3.x = 830
bd.siguiente_eje1_N3.y = 0

bd.no_eje1_N3 = MetaData()
bd.no_eje1_N3.path = 'img/dormido.gif'
bd.no_eje1_N3.w = 207
bd.no_eje1_N3.h = 112
bd.no_eje1_N3.x = 530
bd.no_eje1_N3.y = 0

bd.exe_eje1_N3 = MetaData()
bd.exe_eje1_N3.path = 'img/gano.gif'
bd.exe_eje1_N3.w = 247
bd.exe_eje1_N3.h = 149
bd.exe_eje1_N3.x = 530
bd.exe_eje1_N3.y = 0

bd.tiempo_caida_campo_eje1_N3 = MetaData()
bd.tiempo_caida_campo_eje1_N3.path = 'img/campo.png'
bd.tiempo_caida_campo_eje1_N3.w = 75
bd.tiempo_caida_campo_eje1_N3.h = 30
bd.tiempo_caida_campo_eje1_N3.x = 625
bd.tiempo_caida_campo_eje1_N3.y = 470

bd.res_campo_eje1_N3 = MetaData()
bd.res_campo_eje1_N3.path = 'img/campo.png'
bd.res_campo_eje1_N3.w = 75
bd.res_campo_eje1_N3.h = 30
bd.res_campo_eje1_N3.x = 470
bd.res_campo_eje1_N3.y = 275

bd.distancia_recorrida_eje1_N3 = MetaData()
bd.distancia_recorrida_eje1_N3.path = 'img/distanciaRecorrida.png'
bd.distancia_recorrida_eje1_N3.w = 170
bd.distancia_recorrida_eje1_N3.h = 28
bd.distancia_recorrida_eje1_N3.x = 425
bd.distancia_recorrida_eje1_N3.y = 300

bd.tiempo_caida_eje1_N3 = MetaData()
bd.tiempo_caida_eje1_N3.path = 'img/tiempoCaida.png'
bd.tiempo_caida_eje1_N3.w = 121
bd.tiempo_caida_eje1_N3.h = 29
bd.tiempo_caida_eje1_N3.x = 605
bd.tiempo_caida_eje1_N3.y = 495

bd.ldescripcion_eje1_N3 = MetaData()
bd.ldescripcion_eje1_N3.text = ''
bd.ldescripcion_eje1_N3.color = (0, 0, 0, 255)
bd.ldescripcion_eje1_N3.fname = 'DejaVu Sans Mono'
bd.ldescripcion_eje1_N3.fsize = 12
bd.ldescripcion_eje1_N3.x = 500
bd.ldescripcion_eje1_N3.y = 700

bd.ldistancia_recorrida_eje1_N3 = MetaData()
bd.ldistancia_recorrida_eje1_N3.text = ''
bd.ldistancia_recorrida_eje1_N3.color = (0, 0, 0, 255)
bd.ldistancia_recorrida_eje1_N3.fname = 'DejaVu Sans Mono'
bd.ldistancia_recorrida_eje1_N3.fsize = 12
bd.ldistancia_recorrida_eje1_N3.x = 485
bd.ldistancia_recorrida_eje1_N3.y = 288

bd.ltiempo_caida_eje1_N3 = MetaData()
bd.ltiempo_caida_eje1_N3.text = ''
bd.ltiempo_caida_eje1_N3.color = (0, 0, 0, 255)
bd.ltiempo_caida_eje1_N3.fname = 'DejaVu Sans Mono'
bd.ltiempo_caida_eje1_N3.fsize = 12
bd.ltiempo_caida_eje1_N3.x = 645
bd.ltiempo_caida_eje1_N3.y = 482

bd.zones['EJERCICIO1_N3'] = {}
bd.zones['EJERCICIO1_N3'] ['ir_niveles'] = [(bd.anterior_eje1_N3.x, bd.anterior_eje1_N3.y, bd.anterior_eje1_N3.w, bd.anterior_eje1_N3.h)]
bd.zones['EJERCICIO1_N3'] ['ir_ok'] = [(bd.ok_eje1_N3.x, bd.ok_eje1_N3.y, bd.ok_eje1_N3.w, bd.ok_eje1_N3.h)]
bd.zones['EJERCICIO1_N3'] ['ir_casa'] = [(bd.casa_eje1_N3.x, bd.casa_eje1_N3.y, bd.casa_eje1_N3.w, bd.casa_eje1_N3.h)]
bd.zones['EJERCICIO1_N3'] ['ir_actualizar'] = [(bd.actualizar_eje1_N3.x, bd.actualizar_eje1_N3.y, bd.actualizar_eje1_N3.w, bd.actualizar_eje1_N3.h)]
bd.zones['EJERCICIO1_N3'] ['ir_bombillo'] = [(bd.bombillo_eje1_N3.x, bd.bombillo_eje1_N3.y, bd.bombillo_eje1_N3.w, bd.bombillo_eje1_N3.h)]

#=====================================================================
# EJERCICIO2_N3 1024X768 
#=====================================================================

bd.anterior_eje2_N3 = MetaData()
bd.anterior_eje2_N3.path = 'img/anterior.png'
bd.anterior_eje2_N3.w = 83
bd.anterior_eje2_N3.h = 76
bd.anterior_eje2_N3.x = 0
bd.anterior_eje2_N3.y = 0

bd.pasto_eje2_N3 = MetaData()
bd.pasto_eje2_N3.path = 'img/pasto.png'
bd.pasto_eje2_N3.w = 1024
bd.pasto_eje2_N3.h = 126
bd.pasto_eje2_N3.x = 0
bd.pasto_eje2_N3.y = 0

bd.montana_eje2_N3 = MetaData()
bd.montana_eje2_N3.path = 'img/montana.png'
bd.montana_eje2_N3.w = 540
bd.montana_eje2_N3.h = 450
bd.montana_eje2_N3.x = 484
bd.montana_eje2_N3.y = 0

bd.arco_eje2_N3 = MetaData()
bd.arco_eje2_N3.path = 'img/arco.png'
bd.arco_eje2_N3.w = 818
bd.arco_eje2_N3.h = 500
bd.arco_eje2_N3.x = 0
bd.arco_eje2_N3.y = 0

bd.helicoptero_eje2_N3 = MetaData()
bd.helicoptero_eje2_N3.path = 'img/helicoptero.png'
bd.helicoptero_eje2_N3.w = 350
bd.helicoptero_eje2_N3.h = 166
bd.helicoptero_eje2_N3.x = 210
bd.helicoptero_eje2_N3.y = 360

bd.pepe_eje2_N3 = MetaData()
bd.pepe_eje2_N3.path = 'img/pepe.png'
bd.pepe_eje2_N3.w = 36
bd.pepe_eje2_N3.h = 50
bd.pepe_eje2_N3.x = 410
bd.pepe_eje2_N3.y = 415

bd.paracaidas_eje2_N3 = MetaData()
bd.paracaidas_eje2_N3.path = 'img/paracaidas.png'
bd.paracaidas_eje2_N3.w = 76
bd.paracaidas_eje2_N3.h = 93
bd.paracaidas_eje2_N3.x = 388
bd.paracaidas_eje2_N3.y = 455

bd.ok_eje2_N3 = MetaData()
bd.ok_eje2_N3.path = 'img/ok.png'
bd.ok_eje2_N3.w = 47
bd.ok_eje2_N3.h = 49
bd.ok_eje2_N3.x = 950
bd.ok_eje2_N3.y = 530

bd.actualizar_eje2_N3 = MetaData()
bd.actualizar_eje2_N3.path = 'img/actualizar.png'
bd.actualizar_eje2_N3.w = 47
bd.actualizar_eje2_N3.h = 47
bd.actualizar_eje2_N3.x = 950
bd.actualizar_eje2_N3.y = 610

bd.casa_eje2_N3 = MetaData()
bd.casa_eje2_N3.path = 'img/casa.png'
bd.casa_eje2_N3.w = 47
bd.casa_eje2_N3.h = 45
bd.casa_eje2_N3.x = 950
bd.casa_eje2_N3.y = 680

bd.bombillo_eje2_N3 = MetaData()
bd.bombillo_eje2_N3.path = 'img/bombillo.png'
bd.bombillo_eje2_N3.w = 40
bd.bombillo_eje2_N3.h = 40
bd.bombillo_eje2_N3.x = 970
bd.bombillo_eje2_N3.y = 10

bd.siguiente_eje2_N3 = MetaData()
bd.siguiente_eje2_N3.path = 'img/siguiente.png'
bd.siguiente_eje2_N3.w = 192
bd.siguiente_eje2_N3.h = 91
bd.siguiente_eje2_N3.x = 830
bd.siguiente_eje2_N3.y = 0

bd.no_eje2_N3 = MetaData()
bd.no_eje2_N3.path = 'img/dormido.gif'
bd.no_eje2_N3.w = 207
bd.no_eje2_N3.h = 112
bd.no_eje2_N3.x = 250
bd.no_eje2_N3.y = 0

bd.exe_eje2_N3 = MetaData()
bd.exe_eje2_N3.path = 'img/gano.gif'
bd.exe_eje2_N3.w = 247
bd.exe_eje2_N3.h = 149
bd.exe_eje2_N3.x = 270
bd.exe_eje2_N3.y = 0

bd.velocidad_inicial_campo_eje2_N3 = MetaData()
bd.velocidad_inicial_campo_eje2_N3.path = 'img/campo.png'
bd.velocidad_inicial_campo_eje2_N3.w = 75
bd.velocidad_inicial_campo_eje2_N3.h = 30
bd.velocidad_inicial_campo_eje2_N3.x = 35
bd.velocidad_inicial_campo_eje2_N3.y = 275

bd.altura_helicoptero_campo_eje2_N3 = MetaData()
bd.altura_helicoptero_campo_eje2_N3.path = 'img/campo.png'
bd.altura_helicoptero_campo_eje2_N3.w = 75
bd.altura_helicoptero_campo_eje2_N3.h = 30
bd.altura_helicoptero_campo_eje2_N3.x = 35
bd.altura_helicoptero_campo_eje2_N3.y = 180

bd.res_campo_eje2_N3 = MetaData()
bd.res_campo_eje2_N3.path = 'img/campo.png'
bd.res_campo_eje2_N3.w = 75
bd.res_campo_eje2_N3.h = 30
bd.res_campo_eje2_N3.x = 735
bd.res_campo_eje2_N3.y = 470

bd.velocidad_final_eje2_N3 = MetaData()
bd.velocidad_final_eje2_N3.path = 'img/velocidadF.png'
bd.velocidad_final_eje2_N3.w = 136
bd.velocidad_final_eje2_N3.h = 29
bd.velocidad_final_eje2_N3.x = 705
bd.velocidad_final_eje2_N3.y = 495

bd.velocidad_inicial_eje2_N3 = MetaData()
bd.velocidad_inicial_eje2_N3.path = 'img/velocidadI.png'
bd.velocidad_inicial_eje2_N3.w = 145
bd.velocidad_inicial_eje2_N3.h = 28
bd.velocidad_inicial_eje2_N3.x = 5
bd.velocidad_inicial_eje2_N3.y = 300

bd.altura_helicoptero_eje2_N3 = MetaData()
bd.altura_helicoptero_eje2_N3.path = 'img/alturaH.png'
bd.altura_helicoptero_eje2_N3.w = 165
bd.altura_helicoptero_eje2_N3.h = 31
bd.altura_helicoptero_eje2_N3.x = 5
bd.altura_helicoptero_eje2_N3.y = 205

bd.ldescripcion_eje2_N3 = MetaData()
bd.ldescripcion_eje2_N3.text = ''
bd.ldescripcion_eje2_N3.color = (0, 0, 0, 255)
bd.ldescripcion_eje2_N3.fname = 'DejaVu Sans Mono'
bd.ldescripcion_eje2_N3.fsize = 12
bd.ldescripcion_eje2_N3.x = 500
bd.ldescripcion_eje2_N3.y = 700

bd.lvelocidad_inicial_eje2_N3 = MetaData()
bd.lvelocidad_inicial_eje2_N3.text = ''
bd.lvelocidad_inicial_eje2_N3.color = (0, 0, 0, 255)
bd.lvelocidad_inicial_eje2_N3.fname = 'DejaVu Sans Mono'
bd.lvelocidad_inicial_eje2_N3.fsize = 12
bd.lvelocidad_inicial_eje2_N3.x = 65
bd.lvelocidad_inicial_eje2_N3.y = 288

bd.lvelocidad_final_eje2_N3 = MetaData()
bd.lvelocidad_final_eje2_N3.text = ''
bd.lvelocidad_final_eje2_N3.color = (0, 0, 0, 255)
bd.lvelocidad_final_eje2_N3.fname = 'DejaVu Sans Mono'
bd.lvelocidad_final_eje2_N3.fsize = 12
bd.lvelocidad_final_eje2_N3.x = 745
bd.lvelocidad_final_eje2_N3.y = 482

bd.laltura_helicoptero_eje2_N3 = MetaData()
bd.laltura_helicoptero_eje2_N3.text = ''
bd.laltura_helicoptero_eje2_N3.color = (0, 0, 0, 255)
bd.laltura_helicoptero_eje2_N3.fname = 'DejaVu Sans Mono'
bd.laltura_helicoptero_eje2_N3.fsize = 12
bd.laltura_helicoptero_eje2_N3.x = 10
bd.laltura_helicoptero_eje2_N3.y = 230


bd.zones['EJERCICIO2_N3'] = {}
bd.zones['EJERCICIO2_N3'] ['ir_niveles'] = [(bd.anterior_eje1_N3.x, bd.anterior_eje1_N3.y, bd.anterior_eje1_N3.w, bd.anterior_eje1_N3.h)]
bd.zones['EJERCICIO2_N3'] ['ir_ok'] = [(bd.ok_eje1_N3.x, bd.ok_eje1_N3.y, bd.ok_eje1_N3.w, bd.ok_eje1_N3.h)]
bd.zones['EJERCICIO2_N3'] ['ir_casa'] = [(bd.casa_eje1_N3.x, bd.casa_eje1_N3.y, bd.casa_eje1_N3.w, bd.casa_eje1_N3.h)]
bd.zones['EJERCICIO2_N3'] ['ir_actualizar'] = [(bd.actualizar_eje1_N3.x, bd.actualizar_eje1_N3.y, bd.actualizar_eje1_N3.w, bd.actualizar_eje1_N3.h)]
bd.zones['EJERCICIO2_N3'] ['ir_bombillo'] = [(bd.bombillo_eje1_N3.x, bd.bombillo_eje1_N3.y, bd.bombillo_eje1_N3.w, bd.bombillo_eje1_N3.h)]

#=====================================================================
# EJERCICIO3_N3 1024X768 
#=====================================================================

bd.anterior_eje3_N3 = MetaData()
bd.anterior_eje3_N3.path = 'img/anterior.png'
bd.anterior_eje3_N3.w = 47
bd.anterior_eje3_N3.h = 43
bd.anterior_eje3_N3.x = 950
bd.anterior_eje3_N3.y = 450

bd.mar_eje3_N3 = MetaData()
bd.mar_eje3_N3.path = 'img/mar.png'
bd.mar_eje3_N3.w = 1024
bd.mar_eje3_N3.h = 225
bd.mar_eje3_N3.x = 0
bd.mar_eje3_N3.y = 0

bd.balon_eje3_N3 = MetaData()
bd.balon_eje3_N3.path = 'img/balon.png'
bd.balon_eje3_N3.w = 75
bd.balon_eje3_N3.h = 75
bd.balon_eje3_N3.x = 750
bd.balon_eje3_N3.y = 50

bd.nina_eje3_N3 = MetaData()
bd.nina_eje3_N3.path = 'img/nina.png'
bd.nina_eje3_N3.w = 265
bd.nina_eje3_N3.h = 190
bd.nina_eje3_N3.x = 759
bd.nina_eje3_N3.y = 35

bd.sol_eje3_N3 = MetaData()
bd.sol_eje3_N3.path = 'img/sol.png'
bd.sol_eje3_N3.w = 220
bd.sol_eje3_N3.h = 220
bd.sol_eje3_N3.x = 150
bd.sol_eje3_N3.y = 350

bd.nina_lanzando_eje3_N3 = MetaData()
bd.nina_lanzando_eje3_N3.path = 'img/ninalanzandopelota2.gif'
bd.nina_lanzando_eje3_N3.w = 280
bd.nina_lanzando_eje3_N3.h = 280
bd.nina_lanzando_eje3_N3.x = 730
bd.nina_lanzando_eje3_N3.y = 0

bd.ok_eje3_N3 = MetaData()
bd.ok_eje3_N3.path = 'img/ok.png'
bd.ok_eje3_N3.w = 47
bd.ok_eje3_N3.h = 49
bd.ok_eje3_N3.x = 950
bd.ok_eje3_N3.y = 530

bd.actualizar_eje3_N3 = MetaData()
bd.actualizar_eje3_N3.path = 'img/actualizar.png'
bd.actualizar_eje3_N3.w = 47
bd.actualizar_eje3_N3.h = 47
bd.actualizar_eje3_N3.x = 950
bd.actualizar_eje3_N3.y = 610

bd.casa_eje3_N3 = MetaData()
bd.casa_eje3_N3.path = 'img/casa.png'
bd.casa_eje3_N3.w = 47
bd.casa_eje3_N3.h = 45
bd.casa_eje3_N3.x = 950
bd.casa_eje3_N3.y = 680

bd.bombillo_eje3_N3 = MetaData()
bd.bombillo_eje3_N3.path = 'img/bombillo.png'
bd.bombillo_eje3_N3.w = 40
bd.bombillo_eje3_N3.h = 40
bd.bombillo_eje3_N3.x = 970
bd.bombillo_eje3_N3.y = 120

bd.siguiente_eje3_N3 = MetaData()
bd.siguiente_eje3_N3.path = 'img/siguiente.png'
bd.siguiente_eje3_N3.w = 150
bd.siguiente_eje3_N3.h = 71
bd.siguiente_eje3_N3.x = 640
bd.siguiente_eje3_N3.y = 0

bd.no_eje3_N3 = MetaData()
bd.no_eje3_N3.path = 'img/dormido.gif'
bd.no_eje3_N3.w = 162
bd.no_eje3_N3.h = 87
bd.no_eje3_N3.x = 450
bd.no_eje3_N3.y = 0

bd.exe_eje3_N3 = MetaData()
bd.exe_eje3_N3.path = 'img/gano.gif'
bd.exe_eje3_N3.w = 193
bd.exe_eje3_N3.h = 116
bd.exe_eje3_N3.x = 450
bd.exe_eje3_N3.y = 0

bd.velocidad_pelota_campo_eje3_N3 = MetaData()
bd.velocidad_pelota_campo_eje3_N3.path = 'img/campo.png'
bd.velocidad_pelota_campo_eje3_N3.w = 75
bd.velocidad_pelota_campo_eje3_N3.h = 30
bd.velocidad_pelota_campo_eje3_N3.x = 300
bd.velocidad_pelota_campo_eje3_N3.y = 180

bd.res_campo_eje3_N3 = MetaData()
bd.res_campo_eje3_N3.path = 'img/campo.png'
bd.res_campo_eje3_N3.w = 75
bd.res_campo_eje3_N3.h = 30
bd.res_campo_eje3_N3.x = 525
bd.res_campo_eje3_N3.y = 380

bd.altura_maxima_eje3_N3 = MetaData()
bd.altura_maxima_eje3_N3.path = 'img/alturaMaxima.png'
bd.altura_maxima_eje3_N3.w = 131
bd.altura_maxima_eje3_N3.h = 28
bd.altura_maxima_eje3_N3.x = 500
bd.altura_maxima_eje3_N3.y = 400

bd.velocidad_pelota_eje3_N3 = MetaData()
bd.velocidad_pelota_eje3_N3.path = 'img/velocidadPelota.png'
bd.velocidad_pelota_eje3_N3.w = 145
bd.velocidad_pelota_eje3_N3.h = 29
bd.velocidad_pelota_eje3_N3.x = 265
bd.velocidad_pelota_eje3_N3.y = 200

bd.ldescripcion_eje3_N3 = MetaData()
bd.ldescripcion_eje3_N3.text = ''
bd.ldescripcion_eje3_N3.color = (0, 0, 0, 255)
bd.ldescripcion_eje3_N3.fname = 'DejaVu Sans Mono'
bd.ldescripcion_eje3_N3.fsize = 12
bd.ldescripcion_eje3_N3.x = 500
bd.ldescripcion_eje3_N3.y = 700

bd.lvelocidad_pelota_eje3_N3 = MetaData()
bd.lvelocidad_pelota_eje3_N3.text = ''
bd.lvelocidad_pelota_eje3_N3.color = (0, 0, 0, 255)
bd.lvelocidad_pelota_eje3_N3.fname = 'DejaVu Sans Mono'
bd.lvelocidad_pelota_eje3_N3.fsize = 12
bd.lvelocidad_pelota_eje3_N3.x = 300
bd.lvelocidad_pelota_eje3_N3.y = 180

bd.laltura_maxima_eje3_N3 = MetaData()
bd.laltura_maxima_eje3_N3.text = ''
bd.laltura_maxima_eje3_N3.color = (0, 0, 0, 255)
bd.laltura_maxima_eje3_N3.fname = 'DejaVu Sans Mono'
bd.laltura_maxima_eje3_N3.fsize = 12
bd.laltura_maxima_eje3_N3.x = 520
bd.laltura_maxima_eje3_N3.y = 380


bd.zones['EJERCICIO3_N3'] = {}
bd.zones['EJERCICIO3_N3'] ['ir_niveles'] = [(bd.anterior_eje3_N3.x, bd.anterior_eje3_N3.y, bd.anterior_eje3_N3.w, bd.anterior_eje3_N3.h)]
bd.zones['EJERCICIO3_N3'] ['ir_ok'] = [(bd.ok_eje3_N3.x, bd.ok_eje3_N3.y, ld.ok_eje3_N3.w, bd.ok_eje3_N3.h)]
bd.zones['EJERCICIO3_N3'] ['ir_casa'] = [(bd.casa_eje3_N3.x, bd.casa_eje3_N3.y, bd.casa_eje3_N3.w, bd.casa_eje3_N3.h)]
bd.zones['EJERCICIO3_N3'] ['ir_actualizar'] = [(bd.actualizar_eje3_N3.x, bd.actualizar_eje3_N3.y, bd.actualizar_eje3_N3.w, bd.actualizar_eje3_N3.h)]
bd.zones['EJERCICIO3_N3'] ['ir_bombillo'] = [(bd.bombillo_eje3_N3.x, bd.bombillo_eje3_N3.y, bd.bombillo_eje3_N3.w, bd.bombillo_eje3_N3.h)]

#=====================================================================
# REGISTRO DE USUARIO 1366X768
#=====================================================================

hd.fondo = MetaData()
hd.fondo.path = 'img/fondo.png'
hd.fondo.w = 1366
hd.fondo.h = 768
hd.fondo.x = 0
hd.fondo.y = 0

hd.registro = MetaData()
hd.registro.path = 'img/registro.png'
hd.registro.w = 575
hd.registro.h = 90
hd.registro.x = 395
hd.registro.y = 640

hd.nombre = MetaData()
hd.nombre.path = 'img/nombre.png'
hd.nombre.w = 209
hd.nombre.h = 63
hd.nombre.x = 10
hd.nombre.y = 540

hd.apellido = MetaData()
hd.apellido.path = 'img/apellido.png'
hd.apellido.w = 217
hd.apellido.h = 70
hd.apellido.x = 10
hd.apellido.y = 465

hd.correo = MetaData()
hd.correo.path = 'img/correo.png'
hd.correo.w = 184
hd.correo.h = 62
hd.correo.x = 10
hd.correo.y = 400

hd.clave = MetaData()
hd.clave.path = 'img/clave.png'
hd.clave.w = 158
hd.clave.h = 63
hd.clave.x = 10
hd.clave.y = 330

hd.verificar = MetaData()
hd.verificar.path = 'img/verificar.png'
hd.verificar.w = 230
hd.verificar.h = 62
hd.verificar.x = 10
hd.verificar.y = 260

hd.grado = MetaData()
hd.grado.path = 'img/grado.png'
hd.grado.w = 171
hd.grado.h = 63
hd.grado.x = 10
hd.grado.y = 190

hd.rol = MetaData()
hd.rol.path = 'img/rol.png'
hd.rol.w = 112
hd.rol.h = 63
hd.rol.x = 10
hd.rol.y = 120

hd.guardar = MetaData()
hd.guardar.path = 'img/guardar.png'
hd.guardar.w = 256
hd.guardar.h = 114
hd.guardar.x = 1090
hd.guardar.y = 0

hd.anterior = MetaData()
hd.anterior.path = 'img/anterior.png'
hd.anterior.w = 110
hd.anterior.h = 101
hd.anterior.x = 10
hd.anterior.y = 10

hd.cnombre = MetaData()
hd.cnombre.path = 'img/cuadro.png'
hd.cnombre.w = 1126
hd.cnombre.h = 80
hd.cnombre.x = 230
hd.cnombre.y = 520

hd.capellido = MetaData()
hd.capellido.path = 'img/cuadro.png'
hd.capellido.w = 1126
hd.capellido.h = 80
hd.capellido.x = 230
hd.capellido.y = 450

hd.ccorreo = MetaData()
hd.ccorreo.path = 'img/cuadro.png'
hd.ccorreo.w = 1126
hd.ccorreo.h = 80
hd.ccorreo.x = 230
hd.ccorreo.y = 380

hd.cclave = MetaData()
hd.cclave.path = 'img/cuadro.png'
hd.cclave.w = 1126
hd.cclave.h = 80
hd.cclave.x = 230
hd.cclave.y = 310

hd.cverificar = MetaData()
hd.cverificar.path = 'img/cuadro.png'
hd.cverificar.w = 1126
hd.cverificar.h = 80
hd.cverificar.x = 230
hd.cverificar.y = 240

hd.cgrado = MetaData()
hd.cgrado.path = 'img/cuadro.png'
hd.cgrado.w = 1126
hd.cgrado.h = 80
hd.cgrado.x = 230
hd.cgrado.y = 170

hd.crol = MetaData()
hd.crol.path = 'img/cuadro.png'
hd.crol.w = 1126
hd.crol.h = 80
hd.crol.x = 230
hd.crol.y = 100

hd.flecha = MetaData()
hd.flecha.path = 'img/flecha.png'
hd.flecha.w = 30
hd.flecha.h = 22
hd.flecha.x = 1290
hd.flecha.y = 138

hd.lnombre = MetaData()
hd.lnombre.text = ''
hd.lnombre.color = (0, 0, 0, 255)
hd.lnombre.fname = 'DejaVu Sans Mono'
hd.lnombre.fsize = 16
hd.lnombre.x = 260
hd.lnombre.y = 560

hd.lapellido = MetaData()
hd.lapellido.text = ''
hd.lapellido.color = (0, 0, 0, 255)
hd.lapellido.fname = 'DejaVu Sans Mono'
hd.lapellido.fsize = 16
hd.lapellido.x = 260
hd.lapellido.y = 490

hd.lcorreo = MetaData()
hd.lcorreo.text = ''
hd.lcorreo.color = (0, 0, 0, 255)
hd.lcorreo.fname = 'DejaVu Sans Mono'
hd.lcorreo.fsize = 16
hd.lcorreo.x = 260
hd.lcorreo.y = 420

hd.lclave = MetaData()
hd.lclave.text = ''
hd.lclave.color = (0, 0, 0, 255)
hd.lclave.fname = 'DejaVu Sans Mono'
hd.lclave.fsize = 16
hd.lclave.x = 260
hd.lclave.y = 350

hd.lverificar = MetaData()
hd.lverificar.text = ''
hd.lverificar.color = (0, 0, 0, 255)
hd.lverificar.fname = 'DejaVu Sans Mono'
hd.lverificar.fsize = 16
hd.lverificar.x = 260
hd.lverificar.y = 280

hd.lgrado = MetaData()
hd.lgrado.text = ''
hd.lgrado.color = (0, 0, 0, 255)
hd.lgrado.fname = 'DejaVu Sans Mono'
hd.lgrado.fsize = 16
hd.lgrado.x = 260
hd.lgrado.y = 210

hd.lrol = MetaData()
hd.lrol.text = '                      >>  DOCENTE   <<'
hd.lrol.color = (17, 33, 98, 255)
hd.lrol.fname = 'DejaVu Sans Mono'
hd.lrol.fsize = 16
hd.lrol.x = 400
hd.lrol.y = 142

hd.advertencia1 = MetaData()
hd.advertencia1.path = 'img/advertencia1.png'
hd.advertencia1.w = 628
hd.advertencia1.h = 353
hd.advertencia1.x = 400
hd.advertencia1.y = 200

hd.advertencia2 = MetaData()
hd.advertencia2.path = 'img/advertencia2.png'
hd.advertencia2.w = 628
hd.advertencia2.h = 353
hd.advertencia2.x = 400
hd.advertencia2.y = 200

hd.pointer = MetaData()
hd.pointer.path = 'img/pointer.png'
hd.pointer.w = 1094
hd.pointer.h = 48
hd.pointer.x = 236
hd.pointer.y = 546
hd.pointer.ylist = ['lnombre', 'lapellido', 'lcorreo', 'lclave', 'lverificar', 'lgrado', 'lrol']
hd.pointer.ypos = {'cnombre': 546, 'capellido': 476, 'ccorreo': 406, 'cclave': 336, 'cverificar': 266, 'cgrado': 196, 'crol': 126}

hd.zones = {}
hd.zones['REGISTRO'] = {}
hd.zones['REGISTRO']['cnombre'] = [(hd.cnombre.x, hd.cnombre.y, hd.cnombre.w, hd.cnombre.h)]
hd.zones['REGISTRO']['capellido'] = [(hd.capellido.x, hd.capellido.y, hd.capellido.w, hd.capellido.h)]
hd.zones['REGISTRO']['ccorreo'] = [(hd.ccorreo.x, hd.ccorreo.y, hd.ccorreo.w, hd.ccorreo.h)]
hd.zones['REGISTRO']['cclave'] = [(hd.cclave.x, hd.cclave.y, hd.cclave.w, hd.cclave.h)]
hd.zones['REGISTRO']['cverificar'] = [(hd.cverificar.x, hd.cverificar.y, hd.cverificar.w, hd.cverificar.h)]
hd.zones['REGISTRO']['cgrado'] = [(hd.cgrado.x, hd.cgrado.y, hd.cgrado.w, hd.cgrado.h)]
hd.zones['REGISTRO']['crol'] = [(hd.crol.x, hd.crol.y, hd.crol.w, hd.crol.h)]
hd.zones['REGISTRO']['ir_principal2'] = [(10, 10, 108, 102)]
hd.zones['REGISTRO']['guardar'] = [(hd.guardar.x, hd.guardar.y, hd.guardar.w, hd.guardar.h)]
hd.zones['REGISTRO']['cerrar_advertencia1'] = [(402, 432, 120, 120)]
hd.zones['REGISTRO']['cerrar_advertencia2'] = [(402, 432, 120, 120)]

#=====================================================================
# MENU 1366X768
#=====================================================================

hd.menu1= MetaData()
hd.menu1.path = 'img/menu1.png'
hd.menu1.w = 300
hd.menu1.h = 90
hd.menu1.x = 540
hd.menu1.y = 655

hd.logo1 = MetaData()
hd.logo1.path = 'img/logo.png'
hd.logo1.w = 128
hd.logo1.h = 122
hd.logo1.x = 1230
hd.logo1.y = 645

hd.menu2 = MetaData()
hd.menu2.path = 'img/menu2.png'
hd.menu2.w = 565
hd.menu2.h = 565
hd.menu2.x = 370
hd.menu2.y = 50

hd.zones['MENU'] = {}
hd.zones['MENU']['ir_ajustes'] = [(525, 420, 160, 160)]
hd.zones['MENU']['ir_principal'] = [(605, 100, 220, 220)]
hd.zones['MENU']['ir_ayuda'] = [(820, 380, 70, 70)]
hd.zones['MENU']['ir_cerrar'] = [(415, 80, 105, 110)]

#=====================================================================
# PRINCIPAL 1366X768
#=====================================================================

hd.iniciar = MetaData()
hd.iniciar.path = 'img/iniciar.png'
hd.iniciar.w = 335
hd.iniciar.h = 81
hd.iniciar.x = 510
hd.iniciar.y = 655

hd.ingresar = MetaData()
hd.ingresar.path = 'img/ingresar.png'
hd.ingresar.w = 209
hd.ingresar.h = 197
hd.ingresar.x = 590
hd.ingresar.y = 400

hd.nuevo = MetaData()
hd.nuevo.path = 'img/nuevo.png'
hd.nuevo.w = 336
hd.nuevo.h = 190
hd.nuevo.x = 550
hd.nuevo.y = 120

hd.anterior5 = MetaData()
hd.anterior5.path = 'img/anterior.png'
hd.anterior5.w = 110
hd.anterior5.h = 101
hd.anterior5.x = 10
hd.anterior5.y = 10

hd.zones['PRINCIPAL'] = {}
hd.zones['PRINCIPAL'] ['ir_menu'] = [(10, 10, 110, 101)]
hd.zones['PRINCIPAL'] ['ir_login'] = [(590, 400, 192, 192)]
hd.zones['PRINCIPAL'] ['ir_registro'] = [(550, 120, 320, 185)]

#=====================================================================
# AJUSTES 1366X768
#=====================================================================

hd.ajustes = MetaData()
hd.ajustes.path = 'img/ajustes.png'
hd.ajustes.w = 320
hd.ajustes.h = 95
hd.ajustes.x = 530
hd.ajustes.y = 655

hd.sonido1 = MetaData()
hd.sonido1.path = 'img/sonido1.png'
hd.sonido1.w = 200
hd.sonido1.h = 200
hd.sonido1.x = 200
hd.sonido1.y = 400

hd.sonido2 = MetaData()
hd.sonido2.path = 'img/sonido2.png'
hd.sonido2.w = 200
hd.sonido2.h = 200
hd.sonido2.x = 200
hd.sonido2.y = 110

hd.pantalla1 = MetaData()
hd.pantalla1.path = 'img/pantalla1.png'
hd.pantalla1.w = 260
hd.pantalla1.h = 208
hd.pantalla1.x = 950
hd.pantalla1.y = 390

hd.pantalla2 = MetaData()
hd.pantalla2.path = 'img/pantalla2.png'
hd.pantalla2.w = 260
hd.pantalla2.h = 208
hd.pantalla2.x = 950
hd.pantalla2.y = 90

hd.anterior2 = MetaData()
hd.anterior2.path = 'img/anterior.png'
hd.anterior2.w = 110
hd.anterior2.h = 101
hd.anterior2.x = 10
hd.anterior2.y = 10

hd.zones['AJUSTES'] = {}
hd.zones['AJUSTES'] ['ir_menu'] = [(10, 10, 110, 101)]
hd.zones['AJUSTES'] ['pantalla1'] = [(hd.pantalla1.x, hd.pantalla1.y, hd.pantalla1.w, hd.pantalla1.h)]
hd.zones['AJUSTES'] ['pantalla2'] = [(hd.pantalla2.x, hd.pantalla2.y, hd.pantalla2.w, hd.pantalla2.h)]

#=====================================================================
# LOGIN 1366X768
#=====================================================================

hd.login = MetaData()
hd.login.path = 'img/login.png'
hd.login.w = 535
hd.login.h = 80
hd.login.x = 420
hd.login.y = 665

hd.correo2 = MetaData()
hd.correo2.path = 'img/correo2.png'
hd.correo2.w = 268
hd.correo2.h = 66
hd.correo2.x = 200
hd.correo2.y = 460

hd.clave2 = MetaData()
hd.clave2.path = 'img/clave2.png'
hd.clave2.w = 228
hd.clave2.h = 70
hd.clave2.x = 210
hd.clave2.y = 250

hd.lcorreo2 = MetaData()
hd.lcorreo2.text = ''
hd.lcorreo2.color = (0, 0, 0, 255)
hd.lcorreo2.fname = 'DejaVu Sans Mono'
hd.lcorreo2.fsize = 16
hd.lcorreo2.x = 490
hd.lcorreo2.y = 482

hd.lclave2 = MetaData()
hd.lclave2.text = ''
hd.lclave2.color = (0, 0, 0, 255)
hd.lclave2.fname = 'DejaVu Sans Mono'
hd.lclave2.fsize = 16
hd.lclave2.x = 490
hd.lclave2.y = 270

hd.cucorreo2 = MetaData()
hd.cucorreo2.path = 'img/cuadrito.png'
hd.cucorreo2.w = 700
hd.cucorreo2.h = 80
hd.cucorreo2.x = 460
hd.cucorreo2.y = 440

hd.cuclave2 = MetaData()
hd.cuclave2.path = 'img/cuadrito.png'
hd.cuclave2.w = 700
hd.cuclave2.h = 80
hd.cuclave2.x = 460
hd.cuclave2.y = 230

hd.anterior3 = MetaData()
hd.anterior3.path = 'img/anterior.png'
hd.anterior3.w = 110
hd.anterior3.h = 101
hd.anterior3.x = 10
hd.anterior3.y = 10

hd.enter = MetaData()
hd.enter.path = 'img/enter.png'
hd.enter.w = 236
hd.enter.h = 105
hd.enter.x = 915
hd.enter.y = 80

hd.login_adv1 = MetaData()
hd.login_adv1.path = 'img/login_adv1.png'
hd.login_adv1.w = 628
hd.login_adv1.h = 353
hd.login_adv1.x = 400
hd.login_adv1.y = 200

hd.pointersito = MetaData()
hd.pointersito.path = 'img/pointersito.png'
hd.pointersito.w = 670
hd.pointersito.h = 48
hd.pointersito.x = 465
hd.pointersito.y = 466
hd.pointersito.ylist = ['lcorreo2', 'lclave2']
hd.pointersito.ypos = {'cucorreo2': 466, 'cuclave2': 256}

hd.zones['LOGIN'] = {}
hd.zones['LOGIN'] ['ir_principal2'] = [(10, 10, 108, 102)]
hd.zones['LOGIN'] ['cucorreo2'] = [(hd.cucorreo2.x, hd.cucorreo2.y, hd.cucorreo2.w, hd.cucorreo2.h)]
hd.zones['LOGIN'] ['cuclave2'] = [(hd.cuclave2.x, hd.cuclave2.y, hd.cuclave2.w, hd.cuclave2.h)]
hd.zones['LOGIN'] ['enter'] = [(hd.enter.x, hd.enter.y, hd.enter.w, hd.enter.h)]
hd.zones['LOGIN'] ['cerrar_login_adv1'] = [(402, 432, 120, 120)]
#=====================================================================
# AYUDA 1366X768
#=====================================================================

hd.ayuda = MetaData()
hd.ayuda.path = 'img/ayuda.png'
hd.ayuda.w = 844
hd.ayuda.h = 89
hd.ayuda.x = 270
hd.ayuda.y = 655

hd.tabla = MetaData()
hd.tabla.path = 'img/tabla.png'
hd.tabla.w = 800
hd.tabla.h = 550
hd.tabla.x = 90
hd.tabla.y = 80

hd.idea = MetaData()
hd.idea.path = 'img/idea.gif'
hd.idea.w = 228
hd.idea.h = 350
hd.idea.x = 1050
hd.idea.y = 180

hd.piso = MetaData()
hd.piso.path = 'img/piso.png'
hd.piso.w = 200
hd.piso.h = 100
hd.piso.x = 1040
hd.piso.y = 145

hd.anterior4 = MetaData()
hd.anterior4.path = 'img/anterior.png'
hd.anterior4.w = 110
hd.anterior4.h = 101
hd.anterior4.x = 10
hd.anterior4.y = 10

hd.zones['AYUDA'] = {}
hd.zones['AYUDA'] ['ir_menu'] = [(10, 10, 110, 101)]

#=====================================================================
# NIVELES 1366X768
#=====================================================================

hd.niveles = MetaData()
hd.niveles.path = 'img/niveles.png'
hd.niveles.w = 435
hd.niveles.h = 57
hd.niveles.x = 450
hd.niveles.y = 675

hd.rectilineo = MetaData()
hd.rectilineo.path = 'img/rectilineo.png'
hd.rectilineo.w = 255
hd.rectilineo.h = 95
hd.rectilineo.x = 100
hd.rectilineo.y = 540

hd.curvilineo = MetaData()
hd.curvilineo.path = 'img/curvilineo.png'
hd.curvilineo.w = 255
hd.curvilineo.h = 95
hd.curvilineo.x = 565
hd.curvilineo.y = 540

hd.especial = MetaData()
hd.especial.path = 'img/especial.png'
hd.especial.w = 255
hd.especial.h = 95
hd.especial.x = 1025
hd.especial.y = 540

hd.nivel1 = MetaData()
hd.nivel1.path = 'img/nivel1.png'
hd.nivel1.w = 400
hd.nivel1.h = 225
hd.nivel1.x = 20
hd.nivel1.y = 310

hd.nivel2 = MetaData()
hd.nivel2.path = 'img/nivel1.png'
hd.nivel2.w = 400
hd.nivel2.h = 225
hd.nivel2.x = 485
hd.nivel2.y = 310

hd.nivel3 = MetaData()
hd.nivel3.path = 'img/nivel1.png'
hd.nivel3.w = 400
hd.nivel3.h = 225
hd.nivel3.x = 946
hd.nivel3.y = 310

hd.des_nivel1 = MetaData()
hd.des_nivel1.path = 'img/des_nivel1.png'
hd.des_nivel1.w = 382
hd.des_nivel1.h = 174
hd.des_nivel1.x = 30
hd.des_nivel1.y = 110

hd.des_nivel2 = MetaData()
hd.des_nivel2.path = 'img/des_nivel2.png'
hd.des_nivel2.w = 444
hd.des_nivel2.h = 176
hd.des_nivel2.x = 495
hd.des_nivel2.y = 105

hd.des_nivel3 = MetaData()
hd.des_nivel3.path = 'img/des_nivel3.png'
hd.des_nivel3.w = 362
hd.des_nivel3.h = 174
hd.des_nivel3.x = 966
hd.des_nivel3.y = 105

hd.anterior_niveles = MetaData()
hd.anterior_niveles.path = 'img/anterior.png'
hd.anterior_niveles.w = 110
hd.anterior_niveles.h = 101
hd.anterior_niveles.x = 10
hd.anterior_niveles.y = 10

hd.medalla_nivel1 = MetaData()
hd.medalla_nivel1.path = 'img/medalla.png'
hd.medalla_nivel1.w = 100
hd.medalla_nivel1.h = 150
hd.medalla_nivel1.x = 315
hd.medalla_nivel1.y = 250

hd.medalla_nivel2 = MetaData()
hd.medalla_nivel2.path = 'img/medalla.png'
hd.medalla_nivel2.w = 100
hd.medalla_nivel2.h = 150
hd.medalla_nivel2.x = 780
hd.medalla_nivel2.y = 250

hd.medalla_nivel3 = MetaData()
hd.medalla_nivel3.path = 'img/medalla.png'
hd.medalla_nivel3.w = 100
hd.medalla_nivel3.h = 150
hd.medalla_nivel3.x = 1240
hd.medalla_nivel3.y = 250

hd.zones['NIVELES'] = {}
hd.zones['NIVELES'] ['ir_nivel1'] = [(hd.nivel1.x, hd.nivel1.y, hd.nivel1.w, hd.nivel1.h)]
hd.zones['NIVELES'] ['ir_nivel2'] = [(hd.nivel2.x, hd.nivel1.y, hd.nivel2.w, hd.nivel2.h)]
hd.zones['NIVELES'] ['ir_nivel3'] = [(hd.nivel3.x, hd.nivel3.y, hd.nivel3.w, hd.nivel3.h)]
hd.zones['NIVELES'] ['ir_casa'] = [(hd.anterior_niveles.x, hd.anterior_niveles.y, hd.anterior_niveles.w, hd.anterior_niveles.h)]

#=====================================================================
#NIVEL1 1366X768
#=====================================================================

hd.carro1 = MetaData()
hd.carro1.path = 'img/carro1.png'
hd.carro1.w = 140
hd.carro1.h = 70
hd.carro1.x = 12
hd.carro1.y = 160

hd.carro2 = MetaData()
hd.carro2.path = 'img/carro2.png'
hd.carro2.w = 140
hd.carro2.h = 70
hd.carro2.x = 1215
hd.carro2.y = 160

hd.carretera = MetaData()
hd.carretera.path = 'img/carretera.jpg'
hd.carretera.w = 1366
hd.carretera.h = 50
hd.carretera.x = 0
hd.carretera.y = 150

hd.colegio = MetaData()
hd.colegio.path = 'img/colegio.png'
hd.colegio.w = 400
hd.colegio.h = 200
hd.colegio.x = 0
hd.colegio.y = 199

hd.parque = MetaData()
hd.parque.path = 'img/parque.png'
hd.parque.w = 450
hd.parque.h = 250
hd.parque.x = 916
hd.parque.y = 200

hd.casa = MetaData()
hd.casa.path = 'img/casa.png'
hd.casa.w = 60
hd.casa.h = 57
hd.casa.x = 1250
hd.casa.y = 660

hd.ok = MetaData()
hd.ok.path = 'img/ok.png'
hd.ok.w = 61
hd.ok.h = 63
hd.ok.x = 1250
hd.ok.y = 480

hd.actualizar = MetaData()
hd.actualizar.path = 'img/actualizar.png'
hd.actualizar.w = 63
hd.actualizar.h = 63
hd.actualizar.x = 1250
hd.actualizar.y = 570

hd.bombillo= MetaData()
hd.bombillo.path = 'img/bombillo.png'
hd.bombillo.w = 53
hd.bombillo.h = 53
hd.bombillo.x = 1290
hd.bombillo.y = 20

hd.anterior6 = MetaData()
hd.anterior6.path = 'img/anterior.png'
hd.anterior6.w = 110
hd.anterior6.h = 101
hd.anterior6.x = 10
hd.anterior6.y = 10

hd.dis_campo = MetaData()
hd.dis_campo.path = 'img/campo.png'
hd.dis_campo.w = 100
hd.dis_campo.h = 40
hd.dis_campo.x = 635
hd.dis_campo.y = 50

hd.car1_campo = MetaData()
hd.car1_campo.path = 'img/campo.png'
hd.car1_campo.w = 100
hd.car1_campo.h = 40
hd.car1_campo.x = 170
hd.car1_campo.y = 50

hd.car2_campo = MetaData()
hd.car2_campo.path = 'img/campo.png'
hd.car2_campo.w = 100
hd.car2_campo.h = 40
hd.car2_campo.x = 1120
hd.car2_campo.y = 50

hd.vel_car1_campo = MetaData()
hd.vel_car1_campo.path = 'img/campo.png'
hd.vel_car1_campo.w = 100
hd.vel_car1_campo.h = 40
hd.vel_car1_campo.x = 435
hd.vel_car1_campo.y = 250

hd.vel_car2_campo = MetaData()
hd.vel_car2_campo.path = 'img/campo.png'
hd.vel_car2_campo.w = 100
hd.vel_car2_campo.h = 40
hd.vel_car2_campo.x = 805
hd.vel_car2_campo.y = 250

hd.res_campo = MetaData()
hd.res_campo.path = 'img/campo.png'
hd.res_campo.w = 100
hd.res_campo.h = 40
hd.res_campo.x = 635
hd.res_campo.y = 500

hd.distancia = MetaData()
hd.distancia.path = 'img/distancia.png'
hd.distancia.w = 167
hd.distancia.h = 39
hd.distancia.x = 600
hd.distancia.y = 20

hd.distanciaA_u = MetaData()
hd.distanciaA_u.path = 'img/distanciaA_u.png'
hd.distanciaA_u.w = 176
hd.distanciaA_u.h = 39
hd.distanciaA_u.x = 140
hd.distanciaA_u.y = 20

hd.distanciaB_v = MetaData()
hd.distanciaB_v.path = 'img/distanciaB_v.png'
hd.distanciaB_v.w = 173
hd.distanciaB_v.h = 41
hd.distanciaB_v.x = 1090
hd.distanciaB_v.y = 20

hd.velocidadU = MetaData()
hd.velocidadU.path = 'img/velocidadU.png'
hd.velocidadU.w = 133
hd.velocidadU.h = 39
hd.velocidadU.x = 420
hd.velocidadU.y = 280

hd.velocidadV = MetaData()
hd.velocidadV.path = 'img/velocidadV.png'
hd.velocidadV.w = 130
hd.velocidadV.h = 39
hd.velocidadV.x = 790
hd.velocidadV.y = 280

hd.resultado = MetaData()
hd.resultado.path = 'img/tiempo.png'
hd.resultado.w = 92
hd.resultado.h = 42
hd.resultado.x = 640
hd.resultado.y = 530

hd.mano = MetaData()
hd.mano.path = 'img/mano.png'
hd.mano.w = 41
hd.mano.h = 48
hd.mano.x = 660
hd.mano.y = 100

hd.no = MetaData()
hd.no.path = 'img/no.gif'
hd.no.w = 276
hd.no.h = 149
hd.no.x = 560
hd.no.y = 250

hd.bien = MetaData()
hd.bien.path = 'img/bien.gif'
hd.bien.w = 302
hd.bien.h = 350
hd.bien.x = 520
hd.bien.y = 150

hd.explosion = MetaData()
hd.explosion.path = 'img/explosion.gif'
hd.explosion.w = 157
hd.explosion.h = 229
hd.explosion.x = 600
hd.explosion.y = 150

hd.siguiente = MetaData()
hd.siguiente.path = 'img/siguiente.png'
hd.siguiente.w = 256
hd.siguiente.h = 121
hd.siguiente.x = 1090
hd.siguiente.y = 0

hd.ldescripcion = MetaData()
hd.ldescripcion.text = ''
hd.ldescripcion.color = (0, 0, 0, 255)
hd.ldescripcion.fname = 'DejaVu Sans Mono'
hd.ldescripcion.fsize = 14
hd.ldescripcion.x = 683
hd.ldescripcion.y = 700

hd.ldistancia_total = MetaData()
hd.ldistancia_total.text = ''
hd.ldistancia_total.color = (0, 0, 0, 255)
hd.ldistancia_total.fname = 'DejaVu Sans Mono'
hd.ldistancia_total.fsize = 14
hd.ldistancia_total.x = 655
hd.ldistancia_total.y = 68

hd.ldistanciaA_u = MetaData()
hd.ldistanciaA_u.text = ''
hd.ldistanciaA_u.color = (0, 0, 0, 255)
hd.ldistanciaA_u.fname = 'DejaVu Sans Mono'
hd.ldistanciaA_u.fsize = 14
hd.ldistanciaA_u.x = 195
hd.ldistanciaA_u.y = 68

hd.ldistanciaB_V = MetaData()
hd.ldistanciaB_V.text = ''
hd.ldistanciaB_V.color = (0, 0, 0, 255)
hd.ldistanciaB_V.fname = 'DejaVu Sans Mono'
hd.ldistanciaB_V.fsize = 14
hd.ldistanciaB_V.x = 1145
hd.ldistanciaB_V.y = 68

hd.lvelocidadU = MetaData()
hd.lvelocidadU.text = ''
hd.lvelocidadU.color = (0, 0, 0, 255)
hd.lvelocidadU.fname = 'DejaVu Sans Mono'
hd.lvelocidadU.fsize = 14
hd.lvelocidadU.x = 470
hd.lvelocidadU.y = 270

hd.lvelocidadV = MetaData()
hd.lvelocidadV.text = ''
hd.lvelocidadV.color = (0, 0, 0, 255)
hd.lvelocidadV.fname = 'DejaVu Sans Mono'
hd.lvelocidadV.fsize = 14
hd.lvelocidadV.x = 845
hd.lvelocidadV.y = 270

hd.ltiempo = MetaData()
hd.ltiempo.text = ''
hd.ltiempo.color = (0, 0, 0, 255)
hd.ltiempo.fname = 'DejaVu Sans Mono'
hd.ltiempo.fsize = 14
hd.ltiempo.x = 660
hd.ltiempo.y = 520

hd.zones['NIVEL1'] = {}

hd.zones['NIVEL1'] ['mover_mano'] = [(hd.mano.x, hd.mano.y, hd.mano.w, hd.mano.h)]
hd.zones['NIVEL1'] ['ir_ok'] = [(hd.ok.x, hd.ok.y, hd.ok.w, hd.ok.h)]
hd.zones['NIVEL1'] ['ir_casa'] = [(hd.casa.x, hd.casa.y, hd.casa.w, hd.casa.h)]
hd.zones['NIVEL1'] ['ir_actualizar'] = [(hd.actualizar.x, hd.actualizar.y, hd.actualizar.w, hd.actualizar.h)]
hd.zones['NIVEL1'] ['ir_bombillo'] = [(hd.bombillo.x, hd.bombillo.y, hd.bombillo.w, hd.bombillo.h)]
hd.zones['NIVEL1'] ['ir_niveles'] = [(hd.anterior6.x, hd.anterior6.y, hd.anterior6.w, hd.anterior6.h)]


#=====================================================================
# EJERCICIO2_N1 1366X768
#=====================================================================

hd.barco1_eje2 = MetaData()
hd.barco1_eje2.path = 'img/barco1.png'
hd.barco1_eje2.w = 150
hd.barco1_eje2.h = 159
hd.barco1_eje2.x = 10
hd.barco1_eje2.y = 180

hd.barco2_eje2 = MetaData()
hd.barco2_eje2.path = 'img/barco2.png'
hd.barco2_eje2.w = 150
hd.barco2_eje2.h = 136
hd.barco2_eje2.x = 1206
hd.barco2_eje2.y = 160

hd.agua_eje2 = MetaData()
hd.agua_eje2.path = 'img/agua.jpg'
hd.agua_eje2.w = 1366
hd.agua_eje2.h = 90
hd.agua_eje2.x = 0
hd.agua_eje2.y = 150

hd.faro_eje2 = MetaData()
hd.faro_eje2.path = 'img/faro.png'
hd.faro_eje2.w = 225
hd.faro_eje2.h = 450
hd.faro_eje2.x = 0
hd.faro_eje2.y = 220

hd.playa_eje2 = MetaData()
hd.playa_eje2.path = 'img/playa.png'
hd.playa_eje2.w = 600
hd.playa_eje2.h = 272
hd.playa_eje2.x = 766
hd.playa_eje2.y = 215

hd.anterior7 = MetaData()
hd.anterior7.path = 'img/anterior.png'
hd.anterior7.w = 110
hd.anterior7.h = 101
hd.anterior7.x = 10
hd.anterior7.y = 10

hd.tiempo_campo = MetaData()
hd.tiempo_campo.path = 'img/campo.png'
hd.tiempo_campo.w = 100
hd.tiempo_campo.h = 40
hd.tiempo_campo.x = 635
hd.tiempo_campo.y = 50

hd.car1_campo_eje2 = MetaData()
hd.car1_campo_eje2.path = 'img/campo.png'
hd.car1_campo_eje2.w = 100
hd.car1_campo_eje2.h = 40
hd.car1_campo_eje2.x = 170
hd.car1_campo_eje2.y = 50

hd.car2_campo_eje2 = MetaData()
hd.car2_campo_eje2.path = 'img/campo.png'
hd.car2_campo_eje2.w = 100
hd.car2_campo_eje2.h = 40
hd.car2_campo_eje2.x = 1120
hd.car2_campo_eje2.y = 50

hd.vel_car1_campo_eje2 = MetaData()
hd.vel_car1_campo_eje2.path = 'img/campo.png'
hd.vel_car1_campo_eje2.w = 100
hd.vel_car1_campo_eje2.h = 40
hd.vel_car1_campo_eje2.x = 340
hd.vel_car1_campo_eje2.y = 350

hd.vel_car2_campo_eje2 = MetaData()
hd.vel_car2_campo_eje2.path = 'img/campo.png'
hd.vel_car2_campo_eje2.w = 100
hd.vel_car2_campo_eje2.h = 40
hd.vel_car2_campo_eje2.x = 900
hd.vel_car2_campo_eje2.y = 350

hd.res_campo_eje2 = MetaData()
hd.res_campo_eje2.path = 'img/campo.png'
hd.res_campo_eje2.w = 100
hd.res_campo_eje2.h = 40
hd.res_campo_eje2.x = 635
hd.res_campo_eje2.y = 505

hd.tiempo_eje2 = MetaData()
hd.tiempo_eje2.path = 'img/tiempo.png'
hd.tiempo_eje2.w = 88
hd.tiempo_eje2.h = 38
hd.tiempo_eje2.x = 640
hd.tiempo_eje2.y = 20

hd.distanciaA_u_eje2 = MetaData()
hd.distanciaA_u_eje2.path = 'img/distanciaA_u.png'
hd.distanciaA_u_eje2.w = 176
hd.distanciaA_u_eje2.h = 39
hd.distanciaA_u_eje2.x = 140
hd.distanciaA_u_eje2.y = 20

hd.distanciaB_v_eje2 = MetaData()
hd.distanciaB_v_eje2.path = 'img/distanciaB_v.png'
hd.distanciaB_v_eje2.w = 173
hd.distanciaB_v_eje2.h = 41
hd.distanciaB_v_eje2.x = 1090
hd.distanciaB_v_eje2.y = 20

hd.velocidadU_eje2 = MetaData()
hd.velocidadU_eje2.path = 'img/velocidadU.png'
hd.velocidadU_eje2.w = 133
hd.velocidadU_eje2.h = 39
hd.velocidadU_eje2.x = 330
hd.velocidadU_eje2.y = 380

hd.velocidadV_eje2 = MetaData()
hd.velocidadV_eje2.path = 'img/velocidadV.png'
hd.velocidadV_eje2.w = 130
hd.velocidadV_eje2.h = 39
hd.velocidadV_eje2.x = 890
hd.velocidadV_eje2.y = 380

hd.distancia_eje2 = MetaData()
hd.distancia_eje2.path = 'img/distancia_eje2.png'
hd.distancia_eje2.w = 119
hd.distancia_eje2.h = 38
hd.distancia_eje2.x = 630
hd.distancia_eje2.y = 535

hd.mano_eje2 = MetaData()
hd.mano_eje2.path = 'img/mano.png'
hd.mano_eje2.w = 41
hd.mano_eje2.h = 48
hd.mano_eje2.x = 660
hd.mano_eje2.y = 100

hd.no_eje2 = MetaData()
hd.no_eje2.path = 'img/no.gif'
hd.no_eje2.w = 276
hd.no_eje2.h = 149
hd.no_eje2.x = 560
hd.no_eje2.y = 250

hd.bien_eje2 = MetaData()
hd.bien_eje2.path = 'img/bien.gif'
hd.bien_eje2.w = 302
hd.bien_eje2.h = 350
hd.bien_eje2.x = 520
hd.bien_eje2.y = 150

hd.explosion_eje2 = MetaData()
hd.explosion_eje2.path = 'img/explosion.gif'
hd.explosion_eje2.w = 157
hd.explosion_eje2.h = 229
hd.explosion_eje2.x = 600
hd.explosion_eje2.y = 150

hd.casa_eje2 = MetaData()
hd.casa_eje2.path = 'img/casa.png'
hd.casa_eje2.w = 60
hd.casa_eje2.h = 57
hd.casa_eje2.x = 1250
hd.casa_eje2.y = 660

hd.ok_eje2 = MetaData()
hd.ok_eje2.path = 'img/ok.png'
hd.ok_eje2.w = 61
hd.ok_eje2.h = 63
hd.ok_eje2.x = 1250
hd.ok_eje2.y = 480

hd.actualizar_eje2 = MetaData()
hd.actualizar_eje2.path = 'img/actualizar.png'
hd.actualizar_eje2.w = 63
hd.actualizar_eje2.h = 63
hd.actualizar_eje2.x = 1250
hd.actualizar_eje2.y = 570

hd.bombillo_eje2= MetaData()
hd.bombillo_eje2.path = 'img/bombillo.png'
hd.bombillo_eje2.w = 53
hd.bombillo_eje2.h = 53
hd.bombillo_eje2.x = 1290
hd.bombillo_eje2.y = 20

hd.siguiente_eje2 = MetaData()
hd.siguiente_eje2.path = 'img/siguiente.png'
hd.siguiente_eje2.w = 256
hd.siguiente_eje2.h = 121
hd.siguiente_eje2.x = 1090
hd.siguiente_eje2.y = 0

hd.ldescripcion_eje2 = MetaData()
hd.ldescripcion_eje2.text = ''
hd.ldescripcion_eje2.color = (0, 0, 0, 255)
hd.ldescripcion_eje2.fname = 'DejaVu Sans Mono'
hd.ldescripcion_eje2.fsize = 14
hd.ldescripcion_eje2.x = 683
hd.ldescripcion_eje2.y = 700

hd.ltiempo_total = MetaData()
hd.ltiempo_total.text = ''
hd.ltiempo_total.color = (0, 0, 0, 255)
hd.ltiempo_total.fname = 'DejaVu Sans Mono'
hd.ltiempo_total.fsize = 14
hd.ltiempo_total.x = 670
hd.ltiempo_total.y = 68

hd.ldistanciaA_u_eje2 = MetaData()
hd.ldistanciaA_u_eje2.text = ''
hd.ldistanciaA_u_eje2.color = (0, 0, 0, 255)
hd.ldistanciaA_u_eje2.fname = 'DejaVu Sans Mono'
hd.ldistanciaA_u_eje2.fsize = 14
hd.ldistanciaA_u_eje2.x = 195
hd.ldistanciaA_u_eje2.y = 68

hd.ldistanciaB_V_eje2 = MetaData()
hd.ldistanciaB_V_eje2.text = ''
hd.ldistanciaB_V_eje2.color = (0, 0, 0, 255)
hd.ldistanciaB_V_eje2.fname = 'DejaVu Sans Mono'
hd.ldistanciaB_V_eje2.fsize = 14
hd.ldistanciaB_V_eje2.x = 1145
hd.ldistanciaB_V_eje2.y = 68

hd.lvelocidadU_eje2 = MetaData()
hd.lvelocidadU_eje2.text = ''
hd.lvelocidadU_eje2.color = (0, 0, 0, 255)
hd.lvelocidadU_eje2.fname = 'DejaVu Sans Mono'
hd.lvelocidadU_eje2.fsize = 14
hd.lvelocidadU_eje2.x = 380
hd.lvelocidadU_eje2.y = 370

hd.lvelocidadV_eje2 = MetaData()
hd.lvelocidadV_eje2.text = ''
hd.lvelocidadV_eje2.color = (0, 0, 0, 255)
hd.lvelocidadV_eje2.fname = 'DejaVu Sans Mono'
hd.lvelocidadV_eje2.fsize = 14
hd.lvelocidadV_eje2.x = 940
hd.lvelocidadV_eje2.y = 370

hd.ldistancia_eje2 = MetaData()
hd.ldistancia_eje2.text = ''
hd.ldistancia_eje2.color = (0, 0, 0, 255)
hd.ldistancia_eje2.fname = 'DejaVu Sans Mono'
hd.ldistancia_eje2.fsize = 14
hd.ldistancia_eje2.x = 650
hd.ldistancia_eje2.y = 525

hd.zones['EJERCICIO2_N1'] = {}

hd.zones['EJERCICIO2_N1'] ['mover_mano'] = [(hd.mano_eje2.x, hd.mano_eje2.y, hd.mano_eje2.w, hd.mano_eje2.h)]
hd.zones['EJERCICIO2_N1'] ['ir_ok'] = [(hd.ok_eje2.x, hd.ok_eje2.y, hd.ok_eje2.w, hd.ok_eje2.h)]
hd.zones['EJERCICIO2_N1'] ['ir_casa'] = [(hd.casa_eje2.x, hd.casa_eje2.y, hd.casa_eje2.w, hd.casa_eje2.h)]
hd.zones['EJERCICIO2_N1'] ['ir_actualizar'] = [(hd.actualizar_eje2.x, hd.actualizar_eje2.y, hd.actualizar_eje2.w, hd.actualizar_eje2.h)]
hd.zones['EJERCICIO2_N1'] ['ir_bombillo'] = [(hd.bombillo_eje2.x, hd.bombillo_eje2.y, hd.bombillo_eje2.w, hd.bombillo_eje2.h)]
hd.zones['EJERCICIO2_N1'] ['ir_niveles'] = [(hd.anterior7.x, hd.anterior7.y, hd.anterior7.w, hd.anterior7.h)]

#=====================================================================
# EJERCICIO3_N1 1366X768
#=====================================================================

hd.anterior9_eje3_N1 = MetaData()
hd.anterior9_eje3_N1.path = 'img/anterior.png'
hd.anterior9_eje3_N1.w = 110
hd.anterior9_eje3_N1.h = 101
hd.anterior9_eje3_N1.x = 10
hd.anterior9_eje3_N1.y = 10

hd.tractor1_eje3_N1 = MetaData()
hd.tractor1_eje3_N1.path = 'img/tractor1.png'
hd.tractor1_eje3_N1.w = 150
hd.tractor1_eje3_N1.h = 104
hd.tractor1_eje3_N1.x = 10
hd.tractor1_eje3_N1.y = 175

hd.tractor2_eje3_N1 = MetaData()
hd.tractor2_eje3_N1.path = 'img/tractor2.png'
hd.tractor2_eje3_N1.w = 150
hd.tractor2_eje3_N1.h = 104
hd.tractor2_eje3_N1.x = 1212
hd.tractor2_eje3_N1.y = 155

hd.tierra_eje3_N1 = MetaData()
hd.tierra_eje3_N1.path = 'img/tierra.jpg'
hd.tierra_eje3_N1.w = 1366
hd.tierra_eje3_N1.h = 90
hd.tierra_eje3_N1.x = 0
hd.tierra_eje3_N1.y = 150

hd.molino_eje3_N1 = MetaData()
hd.molino_eje3_N1.path = 'img/molino.png'
hd.molino_eje3_N1.w = 317
hd.molino_eje3_N1.h = 450
hd.molino_eje3_N1.x = 4
hd.molino_eje3_N1.y = 200

hd.granja_eje3_N1 = MetaData()
hd.granja_eje3_N1.path = 'img/granja.png'
hd.granja_eje3_N1.w = 486
hd.granja_eje3_N1.h = 250
hd.granja_eje3_N1.x = 880
hd.granja_eje3_N1.y = 234

hd.tiempo_campo_eje3_N1 = MetaData()
hd.tiempo_campo_eje3_N1.path = 'img/campo.png'
hd.tiempo_campo_eje3_N1.w = 100
hd.tiempo_campo_eje3_N1.h = 40
hd.tiempo_campo_eje3_N1.x = 315
hd.tiempo_campo_eje3_N1.y = 300

hd.car1_campo_eje3_N1 = MetaData()
hd.car1_campo_eje3_N1.path = 'img/campo.png'
hd.car1_campo_eje3_N1.w = 100
hd.car1_campo_eje3_N1.h = 40
hd.car1_campo_eje3_N1.x = 170
hd.car1_campo_eje3_N1.y = 50

hd.car2_campo_eje3_N1 = MetaData()
hd.car2_campo_eje3_N1.path = 'img/campo.png'
hd.car2_campo_eje3_N1.w = 100
hd.car2_campo_eje3_N1.h = 40
hd.car2_campo_eje3_N1.x = 1120
hd.car2_campo_eje3_N1.y = 50

hd.vel_car2_campo_eje3_N1 = MetaData()
hd.vel_car2_campo_eje3_N1.path = 'img/campo.png'
hd.vel_car2_campo_eje3_N1.w = 100
hd.vel_car2_campo_eje3_N1.h = 40
hd.vel_car2_campo_eje3_N1.x = 770
hd.vel_car2_campo_eje3_N1.y = 300

hd.distancia_campo_eje3_N1 = MetaData()
hd.distancia_campo_eje3_N1.path = 'img/campo.png'
hd.distancia_campo_eje3_N1.w = 100
hd.distancia_campo_eje3_N1.h = 40
hd.distancia_campo_eje3_N1.x = 635
hd.distancia_campo_eje3_N1.y = 50

hd.res_campo_eje3_N1 = MetaData()
hd.res_campo_eje3_N1.path = 'img/campo.png'
hd.res_campo_eje3_N1.w = 100
hd.res_campo_eje3_N1.h = 40
hd.res_campo_eje3_N1.x = 635
hd.res_campo_eje3_N1.y = 460

hd.mano_eje3_N1 = MetaData()
hd.mano_eje3_N1.path = 'img/mano.png'
hd.mano_eje3_N1.w = 41
hd.mano_eje3_N1.h = 48
hd.mano_eje3_N1.x = 660
hd.mano_eje3_N1.y = 100

hd.distancia_eje3_N1 = MetaData()
hd.distancia_eje3_N1.path = 'img/distancia.png'
hd.distancia_eje3_N1.w = 167
hd.distancia_eje3_N1.h = 39
hd.distancia_eje3_N1.x = 600
hd.distancia_eje3_N1.y = 20

hd.distanciaA_u_eje3_N1 = MetaData()
hd.distanciaA_u_eje3_N1.path = 'img/distanciaA_u.png'
hd.distanciaA_u_eje3_N1.w = 176
hd.distanciaA_u_eje3_N1.h = 39
hd.distanciaA_u_eje3_N1.x = 140
hd.distanciaA_u_eje3_N1.y = 20

hd.distanciaB_v_eje3_N1 = MetaData()
hd.distanciaB_v_eje3_N1.path = 'img/distanciaB_v.png'
hd.distanciaB_v_eje3_N1.w = 173
hd.distanciaB_v_eje3_N1.h = 41
hd.distanciaB_v_eje3_N1.x = 1090
hd.distanciaB_v_eje3_N1.y = 20

hd.velocidad_auto_U_eje3_N1 = MetaData()
hd.velocidad_auto_U_eje3_N1.path = 'img/velocidadU.png'
hd.velocidad_auto_U_eje3_N1.w =  130
hd.velocidad_auto_U_eje3_N1.h =  39
hd.velocidad_auto_U_eje3_N1.x =  620
hd.velocidad_auto_U_eje3_N1.y =  490

hd.velocidadV_eje3_N1 = MetaData()
hd.velocidadV_eje3_N1.path = 'img/velocidadV.png'
hd.velocidadV_eje3_N1.w = 130 
hd.velocidadV_eje3_N1.h = 39
hd.velocidadV_eje3_N1.x = 755
hd.velocidadV_eje3_N1.y = 330

hd.tiempo_eje3_N1 = MetaData()
hd.tiempo_eje3_N1.path = 'img/tiempo.png'
hd.tiempo_eje3_N1.w = 88
hd.tiempo_eje3_N1.h = 38 
hd.tiempo_eje3_N1.x = 325
hd.tiempo_eje3_N1.y = 330

hd.ok_eje3_N1 = MetaData()
hd.ok_eje3_N1.path = 'img/ok.png'
hd.ok_eje3_N1.w = 63
hd.ok_eje3_N1.h = 63
hd.ok_eje3_N1.x = 1250
hd.ok_eje3_N1.y = 460

hd.actualizar_eje3_N1 = MetaData()
hd.actualizar_eje3_N1.path = 'img/actualizar.png'
hd.actualizar_eje3_N1.w = 63
hd.actualizar_eje3_N1.h = 63
hd.actualizar_eje3_N1.x = 1250
hd.actualizar_eje3_N1.y = 550

hd.casa_eje3_N1 = MetaData()
hd.casa_eje3_N1.path = 'img/casa.png'
hd.casa_eje3_N1.w = 63
hd.casa_eje3_N1.h = 63
hd.casa_eje3_N1.x = 1250
hd.casa_eje3_N1.y = 640

hd.bombillo_eje3_N1 = MetaData()
hd.bombillo_eje3_N1.path = 'img/bombillo.png'
hd.bombillo_eje3_N1.w = 53
hd.bombillo_eje3_N1.h = 53
hd.bombillo_eje3_N1.x = 1290
hd.bombillo_eje3_N1.y = 20

hd.siguiente_eje3_N1 = MetaData()
hd.siguiente_eje3_N1.path = 'img/siguiente.png'
hd.siguiente_eje3_N1.w = 256
hd.siguiente_eje3_N1.h = 114
hd.siguiente_eje3_N1.x = 1090
hd.siguiente_eje3_N1.y = 0

hd.no_eje3_N1 = MetaData()
hd.no_eje3_N1.path = 'img/no.gif'
hd.no_eje3_N1.w = 41
hd.no_eje3_N1.h = 41
hd.no_eje3_N1.x = 550
hd.no_eje3_N1.y = 330

hd.bien_eje3_N1 = MetaData()
hd.bien_eje3_N1.path = 'img/bien.gif'
hd.bien_eje3_N1.w = 41
hd.bien_eje3_N1.h = 41
hd.bien_eje3_N1.x = 520
hd.bien_eje3_N1.y = 150

hd.ldescripcion_eje3_N1 = MetaData()
hd.ldescripcion_eje3_N1.text = ''
hd.ldescripcion_eje3_N1.color = (0, 0, 0, 255)
hd.ldescripcion_eje3_N1.fname = 'DejaVu Sans Mono'
hd.ldescripcion_eje3_N1.fsize = 14
hd.ldescripcion_eje3_N1.x = 683
hd.ldescripcion_eje3_N1.y = 700

hd.ldistancia_total_eje3_N1 = MetaData()
hd.ldistancia_total_eje3_N1.text = ''
hd.ldistancia_total_eje3_N1.color = (0, 0, 0, 255)
hd.ldistancia_total_eje3_N1.fname = 'DejaVu Sans Mono'
hd.ldistancia_total_eje3_N1.fsize = 14
hd.ldistancia_total_eje3_N1.x = 655 
hd.ldistancia_total_eje3_N1.y = 68

hd.ldistanciaA_u_eje3_N1 = MetaData()
hd.ldistanciaA_u_eje3_N1.text = ''
hd.ldistanciaA_u_eje3_N1.color = (0, 0, 0, 255)
hd.ldistanciaA_u_eje3_N1.fname = 'DejaVu Sans Mono'
hd.ldistanciaA_u_eje3_N1.fsize = 14
hd.ldistanciaA_u_eje3_N1.x = 195
hd.ldistanciaA_u_eje3_N1.y = 68

hd.ldistanciaB_V_eje3_N1 = MetaData()
hd.ldistanciaB_V_eje3_N1.text = ''
hd.ldistanciaB_V_eje3_N1.color = (0, 0, 0, 255)
hd.ldistanciaB_V_eje3_N1.fname = 'DejaVu Sans Mono'
hd.ldistanciaB_V_eje3_N1.fsize = 14
hd.ldistanciaB_V_eje3_N1.x = 1145
hd.ldistanciaB_V_eje3_N1.y = 68

hd.lvelocidad_auto_U_eje3_N1 = MetaData()
hd.lvelocidad_auto_U_eje3_N1.text = ''
hd.lvelocidad_auto_U_eje3_N1.color = (0, 0, 0, 255)
hd.lvelocidad_auto_U_eje3_N1.fname = 'DejaVu Sans Mono'
hd.lvelocidad_auto_U_eje3_N1.fsize = 14
hd.lvelocidad_auto_U_eje3_N1.x = 650
hd.lvelocidad_auto_U_eje3_N1.y = 478

hd.lvelocidadV_eje3_N1 = MetaData()
hd.lvelocidadV_eje3_N1.text = ''
hd.lvelocidadV_eje3_N1.color = (0, 0, 0, 255)
hd.lvelocidadV_eje3_N1.fname = 'DejaVu Sans Mono'
hd.lvelocidadV_eje3_N1.fsize = 14
hd.lvelocidadV_eje3_N1.x = 805
hd.lvelocidadV_eje3_N1.y = 318

hd.ltiempo_transcurrido_eje3_N1 = MetaData()
hd.ltiempo_transcurrido_eje3_N1.text = ''
hd.ltiempo_transcurrido_eje3_N1.color = (0, 0, 0, 255)
hd.ltiempo_transcurrido_eje3_N1.fname = 'DejaVu Sans Mono'
hd.ltiempo_transcurrido_eje3_N1.fsize = 14
hd.ltiempo_transcurrido_eje3_N1.x = 350
hd.ltiempo_transcurrido_eje3_N1.y = 318

hd.diploma_N1 = MetaData()
hd.diploma_N1.path = 'img/diploma_n1.png'
hd.diploma_N1.w = 750
hd.diploma_N1.h = 580
hd.diploma_N1.x = 300
hd.diploma_N1.y = 50

hd.zones['EJERCICIO3_N1'] = {}

hd.zones['EJERCICIO3_N1'] ['mover_mano'] = [(hd.mano_eje3_N1.x, hd.mano_eje3_N1.y, hd.mano_eje3_N1.w, hd.mano_eje3_N1.h)]
hd.zones['EJERCICIO3_N1'] ['ir_ok'] = [(hd.ok_eje3_N1.x, hd.ok_eje3_N1.y, hd.ok_eje3_N1.w, hd.ok_eje3_N1.h)]
hd.zones['EJERCICIO3_N1'] ['ir_casa'] = [(hd.casa_eje3_N1.x, hd.casa_eje3_N1.y, hd.casa_eje3_N1.w, hd.casa_eje3_N1.h)]
hd.zones['EJERCICIO3_N1'] ['ir_actualizar'] = [(hd.actualizar_eje3_N1.x, hd.actualizar_eje3_N1.y, hd.actualizar_eje3_N1.w, hd.actualizar_eje3_N1.h)]
hd.zones['EJERCICIO3_N1'] ['ir_bombillo'] = [(hd.bombillo_eje3_N1.x, hd.bombillo_eje3_N1.y, hd.bombillo_eje3_N1.w, hd.bombillo_eje3_N1.h)]
hd.zones['EJERCICIO3_N1'] ['ir_niveles'] = [(hd.anterior9_eje3_N1.x, hd.anterior9_eje3_N1.y, hd.anterior9_eje3_N1.w, hd.anterior9_eje3_N1.h)]
hd.zones['EJERCICIO3_N1'] ['terminar_nivel'] = [(870, 170, 240, 100)]

#=====================================================================
# EJERCICIO1_N2 1366X768
#=====================================================================

hd.anterior_eje1_N2 = MetaData()
hd.anterior_eje1_N2.path = 'img/anterior.png'
hd.anterior_eje1_N2.w = 110
hd.anterior_eje1_N2.h = 101
hd.anterior_eje1_N2.x = 10
hd.anterior_eje1_N2.y = 5

hd.pinguino_eje1_N2 = MetaData()
hd.pinguino_eje1_N2.path = 'img/pinguino.png'
hd.pinguino_eje1_N2.w = 60
hd.pinguino_eje1_N2.h = 90
hd.pinguino_eje1_N2.x = 180
hd.pinguino_eje1_N2.y = 485

hd.hielo_eje1_N2 = MetaData()
hd.hielo_eje1_N2.path = 'img/hielo.png'
hd.hielo_eje1_N2.w = 280
hd.hielo_eje1_N2.h = 400
hd.hielo_eje1_N2.x = 0
hd.hielo_eje1_N2.y = 120

hd.nevado_eje1_N2 = MetaData()
hd.nevado_eje1_N2.path = 'img/nevado.png'
hd.nevado_eje1_N2.w = 700
hd.nevado_eje1_N2.h = 260
hd.nevado_eje1_N2.x = 663
hd.nevado_eje1_N2.y = 120

hd.iglu_eje1_N2 = MetaData()
hd.iglu_eje1_N2.path = 'img/iglu.png'
hd.iglu_eje1_N2.w = 150
hd.iglu_eje1_N2.h = 100
hd.iglu_eje1_N2.x = 820
hd.iglu_eje1_N2.y = 170

hd.rio_eje1_N2 = MetaData()
hd.rio_eje1_N2.path = 'img/rio.png'
hd.rio_eje1_N2.w = 1366
hd.rio_eje1_N2.h = 143
hd.rio_eje1_N2.x = 0
hd.rio_eje1_N2.y = 120

hd.orca_eje1_N2 = MetaData()
hd.orca_eje1_N2.path = 'img/orca.png'
hd.orca_eje1_N2.w = 380
hd.orca_eje1_N2.h = 217
hd.orca_eje1_N2.x = 330
hd.orca_eje1_N2.y = 185

hd.ok_eje1_N2 = MetaData()
hd.ok_eje1_N2.path = 'img/ok.png'
hd.ok_eje1_N2.w = 63
hd.ok_eje1_N2.h = 63
hd.ok_eje1_N2.x = 1250
hd.ok_eje1_N2.y = 470

hd.actualizar_eje1_N2 = MetaData()
hd.actualizar_eje1_N2.path = 'img/actualizar.png'
hd.actualizar_eje1_N2.w = 63
hd.actualizar_eje1_N2.h = 63
hd.actualizar_eje1_N2.x = 1250
hd.actualizar_eje1_N2.y = 560

hd.casa_eje1_N2 = MetaData()
hd.casa_eje1_N2.path = 'img/casa.png'
hd.casa_eje1_N2.w = 63
hd.casa_eje1_N2.h = 63
hd.casa_eje1_N2.x = 1250
hd.casa_eje1_N2.y = 650

hd.bombillo_eje1_N2 = MetaData()
hd.bombillo_eje1_N2.path = 'img/bombillo.png'
hd.bombillo_eje1_N2.w = 53
hd.bombillo_eje1_N2.h = 53
hd.bombillo_eje1_N2.x = 1290
hd.bombillo_eje1_N2.y = 20

hd.siguiente_eje1_N2 = MetaData()
hd.siguiente_eje1_N2.path = 'img/siguiente.png'
hd.siguiente_eje1_N2.w = 256
hd.siguiente_eje1_N2.h = 114
hd.siguiente_eje1_N2.x = 1090
hd.siguiente_eje1_N2.y = 0

hd.no_eje1_N2 = MetaData()
hd.no_eje1_N2.path = 'img/mal.gif'
hd.no_eje1_N2.w = 276
hd.no_eje1_N2.h = 149
hd.no_eje1_N2.x = 420
hd.no_eje1_N2.y = 200

hd.exe_eje1_N2 = MetaData()
hd.exe_eje1_N2.path = 'img/banana.gif'
hd.exe_eje1_N2.w = 329
hd.exe_eje1_N2.h = 198
hd.exe_eje1_N2.x = 380
hd.exe_eje1_N2.y = 200

hd.flecha_menos_eje1_N2 = MetaData()
hd.flecha_menos_eje1_N2.path = 'img/flecha-.png'
hd.flecha_menos_eje1_N2.w = 22
hd.flecha_menos_eje1_N2.h = 30
hd.flecha_menos_eje1_N2.x = 910
hd.flecha_menos_eje1_N2.y = 498

hd.flecha_mas_eje1_N2 = MetaData()
hd.flecha_mas_eje1_N2.path = 'img/flecha+.png'
hd.flecha_mas_eje1_N2.w = 22
hd.flecha_mas_eje1_N2.h = 30
hd.flecha_mas_eje1_N2.x = 1045
hd.flecha_mas_eje1_N2.y = 498

hd.altura_iceberg_campo_eje1_N2 = MetaData()
hd.altura_iceberg_campo_eje1_N2.path = 'img/campo.png'
hd.altura_iceberg_campo_eje1_N2.w = 100
hd.altura_iceberg_campo_eje1_N2.h = 40
hd.altura_iceberg_campo_eje1_N2.x = 220
hd.altura_iceberg_campo_eje1_N2.y = 50

hd.velocidad_pingui_campo_eje1_N2 = MetaData()
hd.velocidad_pingui_campo_eje1_N2.path = 'img/campo.png'
hd.velocidad_pingui_campo_eje1_N2.w = 100
hd.velocidad_pingui_campo_eje1_N2.h = 40
hd.velocidad_pingui_campo_eje1_N2.x = 1050
hd.velocidad_pingui_campo_eje1_N2.y = 50

hd.res_campo_eje1_N2 = MetaData()
hd.res_campo_eje1_N2.path = 'img/campo.png'
hd.res_campo_eje1_N2.w = 100
hd.res_campo_eje1_N2.h = 40
hd.res_campo_eje1_N2.x = 940
hd.res_campo_eje1_N2.y = 490

hd.altura_eje1_N2 = MetaData()
hd.altura_eje1_N2.path = 'img/altura.png'
hd.altura_eje1_N2.w = 170
hd.altura_eje1_N2.h = 39
hd.altura_eje1_N2.x = 190
hd.altura_eje1_N2.y = 20

hd.velocidad_eje1_N2 = MetaData()
hd.velocidad_eje1_N2.path = 'img/velocidad.png'
hd.velocidad_eje1_N2.w = 222
hd.velocidad_eje1_N2.h = 39
hd.velocidad_eje1_N2.x = 1000
hd.velocidad_eje1_N2.y = 20

hd.alcance_horizontal_eje1_N2 = MetaData()
hd.alcance_horizontal_eje1_N2.path = 'img/alcance.png'
hd.alcance_horizontal_eje1_N2.w = 218
hd.alcance_horizontal_eje1_N2.h = 39
hd.alcance_horizontal_eje1_N2.x = 880
hd.alcance_horizontal_eje1_N2.y = 525

hd.laltura_eje1_N2 = MetaData()
hd.laltura_eje1_N2.text = ''
hd.laltura_eje1_N2.color = (0, 0, 0, 255)
hd.laltura_eje1_N2.fname = 'DejaVu Sans Mono'
hd.laltura_eje1_N2.fsize = 14
hd.laltura_eje1_N2.x = 250
hd.laltura_eje1_N2.y = 70

hd.lvelocidad_eje1_N2 = MetaData()
hd.lvelocidad_eje1_N2.text = ''
hd.lvelocidad_eje1_N2.color = (0, 0, 0, 255)
hd.lvelocidad_eje1_N2.fname = 'DejaVu Sans Mono'
hd.lvelocidad_eje1_N2.fsize = 14
hd.lvelocidad_eje1_N2.x = 1090
hd.lvelocidad_eje1_N2.y = 70

hd.lalcance_horizontal_eje1_N2 = MetaData()
hd.lalcance_horizontal_eje1_N2.text = ''
hd.lalcance_horizontal_eje1_N2.color = (0, 0, 0, 255)
hd.lalcance_horizontal_eje1_N2.fname = 'DejaVu Sans Mono'
hd.lalcance_horizontal_eje1_N2.fsize = 14
hd.lalcance_horizontal_eje1_N2.x = 965
hd.lalcance_horizontal_eje1_N2.y = 510

hd.ldescripcion_eje1_N2 = MetaData()
hd.ldescripcion_eje1_N2.text = ''
hd.ldescripcion_eje1_N2.color = (0, 0, 0, 255)
hd.ldescripcion_eje1_N2.fname = 'DejaVu Sans Mono'
hd.ldescripcion_eje1_N2.fsize = 14
hd.ldescripcion_eje1_N2.x = 683
hd.ldescripcion_eje1_N2.y = 700

hd.zones['EJERCICIO1_N2'] = {}
hd.zones['EJERCICIO1_N2'] ['ir_niveles'] = [(hd.anterior_eje1_N2.x, hd.anterior_eje1_N2.y, hd.anterior_eje1_N2.w, hd.anterior_eje1_N2.h)]
hd.zones['EJERCICIO1_N2'] ['ir_ok'] = [(hd.ok_eje1_N2.x, hd.ok_eje1_N2.y, hd.ok_eje1_N2.w, hd.ok_eje1_N2.h)]
hd.zones['EJERCICIO1_N2'] ['ir_casa'] = [(hd.casa_eje1_N2.x, hd.casa_eje1_N2.y, hd.casa_eje1_N2.w, hd.casa_eje1_N2.h)]
hd.zones['EJERCICIO1_N2'] ['ir_actualizar'] = [(hd.actualizar_eje1_N2.x, hd.actualizar_eje1_N2.y, hd.actualizar_eje1_N2.w, hd.actualizar_eje1_N2.h)]
hd.zones['EJERCICIO1_N2'] ['ir_bombillo'] = [(hd.bombillo_eje1_N2.x, hd.bombillo_eje1_N2.y, hd.bombillo_eje1_N2.w, hd.bombillo_eje1_N2.h)]
hd.zones['EJERCICIO1_N2'] ['mas'] = [(hd.flecha_mas_eje1_N2.x, hd.flecha_mas_eje1_N2.y, hd.flecha_mas_eje1_N2.w, hd.flecha_mas_eje1_N2.h)]
hd.zones['EJERCICIO1_N2'] ['menos'] = [(hd.flecha_menos_eje1_N2.x, hd.flecha_menos_eje1_N2.y, hd.flecha_menos_eje1_N2.w, hd.flecha_menos_eje1_N2.h)]

#=====================================================================
# EJERCICIO2_N2 1366X768 
#=====================================================================

hd.anterior_eje2_N2 = MetaData()
hd.anterior_eje2_N2.path = 'img/anterior.png'
hd.anterior_eje2_N2.w = 110
hd.anterior_eje2_N2.h = 101
hd.anterior_eje2_N2.x = 5
hd.anterior_eje2_N2.y = 5

hd.monster_eje2_N2 = MetaData()
hd.monster_eje2_N2.path = 'img/monster.png'
hd.monster_eje2_N2.w = 150
hd.monster_eje2_N2.h = 87
hd.monster_eje2_N2.x = 1
hd.monster_eje2_N2.y = 346

hd.monster1_eje2_N2 = MetaData()
hd.monster1_eje2_N2.path = 'img/monster1.png'
hd.monster1_eje2_N2.w = 150
hd.monster1_eje2_N2.h = 91
hd.monster1_eje2_N2.x = 171
hd.monster1_eje2_N2.y = 346

hd.monster2_eje2_N2 = MetaData()
hd.monster2_eje2_N2.path = 'img/monster2.png'
hd.monster2_eje2_N2.w = 150
hd.monster2_eje2_N2.h = 91
hd.monster2_eje2_N2.x = 189
hd.monster2_eje2_N2.y = 346

hd.monster3_eje2_N2 = MetaData()
hd.monster3_eje2_N2.path = 'img/monster3.png'
hd.monster3_eje2_N2.w = 153
hd.monster3_eje2_N2.h = 104
hd.monster3_eje2_N2.x = 210
hd.monster3_eje2_N2.y = 346

hd.monster4_eje2_N2 = MetaData()
hd.monster4_eje2_N2.path = 'img/monster4.png'
hd.monster4_eje2_N2.w = 153
hd.monster4_eje2_N2.h = 117
hd.monster4_eje2_N2.x = 234
hd.monster4_eje2_N2.y = 346

hd.monster5_eje2_N2 = MetaData()
hd.monster5_eje2_N2.path = 'img/monster5.png'
hd.monster5_eje2_N2.w = 150
hd.monster5_eje2_N2.h = 125
hd.monster5_eje2_N2.x = 260
hd.monster5_eje2_N2.y = 347

hd.monster6_eje2_N2 = MetaData()
hd.monster6_eje2_N2.path = 'img/monster6.png'
hd.monster6_eje2_N2.w = 150
hd.monster6_eje2_N2.h = 123
hd.monster6_eje2_N2.x = 305
hd.monster6_eje2_N2.y = 365

hd.sombra_eje2_N2 = MetaData()
hd.sombra_eje2_N2.path = 'img/sombra.png'
hd.sombra_eje2_N2.w = 150
hd.sombra_eje2_N2.h = 87
hd.sombra_eje2_N2.x = 900
hd.sombra_eje2_N2.y = 346

hd.piedra_eje2_N2 = MetaData()
hd.piedra_eje2_N2.path = 'img/piedra.png'
hd.piedra_eje2_N2.w = 250
hd.piedra_eje2_N2.h = 100
hd.piedra_eje2_N2.x = 292
hd.piedra_eje2_N2.y = 312

hd.abismo1_eje2_N2 = MetaData()
hd.abismo1_eje2_N2.path = 'img/abismo1.png'
hd.abismo1_eje2_N2.w = 545
hd.abismo1_eje2_N2.h = 350
hd.abismo1_eje2_N2.x = 0
hd.abismo1_eje2_N2.y = 0

hd.abismo2_eje2_N2 = MetaData()
hd.abismo2_eje2_N2.path = 'img/abismo2.png'
hd.abismo2_eje2_N2.w = 545
hd.abismo2_eje2_N2.h = 410
hd.abismo2_eje2_N2.x = 821
hd.abismo2_eje2_N2.y = 0

hd.rocas_eje2_N2 = MetaData()
hd.rocas_eje2_N2.path = 'img/rocas.png'
hd.rocas_eje2_N2.w = 1360
hd.rocas_eje2_N2.h = 60
hd.rocas_eje2_N2.x = 3
hd.rocas_eje2_N2.y = 0

hd.ok_eje2_N2 = MetaData()
hd.ok_eje2_N2.path = 'img/ok.png'
hd.ok_eje2_N2.w = 63
hd.ok_eje2_N2.h = 63
hd.ok_eje2_N2.x = 1250
hd.ok_eje2_N2.y = 485

hd.actualizar_eje2_N2 = MetaData()
hd.actualizar_eje2_N2.path = 'img/actualizar.png'
hd.actualizar_eje2_N2.w = 63
hd.actualizar_eje2_N2.h = 63
hd.actualizar_eje2_N2.x = 1250
hd.actualizar_eje2_N2.y = 575

hd.casa_eje2_N2 = MetaData()
hd.casa_eje2_N2.path = 'img/casa.png'
hd.casa_eje2_N2.w = 63
hd.casa_eje2_N2.h = 63
hd.casa_eje2_N2.x = 1250
hd.casa_eje2_N2.y = 660

hd.bombillo_eje2_N2 = MetaData()
hd.bombillo_eje2_N2.path = 'img/bombillo.png'
hd.bombillo_eje2_N2.w = 53
hd.bombillo_eje2_N2.h = 53
hd.bombillo_eje2_N2.x = 1300
hd.bombillo_eje2_N2.y = 10

hd.siguiente_eje2_N2 = MetaData()
hd.siguiente_eje2_N2.path = 'img/siguiente.png'
hd.siguiente_eje2_N2.w = 256
hd.siguiente_eje2_N2.h = 114
hd.siguiente_eje2_N2.x = 1110
hd.siguiente_eje2_N2.y = 0

hd.no_eje2_N2 = MetaData()
hd.no_eje2_N2.path = 'img/mal.gif'
hd.no_eje2_N2.w = 276
hd.no_eje2_N2.h = 149
hd.no_eje2_N2.x = 520
hd.no_eje2_N2.y = 20

hd.exe_eje2_N2 = MetaData()
hd.exe_eje2_N2.path = 'img/banana.gif'
hd.exe_eje2_N2.w = 329
hd.exe_eje2_N2.h = 198
hd.exe_eje2_N2.x = 500
hd.exe_eje2_N2.y = 20

hd.explosion_eje2_N2 = MetaData()
hd.explosion_eje2_N2.path = 'img/explosion.gif'
hd.explosion_eje2_N2.w = 329
hd.explosion_eje2_N2.h = 198
hd.explosion_eje2_N2.x = 600
hd.explosion_eje2_N2.y = 30

hd.flecha_menos_eje2_N2 = MetaData()
hd.flecha_menos_eje2_N2.path = 'img/flecha-.png'
hd.flecha_menos_eje2_N2.w = 22
hd.flecha_menos_eje2_N2.h = 30
hd.flecha_menos_eje2_N2.x = 910
hd.flecha_menos_eje2_N2.y = 508

hd.flecha_mas_eje2_N2 = MetaData()
hd.flecha_mas_eje2_N2.path = 'img/flecha+.png'
hd.flecha_mas_eje2_N2.w = 22
hd.flecha_mas_eje2_N2.h = 30
hd.flecha_mas_eje2_N2.x = 1045
hd.flecha_mas_eje2_N2.y = 508

hd.altura_colina_campo_eje2_N2 = MetaData()
hd.altura_colina_campo_eje2_N2.path = 'img/campo.png'
hd.altura_colina_campo_eje2_N2.w = 100
hd.altura_colina_campo_eje2_N2.h = 40
hd.altura_colina_campo_eje2_N2.x = 340
hd.altura_colina_campo_eje2_N2.y = 100

hd.angulo_campo_eje2_N2 = MetaData()
hd.angulo_campo_eje2_N2.path = 'img/campo.png'
hd.angulo_campo_eje2_N2.w = 100
hd.angulo_campo_eje2_N2.h = 40
hd.angulo_campo_eje2_N2.x = 65
hd.angulo_campo_eje2_N2.y = 450

hd.res_campo_eje2_N2 = MetaData()
hd.res_campo_eje2_N2.path = 'img/campo.png'
hd.res_campo_eje2_N2.w = 100
hd.res_campo_eje2_N2.h = 40
hd.res_campo_eje2_N2.x = 940
hd.res_campo_eje2_N2.y = 500

hd.altura_colina_eje2_N2 = MetaData()
hd.altura_colina_eje2_N2.path = 'img/alturaColina.png'
hd.altura_colina_eje2_N2.w = 164
hd.altura_colina_eje2_N2.h = 40
hd.altura_colina_eje2_N2.x = 310
hd.altura_colina_eje2_N2.y = 130

hd.angulo_eje2_N2 = MetaData()
hd.angulo_eje2_N2.path = 'img/angulo.png'
hd.angulo_eje2_N2.w = 200
hd.angulo_eje2_N2.h = 43
hd.angulo_eje2_N2.x = 20
hd.angulo_eje2_N2.y = 480

hd.velocidad_eje2_N2 = MetaData()
hd.velocidad_eje2_N2.path = 'img/velocidadAuto.png'
hd.velocidad_eje2_N2.w = 180
hd.velocidad_eje2_N2.h = 40
hd.velocidad_eje2_N2.x = 900
hd.velocidad_eje2_N2.y = 530

hd.ldescripcion_eje2_N2 = MetaData()
hd.ldescripcion_eje2_N2.text = ''
hd.ldescripcion_eje2_N2.color = (0, 0, 0, 255)
hd.ldescripcion_eje2_N2.fname = 'DejaVu Sans Mono'
hd.ldescripcion_eje2_N2.fsize = 14
hd.ldescripcion_eje2_N2.x = 683
hd.ldescripcion_eje2_N2.y = 700

hd.laltura_eje2_N2 = MetaData()
hd.laltura_eje2_N2.text = ''
hd.laltura_eje2_N2.color = (0, 0, 0, 255)
hd.laltura_eje2_N2.fname = 'DejaVu Sans Mono'
hd.laltura_eje2_N2.fsize = 14
hd.laltura_eje2_N2.x = 365
hd.laltura_eje2_N2.y = 118

hd.langulo_elevacion_eje2_N2 = MetaData()
hd.langulo_elevacion_eje2_N2.text = ''
hd.langulo_elevacion_eje2_N2.color = (0, 0, 0, 255)
hd.langulo_elevacion_eje2_N2.fname = 'DejaVu Sans Mono'
hd.langulo_elevacion_eje2_N2.fsize = 14
hd.langulo_elevacion_eje2_N2.x = 105
hd.langulo_elevacion_eje2_N2.y = 468

hd.lvelocidad_eje2_N2 = MetaData()
hd.lvelocidad_eje2_N2.text = ''
hd.lvelocidad_eje2_N2.color = (0, 0, 0, 255)
hd.lvelocidad_eje2_N2.fname = 'DejaVu Sans Mono'
hd.lvelocidad_eje2_N2.fsize = 14
hd.lvelocidad_eje2_N2.x = 955
hd.lvelocidad_eje2_N2.y = 518

hd.zones['EJERCICIO2_N2'] = {}
hd.zones['EJERCICIO2_N2'] ['ir_niveles'] = [(hd.anterior_eje2_N2.x, hd.anterior_eje2_N2.y, hd.anterior_eje2_N2.w, hd.anterior_eje2_N2.h)]
hd.zones['EJERCICIO2_N2'] ['ir_ok'] = [(hd.ok_eje2_N2.x, hd.ok_eje2_N2.y, hd.ok_eje2_N2.w, hd.ok_eje2_N2.h)]
hd.zones['EJERCICIO2_N2'] ['ir_casa'] = [(hd.casa_eje2_N2.x, hd.casa_eje2_N2.y, hd.casa_eje2_N2.w, hd.casa_eje2_N2.h)]
hd.zones['EJERCICIO2_N2'] ['ir_actualizar'] = [(hd.actualizar_eje2_N2.x, hd.actualizar_eje2_N2.y, hd.actualizar_eje2_N2.w, hd.actualizar_eje2_N2.h)]
hd.zones['EJERCICIO2_N2'] ['ir_bombillo'] = [(hd.bombillo_eje2_N2.x, hd.bombillo_eje2_N2.y, hd.bombillo_eje2_N2.w, hd.bombillo_eje2_N2.h)]
hd.zones['EJERCICIO2_N2'] ['mas'] = [(hd.flecha_mas_eje2_N2.x, hd.flecha_mas_eje2_N2.y, hd.flecha_mas_eje2_N2.w, hd.flecha_mas_eje2_N2.h)]
hd.zones['EJERCICIO2_N2'] ['menos'] = [(hd.flecha_menos_eje2_N2.x, hd.flecha_menos_eje2_N2.y, hd.flecha_menos_eje2_N2.w, hd.flecha_menos_eje2_N2.h)]


#=====================================================================
# EJERCICIO3_N2 1366X768 
#=====================================================================

hd.anterior_eje3_N2 = MetaData()
hd.anterior_eje3_N2.path = 'img/anterior.png'
hd.anterior_eje3_N2.w = 110
hd.anterior_eje3_N2.h = 101
hd.anterior_eje3_N2.x = 5
hd.anterior_eje3_N2.y = 5

hd.rocas_eje3_N2 = MetaData()
hd.rocas_eje3_N2.path = 'img/rocas2.png'
hd.rocas_eje3_N2.w = 1360
hd.rocas_eje3_N2.h = 60
hd.rocas_eje3_N2.x = 3
hd.rocas_eje3_N2.y = 0

hd.grua_eje3_N2 = MetaData()
hd.grua_eje3_N2.path = 'img/grua.png'
hd.grua_eje3_N2.w = 640
hd.grua_eje3_N2.h = 550
hd.grua_eje3_N2.x = 140
hd.grua_eje3_N2.y = 5

hd.bola_eje3_N2 = MetaData()
hd.bola_eje3_N2.path = 'img/bola3.gif'
hd.bola_eje3_N2.w = 400
hd.bola_eje3_N2.h = 311
hd.bola_eje3_N2.x = 539
hd.bola_eje3_N2.y = 215

hd.bola1_eje3_N2 = MetaData()
hd.bola1_eje3_N2.path = 'img/bola1.png'
hd.bola1_eje3_N2.w = 90
hd.bola1_eje3_N2.h = 311
hd.bola1_eje3_N2.x = 695
hd.bola1_eje3_N2.y = 215

hd.edificio_eje3_N2 = MetaData()
hd.edificio_eje3_N2.path = 'img/edificio.png'
hd.edificio_eje3_N2.w = 300
hd.edificio_eje3_N2.h = 430
hd.edificio_eje3_N2.x = 905
hd.edificio_eje3_N2.y = 30

hd.luz_eje3_N2 = MetaData()
hd.luz_eje3_N2.path = 'img/luz3.gif'
hd.luz_eje3_N2.w = 540
hd.luz_eje3_N2.h = 520
hd.luz_eje3_N2.x = 786
hd.luz_eje3_N2.y = 0

hd.ok_eje3_N2 = MetaData()
hd.ok_eje3_N2.path = 'img/ok.png'
hd.ok_eje3_N2.w = 63
hd.ok_eje3_N2.h = 63
hd.ok_eje3_N2.x = 1250
hd.ok_eje3_N2.y = 485

hd.actualizar_eje3_N2 = MetaData()
hd.actualizar_eje3_N2.path = 'img/actualizar.png'
hd.actualizar_eje3_N2.w = 63
hd.actualizar_eje3_N2.h = 63
hd.actualizar_eje3_N2.x = 1250
hd.actualizar_eje3_N2.y = 575

hd.casa_eje3_N2 = MetaData()
hd.casa_eje3_N2.path = 'img/casa.png'
hd.casa_eje3_N2.w = 63
hd.casa_eje3_N2.h = 63
hd.casa_eje3_N2.x = 1250
hd.casa_eje3_N2.y = 660

hd.bombillo_eje3_N2 = MetaData()
hd.bombillo_eje3_N2.path = 'img/bombillo.png'
hd.bombillo_eje3_N2.w = 53
hd.bombillo_eje3_N2.h = 53
hd.bombillo_eje3_N2.x = 1300
hd.bombillo_eje3_N2.y = 10

hd.siguiente_eje3_N2 = MetaData()
hd.siguiente_eje3_N2.path = 'img/siguiente.png'
hd.siguiente_eje3_N2.w = 256
hd.siguiente_eje3_N2.h = 114
hd.siguiente_eje3_N2.x = 1110
hd.siguiente_eje3_N2.y = 0

hd.no_eje3_N2 = MetaData()
hd.no_eje3_N2.path = 'img/mal.gif'
hd.no_eje3_N2.w = 276
hd.no_eje3_N2.h = 149
hd.no_eje3_N2.x = 570
hd.no_eje3_N2.y = 20

hd.exe_eje3_N2 = MetaData()
hd.exe_eje3_N2.path = 'img/banana.gif'
hd.exe_eje3_N2.w = 329
hd.exe_eje3_N2.h = 198
hd.exe_eje3_N2.x = 530
hd.exe_eje3_N2.y = 20

hd.flecha_menos_eje3_N2 = MetaData()
hd.flecha_menos_eje3_N2.path = 'img/flecha-.png'
hd.flecha_menos_eje3_N2.w = 22
hd.flecha_menos_eje3_N2.h = 30
hd.flecha_menos_eje3_N2.x = 910
hd.flecha_menos_eje3_N2.y = 508

hd.flecha_mas_eje3_N2 = MetaData()
hd.flecha_mas_eje3_N2.path = 'img/flecha+.png'
hd.flecha_mas_eje3_N2.w = 22
hd.flecha_mas_eje3_N2.h = 30
hd.flecha_mas_eje3_N2.x = 1045
hd.flecha_mas_eje3_N2.y = 508

hd.longitud_cable_campo_eje3_N2 = MetaData()
hd.longitud_cable_campo_eje3_N2.path = 'img/campo.png'
hd.longitud_cable_campo_eje3_N2.w = 100
hd.longitud_cable_campo_eje3_N2.h = 40
hd.longitud_cable_campo_eje3_N2.x = 240
hd.longitud_cable_campo_eje3_N2.y = 400

hd.res_campo_eje3_N2 = MetaData()
hd.res_campo_eje3_N2.path = 'img/campo.png'
hd.res_campo_eje3_N2.w = 100
hd.res_campo_eje3_N2.h = 40
hd.res_campo_eje3_N2.x = 940
hd.res_campo_eje3_N2.y = 500

hd.longitud_eje3_N2 = MetaData()
hd.longitud_eje3_N2.path = 'img/longitud.png'
hd.longitud_eje3_N2.w = 181
hd.longitud_eje3_N2.h = 40
hd.longitud_eje3_N2.x = 210
hd.longitud_eje3_N2.y = 430

hd.periodo_eje3_N2 = MetaData()
hd.periodo_eje3_N2.path = 'img/periodo.png'
hd.periodo_eje3_N2.w = 194
hd.periodo_eje3_N2.h = 40
hd.periodo_eje3_N2.x = 900
hd.periodo_eje3_N2.y = 530

hd.ldescripcion_eje3_N2 = MetaData()
hd.ldescripcion_eje3_N2.text = ''
hd.ldescripcion_eje3_N2.color = (0, 0, 0, 255)
hd.ldescripcion_eje3_N2.fname = 'DejaVu Sans Mono'
hd.ldescripcion_eje3_N2.fsize = 14
hd.ldescripcion_eje3_N2.x = 683
hd.ldescripcion_eje3_N2.y = 700

hd.llongitud_eje3_N2 = MetaData()
hd.llongitud_eje3_N2.text = ''
hd.llongitud_eje3_N2.color = (0, 0, 0, 255)
hd.llongitud_eje3_N2.fname = 'DejaVu Sans Mono'
hd.llongitud_eje3_N2.fsize = 14
hd.llongitud_eje3_N2.x = 265
hd.llongitud_eje3_N2.y = 418

hd.lperiodo_eje3_N2 = MetaData()
hd.lperiodo_eje3_N2.text = ''
hd.lperiodo_eje3_N2.color = (0, 0, 0, 255)
hd.lperiodo_eje3_N2.fname = 'DejaVu Sans Mono'
hd.lperiodo_eje3_N2.fsize = 14
hd.lperiodo_eje3_N2.x = 955
hd.lperiodo_eje3_N2.y = 518

hd.diploma_N2 = MetaData()
hd.diploma_N2.path = 'img/diploma_n2.png'
hd.diploma_N2.w = 750
hd.diploma_N2.h = 580
hd.diploma_N2.x = 300
hd.diploma_N2.y = 50

hd.zones['EJERCICIO3_N2'] = {}
hd.zones['EJERCICIO3_N2'] ['ir_niveles'] = [(hd.anterior_eje3_N2.x, hd.anterior_eje3_N2.y, hd.anterior_eje3_N2.w, hd.anterior_eje3_N2.h)]
hd.zones['EJERCICIO3_N2'] ['ir_ok'] = [(hd.ok_eje3_N2.x, hd.ok_eje3_N2.y, hd.ok_eje3_N2.w, hd.ok_eje3_N2.h)]
hd.zones['EJERCICIO3_N2'] ['ir_casa'] = [(hd.casa_eje3_N2.x, hd.casa_eje3_N2.y, hd.casa_eje3_N2.w, hd.casa_eje3_N2.h)]
hd.zones['EJERCICIO3_N2'] ['ir_actualizar'] = [(hd.actualizar_eje3_N2.x, hd.actualizar_eje3_N2.y, hd.actualizar_eje3_N2.w, hd.actualizar_eje3_N2.h)]
hd.zones['EJERCICIO3_N2'] ['ir_bombillo'] = [(hd.bombillo_eje3_N2.x, hd.bombillo_eje3_N2.y, hd.bombillo_eje3_N2.w, hd.bombillo_eje3_N2.h)]
hd.zones['EJERCICIO3_N2'] ['mas'] = [(hd.flecha_mas_eje3_N2.x, hd.flecha_mas_eje3_N2.y, hd.flecha_mas_eje3_N2.w, hd.flecha_mas_eje3_N2.h)]
hd.zones['EJERCICIO3_N2'] ['menos'] = [(hd.flecha_menos_eje3_N2.x, hd.flecha_menos_eje3_N2.y, hd.flecha_menos_eje3_N2.w, hd.flecha_menos_eje3_N2.h)]

#=====================================================================
# EJERCICIO1_N3 1366X768 
#=====================================================================

hd.anterior_eje1_N3 = MetaData()
hd.anterior_eje1_N3.path = 'img/anterior.png'
hd.anterior_eje1_N3.w = 110
hd.anterior_eje1_N3.h = 101
hd.anterior_eje1_N3.x = 0
hd.anterior_eje1_N3.y = 0

hd.suelo_eje1_N3 = MetaData()
hd.suelo_eje1_N3.path = 'img/suelo.png'
hd.suelo_eje1_N3.w = 1366
hd.suelo_eje1_N3.h = 235
hd.suelo_eje1_N3.x = 0
hd.suelo_eje1_N3.y = 0

hd.arbol_eje1_N3 = MetaData()
hd.arbol_eje1_N3.path = 'img/arbol.png'
hd.arbol_eje1_N3.w = 500
hd.arbol_eje1_N3.h = 555
hd.arbol_eje1_N3.x = 0
hd.arbol_eje1_N3.y = 10

hd.manzana_eje1_N3 = MetaData()
hd.manzana_eje1_N3.path = 'img/manzana.png'
hd.manzana_eje1_N3.w = 35
hd.manzana_eje1_N3.h = 40
hd.manzana_eje1_N3.x = 287
hd.manzana_eje1_N3.y = 300

hd.nino_eje1_N3 = MetaData()
hd.nino_eje1_N3.path = 'img/nino.png'
hd.nino_eje1_N3.w = 300
hd.nino_eje1_N3.h = 160
hd.nino_eje1_N3.x = 250
hd.nino_eje1_N3.y = 0

hd.sol_eje1_N3 = MetaData()
hd.sol_eje1_N3.path = 'img/sol.png'
hd.sol_eje1_N3.w = 250
hd.sol_eje1_N3.h = 250
hd.sol_eje1_N3.x = 960
hd.sol_eje1_N3.y = 350

hd.golpe_eje1_N3 = MetaData()
hd.golpe_eje1_N3.path = 'img/golpe3.gif'
hd.golpe_eje1_N3.w = 191
hd.golpe_eje1_N3.h = 180
hd.golpe_eje1_N3.x = 153
hd.golpe_eje1_N3.y = 52

hd.ok_eje1_N3 = MetaData()
hd.ok_eje1_N3.path = 'img/ok.png'
hd.ok_eje1_N3.w = 63
hd.ok_eje1_N3.h = 63
hd.ok_eje1_N3.x = 1250
hd.ok_eje1_N3.y = 485

hd.actualizar_eje1_N3 = MetaData()
hd.actualizar_eje1_N3.path = 'img/actualizar.png'
hd.actualizar_eje1_N3.w = 63
hd.actualizar_eje1_N3.h = 63
hd.actualizar_eje1_N3.x = 1250
hd.actualizar_eje1_N3.y = 575

hd.casa_eje1_N3 = MetaData()
hd.casa_eje1_N3.path = 'img/casa.png'
hd.casa_eje1_N3.w = 63
hd.casa_eje1_N3.h = 63
hd.casa_eje1_N3.x = 1250
hd.casa_eje1_N3.y = 660

hd.bombillo_eje1_N3 = MetaData()
hd.bombillo_eje1_N3.path = 'img/bombillo.png'
hd.bombillo_eje1_N3.w = 53
hd.bombillo_eje1_N3.h = 53
hd.bombillo_eje1_N3.x = 1300
hd.bombillo_eje1_N3.y = 10

hd.siguiente_eje1_N3 = MetaData()
hd.siguiente_eje1_N3.path = 'img/siguiente.png'
hd.siguiente_eje1_N3.w = 256
hd.siguiente_eje1_N3.h = 114
hd.siguiente_eje1_N3.x = 1110
hd.siguiente_eje1_N3.y = 0

hd.no_eje1_N3 = MetaData()
hd.no_eje1_N3.path = 'img/dormido.gif'
hd.no_eje1_N3.w = 276
hd.no_eje1_N3.h = 149
hd.no_eje1_N3.x = 700
hd.no_eje1_N3.y = 0

hd.exe_eje1_N3 = MetaData()
hd.exe_eje1_N3.path = 'img/gano.gif'
hd.exe_eje1_N3.w = 329
hd.exe_eje1_N3.h = 198
hd.exe_eje1_N3.x = 700
hd.exe_eje1_N3.y = 0

hd.tiempo_caida_campo_eje1_N3 = MetaData()
hd.tiempo_caida_campo_eje1_N3.path = 'img/campo.png'
hd.tiempo_caida_campo_eje1_N3.w = 100
hd.tiempo_caida_campo_eje1_N3.h = 40
hd.tiempo_caida_campo_eje1_N3.x = 845
hd.tiempo_caida_campo_eje1_N3.y = 500

hd.res_campo_eje1_N3 = MetaData()
hd.res_campo_eje1_N3.path = 'img/campo.png'
hd.res_campo_eje1_N3.w = 100
hd.res_campo_eje1_N3.h = 40
hd.res_campo_eje1_N3.x = 530
hd.res_campo_eje1_N3.y = 270

hd.distancia_recorrida_eje1_N3 = MetaData()
hd.distancia_recorrida_eje1_N3.path = 'img/distanciaRecorrida.png'
hd.distancia_recorrida_eje1_N3.w = 227
hd.distancia_recorrida_eje1_N3.h = 38
hd.distancia_recorrida_eje1_N3.x = 470
hd.distancia_recorrida_eje1_N3.y = 300

hd.tiempo_caida_eje1_N3 = MetaData()
hd.tiempo_caida_eje1_N3.path = 'img/tiempoCaida.png'
hd.tiempo_caida_eje1_N3.w = 162
hd.tiempo_caida_eje1_N3.h = 39
hd.tiempo_caida_eje1_N3.x = 820
hd.tiempo_caida_eje1_N3.y = 530

hd.ldescripcion_eje1_N3 = MetaData()
hd.ldescripcion_eje1_N3.text = ''
hd.ldescripcion_eje1_N3.color = (0, 0, 0, 255)
hd.ldescripcion_eje1_N3.fname = 'DejaVu Sans Mono'
hd.ldescripcion_eje1_N3.fsize = 14
hd.ldescripcion_eje1_N3.x = 683
hd.ldescripcion_eje1_N3.y = 700

hd.ldistancia_recorrida_eje1_N3 = MetaData()
hd.ldistancia_recorrida_eje1_N3.text = ''
hd.ldistancia_recorrida_eje1_N3.color = (0, 0, 0, 255)
hd.ldistancia_recorrida_eje1_N3.fname = 'DejaVu Sans Mono'
hd.ldistancia_recorrida_eje1_N3.fsize = 14
hd.ldistancia_recorrida_eje1_N3.x = 485
hd.ldistancia_recorrida_eje1_N3.y = 218

hd.ltiempo_caida_eje1_N3 = MetaData()
hd.ltiempo_caida_eje1_N3.text = ''
hd.ltiempo_caida_eje1_N3.color = (0, 0, 0, 255)
hd.ltiempo_caida_eje1_N3.fname = 'DejaVu Sans Mono'
hd.ltiempo_caida_eje1_N3.fsize = 14
hd.ltiempo_caida_eje1_N3.x = 855
hd.ltiempo_caida_eje1_N3.y = 518


hd.zones['EJERCICIO1_N3'] = {}
hd.zones['EJERCICIO1_N3'] ['ir_niveles'] = [(hd.anterior_eje1_N3.x, hd.anterior_eje1_N3.y, hd.anterior_eje1_N3.w, hd.anterior_eje1_N3.h)]
hd.zones['EJERCICIO1_N3'] ['ir_ok'] = [(hd.ok_eje1_N3.x, hd.ok_eje1_N3.y, hd.ok_eje1_N3.w, hd.ok_eje1_N3.h)]
hd.zones['EJERCICIO1_N3'] ['ir_casa'] = [(hd.casa_eje1_N3.x, hd.casa_eje1_N3.y, hd.casa_eje1_N3.w, hd.casa_eje1_N3.h)]
hd.zones['EJERCICIO1_N3'] ['ir_actualizar'] = [(hd.actualizar_eje1_N3.x, hd.actualizar_eje1_N3.y, hd.actualizar_eje1_N3.w, hd.actualizar_eje1_N3.h)]
hd.zones['EJERCICIO1_N3'] ['ir_bombillo'] = [(hd.bombillo_eje1_N3.x, hd.bombillo_eje1_N3.y, hd.bombillo_eje1_N3.w, hd.bombillo_eje1_N3.h)]

#=====================================================================
# EJERCICIO2_N3 1366X768 
#=====================================================================

hd.anterior_eje2_N3 = MetaData()
hd.anterior_eje2_N3.path = 'img/anterior.png'
hd.anterior_eje2_N3.w = 110
hd.anterior_eje2_N3.h = 101
hd.anterior_eje2_N3.x = 0
hd.anterior_eje2_N3.y = 0

hd.pasto_eje2_N3 = MetaData()
hd.pasto_eje2_N3.path = 'img/pasto.png'
hd.pasto_eje2_N3.w = 1366
hd.pasto_eje2_N3.h = 169
hd.pasto_eje2_N3.x = 0
hd.pasto_eje2_N3.y = 0

hd.montana_eje2_N3 = MetaData()
hd.montana_eje2_N3.path = 'img/montana.png'
hd.montana_eje2_N3.w = 720
hd.montana_eje2_N3.h = 509
hd.montana_eje2_N3.x = 646
hd.montana_eje2_N3.y = 0

hd.arco_eje2_N3 = MetaData()
hd.arco_eje2_N3.path = 'img/arco.png'
hd.arco_eje2_N3.w = 900
hd.arco_eje2_N3.h = 550
hd.arco_eje2_N3.x = 0
hd.arco_eje2_N3.y = 0

hd.helicoptero_eje2_N3 = MetaData()
hd.helicoptero_eje2_N3.path = 'img/helicoptero.png'
hd.helicoptero_eje2_N3.w = 400
hd.helicoptero_eje2_N3.h = 190
hd.helicoptero_eje2_N3.x = 260
hd.helicoptero_eje2_N3.y = 360

hd.pepe_eje2_N3 = MetaData()
hd.pepe_eje2_N3.path = 'img/pepe.png'
hd.pepe_eje2_N3.w = 40
hd.pepe_eje2_N3.h = 56
hd.pepe_eje2_N3.x = 493
hd.pepe_eje2_N3.y = 422

hd.paracaidas_eje2_N3 = MetaData()
hd.paracaidas_eje2_N3.path = 'img/paracaidas.png'
hd.paracaidas_eje2_N3.w = 80
hd.paracaidas_eje2_N3.h = 98
hd.paracaidas_eje2_N3.x = 470
hd.paracaidas_eje2_N3.y = 468

hd.ok_eje2_N3 = MetaData()
hd.ok_eje2_N3.path = 'img/ok.png'
hd.ok_eje2_N3.w = 63
hd.ok_eje2_N3.h = 63
hd.ok_eje2_N3.x = 1250
hd.ok_eje2_N3.y = 485

hd.actualizar_eje2_N3 = MetaData()
hd.actualizar_eje2_N3.path = 'img/actualizar.png'
hd.actualizar_eje2_N3.w = 63
hd.actualizar_eje2_N3.h = 63
hd.actualizar_eje2_N3.x = 1250
hd.actualizar_eje2_N3.y = 575

hd.casa_eje2_N3 = MetaData()
hd.casa_eje2_N3.path = 'img/casa.png'
hd.casa_eje2_N3.w = 63
hd.casa_eje2_N3.h = 63
hd.casa_eje2_N3.x = 1250
hd.casa_eje2_N3.y = 660

hd.bombillo_eje2_N3 = MetaData()
hd.bombillo_eje2_N3.path = 'img/bombillo.png'
hd.bombillo_eje2_N3.w = 53
hd.bombillo_eje2_N3.h = 53
hd.bombillo_eje2_N3.x = 1300
hd.bombillo_eje2_N3.y = 10

hd.siguiente_eje2_N3 = MetaData()
hd.siguiente_eje2_N3.path = 'img/siguiente.png'
hd.siguiente_eje2_N3.w = 256
hd.siguiente_eje2_N3.h = 114
hd.siguiente_eje2_N3.x = 1110
hd.siguiente_eje2_N3.y = 0

hd.no_eje2_N3 = MetaData()
hd.no_eje2_N3.path = 'img/dormido.gif'
hd.no_eje2_N3.w = 276
hd.no_eje2_N3.h = 149
hd.no_eje2_N3.x = 330
hd.no_eje2_N3.y = 0

hd.exe_eje2_N3 = MetaData()
hd.exe_eje2_N3.path = 'img/gano.gif'
hd.exe_eje2_N3.w = 329
hd.exe_eje2_N3.h = 198
hd.exe_eje2_N3.x = 350
hd.exe_eje2_N3.y = 0

hd.velocidad_inicial_campo_eje2_N3 = MetaData()
hd.velocidad_inicial_campo_eje2_N3.path = 'img/campo.png'
hd.velocidad_inicial_campo_eje2_N3.w = 100
hd.velocidad_inicial_campo_eje2_N3.h = 40
hd.velocidad_inicial_campo_eje2_N3.x = 50
hd.velocidad_inicial_campo_eje2_N3.y = 270

hd.altura_helicoptero_campo_eje2_N3 = MetaData()
hd.altura_helicoptero_campo_eje2_N3.path = 'img/campo.png'
hd.altura_helicoptero_campo_eje2_N3.w = 100
hd.altura_helicoptero_campo_eje2_N3.h = 40
hd.altura_helicoptero_campo_eje2_N3.x = 50
hd.altura_helicoptero_campo_eje2_N3.y = 180

hd.res_campo_eje2_N3 = MetaData()
hd.res_campo_eje2_N3.path = 'img/campo.png'
hd.res_campo_eje2_N3.w = 100
hd.res_campo_eje2_N3.h = 40
hd.res_campo_eje2_N3.x = 960
hd.res_campo_eje2_N3.y = 500

hd.velocidad_final_eje2_N3 = MetaData()
hd.velocidad_final_eje2_N3.path = 'img/velocidadF.png'
hd.velocidad_final_eje2_N3.w = 181
hd.velocidad_final_eje2_N3.h = 38
hd.velocidad_final_eje2_N3.x = 920
hd.velocidad_final_eje2_N3.y = 530

hd.velocidad_inicial_eje2_N3 = MetaData()
hd.velocidad_inicial_eje2_N3.path = 'img/velocidadI.png'
hd.velocidad_inicial_eje2_N3.w = 194
hd.velocidad_inicial_eje2_N3.h = 37
hd.velocidad_inicial_eje2_N3.x = 10
hd.velocidad_inicial_eje2_N3.y = 300

hd.altura_helicoptero_eje2_N3 = MetaData()
hd.altura_helicoptero_eje2_N3.path = 'img/alturaH.png'
hd.altura_helicoptero_eje2_N3.w = 213
hd.altura_helicoptero_eje2_N3.h = 40
hd.altura_helicoptero_eje2_N3.x = 5
hd.altura_helicoptero_eje2_N3.y = 210

hd.ldescripcion_eje2_N3 = MetaData()
hd.ldescripcion_eje2_N3.text = ''
hd.ldescripcion_eje2_N3.color = (0, 0, 0, 255)
hd.ldescripcion_eje2_N3.fname = 'DejaVu Sans Mono'
hd.ldescripcion_eje2_N3.fsize = 14
hd.ldescripcion_eje2_N3.x = 683
hd.ldescripcion_eje2_N3.y = 700

hd.lvelocidad_inicial_eje2_N3 = MetaData()
hd.lvelocidad_inicial_eje2_N3.text = ''
hd.lvelocidad_inicial_eje2_N3.color = (0, 0, 0, 255)
hd.lvelocidad_inicial_eje2_N3.fname = 'DejaVu Sans Mono'
hd.lvelocidad_inicial_eje2_N3.fsize = 14
hd.lvelocidad_inicial_eje2_N3.x = 10
hd.lvelocidad_inicial_eje2_N3.y = 300

hd.lvelocidad_final_eje2_N3 = MetaData()
hd.lvelocidad_final_eje2_N3.text = ''
hd.lvelocidad_final_eje2_N3.color = (0, 0, 0, 255)
hd.lvelocidad_final_eje2_N3.fname = 'DejaVu Sans Mono'
hd.lvelocidad_final_eje2_N3.fsize = 14
hd.lvelocidad_final_eje2_N3.x = 955
hd.lvelocidad_final_eje2_N3.y = 518

hd.laltura_helicoptero_eje2_N3 = MetaData()
hd.laltura_helicoptero_eje2_N3.text = ''
hd.laltura_helicoptero_eje2_N3.color = (0, 0, 0, 255)
hd.laltura_helicoptero_eje2_N3.fname = 'DejaVu Sans Mono'
hd.laltura_helicoptero_eje2_N3.fsize = 14
hd.laltura_helicoptero_eje2_N3.x = 10
hd.laltura_helicoptero_eje2_N3.y = 230

hd.zones['EJERCICIO2_N3'] = {}
hd.zones['EJERCICIO2_N3'] ['ir_niveles'] = [(hd.anterior_eje2_N3.x, hd.anterior_eje2_N3.y, hd.anterior_eje2_N3.w, hd.anterior_eje2_N3.h)]
hd.zones['EJERCICIO2_N3'] ['ir_ok'] = [(hd.ok_eje2_N3.x, hd.ok_eje2_N3.y, hd.ok_eje2_N3.w, hd.ok_eje2_N3.h)]
hd.zones['EJERCICIO2_N3'] ['ir_casa'] = [(hd.casa_eje2_N3.x, hd.casa_eje2_N3.y, hd.casa_eje2_N3.w, hd.casa_eje2_N3.h)]
hd.zones['EJERCICIO2_N3'] ['ir_actualizar'] = [(hd.actualizar_eje2_N3.x, hd.actualizar_eje2_N3.y, hd.actualizar_eje2_N3.w, hd.actualizar_eje2_N3.h)]
hd.zones['EJERCICIO2_N3'] ['ir_bombillo'] = [(hd.bombillo_eje2_N3.x, hd.bombillo_eje2_N3.y, hd.bombillo_eje2_N3.w, hd.bombillo_eje2_N3.h)]

#=====================================================================
# EJERCICIO3_N3 1366X768 
#=====================================================================

hd.anterior_eje3_N3 = MetaData()
hd.anterior_eje3_N3.path = 'img/anterior.png'
hd.anterior_eje3_N3.w = 63
hd.anterior_eje3_N3.h = 58
hd.anterior_eje3_N3.x = 1250
hd.anterior_eje3_N3.y = 395

hd.mar_eje3_N3 = MetaData()
hd.mar_eje3_N3.path = 'img/mar.png'
hd.mar_eje3_N3.w = 1366
hd.mar_eje3_N3.h = 300
hd.mar_eje3_N3.x = 0
hd.mar_eje3_N3.y = 0

hd.balon_eje3_N3 = MetaData()
hd.balon_eje3_N3.path = 'img/balon.png'
hd.balon_eje3_N3.w = 100
hd.balon_eje3_N3.h = 100
hd.balon_eje3_N3.x = 1015
hd.balon_eje3_N3.y = 80

hd.nina_eje3_N3 = MetaData()
hd.nina_eje3_N3.path = 'img/nina.png'
hd.nina_eje3_N3.w = 340
hd.nina_eje3_N3.h = 245
hd.nina_eje3_N3.x = 1025
hd.nina_eje3_N3.y = 50

hd.sol_eje3_N3 = MetaData()
hd.sol_eje3_N3.path = 'img/sol.png'
hd.sol_eje3_N3.w = 250
hd.sol_eje3_N3.h = 250
hd.sol_eje3_N3.x = 160
hd.sol_eje3_N3.y = 300

hd.nina_lanzando_eje3_N3 = MetaData()
hd.nina_lanzando_eje3_N3.path = 'img/ninalanzandopelota3.gif'
hd.nina_lanzando_eje3_N3.w = 350
hd.nina_lanzando_eje3_N3.h = 350
hd.nina_lanzando_eje3_N3.x = 1000
hd.nina_lanzando_eje3_N3.y = 0

hd.ok_eje3_N3 = MetaData()
hd.ok_eje3_N3.path = 'img/ok.png'
hd.ok_eje3_N3.w = 63
hd.ok_eje3_N3.h = 63
hd.ok_eje3_N3.x = 1250
hd.ok_eje3_N3.y = 485

hd.actualizar_eje3_N3 = MetaData()
hd.actualizar_eje3_N3.path = 'img/actualizar.png'
hd.actualizar_eje3_N3.w = 63
hd.actualizar_eje3_N3.h = 63
hd.actualizar_eje3_N3.x = 1250
hd.actualizar_eje3_N3.y = 575

hd.casa_eje3_N3 = MetaData()
hd.casa_eje3_N3.path = 'img/casa.png'
hd.casa_eje3_N3.w = 63
hd.casa_eje3_N3.h = 63
hd.casa_eje3_N3.x = 1250
hd.casa_eje3_N3.y = 660

hd.bombillo_eje3_N3 = MetaData()
hd.bombillo_eje3_N3.path = 'img/bombillo.png'
hd.bombillo_eje3_N3.w = 53
hd.bombillo_eje3_N3.h = 53
hd.bombillo_eje3_N3.x = 1310
hd.bombillo_eje3_N3.y = 150

hd.siguiente_eje3_N3 = MetaData()
hd.siguiente_eje3_N3.path = 'img/siguiente.png'
hd.siguiente_eje3_N3.w = 256
hd.siguiente_eje3_N3.h = 114
hd.siguiente_eje3_N3.x = 1110
hd.siguiente_eje3_N3.y = 0

hd.no_eje3_N3 = MetaData()
hd.no_eje3_N3.path = 'img/dormido.gif'
hd.no_eje3_N3.w = 276
hd.no_eje3_N3.h = 149
hd.no_eje3_N3.x = 760
hd.no_eje3_N3.y = 0

hd.exe_eje3_N3 = MetaData()
hd.exe_eje3_N3.path = 'img/gano.gif'
hd.exe_eje3_N3.w = 329
hd.exe_eje3_N3.h = 198
hd.exe_eje3_N3.x = 740
hd.exe_eje3_N3.y = 0

hd.velocidad_pelota_campo_eje3_N3 = MetaData()
hd.velocidad_pelota_campo_eje3_N3.path = 'img/campo.png'
hd.velocidad_pelota_campo_eje3_N3.w = 100
hd.velocidad_pelota_campo_eje3_N3.h = 40
hd.velocidad_pelota_campo_eje3_N3.x = 515
hd.velocidad_pelota_campo_eje3_N3.y = 270

hd.res_campo_eje3_N3 = MetaData()
hd.res_campo_eje3_N3.path = 'img/campo.png'
hd.res_campo_eje3_N3.w = 100
hd.res_campo_eje3_N3.h = 40
hd.res_campo_eje3_N3.x = 820
hd.res_campo_eje3_N3.y = 500

hd.altura_maxima_eje3_N3 = MetaData()
hd.altura_maxima_eje3_N3.path = 'img/alturaMaxima.png'
hd.altura_maxima_eje3_N3.w = 175
hd.altura_maxima_eje3_N3.h = 37
hd.altura_maxima_eje3_N3.x = 790
hd.altura_maxima_eje3_N3.y = 530

hd.velocidad_pelota_eje3_N3 = MetaData()
hd.velocidad_pelota_eje3_N3.path = 'img/velocidadPelota.png'
hd.velocidad_pelota_eje3_N3.w = 193
hd.velocidad_pelota_eje3_N3.h = 38
hd.velocidad_pelota_eje3_N3.x = 470
hd.velocidad_pelota_eje3_N3.y = 300

hd.ldescripcion_eje3_N3 = MetaData()
hd.ldescripcion_eje3_N3.text = ''
hd.ldescripcion_eje3_N3.color = (0, 0, 0, 255)
hd.ldescripcion_eje3_N3.fname = 'DejaVu Sans Mono'
hd.ldescripcion_eje3_N3.fsize = 14
hd.ldescripcion_eje3_N3.x = 683
hd.ldescripcion_eje3_N3.y = 700

hd.lvelocidad_pelota_eje3_N3 = MetaData()
hd.lvelocidad_pelota_eje3_N3.text = ''
hd.lvelocidad_pelota_eje3_N3.color = (0, 0, 0, 255)
hd.lvelocidad_pelota_eje3_N3.fname = 'DejaVu Sans Mono'
hd.lvelocidad_pelota_eje3_N3.fsize = 14
hd.lvelocidad_pelota_eje3_N3.x = 485
hd.lvelocidad_pelota_eje3_N3.y = 218

hd.laltura_maxima_eje3_N3 = MetaData()
hd.laltura_maxima_eje3_N3.text = ''
hd.laltura_maxima_eje3_N3.color = (0, 0, 0, 255)
hd.laltura_maxima_eje3_N3.fname = 'DejaVu Sans Mono'
hd.laltura_maxima_eje3_N3.fsize = 14
hd.laltura_maxima_eje3_N3.x = 855
hd.laltura_maxima_eje3_N3.y = 518


hd.zones['EJERCICIO3_N3'] = {}
hd.zones['EJERCICIO3_N3'] ['ir_niveles'] = [(hd.anterior_eje3_N3.x, hd.anterior_eje3_N3.y, hd.anterior_eje3_N3.w, hd.anterior_eje3_N3.h)]
hd.zones['EJERCICIO3_N3'] ['ir_ok'] = [(hd.ok_eje3_N3.x, hd.ok_eje3_N3.y, hd.ok_eje3_N3.w, hd.ok_eje3_N3.h)]
hd.zones['EJERCICIO3_N3'] ['ir_casa'] = [(hd.casa_eje3_N3.x, hd.casa_eje3_N3.y, hd.casa_eje3_N3.w, hd.casa_eje3_N3.h)]
hd.zones['EJERCICIO3_N3'] ['ir_actualizar'] = [(hd.actualizar_eje3_N3.x, hd.actualizar_eje3_N3.y, hd.actualizar_eje3_N3.w, hd.actualizar_eje3_N3.h)]
hd.zones['EJERCICIO3_N3'] ['ir_bombillo'] = [(hd.bombillo_eje3_N3.x, hd.bombillo_eje3_N3.y, hd.bombillo_eje3_N3.w, hd.bombillo_eje3_N3.h)]
#=====================================================================


resol = {'1366x768': hd, '1024x768': bd, '800x600': ld, '400x400': lu}
