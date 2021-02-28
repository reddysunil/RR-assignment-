from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Users
from .serializers import UserSerializer,registerSerializer,UserSerializer2
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


# Create your views here.

@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        users=Users.objects.all()
        serializer=UserSerializer2(users,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=UserSerializer2(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class register(generics.GenericAPIView):
    serializer_class = registerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



# @api_view(['POST','GET'])
# def register(request):
#     if request.method == 'POST':
#         serializer = registerserializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
        
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         users = User.objects.all()
#         serializer = registerserializer(users,many=True)
#         return Response(serializer.data)
# @api_view(['POST'])
# def login(request):
#     if request.method == 'POST':
#         # print(request.data)
#         # print(request.POST['password'])
#         serializer = loginserializer(data = request.data)
#         if serializer.is_valid():
#             user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
#             if user is not None:
#                 return Response(serializer.data, status = status.HTTP_201_CREATED)
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
