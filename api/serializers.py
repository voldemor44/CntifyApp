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


class Role_PermissionSerializer(ModelSerializer):
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
