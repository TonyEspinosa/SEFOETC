from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class m_user(models.Model):
    pass
#   id_user = models.AutoField(primary_key = True, db_column='id_user')

#    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

#    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name = "Creación")
    
#    class Meta:
#        db_table = 'u_user'
#        verbose_name = "Usuario"
#        verbose_name_plural = "Usuarios"
#        ordering = ["user"]

#    def __str__(self):
#        return self.user.username