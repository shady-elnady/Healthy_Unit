from os.path import join


def upload_image_to(instance, fileName):
    extention = fileName.split(".")[-1]
    imgName = getattr(instance, f"{instance.id}", f"{instance.pk}")
    instanceName = getattr(instance, f"{instance.name}", f"{instance.pk}")
    newName = f"{imgName}.{extention}"
    return str(join("images", f"{instance.__class__.__name__}s", instanceName, newName))


def upload_svg_to(instance, fileName):
    extention = fileName.split(".")[-1]
    imgName = getattr(instance, f"{instance.id}", f"{instance.pk}")
    newName = f"{imgName}.{extention}"
    return str(join("svg", f"{instance.__class__.__name__}s/", newName))


def upload_file_to(instance, fileName):
    extention = fileName.split(".")[-1]
    imgName = getattr(instance, f"{instance.id}", f"{instance.pk}")
    newName = f"{imgName}.{extention}"
    return str(join("files", f"{instance.__class__.__name__}s/", newName))


def upload_logo_to(instance, fileName):
    extention = fileName.split(".")[-1]
    imgName = getattr(instance, f"{instance.id}", f"{instance.pk}")
    instanceName = getattr(instance, f"{instance.name}", f"{instance.pk}")
    newName = f"{imgName}.{extention}"
    return str(join("logo", f"{instance.__class__.__name__}s/", instanceName, newName))
