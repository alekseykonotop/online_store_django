from store.models import Category


def navigation_menu(request):
    return {'main_categories': Category.objects.filter(parent__isnull=True)}
