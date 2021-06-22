from django.urls import path
from . import views

app_name = 'blog' # allows using 'bloh:index' for url and reverse_lazy methods
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mine', views.MyView.as_view(), name='mine'),
    path('alpha', views.AlphaView.as_view(), name='alpha'),
    path('myalpha', views.MyAlphaView.as_view(), name='myalpha'),
    path('new', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
]
