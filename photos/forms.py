from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'customer_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'email': forms.EmailInput(
                attrs={'class':'form-control'}
            ),

            'event_date': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':4
                }
            ),
        }