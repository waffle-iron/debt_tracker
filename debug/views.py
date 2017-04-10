import pip
from django.shortcuts import render_to_response


def requirements(request):
    # TODO needs redirect or error message
    if request.user.is_superuser:
        installed_packages = sorted(pip.get_installed_distributions())
        installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])

        response = render_to_response('debug/requirements.html', locals())

        return response
