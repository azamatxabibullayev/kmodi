from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),

    # Category
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Material
    path('materials/', views.material_list, name='material_list'),
    path('materials/create/', views.material_create, name='material_create'),
    path('materials/<int:pk>/edit/', views.material_edit, name='material_edit'),
    path('materials/<int:pk>/delete/', views.material_delete, name='material_delete'),

    # MaterialProgress
    path('progress/', views.progress_list, name='progress_list'),
    path('progress/create/', views.progress_create, name='progress_create'),
    path('progress/<int:pk>/edit/', views.progress_edit, name='progress_edit'),
    path('progress/<int:pk>/delete/', views.progress_delete, name='progress_delete'),

    # LibraryBook
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # SalfedjioVideo
    path('videos/', views.video_list, name='video_list'),
    path('videos/create/', views.video_create, name='video_create'),
    path('videos/<int:pk>/edit/', views.video_edit, name='video_edit'),
    path('videos/<int:pk>/delete/', views.video_delete, name='video_delete'),

    # YouTubeRecommendation
    path('recommendations/', views.recommendation_list, name='recommendation_list'),
    path('recommendations/create/', views.recommendation_create, name='recommendation_create'),
    path('recommendations/<int:pk>/edit/', views.recommendation_edit, name='recommendation_edit'),
    path('recommendations/<int:pk>/delete/', views.recommendation_delete, name='recommendation_delete'),

    # TeamMember
    path('team/', views.team_list, name='team_list'),
    path('team/create/', views.team_create, name='team_create'),
    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),

    # Student (User with role='student')
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
]
