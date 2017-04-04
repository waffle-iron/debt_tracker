from debug import packages_view


def requirements(request):
    return packages_view.getView()
