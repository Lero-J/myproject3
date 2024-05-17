from django.urls import path

from my_app import views

urlpatterns = [
    path('', views.show_info, name='app.info'),
    path('article/info/<int:article_id>', views.show_articles_info, name='article.info')
    # path('article/info/<int:article_id>', views.show_articles_info, name='article.info')
]



