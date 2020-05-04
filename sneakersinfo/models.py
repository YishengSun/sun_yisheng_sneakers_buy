from django.db import models
from django.urls import reverse


class Year(models.Model):
    year_id = models.AutoField(primary_key=True)
    year_name = models.CharField(max_length=4)

    def get_absolute_url(self):
        return reverse('sneakersinfo_year_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('sneakersinfo_year_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sneakersinfo_year_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def __str__(self):
        return '%s' % self.year_name

    class Meta:
        ordering = ['-year_name']
        unique_together = (('year_name'),)


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('sneakersinfo_type_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('sneakersinfo_type_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sneakersinfo_type_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def __str__(self):
        return '%s' % self.type_name

    class Meta:
        unique_together = ('type_name',)


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('sneakersinfo_country_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('sneakersinfo_country_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sneakersinfo_country_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def __str__(self):
        return '%s' % self.country_name

    class Meta:
        unique_together = (('country_name'),)


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=20)
    company_country = models.ForeignKey(Country, related_name='companies', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.company_name, self.company_country)

    def get_absolute_url(self):
        return reverse('sneakersinfo_company_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('sneakersinfo_company_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sneakersinfo_company_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['company_country', 'company_name']
        unique_together = (('company_country', 'company_name'),)


class Agency(models.Model):
    agency_id = models.AutoField(primary_key=True)
    agency_name = models.CharField(max_length=20)
    agency_country = models.ForeignKey(Country, related_name='agencies', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.agency_name, self.agency_country)

    def get_absolute_url(self):
        return reverse('sneakersinfo_agency_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('sneakersinfo_agency_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sneakersinfo_agency_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['agency_country', 'agency_name']
        unique_together = (('agency_country', 'agency_name'),)


class Sneakers(models.Model):
    sneakers_id = models.AutoField(primary_key=True)
    sneakers_name = models.CharField(max_length=50)
    sneakers_url = models.CharField(max_length=500)
    publish_year = models.ForeignKey(Year, related_name='sneakers', on_delete=models.PROTECT)
    type = models.ForeignKey(Type, related_name='sneakers', on_delete=models.PROTECT)
    company = models.ForeignKey(Company, related_name='sneakers', on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % self.sneakers_name

    def get_absolute_url(self):
        return reverse('sneakersinfo_sneakers_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('sneakersinfo_sneakers_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sneakersinfo_sneakers_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['company', 'publish_year']
        unique_together = (('sneakers_name', 'publish_year'),)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_quantity = models.IntegerField()
    date = models.DateField()
    agency = models.ForeignKey(Agency, related_name='orders', on_delete=models.PROTECT)
    sneakers = models.ForeignKey(Sneakers, related_name='orders', on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s' % (self.agency.agency_name, self.date)

    def get_absolute_url(self):
        return reverse('sneakersinfo_order_detail_urlpattern',
                       kwargs={'pk':self.pk}
                       )

    def get_update_url(self):
        return reverse('sneakersinfo_order_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('sneakersinfo_order_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['date','agency']
        unique_together = (('date','agency','sneakers'),)










