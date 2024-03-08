from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('menu-items', views.MenuItemListView.as_view()),
    path('menu-items/category', views.CategoryView.as_view()),
    path('menu-items/<int:pk>', views.MenuItemDetailView.as_view()),
    path('groups/managers/users', views.ManagersListView.as_view()),
    path('groups/managers/users/<int:pk>', views.ManagersRemoveView.as_view()),
    path('groups/delivery-crew/users', views.DeliveryCrewListView.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.DeliveryCrewRemoveView.as_view()),
    path('cart/menu-items', views.CartOperationsView.as_view()),
    path('orders', views.OrderOperationsView.as_view()),
    path('orders/<int:pk>', views.SingleOrderView.as_view()),
]



# as per Meta

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('categories', views.CategoriesView.as_view()),
#     path('menu-items', views.MenuItemsView.as_view()),
#     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
#     path('cart/menu-items', views.CartView.as_view()),
#     path('orders', views.OrderView.as_view()),
#     path('orders/<int:pk>', views.SingleOrderView.as_view()),
#     path('groups/manager/users', views.GroupViewSet.as_view(
#         {'get': 'list', 'post': 'create', 'delete': 'destroy'})),

#     path('groups/delivery-crew/users', views.DeliveryCrewViewSet.as_view(
#         {'get': 'list', 'post': 'create', 'delete': 'destroy'}))
# ]