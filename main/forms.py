from django import forms


class CreateNewPost(forms.Form):
    name = forms.CharField(label= "Post title", max_length=200)
    text = forms.CharField(label= "Post text", widget=forms.Textarea)
    public = forms.BooleanField(label="Make public", required=False)
