import pip
from django.http import HttpResponse

from debug import Packages


def requirements(request):
    packages = Packages.getPackages()
    return HttpResponse("Required Packages:\n" + packages)
