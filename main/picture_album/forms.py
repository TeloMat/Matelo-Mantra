from django import forms

from main.picture_album.models import PictureAlbum


class CreateNewAlbum(forms.Form):

    title = forms.CharField(label="Album title", max_length=200)
    description = forms.CharField(label="Album description", widget=forms.Textarea)
    public = forms.BooleanField(label="Make public", required=False)
    thumbnail = forms.ImageField(label="Thumbnail picture", required=False)


class EditAlbum(forms.Form):
    def __init__(self, album, *args, **kwargs):
        super(EditAlbum, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(label="Album title",
                                               widget=forms.TextInput(attrs={'value': album.title}))
        self.fields['description'] = forms.CharField(label="Album description",
                                                     required=False,
                                                     widget=forms.Textarea(
                                                         attrs={'placeholder': album.title}
                                                     ))
        self.id = album.id
        if album.public == True:
            self.fields['public'] = forms.BooleanField(label="Make public", required=False,
                                                       widget=forms.CheckboxInput(attrs={'checked': 'checked'}))
        else:
            self.fields['public'] = forms.BooleanField(label="Make public", required=False,
                                                       widget=forms.CheckboxInput())

    title = forms.CharField()
    description = forms.CharField()
    public = forms.BooleanField()
    thumbnail = forms.ImageField(label="Thumbnail picture", required=False)

