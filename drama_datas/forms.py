from django import forms

from drama_datas.models import DramaData, Company, Cast


class DramaDataForm(forms.ModelForm):
    class Meta:
        model = DramaData
        fields = ('title', 'year', 'company', 'patern', 'memo')

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'country', 'memo')

class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = ('name', 'role')