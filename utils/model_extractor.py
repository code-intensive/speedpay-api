from django.db.models import Model
from rest_framework.serializers import ModelSerializer


def model_from_meta(serializer: ModelSerializer) -> Model:
    """Extracts model from a rest_framework ModelSerializer's Meta class"""

    assert type(serializer) is type(ModelSerializer), (
        "Serializer must be an subclass of "
        "rest_framework.serializers.ModelSerializer "
        f"not {serializer.__class__}"
    )
    return serializer.Meta.model
