from django import forms


class CreateNewDescription(forms.Form):
    name = forms.CharField(label="Description name")
    text = forms.CharField(label="Description text", widget=forms.Textarea)
    quote = forms.CharField(label="Description Quote")
    picture = forms.ImageField(label="Profile picture")
    musician = forms.ImageField(label="Musician picture", required=True)
    writer = forms.ImageField(label="writer picture", required=True)
    traveler = forms.ImageField(label="traveler picture", required=True)
    public = forms.BooleanField(label="Use this description")



class EditDescription(forms.Form):
    def __init__(self, description, *args, **kwargs):
        super(EditDescription, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label="Description name",
                                              widget=forms.TextInput(
                                                  attrs={'value': description.name}
                                              ))
        self.fields['text'] = forms.CharField(label="Description Text",
                                              required=False,
                                              widget=forms.Textarea(
                                                  attrs={
                                                    'placeholder': description.text
                                                  }
                                              ))
        self.id = description.id
        if description.public:
            self.fields['public'] = forms.BooleanField(label="Make public", required=False,
                                                       widget=forms.CheckboxInput(
                                                           attrs={'checked': 'checked'}
                                                       ))
        else:
            self.fields['public'] = forms.BooleanField(label="Make public", required=False,
                                                       widget=forms.CheckboxInput())

    name = forms.CharField()
    text = forms.CharField()
    quote = forms.CharField()
    picture = forms.ImageField(label="Description picture", required=False)
    musician = forms.ImageField(label="Musician picture", required=False)
    writer = forms.ImageField(label="writer picture", required=False)
    traveler = forms.ImageField(label="traveler picture", required=False)
    public = forms.BooleanField()