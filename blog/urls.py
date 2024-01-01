from django.urls import path

from .views import BlogArticleView

urlpatterns = [
    path("<slug:slug>/", BlogArticleView.as_view(), name="blog_article"),
]
