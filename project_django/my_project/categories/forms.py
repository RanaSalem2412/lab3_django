from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name'].strip()  

        
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 letters")

        
        if Category.objects.filter(name__iexact=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This category name already exists. Please choose another name.")

        return name
