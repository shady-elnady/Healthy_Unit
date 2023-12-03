from django.contrib import admin
from django.apps import apps
from django.conf import settings
from django.forms import Widget
from django.utils.translation import gettext_lazy as _

# from import_export import fields, resources
# from import_export.fields import Field
# from import_export.admin import ImportExportModelAdmin
# from import_export.admin import ImportExportActionModelAdmin

# # from guardian.admin import GuardedModelAdmin

# # Register your models here.

# class BookResource(resources.ModelResource):
#     delete = fields.Field(widget=Widget.BooleanWidget())

#     def for_delete(self, row, instance):
#         return self.fields['delete'].clean(row)

#     class Meta:
#         model = Book


models = apps.get_models()
# post_models = apps.get_app_config('post').get_models()


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


# # class BookResource(resources.ModelResource):

# #     class Meta:
# #         model = Book
# #         fields = ('id', 'name', 'author', 'price',)
# #         export_order = ('id', 'price', 'author', 'name')
# #         exclude = ('imported', )
# #         export_order = ('id', 'price', 'author', 'name')
# #         widgets = {
# #                 'published': {'format': '%d.%m.%Y'},
# #                 }


# # class BookAdmin(ImportExportModelAdmin):
# #     resource_classes = [BookResource]


# # class BookAdmin(ImportExportActionModelAdmin):
# #     pass


# # admin.site.register(Book, BookAdmin)


# # class BookNameResource(resources.ModelResource):

# #     class Meta:
# #         model = Book
# #         fields = ['id', 'name']
# #         name = "Export/Import only book names"


# # class CustomBookAdmin(ImportMixin, admin.ModelAdmin):
# #     resource_classes = [BookResource, BookNameResource]


# # class ProjectAdmin(GuardedModelAdmin):
# #     pass


# # for model in models:
# #     try:
# #         admin.site.register(model, ProjectAdmin)
# #     except admin.sites.AlreadyRegistered:
# #         pass
