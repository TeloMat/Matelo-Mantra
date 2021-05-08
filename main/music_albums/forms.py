from django import forms


class CreateNewMAlbum(forms.Form):
    title = forms.CharField(label="Album title", max_length=50)
    artist = forms.CharField(label="Artist", max_length=50)
    description = forms.CharField(label="Album description",
                                  widget=forms.Textarea, max_length=250)
    public = forms.BooleanField(label="Make public", required=False)
    cover = forms.ImageField(label="Cover picture", required=False)


class EditMAlbum(forms.Form):
    def __init__(self, album, *args, **kwargs):
        super(EditMAlbum, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(label="Album title",
                                               widget=forms.TextInput(
                                                   attrs={'value': album.title}
                                               ))
        self.fields['artist'] = forms.CharField(label="Artist",
                                                widget=forms.TextInput(
                                                    attrs={'value': album.artist}))
        self.fields['description'] = forms.CharField(label="Album description",
                                                     required=False,
                                                     widget=forms.Textarea(
                                                         attrs={'placeholder': album.title}
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
    artist = forms.CharField()
    description = forms.CharField()
    public = forms.BooleanField()
    cover = forms.ImageField(label="Cover picture", required=False)


class AddNewSong(forms.Form):
    title = forms.CharField(label="Song Title", max_length=50)
    description = forms.CharField(label="Description", max_length=250, required=False, widget=forms.Textarea)
    track = forms.FileField(label="Track")