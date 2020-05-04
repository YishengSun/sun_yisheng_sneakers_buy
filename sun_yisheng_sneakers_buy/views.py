from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('sneakersinfo_order_list_urlpattern')