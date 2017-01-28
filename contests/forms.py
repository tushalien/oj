from django import forms

class AddContest(forms.Form):
    code = forms.CharField(max_length=256)
    name = forms.CharField(max_length=256)
    organiser = forms.CharField(max_length=256)
    starttime=forms.DateTimeField()
    endtime=forms.DateTimeField()
    anouncement = forms.CharField(widget=forms.Textarea(attrs={'rows':20}))
