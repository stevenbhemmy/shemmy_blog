from django.contrib import admin


from .models import BlogArticle, BlogCategory, BlogTag


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "author",
        "created",
        "published",
    )


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "description",
    )


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
