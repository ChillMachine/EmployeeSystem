from django.db import models
from datetime import date

family_statuses = [('Холост', 'Холост'),('Женат', 'Женат'),('В разводе', 'В разводе')]
groups = [('-','-'),('Группа 1','Группа 1'),('Группа 2','Группа 2'),('Группа 3','Группа 3'),('Группа 4','Группа 4'),('Группа 5','Группа 5')]

class Rank(models.Model):
    rank_name = models.CharField(max_length=20, unique=True)
    salary = models.CharField(max_length=10)

class Post(models.Model):
    post_name = models.CharField(max_length=20, unique=True)
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    salary = models.CharField(max_length=10)

class Employee(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    third_name = models.CharField(max_length=20) 
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    b_day = models.DateField()
    personal_num = models.CharField(max_length=4, unique=True)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=20)
    group_num = models.CharField(max_length=10, choices=groups)
    family_status = models.CharField(max_length=10, choices=family_statuses)
    place_of_bd = models.CharField(max_length=20)
    appointment_order_num = models.CharField(max_length=10)
    appointment_order_date = models.DateField()

class Auto(models.Model):
    model = models.CharField(max_length=20)
    gos_num = models.CharField(max_length=10)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

# class Scedule(models.Model):

class Promotions(models.Model):
    promotion_type = models.CharField(max_length=20)
    rights = models.CharField(max_length=20)
    date_of_rec = models.DateField()
    order_num = models.CharField(max_length=10, default='-')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, blank=True)

class Property(models.Model):
    name = models.CharField(max_length=20)
    inv_num = models.CharField(max_length=20, default='-', blank=True)
    date_of_rec = models.DateField()
    description = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, default='Выдано')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Relatives(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    third_name = models.CharField(max_length=20) 
    relation_degree = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12, default='-', blank=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Training(models.Model):
    thread_code = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)
    start_date = models.DateField()
    duratin = models.CharField(max_length=10)
    description = models.CharField(max_length=50, default='-', blank=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Weapons(models.Model):
    weapon_name = models.CharField(max_length=20)
    count = models.IntegerField(default=1, blank=True)
    weapon_num = models.CharField(max_length=20)
    date_of_rec = models.DateField()
    description = models.CharField(max_length=50, default='-')
    status = models.CharField(max_length=20, default='-')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Vaccination(models.Model):
    vaccine_name = models.CharField(max_length=20)
    date = models.DateField()
    description = models.CharField(max_length=50, blank=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Education(models.Model):
    grade = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)
    date_of_graduate = models.DateField()
    speciality = models.CharField(max_length=20, default='-')
    description = models.CharField(max_length=50)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Driver_license(models.Model):
    A = models.BooleanField()
    B = models.BooleanField()
    BE = models.BooleanField()
    C = models.BooleanField()
    CE = models.BooleanField()
    D = models.BooleanField()
    DE = models.BooleanField()
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key = True)

class Clothing_sizes(models.Model):
    head_size = models.CharField(max_length=10)
    shoes_size = models.CharField(max_length=10)
    cloth_size = models.CharField(max_length=10)
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key = True)

