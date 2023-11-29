from django import forms
from .models import Comment
from crispy_forms.helper import FromHelper 
from crispy_forms.layout import Layout, Submit

# Create Model for the forms 

class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['author', 'body', 'created_on']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FromHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'author',
            'created_on',
            'body',
            Submit('submit','Submit, css_class='btn-primary')
        )