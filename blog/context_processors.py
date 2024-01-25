from .models import Page


def menu_items(request):
    return {"page_items": Page.objects.all()}
