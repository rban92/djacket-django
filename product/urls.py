from django.urls import path
from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductView.as_view()),
    path('products/<slug:category_slug>/', views.CategoryView.as_view()),
    
]