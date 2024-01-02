from django.urls import path

from .views import BlogArticleView, BlogTagListView, BlogCategoryListView

app_name = "blog"
urlpatterns = [
    path("tag/<name>/", BlogTagListView.as_view(), name="tag_articles"),
    path("category/<name>/", BlogCategoryListView.as_view(), name="category_articles"),
    path("<slug:slug>/", BlogArticleView.as_view(), name="article"),
]
