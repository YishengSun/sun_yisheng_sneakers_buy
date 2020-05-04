from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from sneakersinfo.forms import TypeForm, YearForm, CompanyForm, CountryForm, AgencyForm, SneakersForm, OrderForm
from sneakersinfo.utils import PageLinksMixin

from .models import (
    Year,
    Sneakers,
    Type,
    Country,
    Company,
    Agency,
    Order
)


class TypeList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 5
    model = Type
    permission_required = 'sneakersinfo.view_type'


class TypeDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sneakersinfo.view_type'

    def get(self,request,pk):
        type = get_object_or_404(
            Type,
            pk = pk
        )
        sneakers_list = type.sneakers.all()
        return render(
            request,
            'sneakersinfo/type_detail.html',
            {'type': type, 'sneakers_list': sneakers_list}
        )


class TypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TypeForm
    model = Type
    permission_required = 'sneakersinfo.add_type'


class TypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TypeForm
    model = Type
    template_name = 'sneakersinfo/type_form_update.html'
    permission_required = 'sneakersinfo.change_type'


class TypeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Type
    success_url = reverse_lazy('sneakersinfo_type_list_urlpattern')
    permission_required = 'sneakersinfo.delete_type'


class YearList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 5
    model = Year
    permission_required = 'sneakersinfo.view_year'


class YearDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sneakersinfo.view_year'

    def get(self,request,pk):
        year = get_object_or_404(
            Year,
            pk = pk
        )
        sneakers_list = year.sneakers.all()
        return render(
            request,
            'sneakersinfo/year_detail.html',
            {'year': year, 'sneakers_list': sneakers_list}
        )


class YearCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = YearForm
    model = Year
    permission_required = 'sneakersinfo.add_year'


class YearUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = YearForm
    model = Year
    template_name = 'sneakersinfo/year_form_update.html'
    permission_required = 'sneakersinfo.change_year'


class YearDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Year
    success_url = reverse_lazy('sneakersinfo_year_list_urlpattern')
    permission_required = 'sneakersinfo.delete_year'
        
        
class CompanyList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 5
    model = Company
    permission_required = 'sneakersinfo.view_company'


class CompanyDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sneakersinfo.view_company'
    def get(self,request,pk):
        company = get_object_or_404(
            Company,
            pk = pk
        )
        country = company.company_country
        sneakers_list = company.sneakers.all()
        return render(
            request,
            'sneakersinfo/company_detail.html',
            {'company': company, 'country': country, 'sneakers_list': sneakers_list}
        )


class CompanyCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CompanyForm
    model = Company
    permission_required = 'sneakersinfo.add_company'


class CompanyUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CompanyForm
    model = Company
    template_name = 'sneakersinfo/company_form_update.html'
    permission_required = 'sneakersinfo.change_company'


class CompanyDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('sneakersinfo_company_list_urlpattern')
    permission_required = 'sneakersinfo.delete_company'


class CountryList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 5
    model = Country
    permission_required = 'sneakersinfo.view_country'


class CountryDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sneakersinfo.view_country'
    def get(self,request,pk):
        country = get_object_or_404(
            Country,
            pk = pk
        )
        agency_list = country.agencies.all()
        company_list = country.companies.all()
        return render(
            request,
            'sneakersinfo/country_detail.html',
            {'country': country, 'agency_list': agency_list, 'company_list': company_list}
        )


class CountryCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CountryForm
    model = Country
    permission_required = 'sneakersinfo.add_country'


class CountryUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CountryForm
    model = Country
    template_name = 'sneakersinfo/country_form_update.html'
    permission_required = 'sneakersinfo.change_country'


class CountryDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Country
    success_url = reverse_lazy('sneakersinfo_country_list_urlpattern')
    permission_required = 'sneakersinfo.delete_country'
    
    
class AgencyList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 5
    model = Agency
    permission_required = 'sneakersinfo.view_agency'


class AgencyDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sneakersinfo.view_agency'
    def get(self,request,pk):
        agency = get_object_or_404(
            Agency,
            pk = pk
        )
        country = agency.agency_country
        order_list = agency.orders.all()
        return render(
            request,
            'sneakersinfo/agency_detail.html',
            {'agency': agency, 'country': country, 'order_list': order_list}
        )


class AgencyCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AgencyForm
    model = Agency
    permission_required = 'sneakersinfo.add_agency'


class AgencyUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AgencyForm
    model = Agency
    template_name = 'sneakersinfo/agency_form_update.html'
    permission_required = 'sneakersinfo.change_agency'


class AgencyDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Agency
    success_url = reverse_lazy('sneakersinfo_agency_list_urlpattern')
    permission_required = 'sneakersinfo.delete_agency'
    
        
class SneakersList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 5
    model = Sneakers
    permission_required = 'sneakersinfo.view_sneakers'


class SneakersDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sneakersinfo.view_sneakers'
    def get(self,request,pk):
        sneakers = get_object_or_404(
            Sneakers,
            pk = pk
        )
        type = sneakers.type
        year = sneakers.publish_year
        company = sneakers.company
        order_list = sneakers.orders.all()
        return render(
            request,
            'sneakersinfo/sneakers_detail.html',
            {'sneakers': sneakers, 'type': type, 'year': year, 'company': company, 'order_list': order_list}
        )


class SneakersCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SneakersForm
    model = Sneakers
    permission_required = 'sneakersinfo.add_sneakers'
    

class SneakersUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SneakersForm
    model = Sneakers
    template_name = 'sneakersinfo/sneakers_form_update.html'
    permission_required = 'sneakersinfo.change_sneakers'


class SneakersDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Sneakers
    success_url = reverse_lazy('sneakersinfo_sneakers_list_urlpattern')
    permission_required = 'sneakersinfo.delete_sneakers'


class OrderList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 5
    model = Order
    permission_required = 'sneakersinfo.view_order'


class OrderDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'sneakersinfo.view_order'
    def get(self,request,pk):
        order = get_object_or_404(
            Order,
            pk = pk
        )
        sneakers = order.sneakers
        agency = order.agency
        return render(
            request,
            'sneakersinfo/order_detail.html',
            {'order': order, 'sneakers': sneakers, 'agency': agency}
        )


class OrderCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = OrderForm
    model = Order
    permission_required = 'sneakersinfo.add_order'


class OrderUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = OrderForm
    model = Order
    template_name = 'sneakersinfo/order_form_update.html'
    permission_required = 'sneakersinfo.change_order'


class OrderDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('sneakersinfo_order_list_urlpattern')
    permission_required = 'sneakersinfo.delete_order'




