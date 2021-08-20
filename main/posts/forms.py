from django import forms


class CreateNewPost(forms.Form):
    name = forms.CharField(label="Post title", max_length=200)
    text = forms.CharField(label="Post text", widget=forms.Textarea)
    thumbnail = forms.ImageField(label="Thumbnail picture", required=True)
    public = forms.BooleanField(label="Make public", required=False)


class EditPost(forms.Form):
    def __init__(self, post, *args, **kwargs):
        super(EditPost, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label="Post title",
                                              widget=forms.TextInput(attrs={'value': post.name}))
        self.fields['text'] = forms.CharField(label="Post text",
                                              required=False,
                                              widget=forms.Textarea(
                                                  attrs={'placeholder': post.text}
                                              ))
        self.id = post.id
        if post.public:
            self.fields['public'] = forms.BooleanField(label="Make public", required=False,
                                                       widget=forms.CheckboxInput(attrs={'checked': 'checked'}))
        else:
            self.fields['public'] = forms.BooleanField(label="Make public", required=False,
                                                       widget=forms.CheckboxInput())

    name = forms.CharField()
    text = forms.CharField()
    public = forms.BooleanField()
    thumbnail = forms.ImageField(label="Thumbnail picture", required=False)


class AddPostTag(forms.Form):
    val = forms.CharField(label="tag", max_length=15, required=True)


class AddPostCredit(forms.Form):
    contributor = forms.CharField(label="Contributor", max_length=50, required=True)
    contribution = forms.CharField(label="Contribution", max_length=50, required=False)
