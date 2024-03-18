from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser,
        PermissionsMixin,
        BaseUserManager,
    )

class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, email, password):
        if not email:
            raise ValueError('please enter your email address')
        
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    # 슈퍼 유저 생성
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user      

# Createsuperuser -> email(option 선택), username(required 필수), password
# - email
# - password
# - nickname
# - is_business: personal, business
class User(AbstractBaseUser, PermissionsMixin):
    # CharField => VARCHAR(255) (VARCHAR 특징 : 가변성)
    email = models.CharField(max_length=255, unique=True) #
    nickname = models.CharField(max_length=255)
    is_bussiness = models.BooleanField(default=False)
    
    # PermissionMixin : 권한 관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager() #유저 생성 및 관리
    
    def __str__(self):
        return f'email: {self.email}, nickname:{self.nickname}'
    