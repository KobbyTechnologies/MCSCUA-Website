from django import forms

class PostSearchForm(forms.Form):
    q = forms.CharField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = 'search for'
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control'}
        )
