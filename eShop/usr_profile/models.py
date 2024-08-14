from django.db import models

from login.models import User


class Cart(models.Model):
    def __init__(self, user=models.ForeignKey(User, on_delete=models.CASCADE)):
        self.user = user


    def __repr__(self):
        return f"{self.user}'s cart"

#try to use classmethods, static methods and instance methods here
    

def main():

    chykee = Cart(User.objects.get(id=1))

    print(chykee)

if __name__=="__main__":
    main()