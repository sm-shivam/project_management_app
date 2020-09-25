from django.contrib.auth.base_user import BaseUserManager
# from .models import User


class UserManager(BaseUserManager):

    def create_user(self, firstname, lastname, email, password):
        if not (firstname and lastname and email and password):
            raise ValueError('User must have a valid firstname,lastname,email and password')

        user = self.model(firstname=firstname, lastname=lastname , email=email)
        user.set_password = password

        user.set_password(password)
        user.save()
        return user

    def createsuperuser(self, firstname, lastname, email, password):
        if not (firstname and lastname and email and password):
            raise ValueError('SuperUser must have a valid firstname,lastname,email and password')

        user = self.model(firstname=firstname, lastname=lastname , email=email)
        user.set_password = password

        user.is_staff=True
        user.is_superuser=True

        user.save()
        return user