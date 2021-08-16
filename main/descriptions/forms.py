from django import forms


class CreateNewDescription(forms.Form):
    name = forms.CharField(label="Description name", max_length=200)
    text = forms.CharField(label="Description text", widget=forms.Textarea, max_length=800)
    quote = forms.CharField(label="Description quote", max_length=300)
    picture = forms.ImageField(label="Profile picture", required=False)
    musician = forms.ImageField(label="Menu Picture : Musician Item picture", required=False)
    writer = forms.ImageField(label="Menu Picture : Writer Item Picture", required=False)
    traveler = forms.ImageField(label="Menu Picture : Traveler Item Picture", required=False)
    public = forms.BooleanField(label="Select this description for display (Selecting this box will disable display on any other existing description)",
                                required=False)



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
        self.fields['quote'] = forms.CharField(label="Description quote",
                                              widget=forms.TextInput(
                                                  attrs={'value': description.name}
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