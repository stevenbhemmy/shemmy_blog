from django.contrib import admin


from .models import Page, BlogArticle, BlogCategory, BlogTag


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


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )

    def title(self, obj):
        return obj.blog.title

    def slug(self, obj):
        return obj.blog.title
