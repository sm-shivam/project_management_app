from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from .managers import UserManager
# from projects.models import Project

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_at = models. DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True) 


class User(BaseModel,AbstractUser):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=254)
    email_verified = models.BooleanField(default=False)
    mobile= models.BigIntegerField(default=0)
    mobile_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.uuid)

    def invite(self, invite_profile):
        invite = Invite(inviter=self, invited=invite_profile)
        invites = invite_profile.received_invites.filter(inviter_id=self.id)
        if not len(invites) > 0:    # don't accept duplicated invites
            invite.save()

    def remove_friend(self, profile_id):
        friend = UserProfile.objects.filter(id=profile_id)[0]
        self.friends.remove(friend)

    @property
    def get_profile(self):
        profile = UserProfile.objects.filter(user=self)
        return profile

    @property
    def get_all_task_report(self):
        pass

    @property
    def get_pending_task(self):
        pass

    @property
    def get_overdue_task(self):
        pass

    @property
    def get_completed_task(self):
        pass

class Company(models.Model):
    social_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    found_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ('name',)


    def __str__(self):
        return (self.name)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # project = models.ManyToManyField(Project, blank=True)
    img = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return (str(self.user))


class Invite(BaseModel):
    inviter = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='made_invites')
    invited = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_invites')

    def accept(self):
        self.invited.friends.add(self.inviter)
        self.inviter.friends.add(self.invited)
        self.delete()

    def __str__(self):
        return str(self.inviter)