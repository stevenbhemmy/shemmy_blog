from django.views.generic import TemplateView

from .models import BlogArticle


class BlogArticleView(TemplateView):
    template_name = "blog_article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = BlogArticle.objects.get(slug=self.kwargs["slug"])
        context["blog"] = blog
        return context
