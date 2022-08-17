from django import forms


class AvailabilityForm(forms.Form):
    location = forms.CharField(max_length=256)
    pickup_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M"])
    return_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M"])
