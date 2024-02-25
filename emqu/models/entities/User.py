from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, username, password, idAplicacion, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.idAplicacion = idAplicacion
        self.fullname = fullname
    
    # con este decorador se utiliza sin necesidad de instanciar la clase
    @classmethod
    def check_password(self, hashed_password, password):
        #print(hashed_password)
        #print(password)
        return check_password_hash(hashed_password, password)

#print(generate_password_hash("12345"))
#print(len(generate_password_hash("12345")))
#print(len("32768:8:1$GKGTo5i24AxRU9Ac$e149005bd8f135ad9d83a4b354dbb8cf84d3826b4f7a9887831bf7eda12e2d6a900de4053efdcdcf6009fad56c89fc42b9a24e415fd1cd4bac1938fc829230e6"))