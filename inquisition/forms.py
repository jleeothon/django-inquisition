from django import forms


class SimpleSearch(forms.Form):
    """
    Provides a simple search form with a single field for querying.
    """

    q_help_text = ''

    q = forms.CharField(
        required=False,
        )

    def clean_q(self):
        q = self.cleaned_data['q']
        q = q.strip()
        return q

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].help_text = self.q_help_text
        self.fields['q'].widget.attrs['placeholder'] = self.q_help_text
