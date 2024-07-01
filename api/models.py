from django.db import models

# Create your models here.


class Roles(models.Model):
    name = models.CharField(max_length=100)


class Permissions(models.Model):
    name = models.CharField(max_length=300)


class RolePermissions(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permissions, on_delete=models.CASCADE)


class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    email_verified_at = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=0)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)


class Partners(models.Model):
    company_name = models.CharField(max_length=30)
    activity_sector = models.CharField(max_length=50)
    rccm = models.IntegerField()
    turnover = models.IntegerField()
    web_site = models.CharField(max_length=50)
    manager_last_name = models.CharField(max_length=30)
    manager_first_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    sold = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Phonebooks(models.Model):
    type = models.CharField()
    name = models.CharField()
    phone = models.IntegerField()
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)


class Advertising(models.Model):
    content = models.CharField()
    status = models.CharField(default="En cours")


class PhonebookAdvertising(models.Model):
    phonebook = models.ForeignKey(Phonebooks, on_delete=models.CASCADE)
    advertising = models.ForeignKey(Advertising, on_delete=models.CASCADE)


class Allocationtypes(models.Model):
    type = models.CharField()


class PhonebookAllocationtypes(models.Model):
    phonebook = models.ForeignKey(Phonebooks, on_delete=models.CASCADE)
    allocationtype = models.ForeignKey(Allocationtypes, on_delete=models.CASCADE)
    default_amount = models.IntegerField()


class Transactions(models.Model):
    type = models.CharField()
    amount = models.IntegerField()
    status = models.CharField(null=True)
    phonebook = models.ForeignKey(Phonebooks, on_delete=models.CASCADE)


class Newsletters(models.Model):
    content = models.CharField()
    status = models.CharField()
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)


class PartenerNewsletter(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    newsletter = models.ForeignKey(Newsletters, on_delete=models.CASCADE)


class Deposits(models.Model):
    amount = models.IntegerField()
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)


class Notifications(models.Model):
    content = models.CharField()
    status = models.CharField()
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)


class Departments(models.Model):
    name = models.CharField()


class DepartmentAllocationtypes(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    allocationtype = models.ForeignKey(Allocationtypes, on_delete=models.CASCADE)
    default_amount = models.IntegerField()
