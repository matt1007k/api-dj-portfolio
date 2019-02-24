# All resource operation of CRUD urls
from categories.api.views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, base_name='categories')
urlpatterns = router.urls



# for each operation of CRUD urls

#from django.urls import path
#from .views import(
#    CategoryListView,
#    CategoryDetailView,
#    CategoryCreateView,
#    CategoryUpdateView,
#    CategoryDeleteView
#)

#urlpatterns = [
#    path('', CategoryListView.as_view()),
#    path('create/', CategoryCreateView.as_view()),
#    path('<pk>', CategoryDetailView.as_view()),
#    path('<pk>/update/', CategoryUpdateView.as_view()),
#    path('<pk>.delete/', CategoryDeleteView.as_view())
#]
