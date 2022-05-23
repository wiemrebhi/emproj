from django.db import models





# Create your models here.
class Employee(models.Model):
    POSITION_CHOICES = (
       ('Manager', 'manager'),
       ('Developer', 'developer'),
       ('Designer', 'designer'),
     )
    TEAM_CHOICES=(
        ('DevOps team','devops team'),
       ('Dev team','dev team'),
       ('Design team','design team'),
                 )
    id_carte=models.CharField(primary_key='true',max_length=50,unique='true')
    name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    birth_date =models.DateField(null=True) 
    Email = models.EmailField()
    Phone = models.CharField(max_length=50)
    hired_on = models.DateField(null=True) 
    position= models.CharField(max_length=50,null=True,choices=POSITION_CHOICES)
    
   

    class Meta:
        db_table = "employee"



class Team(models.Model):
    TEAM_CHOICES=(
       ('DevOps team','devops team'),
       ('Dev team','dev team'),
        ('Design team','design team'),
    )
    TEAM=models.CharField(max_length=50,null=True,choices=TEAM_CHOICES)
    employe=models.ForeignKey(Employee,related_name='Manager',on_delete=models.CASCADE,null=True)

    class Meta:
       db_table = "team"
