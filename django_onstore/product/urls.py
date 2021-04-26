from django.urls import path, include


from product import views


urlpatterns = [
    path('latest-products/', views.LatestProcductsList.as_view()),
    path('products/search/', views.search),
    path('products/add/', views.additem),
    path('products/deleteItem/',views.deleteitem),
    path('products/updateItem/',views.updateitem),
    path('products/',views.ProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/',views.CategoryDetail.as_view())
]
