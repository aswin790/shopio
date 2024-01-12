from django import forms
from . models import item


CLASS_FORMS = ' w-100 border form-control-lg'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name','category','description','location','year','image','price']
        widgets = {
            'category':forms.Select(attrs={
                'class': CLASS_FORMS
            }),
            'name':forms.TextInput(attrs={
                'class': CLASS_FORMS
            }),
            'description':forms.Textarea(attrs={
                'class': 'w-100 border'
            }),
            'location':forms.TextInput(attrs={
                'class': CLASS_FORMS
            }),
            'year':forms.TextInput(attrs={
                'class': CLASS_FORMS
            }),
            'price':forms.TextInput(attrs={
                'class': CLASS_FORMS
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name','description','location','year','image','price','is_sold']
        widgets = {
            
            'name':forms.TextInput(attrs={
                'class': CLASS_FORMS
            }),
            'description':forms.Textarea(attrs={
                'class': 'w-100 border'
            }),
            'location':forms.TextInput(attrs={
                'class': CLASS_FORMS
            }),
            'year':forms.TextInput(attrs={
                'class': CLASS_FORMS
            }),
            'price':forms.TextInput(attrs={
                'class': CLASS_FORMS
            })
        }