from rest_framework.serializers import ModelSerializer
from .models import *


class RolesSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class PermissionsSerializer(ModelSerializer):
    class Meta:
        model = Permissions
        fields = "__all__"


class RolePermissionSerializer(ModelSerializer):
    class Meta:
        model = RolePermissions
        fields = "__all__"


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class PartnersSerializer(ModelSerializer):
    class Meta:
        model = Partners
        fields = "__all__"


class PhonebooksSerializer(ModelSerializer):
    class Meta:
        model = Phonebooks
        fields = "__all__"
 
        
class AdvertisingSerializer(ModelSerializer):
    class Meta:
        model = Advertising
        fields = "__all__"


class NewslettersSerializer(ModelSerializer):
    class Meta:
        model = Newsletters
        fields = "__all__"
        

class NotificationsSerializer(ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"


class PhonebookAdvertisingSerializer(ModelSerializer):
    class Meta:
        model = PhonebookAdvertising
        fields = "__all__"


class AllocationTypeSerializer(ModelSerializer):
    class Meta:
        model = Allocationtypes
        fields = "__all__"


class PhoneAllocationTypeSerializer(ModelSerializer):
    class Meta:
        model = PhonebookAllocationtypes
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class DepositsSerializer(ModelSerializer):
    class Meta:
        model = Deposits
        fields = "__all__"


class DepartmentsSerializer(ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"


class DepartmentAllocationTypesSerializer(ModelSerializer):
    class Meta:
        model = DepartmentAllocationtypes
        fields = "__all__"
