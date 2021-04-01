from django import forms


class CreateNewPost(forms.Form):
    name = forms.CharField(label= "Post name", max_length=200)
    check = forms.BooleanField(required=False)
