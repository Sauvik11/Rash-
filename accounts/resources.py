from import_export import resources
from .models import carModel

class carModelResource(resources.ModelResource):
    class Meta:
        model = carModel 