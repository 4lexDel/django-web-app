# listings/forms.py

from django import forms
from listings.models import Band
from listings.models import Listing

class ContactUsForm(forms.Form):
   nom = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
   class Meta:
     model = Band
     fields = '__all__'
     labels = {
        "name": "Nom",
        "biography":"Biographie",            #Tradution
        "year_formed":"Année de formation",
        "official_homepage":"Page officiel"
      }

class ListingForm(forms.ModelForm):
   class Meta:
     model = Listing
     fields = '__all__'
     labels = {
        "title": "Titre",
        "sold":"Vendus",            #Tradution
        "year":"Année",
        "official_homepage":"Page officiel",
        "band":"Groupe"
      }