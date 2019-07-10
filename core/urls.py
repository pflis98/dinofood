from django.urls import path, include

from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

import bug_report.views
import main_app.views
import main_app.food_views.ingredient_views as ingredient_views
import main_app.food_views.cookingtools_views as cookingtools_views
import main_app.food_views.unit_views as unit_views
import main_app.food_views.recipe_views as recipe_views
import main_app.food_views.search_views as search_views
import main_app.food_views.cient_equipment_views as cient_equipment_views
import main_app.tests.test_views as test_views

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("test", main_app.views.test_view, name='test_view'),
    path('recipe/ajax/recipe/ing_unit', main_app.views.search_units, name="ing_unit"),
    path("", main_app.views.index, name="index"),
    # path("db/", base.views.db, name="db"),
    path("admin/", admin.site.urls),

    path('accounts/', include('accounts.urls')),  # first search in accounts app
    path('accounts/', include('django.contrib.auth.urls')),  # then in built in auth

    path("report", bug_report.views.bug_report, name="bug_report"),
    path("report/successful", bug_report.views.report_successful, name="report_successful"),

    path("recipe/", recipe_views.recipe, name="recipe"),
    path("recipe/new", recipe_views.add_recipe, name="add_recipe"),
    path("recipe/accept", recipe_views.accept_recipes, name="accept_recipes"),
    path("recipe/<int:object_id>", recipe_views.recipe_id, name="recipe_id"),
    path("recipe/<int:object_id>/delete", recipe_views.recipe_id_delete, name="recipe_delete"),
    path("recipe/<int:object_id>/accept", recipe_views.recipe_id_accept, name="recipe_accept"),
    path("recipe/<int:object_id>/rate", recipe_views.recipe_id_rate, name="recipe_rate"),

    path("recipe/search", search_views.recipe_search, name="search_recipe"),

    path("ingredient/", ingredient_views.IngredientList.as_view(), name="ingredient"),
    path("ingredient/new", ingredient_views.AddIngredient.as_view(), name="add_ingredient"),
    path("ingredient/<int:object_id>", ingredient_views.IngredientId.as_view(), name="ingredient_id"),
    path("ingredient/<int:object_id>/delete", ingredient_views.IngredientDelete.as_view(), name="ingredient_delete"),
    path("ingredient/<int:object_id>/update", ingredient_views.IngredientUpdate.as_view(), name="ingredient_update"),


    path("unit/", unit_views.UnitList.as_view(), name="unit"),
    path("unit/new", unit_views.AddUnit.as_view(), name="add_unit"),
    path("unit/<int:object_id>", unit_views.UnitId.as_view(), name="unit_id"),
    path("unit/<int:object_id>/delete", unit_views.UnitDelete.as_view(), name="unit_delete"),
    path("unit/<int:object_id>/update", unit_views.UnitUpdate.as_view(), name="unit_update"),

    path("cooking_tool/", cookingtools_views.CookingToolList.as_view(), name="cooking_tool"),
    path("cooking_tool/new", cookingtools_views.AddCookingTool.as_view(), name="add_cooking_tool"),
    path("cooking_tool/<int:object_id>", cookingtools_views.CookingToolId.as_view(), name="cooking_tool_id"),
    path("cooking_tool/<int:object_id>/delete", cookingtools_views.CookingToolDelete.as_view(),
         name="cooking_tool_delete"),
    path("cooking_tool/<int:object_id>/update", cookingtools_views.CookingToolUpdate.as_view(),
         name="cooking_tool_update"),

    path("fridge", cient_equipment_views.modify_fridge, name="fridge"),
    path("tools", cient_equipment_views.modify_tools, name="tools"),

    path("test/empty", main_app.tests.test_views.test_empty_database, name="test_empty_database"),
    path("test/default", main_app.tests.test_views.test_default_database, name="test_default_database"),
    path("test/save", main_app.tests.test_views.save_database_to_default, name="save_db_to_default"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
