from datetime import datetime

class user:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth


    @property
    def age (self):
        today = datetime.now().date()
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d").date()
        age= today.year - birth_date.year


        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -=1

        return age
    

def only_adult(func):
    def verification(user):
        if user.age < 18:
            raise PermissionError (f"Access denied {user.name} you are only : {user.age} years")
        return func(user)
    return verification

@only_adult
def access_VIP_ZONE(user):
    return f"Congratulations to visit the VIP ZONE {user.name}"



adult= user("Jeffree", "1997-09-09")
younger= user ("Luca", "2010-09-10")

print(access_VIP_ZONE(adult))
print(access_VIP_ZONE(younger))