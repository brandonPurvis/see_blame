from django import forms


class QueryForm(forms.Form):
    query = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            initial='Search')
