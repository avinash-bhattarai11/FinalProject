from django.urls import path
from products import views
urlpatterns=[
    path('',views.home, name='products-home'),
    path('create',views.create,name='create'),
    path('<int:product_id>',views.detail,name='detail'),
    path('<int:product_id>/add_comment',views.add_comment,name='add-comment'),

]
