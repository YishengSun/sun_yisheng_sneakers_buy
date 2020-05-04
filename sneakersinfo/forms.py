from django import forms
from sneakersinfo.models import Year, Type, Country, Company, Agency, Sneakers, Order


class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = '__all__'

    def clean_year_name(self):
        return self.cleaned_data['year_name'].strip()



class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

    def clean_type_name(self):
        return self.cleaned_data['type_name'].strip()


class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = '__all__'

    def clean_year_name(self):
        return self.cleaned_data['year_name'].strip()


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    def clean_company_name(self):
        return self.cleaned_data['company_name'].strip()


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

    def clean_country_name(self):
        return self.cleaned_data['country_name'].strip()


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'

    def clean_agency_name(self):
        return self.cleaned_data['agency_name'].strip()


class SneakersForm(forms.ModelForm):
    class Meta:
        model = Sneakers
        fields = '__all__'

    def clean_sneakers_name(self):
        return self.cleaned_data['sneakers_name'].strip()

    def clean_sneakers_url(self):
        return self.cleaned_data['sneakers_url'].strip()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_order_date(self):
        return self.cleaned_data['order_date'].strip()

    def clean_order_quantity(self):
        return self.cleaned_data['order_quantity']

