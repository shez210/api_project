from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets

from api_app.models import Information
from api_app.serializer import UserSerializer, InformationSerializer


UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def check_permissions(self, request):
        if self.action in "create":
            return True
            return super(UserViewSet, self).check_permissions(request)

    # permission_classes = (DjangoModelPermissions,)

    # @detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf])
    # @detail_route(methods=['post'])
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    # def create(self, request, pk=None, format=None):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #     try:
    #         user = UserModel.objects.create(first_name=request.data['first_name'], last_name=request.data['last_name'], email=request.data['email'], username=request.data['username'])
    #         user.set_password(request.data['password'])
    #
    #         return Response(self.get_serializer(user, many=False).data)
    #     except KeyError:
    #         raise ParseError('Review parameters passed')


    # def update(self, request, *args, **kwargs):
    #     serializer = UserSerializer(self.get_object(pk), data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


