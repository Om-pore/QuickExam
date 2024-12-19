from django.urls import path
from . import views

urlpatterns = [
    path('all_exam', views.all_exam_view, name='all_exam'),
    path('search/<str:category>', views.search_view, name='search'),
    path('<int:exam_id>', views.exam_view, name='exam'),
    
]
