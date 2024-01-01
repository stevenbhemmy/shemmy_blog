from django.db import models
from django.contrib.auth.models import User


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
    body = models.TextField(
        blank=True,
        verbose_name="Body Text.",
    )


class BlogCategory(models.Model):
    name = models.CharField(max_length=175)
    slug = models.SlugField()
    description = models.TextField(
        max_length=256,
        blank=True,
        verbose_name="Category description.",
    )


class BlogTag(models.Model):
    name = models.CharField(max_length=175)
    description = models.TextField(
        max_length=256,
        blank=True,
        verbose_name="Tag description.",
    )
