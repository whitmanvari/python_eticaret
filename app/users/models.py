from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.text import slugify

#custom user model
class CustomUserManager(BaseUserManager):
    #extra_fields lan örneğin first_name, last_name gibi diğer bilgileri yakalar. 
    def create_user(self, email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email must be set.")
        #örn: #GMAİL.COM yazıldıysa küçük harfe çevirerek standartlaştırır. 
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        #hemen metin olarak passwordü kaydetmez, hashler
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        #is_staff kullanıcının admin paneline erişebilmesi için gerekli flagi zorunlu kılar. 
        extra_fields.setdefault("is_staff", True)
        #is_superuser ise kullanıcıya tüm yetkileri tanımlayan superuser bayrağını zorunlu kılar.
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email= models.EmailField(unique=True)
    phone= models.CharField(max_length=20)
    #login işlemlerinde email ile giriş yapsın
    USERNAME_FIELD= "email"
    REQUIRED_FIELDS = []

    objects= CustomUserManager()

    #kullanıcı nesnesi veritabanına yazılmadan hemen önce çalışan bir hooktur.
    def save(self, *args, **kwargs):
        if not self.username and self.email:
            base_username= self.email.split('@')[0]
            #slugify özel karakterleri temizler ve URL için uygun formata getirir örn: irem&can---> iremcan
            username=slugify(base_username)
            counter = 1
            # aynı isimde bulursa test'se mesela, test1, test2 diye unique username nulana kadar artırır.
            while self.__class__.objects.filter(username=username).exists():
                username= f"{slugify(base_username)}{counter}"
                counter += 1
            self.username=username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

