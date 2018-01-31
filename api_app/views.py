import json
import sys

from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import views

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from api_app.models import Information
from api_app.serializer import InformationSerializer

from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

# class InformationViewSet(viewsets.ModelViewSet):
#     queryset = Information.objects.all()
#     serializer_class = InformationSerializer
#
#     def create(self, request, *args, **kwargs):
#
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             information = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({
#             'status': 'Bad request',
#             'message': 'Lounge Area could not be created with received data.'
#         }, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, *args, **wargs):
    #     if self.queryset.filter(id=request.data).count() != 0:
    #         instance = self.queryset.get(id=request.data)
    #         if LoungeAreaMember.objects.filter(lounge_area=instance,
    #                                            email=str(request.user.email)).count() == 0 and instance.is_restricted:
    #             return Response({
    #                 'status': 'Bad request',
    #                 'message': 'Solutions Hub Not Found'
    #             }, status=status.HTTP_404_NOT_FOUND)
    #         serializer = self.serializer_class(instance)
    #         return Response(serializer.data)
    #     return Response({
    #         'status': 'Bad request',
    #         'message': 'Solutions Hub Not Found'
    #     }, status=status.HTTP_404_NOT_FOUND)

# i need urls.py file
# @method_decorator(csrf_exempt, name="dispatch")
# class SignInAuthenticate(views.APIView):
#     """
#     This class handles request for signIn authentication
#     """
#     @csrf_exempt
#     def post(self, request):
#         """
#             This function handles the request for authenticating the user
#             :param request: request contains data information for a new user
#             :return: returns "welcome" if user exists, "wrong username or password" if user does not exists and an
#             error message is exception occures
#             """
#
#         if request.method == "POST":
#             #data = request.query_params.dict()
#             #print("-------", data)
#             user_name = request.POST.get("username")
#             password = request.POST.get("password")
#
#             #csrf_token = csrf.get_token(request)
#             #print(csrf_token)
#
#             # the reason for the error is because you are not passing a csrftoken to postrequest
#             # django restricts it for securitiy reasons. you can disable it but its not recommended
#             # if maknig request from the same site you won't get the error
#
#
#             # did i pass the username/password in postman, yes
#             #print(data, user_name, password)
#
#             ##
#
#             #auth = CustomUserAuth()
#             user = authenticate(username=user_name, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 # serialized = SocialUserSerializer(user)
#                 # return Response(serialized.data)
#
#             else:
#                 return Response({
#                     'status': 'Unauthorized',
#                     'message': 'Username/password combination invalid.'
#                 }, status=status.HTTP_401_UNAUTHORIZED)
#
#             sys.stdout.flush()
#         else:
#             return Response({
#                 'status': 'Unauthorized',
#                 'message': 'Username/password combination invalid.'
#             }, status=status.HTTP_401_UNAUTHORIZED)
