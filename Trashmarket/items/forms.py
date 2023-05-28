from django import forms
from .models import Items

INPUT_CLASSES = 'w-full py-6 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['Category', 'name', 'description', 'price', 'image']

        widgets = {
            'Category': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'description', 'price', 'image', 'is_sold']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }
