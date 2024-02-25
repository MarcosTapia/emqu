from .entities.User import User
class ModelUser():
    # Metodos para panel de Asistencias 
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """select id,username,password,fullname,idAplicacion from user 
                    where username='{}' """.format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                #si el valor de la clave concuerda con el nuevo hasheado devuelve un True o False
                #en el lugar de la columna password
                user = User(row[0], row[1], User.check_password(row[2],user.password), row[3], row[4])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """select id,username,fullname,idAplicacion from user 
                    where id='{}' """.format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2], row[3])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)            
    # Fin Metodos para panel de Asistencias 
