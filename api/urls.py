from django.urls import include, path
from . import views

urlpatterns = [
    path('user/', views.UserView.as_view(), name='user'),
    path('user/watchlist', views.UserWatchlistView.as_view(), name='watchlist'),
    #path('user/alert', views.User.AlertsView.as_view(), name='alert'),
    path('currencies/<currency_id>', views.CurrenciesView.as_view(), name='currencies'),
    path('currencies/', views.CurrenciesView.as_view(), name='currencies')
]