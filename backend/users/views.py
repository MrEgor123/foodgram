from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from djoser.views import UserViewSet

from api.pagination import CustomPagination
from api.serializers import CustomUserSerializer, SubscribeSerializer

from .models import Subscribe


User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = CustomPagination

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=[IsAuthenticated]
    )
    def subscribe(self, request, **kwargs):
        user = request.user
        author_id = self.kwargs.get('id')
        author = get_object_or_404(User, id=author_id)

        if request.method == 'POST':
            serializer = SubscribeSerializer(author,
                                             data=request.data,
                                             context={'request': request})
            serializer.is_valid(raise_exception=True)
            Subscribe.objects.create(user=user, author=author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            subscription = get_object_or_404(Subscribe,
                                             user=user,
                                             author=author)
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        permission_classes=[IsAuthenticated]
    )
    def subscriptions(self, request):
        user = request.user
        queryset = User.objects.filter(subscribing__user=user)
        pages = self.paginate_queryset(queryset)
        serializer = SubscribeSerializer(pages,
                                         many=True,
                                         context={'request': request})
        return self.get_paginated_response(serializer.data)

    @action(
        detail=False,
        methods=['put'],
        parser_classes=[MultiPartParser, FormParser],
        permission_classes=[IsAuthenticated]
    )
    def set_avatar(self, request):
        user = request.user
        avatar = request.FILES.get('avatar')

        if not avatar:
            return Response(
                {'detail': 'Файл не найден.'},
                status=status.HTTP_400_BAD_REQUEST)

        user.avatar = avatar
        user.save()
        return Response(
            {'detail': 'Аватарка обновлена.'},
            status=status.HTTP_200_OK)
