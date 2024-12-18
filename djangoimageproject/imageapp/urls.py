from django.urls import path
from . import views  # Import views from the current directory (your app)

urlpatterns = [
    # URL for listing items
    path('', views.item_list, name='item_list'),  # This will be the home page that lists the items

    # URL for creating an item
    path('create/', views.item_create, name='item_create'),  # Form to create an item

    # URL for updating an item
    path('update/<int:pk>/', views.item_update, name='item_update'),
    # Update an existing item using its primary key (pk)

    # URL for deleting an item
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),  # Delete an item using its pk
]
