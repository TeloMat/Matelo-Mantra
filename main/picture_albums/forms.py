from django import forms

from main.picture_albums.models import PictureAlbum


class CreateNewPAlbum(forms.Form):
    title = forms.CharField(label="Album title", max_length=50)
    description = forms.CharField(label="Album description",
                                  widget=forms.Textarea, max_length=250)
    public = forms.BooleanField(label="Make public", required=False)
    thumbnail = forms.ImageField(label="Thumbnail picture", required=True)


class EditPAlbum(forms.Form):
    def __init__(self, album, *args, **kwargs):
        super(EditPAlbum, self).__init__(*args, **kwargs)
        self.fields['description'] = forms.CharField(label="Album description",
                                                     required=False,
                                                     widget=forms.Textarea(
                                                         attrs={'placeholder': album.description}
                                                     ))
        self.fields['title'] = forms.CharField(label="Album title",
                                               widget=forms.TextInput(
                                                   attrs={'value': album.title}
                                               ))
        self.id = album.id
        if album.public:
            self.fields['public'] = forms.BooleanField(label="Make public", required=False,
                                                       widget=forms.CheckboxInput(
                                                           attrs={'checked': 'checked'}
                                                       ))
        else:
            self.fields['public'] = forms.BooleanField(label="Make public", required=False,
                                                       widget=forms.CheckboxInput())

    title = forms.CharField()
    description = forms.CharField()
    public = forms.BooleanField()
    thumbnail = forms.ImageField(label="Thumbnail picture", required=False)


class AddPAlbumPicture(forms.Form):
    caption = forms.CharField(label="Caption", max_length=255, widget=forms.Textarea)
    photo = forms.ImageField(label="Photo")


class AddPAlbumTag(forms.Form):
    val = forms.CharField(label="tag", max_length=15, required=True)