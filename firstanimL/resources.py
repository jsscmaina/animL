from import_export import resources
from .models import Symptoms, Observation


class SymptomsResource(resources.ModelResource):
    class Meta:
        model = Symptoms


class ObserveResource(resources.ModelResource):
    class Meta:
        model = Observation
