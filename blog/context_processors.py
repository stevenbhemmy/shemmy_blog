from .models import Page


def menu_items(request):
    return {"menu_items": Page.objects.all()}
