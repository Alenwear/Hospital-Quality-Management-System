from django import forms


class AddCheck(forms.Form):
    # CheInfo_id = forms.IntegerField(required=False, label="操作员id")
    fk_CheInfo_opId = forms.IntegerField()
    fk_CheInfo_admErId = forms.IntegerField()
    fk_CheInfo_admEeId = forms.IntegerField()
    # dt = forms.DateTimeField(required=False)
    time = forms.DateField(required=False)
    type = forms.CharField(max_length=50)
    dt = forms.CharField(max_length=50, required=False)
    manageScore = forms.IntegerField()
    personScore = forms.IntegerField()
    fee = forms.IntegerField()
    reason = forms.CharField(widget=forms.Textarea)

