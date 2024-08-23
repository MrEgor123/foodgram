from datetime import datetime 

from django.db.models import Sum
from recipes.models import Ingredient


from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet


from .pagination import CustomPagination
from .serializers import IngredientSerializer
from .permissions import IsAdminOrReadOnly, IsAdminOrReadOnly


class IngredientViewSet(ReadOnlyModelViewSet):
    gueryset = Ingredient.objects.all()
    serializers_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)

