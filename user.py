class User:
    """ Lida com dados do usuário"""


    def __init__(self, username, password, email, birthday, 
                 skinType, sensitivity):
        self.username = username
        self.password = password
        self.email = email
        self.birthday = birthday
        self.skinType = skinType
        self.sensitivity = sensitivity