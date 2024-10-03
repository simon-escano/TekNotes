from django import forms
from .models import Note, Course, Tag

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'course', 'tags']

    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Title',
        'class': 'placeholder-gray-500 text-gray-700 bg-transparent border-none focus:outline-none flex-1'
    }))

    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Content',
        'class': 'placeholder-gray-500 text-gray-700 bg-transparent border-none focus:outline-none flex-1 resize-none', 
        'rows': 5
    }))

    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={
        'class': 'placeholder-gray-500 text-gray-700 bg-transparent border-none focus:outline-none flex-1'
    }))

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.SelectMultiple(attrs={
        'class': 'placeholder-gray-500 text-gray-700 bg-transparent border-none focus:outline-none flex-1'
    }))
