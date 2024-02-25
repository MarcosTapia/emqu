from .entities.Equipo import Equipo
from .entities.PruebaEquipo import PruebaEquipo

class ModelEquipo():
    # Metodos para Equipos
    @classmethod
    def get_all(self, db):
        equipos = []
        try:
            cursor = db.connection.cursor()
            sql = """select * from equipos 
                    """
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                equipos.append(row)
            return equipos
        except Exception as ex:
            raise Exception(ex)            


    @classmethod
    def get_by_id(self, db, idEquipo):
        try:
            cursor = db.connection.cursor()
            sql = """select * from equipos 
                    where idEquipo='{}' """.format(idEquipo)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return row
            else:
                return None
        except Exception as ex:
            raise Exception(ex)            
        

    @classmethod
    def updateEquipo(self, db, equipo):
        try:
            cursor = db.connection.cursor()
            sql = """update equipos set nombre='{}', ipv4='{}' 
                    where idEquipo={} """.format(equipo.nombre, equipo.ipv4, equipo.idEquipo)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)            


    @classmethod
    def deleteEquipo(self, db, idEquipo):
        try:
            cursor = db.connection.cursor()
            sql = """delete from equipos 
                    where idEquipo={} """.format(idEquipo)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)            

    @classmethod
    def insertEquipo(self, db, equipo):
        try:
            cursor = db.connection.cursor()
            sql = """insert into equipos (idEquipo,nombre,ipv4) values 
                    ({},'{}','{}') """.format(equipo.idEquipo, equipo.nombre, equipo.ipv4)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)            

    # Fin Metodos para Equipos 


    # Metodos para Pruebas
    @classmethod
    def insertPruebas(self, db, pruebas):
        try:
            cursor = db.connection.cursor()
            sql = f"insert into pruebas_latencia (idEquipo, resultado_prueba)VALUES(%s,%s)"
            cursor.executemany(sql,pruebas)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)            
         
    @classmethod
    def get_allPruebas(self, db):
        pruebas = []
        try:
            cursor = db.connection.cursor()
            sql = """select * from pruebas_latencia 
                    """
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                pruebas.append(row)
            return pruebas
        except Exception as ex:
            raise Exception(ex)            

