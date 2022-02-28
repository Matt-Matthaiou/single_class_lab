class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        self.fav_language = ""

    def talk(self):
        return "I can talk!"
        
    
    def say_favourite_language(self, language):
        self.fav_language = language
        return f'I love {self.fav_language}'