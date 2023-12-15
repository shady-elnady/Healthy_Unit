from django.db.models import Model


class TemplateModelUtils:
    model: Model = None
    op_serializer = None
    ip_serializer = None

    ALLOWED_PUT_FIELDS = tuple()
    GET_PARAM_CHOICES = tuple()

    @classmethod
    def search_instances(cls):
        pass

    @classmethod
    def get_instance(cls):
        pass

    @classmethod
    def create_instance(cls):
        pass

    @classmethod
    def edit_instance(cls):
        pass

    @classmethod
    def delete_instance(cls):
        pass
