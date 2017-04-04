import pip
from django.http import HttpResponse


def getView():
    html = "<h1>Required Packages:</h1>"

    for package in getPackages():
        html += "<p>%s</p>" % package

    return HttpResponse(html)


def getPackages():
    installed_packages = pip.get_installed_distributions()
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
    return installed_packages_list
