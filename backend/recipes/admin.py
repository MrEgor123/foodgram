from django.contrib import admin
from django.contrib.admin import display

from .models import (Favourite, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Subscribe, Tag, User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'author', 'added_in_favorites')
    readonly_fields = ('added_in_favorites',)
    list_filter = ('author', 'name', 'tags',)
    search_fields = ('name', 'author__username', 'tags__name')

    @display(description='Количество в избранных')
    def added_in_favorites(self, obj):
        return obj.favorites.count()

    def get_inlines(self, request, obj=None):
        # Inline для добавления ингредиентов к рецепту
        return [IngredientInRecipeInline]


class IngredientInRecipeInline(admin.TabularInline):
    model = IngredientInRecipe
    extra = 1
    min_num = 1
    verbose_name = "Ингредиент"
    verbose_name_plural = "Ингредиенты"


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount',)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)
    search_fields = ('user__username', 'author__username',)
