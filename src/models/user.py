class User:
    """Handles the user's data"""


    def __init__(self, username, password, email, birthday, 
                 skinType, sensitivity):
        self.username = username
        self.password = password
        self.email = email
        self.birthday = birthday
        self.skinType = skinType
        self.sensitivity = sensitivity