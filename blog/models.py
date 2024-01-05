from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Page(models.Model):
    # pages are just blogs pinned as main menu item, for now
    # creating separate object in case other objects can be pinned
    # later on
    blog = models.ForeignKey(
        "BlogArticle",
        on_delete=models.CASCADE,
    )


class BlogArticle(models.Model):
    author = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    category = models.ForeignKey(
        "BlogCategory",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    tags = models.ManyToManyField(
        "BlogTag",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=175)
    slug = models.SlugField()
    short_description = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="Short Description",
    )
    description = models.TextField(
        max_length=1024,
        blank=True,
        verbose_name="Description.",
    )
    body = RichTextField(
        blank=True,
        verbose_name="Body Text.",
    )

    def __str__(self):
        return f"{self.title} -- {self.author}"


class BlogCategory(models.Model):
    name = models.CharField(max_length=175)
    slug = models.SlugField()
    description = models.TextField(
        max_length=256,
        blank=True,
        verbose_name="Category description.",
    )

    def __str__(self):
        return self.name


class BlogTag(models.Model):
    name = models.CharField(max_length=175)
    description = models.TextField(
        max_length=256,
        blank=True,
        verbose_name="Tag description.",
    )

    def __str__(self):
        return self.name
