from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LifeSituation, Service, Process, CustomUser
from .serializers.life_situation_serializers import LifeSituationRetrieveSerializer, LifeSituationCreateSerializer, \
    LifeSituationUpdateSerializer, LifeSituationSerializer, LifeSituationListSerializer
from .serializers.process_serializers import ProcessSerializer, ProcessRetrieveSerializer, ProcessCreateSerializer, \
    ProcessUpdateSerializer
from .serializers.service_serializers import ServiceSerializer, ServiceRetrieveSerializer, ServiceCreateSerializer, \
    ServiceUpdateSerializer
from .serializers.user_serialzers import UserSerializer, UserRetrieveSerializer
from .utils import generate_identifier, CustomModelViewSet
import random
import string


class UserViewSet(CustomModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    serializer_list = {
        'retrieve': UserRetrieveSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def reset_password(self, request, pk=None):
        user = self.get_object()
        print('user', user)
        email = request.data.get('email')
        print('email', email)
        new_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        print('new_password', new_password)

        user.set_password(new_password)
        user.save()
        print('user.save()', user)

        recipients = mail.send(
            email, DEFAULT_FROM_EMAIL,
            subject='Сброс пароля',
            message=f'Ваш новый пароль: {new_password}',
            priority='now')

        Response(recipients, status=status.HTTP_201_CREATED)


class LifeSituationViewSet(CustomModelViewSet):
    queryset = LifeSituation.objects.all()
    serializer_class = LifeSituationSerializer
    serializer_list = {
        'list': LifeSituationListSerializer,
        'retrieve': LifeSituationRetrieveSerializer,
        'create': LifeSituationCreateSerializer,
        'update': LifeSituationUpdateSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        organization = user.organization
        queryset = LifeSituation.objects.filter(user__organization=organization)
        return queryset

    def list(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        search_string = self.request.query_params.get('search', None)
        if search_string:
            queryset = queryset.filter(Q(name__icontains=search_string) | Q(services__name__icontains=search_string))
        page = self.paginate_queryset(queryset)
        serializer = LifeSituationListSerializer(page, many=True) if page else LifeSituationListSerializer(queryset,
                                                                                                           many=True)
        return self.get_paginated_response(serializer.data) if page else Response(serializer.data,
                                                                                  status=status.HTTP_200_OK)


class ServiceViewSet(CustomModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    serializer_list = {
        'list': ServiceRetrieveSerializer,
        'retrieve': ServiceRetrieveSerializer,
        'create': ServiceCreateSerializer,
        'update': ServiceUpdateSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        organization = user.organization
        queryset = LifeSituation.objects.filter(user__organization=organization)
        return queryset

    def list(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        search_string = self.request.query_params.get('search', None)
        if search_string:
            queryset = queryset.filter(Q(name__icontains=search_string) | Q(services__name__icontains=search_string))
        page = self.paginate_queryset(queryset)
        serializer = ServiceRetrieveSerializer(page, many=True) if page else ServiceRetrieveSerializer(queryset,
                                                                                                       many=True)
        return self.get_paginated_response(serializer.data) if page else Response(serializer.data,
                                                                                  status=status.HTTP_200_OK)


class ProcessViewSet(CustomModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    serializer_list = {
        'list': ProcessRetrieveSerializer,
        'retrieve': ProcessRetrieveSerializer,
        'create': ProcessCreateSerializer,
        'update': ProcessUpdateSerializer,
    }
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def generate_identifier(self, request):
        identifier = generate_identifier(user=request.user)
        return Response({'identifier': identifier}, status=status.HTTP_200_OK)
