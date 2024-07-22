from django.urls import path
from . import views

urlpatterns = [
    path('entry/', views.entry, name='entry'),
    path('b_entry/', views.b_entry, name='b_entry'),
    path('blog/', views.blog_list.as_view()),
    path('blog/<int:pk>/', views.blog_detail.as_view),

]
