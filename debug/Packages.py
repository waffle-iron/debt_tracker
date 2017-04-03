import pip


def getPackages():
    installed_packages = pip.get_installed_distributions()
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
    return installed_packages_list
