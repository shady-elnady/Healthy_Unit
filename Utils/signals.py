# from django.db.models.signals import pre_save
# from django.dispatch import receiver

# from .models import BaseNamePolymorphicModel


# @receiver(pre_save, sender=BaseNamePolymorphicModel)
# def pre_save_polymorphic_model(sender, instance, **kwargs):

#     try:
#         object = BaseNamePolymorphicModel.objects.filter(name= instance.name)
#         if object.count() > 0 :
#             instance.descriptions= f"{object[0].descriptions},{instance.__class__.__name__}"
#     except BaseNamePolymorphicModel.DoesNotExist:
#         instance.descriptions = f"{instance.__class__.__name__}"