import pip
from django.shortcuts import render_to_response


def requirements(request):
    installed_packages = ""
    installed_packages_list = sorted(pip.get_installed_distributions())

    response = render_to_response('debug/requirements.html', locals())

    return response
