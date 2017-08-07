import pymysql
import hashlib

class DB:
    
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
    
    def crearUsuario(self, nombre, apellido, correo, clave, rol, grado):
        
        if(rol == 'DOCENTE'):
            rol = 2
        else:
            rol = 1
        
        clave = hashlib.sha512(clave.encode('utf-8')).hexdigest()
        
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.pwd, db=self.db)
        cur = conn.cursor()
        cur.execute("insert into usuario values(0, '"+str(nombre)+"', '"+str(apellido)+"', '"+str(correo)+"', '"+str(clave)+"', "+str(rol)+", '"+str(grado)+"');")
        conn.commit()
        conn.close()
        
    def login(self, correo, clave):
        
        clave = hashlib.sha512(clave.encode('utf-8')).hexdigest()
        print(correo)
        print(clave)
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.pwd, db=self.db)
        cur = conn.cursor()
        cur.execute('select count(id) from usuario where correo="'+correo+'" and clave="'+clave+'";')
        #cur.execute('select * from usuario ')
        row=[]
        for r in cur:
            row.append(r)
       
        conn.close()
        if(row[0][0]== 1):
            return True
        else:
            return False
    
    def getEjercicio(self, lvl):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.pwd, db=self.db)
        cur = conn.cursor()
        cur.execute('SELECT ejercicio.id as eid, ejercicio.descripcion as edes from ejercicio where ejercicio.nivel_id = '+str(lvl)+' ORDER by rand() limit 1')
        
        row=[]
        for r in cur:
            row.append(r)
       
        conn.close()
        
        return row[0]
    
    def getCampos(self, eje):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.pwd, db=self.db)
        cur = conn.cursor()
        cur.execute('SELECT campo.nombre as cnombre, operando.numeros as num from ejercicio, campo, operando where ejercicio.id = '+str(eje)+' and operando.ejercicio_id = ejercicio.id and operando.campo_id = campo.id order by campo.nombre ASC ')
        
        row={}
        for r in cur:
            row[r[0]] = r[1]
       
        conn.close()
        
        return row
        
   
       
