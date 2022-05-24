from django import forms
from .models import PaymentScreenshot 






class PaymentForm(forms.ModelForm):  
    class Meta():
        model = PaymentScreenshot 
        fields = ('images',)

        widgets = {
            'images': forms.FileInput(attrs={"class":"form-control","name":"file","id":"InputName","placeholder":"Upload your screenshot"}),
        }