from django.urls import path

from sneakersinfo.views import TypeList, YearList, CountryList, CompanyList, AgencyList, \
    SneakersList, OrderList, TypeDetail, YearDetail, CountryDetail, CompanyDetail, AgencyDetail, SneakersDetail, \
    OrderDetail, TypeCreate, YearCreate, CompanyCreate, CountryCreate, AgencyCreate, SneakersCreate, OrderCreate, \
    TypeUpdate, YearUpdate, CountryUpdate, CompanyUpdate, AgencyUpdate, SneakersUpdate, OrderUpdate, TypeDelete, \
    YearDelete, CompanyDelete, CountryDelete, AgencyDelete, SneakersDelete, OrderDelete

urlpatterns = [
    path('type/',
         TypeList.as_view(),
         name='sneakersinfo_type_list_urlpattern'),

    path('type/<int:pk>/',
         TypeDetail.as_view(),
         name = 'sneakersinfo_type_detail_urlpattern'),

    path('type/create/',
         TypeCreate.as_view(),
         name='sneakersinfo_type_create_urlpattern'),

    path('type/<int:pk>/update/',
         TypeUpdate.as_view(),
         name='sneakersinfo_type_update_urlpattern'),

    path('type/<int:pk>/delete/',
         TypeDelete.as_view(),
         name='sneakersinfo_type_delete_urlpattern'),

    path('year/',
         YearList.as_view(),
         name='sneakersinfo_year_list_urlpattern'),

    path('year/<int:pk>/',
         YearDetail.as_view(),
         name='sneakersinfo_year_detail_urlpattern'),

    path('year/create/',
         YearCreate.as_view(),
         name='sneakersinfo_year_create_urlpattern'),

    path('year/<int:pk>/update/',
         YearUpdate.as_view(),
         name='sneakersinfo_year_update_urlpattern'),

    path('year/<int:pk>/delete/',
         YearDelete.as_view(),
         name='sneakersinfo_year_delete_urlpattern'),

    path('country/',
         CountryList.as_view(),
         name='sneakersinfo_country_list_urlpattern'),

    path('country/<int:pk>/',
         CountryDetail.as_view(),
         name='sneakersinfo_country_detail_urlpattern'),

    path('country/create/',
         CountryCreate.as_view(),
         name='sneakersinfo_country_create_urlpattern'),

    path('country/<int:pk>/update/',
         CountryUpdate.as_view(),
         name='sneakersinfo_country_update_urlpattern'),

    path('country/<int:pk>/delete/',
         CountryDelete.as_view(),
         name='sneakersinfo_country_delete_urlpattern'),

    path('company/',
         CompanyList.as_view(),
         name='sneakersinfo_company_list_urlpattern'),

    path('company/<int:pk>/',
         CompanyDetail.as_view(),
         name='sneakersinfo_company_detail_urlpattern'),

    path('company/create/',
         CompanyCreate.as_view(),
         name='sneakersinfo_company_create_urlpattern'),

    path('company/<int:pk>/update/',
         CompanyUpdate.as_view(),
         name='sneakersinfo_company_update_urlpattern'),

    path('company/<int:pk>/delete/',
         CompanyDelete.as_view(),
         name='sneakersinfo_company_delete_urlpattern'),

    path('agency/',
         AgencyList.as_view(),
         name='sneakersinfo_agency_list_urlpattern'),

    path('agency/<int:pk>/',
         AgencyDetail.as_view(),
         name='sneakersinfo_agency_detail_urlpattern'),

    path('agency/create/',
         AgencyCreate.as_view(),
         name='sneakersinfo_agency_create_urlpattern'),

    path('agency/<int:pk>/update/',
         AgencyUpdate.as_view(),
         name='sneakersinfo_agency_update_urlpattern'),

    path('agency/<int:pk>/delete/',
         AgencyDelete.as_view(),
         name='sneakersinfo_agency_delete_urlpattern'),

    path('sneakers/',
         SneakersList.as_view(),
         name='sneakersinfo_sneakers_list_urlpattern'),

    path('sneakers/<int:pk>/',
         SneakersDetail.as_view(),
         name='sneakersinfo_sneakers_detail_urlpattern'),

    path('sneakers/create/',
         SneakersCreate.as_view(),
         name='sneakersinfo_sneakers_create_urlpattern'),

    path('sneakers/<int:pk>/update/',
         SneakersUpdate.as_view(),
         name='sneakersinfo_sneakers_update_urlpattern'),

    path('sneakers/<int:pk>/delete/',
         SneakersDelete.as_view(),
         name='sneakersinfo_sneakers_delete_urlpattern'),

    path('order/',
         OrderList.as_view(),
         name='sneakersinfo_order_list_urlpattern'),

    path('order/<int:pk>/',
         OrderDetail.as_view(),
         name='sneakersinfo_order_detail_urlpattern'),

    path('order/create/',
         OrderCreate.as_view(),
         name='sneakersinfo_order_create_urlpattern'),

    path('order/<int:pk>/update/',
         OrderUpdate.as_view(),
         name='sneakersinfo_order_update_urlpattern'),

    path('order/<int:pk>/delete/',
         OrderDelete.as_view(),
         name='sneakersinfo_order_delete_urlpattern'),
]
