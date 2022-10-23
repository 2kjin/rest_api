from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articels/<int:articel_pk>/comments/', views.comment_create),
]


# $ python -m venv venv
# $ source venv/Scripts/activate
# $ pip install djangorestframework
# $ pip freeze > requirements.txt
# $ pip install -r requirements.txt