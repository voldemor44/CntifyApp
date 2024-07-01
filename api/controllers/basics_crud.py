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
        return Response({"status": "success", "message": "User was deleted"})


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
        return Response({"status": "success", "message": "Partner was deleted"})


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
        return Response({"status": "success", "message": "Contact was deleted"})


class AdvertisingViewset(APIView):

    def get(self, request, id=None):
        if id:
            advertising = Advertising.objects.get(id=id)
            advertising = AdvertisingSerializer(advertising)
            return Response(
                {"status": "success", "data": advertising.data}, status=status.HTTP_200_OK
            )

        advertisings = Advertising.objects.all()
        advertisings = AdvertisingSerializer(advertisings, many=True)
        return Response(
            {"status": "success", "data": advertisings.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        advertising = AdvertisingSerializer(data=request.data)
        if advertising.is_valid():
            advertising.save()
            return Response(
                {"status": "success", "data": advertising.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": advertising.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        advertising = Advertising.objects.get(id=id)
        advertising = AdvertisingSerializer(advertising, data=request.data, partial=True)
        if advertising.is_valid():
            advertising.save()
            return Response(
                {"status": "success", "data": advertising.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": advertising.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        advertising = Advertising.objects.filter(id=id)
        print(advertising)
        advertising.delete()
        return Response({"status": "success", "message": "Advertising was deleted"})


class NewslettersViewset(APIView):

    def get(self, request, id=None):
        if id:
            new = Newsletters.objects.get(id=id)
            new = NewslettersSerializer(new)
            return Response(
                {"status": "success", "data": new.data}, status=status.HTTP_200_OK
            )

        news = Newsletters.objects.all()
        news = NewslettersSerializer(news, many=True)
        return Response(
            {"status": "success", "data": news.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        new = NewslettersSerializer(data=request.data)
        if new.is_valid():
            new.save()
            return Response(
                {"status": "success", "data": new.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": new.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        new = Newsletters.objects.get(id=id)
        new = NewslettersSerializer(new, data=request.data, partial=True)
        if new.is_valid():
            new.save()
            return Response(
                {"status": "success", "data": new.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": new.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        new = Newsletters.objects.filter(id=id)
        print(new)
        new.delete()
        return Response({"status": "success", "message": "Newsletter was deleted"})


class NotificationsViewset(APIView):

    def get(self, request, id=None):
        if id:
            notification = Notifications.objects.get(id=id)
            notification = NotificationsSerializer(notification)
            return Response(
                {"status": "success", "data": notification.data}, status=status.HTTP_200_OK
            )

        notifications = Notifications.objects.all()
        notifications = NotificationsSerializer(notifications, many=True)
        return Response(
            {"status": "success", "data": notifications.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        notification = NotificationsSerializer(data=request.data)
        if notification.is_valid():
            notification.save()
            return Response(
                {"status": "success", "data": notification.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": notification.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        notification = Notifications.objects.get(id=id)
        notification = NotificationsSerializer(notification, data=request.data, partial=True)
        if notification.is_valid():
            notification.save()
            return Response(
                {"status": "success", "data": notification.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "success", "data": notification.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        notification = Notifications.objects.filter(id=id)
        print(notification)
        notification.delete()
        return Response({"status": "success", "message": "Product was deleted"})
