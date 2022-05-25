from django import forms
from .models import PaymentScreenshot, TaskResult






class PaymentForm(forms.ModelForm):  
    class Meta():
        model = PaymentScreenshot 
        fields = ('images',)

        widgets = {
            'images': forms.FileInput(attrs={"class":"form-control","name":"file","id":"InputName","placeholder":"Upload your screenshot"}),
        }




class TaskForm(forms.ModelForm):  
    class Meta():
        model = TaskResult 
        fields = ('result',)

        widgets = {
            'result': forms.FileInput(attrs={"class":"form-control","name":"file","id":"InputName","placeholder":"Upload your screenshot"}),
        }