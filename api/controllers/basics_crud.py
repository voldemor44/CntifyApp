from django.shortcuts import render, get_object_or_404
from ..models import *
from ..serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# For bascis tables


@api_view(["GET"])
def welcome(request):
    print("Welcome to Cntify API's test ! \n Happy Hacking :)")
    return Response("Welcome to Cntify API's test ! \n Happy Hacking :)")


class UsersViewset(APIView):

    def get(self, request, id=None):
        if id:
            user = Users.objects.get(id=id)
            user = UsersSerializer(user)
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )

        users = Users.objects.all()
        users = UsersSerializer(users, many=True)
        return Response(
            {"status": "success", "data": users.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        user = UsersSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": user.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        user = Users.objects.get(id=id)
        user = UsersSerializer(user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": user.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        user = Users.objects.filter(id=id)
        print(user)
        user.delete()
        return Response({"status": "success", "message": "Product was deleted"})


class PartnersViewset(APIView):

    def get(self, request, id=None):
        if id:
            partner = Partners.objects.get(id=id)
            partner = PartnersSerializer(partner)
            return Response(
                {"status": "success", "data": partner.data}, status=status.HTTP_200_OK
            )

        partners = Partners.objects.all()
        partners = PartnersSerializer(partners, many=True)
        return Response(
            {"status": "success", "data": partners.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        partner = PartnersSerializer(data=request.data)
        if partner.is_valid():
            partner.save()
            return Response(
                {"status": "success", "data": partner.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": partner.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        partner = Partners.objects.get(id=id)
        partner = PartnersSerializer(partner, data=request.data, partial=True)
        if partner.is_valid():
            partner.save()
            return Response(
                {"status": "success", "data": partner.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": partner.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        partner = Partners.objects.filter(id=id)
        print(partner)
        partner.delete()
        return Response({"status": "success", "message": "Product was deleted"})


class PhonebooksViewset(APIView):

    def get(self, request, id=None):
        if id:
            phone = Phonebooks.objects.get(id=id)
            phone = PhonebooksSerializer(phone)
            return Response(
                {"status": "success", "data": phone.data}, status=status.HTTP_200_OK
            )

        phones = Phonebooks.objects.all()
        phones = PhonebooksSerializer(phones, many=True)
        return Response(
            {"status": "success", "data": phones.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        phone = PhonebooksSerializer(data=request.data)
        if phone.is_valid():
            phone.save()
            return Response(
                {"status": "success", "data": phone.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": phone.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        phone = Phonebooks.objects.get(id=id)
        phone = PhonebooksSerializer(phone, data=request.data, partial=True)
        if phone.is_valid():
            phone.save()
            return Response(
                {"status": "success", "data": phone.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": phone.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        phone = Phonebooks.objects.filter(id=id)
        print(phone)
        phone.delete()
        return Response({"status": "success", "message": "Product was deleted"})


class AdvertisingViewset(APIView):

    def get(self, request, id=None):
        if id:
            user = Users.objects.get(id=id)
            user = UsersSerializer(user)
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )

        users = Users.objects.all()
        users = UsersSerializer(users, many=True)
        return Response(
            {"status": "success", "data": users.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        user = UsersSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": user.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        user = Users.objects.get(id=id)
        user = UsersSerializer(user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": user.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        user = Users.objects.filter(id=id)
        print(user)
        user.delete()
        return Response({"status": "success", "message": "Product was deleted"})


class NewslettersViewset(APIView):

    def get(self, request, id=None):
        if id:
            user = Users.objects.get(id=id)
            user = UsersSerializer(user)
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )

        users = Users.objects.all()
        users = UsersSerializer(users, many=True)
        return Response(
            {"status": "success", "data": users.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        user = UsersSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": user.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        user = Users.objects.get(id=id)
        user = UsersSerializer(user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": user.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        user = Users.objects.filter(id=id)
        print(user)
        user.delete()
        return Response({"status": "success", "message": "Product was deleted"})


class NotificationsViewset(APIView):

    def get(self, request, id=None):
        if id:
            user = Users.objects.get(id=id)
            user = UsersSerializer(user)
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )

        users = Users.objects.all()
        users = UsersSerializer(users, many=True)
        return Response(
            {"status": "success", "data": users.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        user = UsersSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": user.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        user = Users.objects.get(id=id)
        user = UsersSerializer(user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            return Response(
                {"status": "success", "data": user.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": user.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        user = Users.objects.filter(id=id)
        print(user)
        user.delete()
        return Response({"status": "success", "message": "Product was deleted"})
