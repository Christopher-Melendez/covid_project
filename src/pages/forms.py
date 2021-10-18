from django import forms
from heat_map.models import Map

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = [
            'map_choice'
        ]