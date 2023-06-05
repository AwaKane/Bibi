#Ici nous ecrivons differentes fonctions pour simplifier le code cote
# view
from .models import RendezVous
from django.shortcuts import get_object_or_404

def checkRdvNumber(etablis, user, forms):
    #On filtre le nombre de rendez vous pour une date donnee dans 
    #le but de savoir combien il y a t-il, si c'est 10 le patient
    #ne pourra pas prendre de rendez-vous
    etablis = get_object_or_404(etablis)
    objet = forms.cleaned_data('objet')
    detail = forms.cleaned_data('detail')
    date = forms.cleaned_data('date')
    specialite = forms.cleaned_data('specialite')
    numberRDV =  len(RendezVous.objects.filter(etablissement=etablis, date=date))
    if numberRDV == 10:
        print('Cette date est pleine')
    else: 
        print('Le nombre de rendez-vous est bas')
        RendezVous(user, etablis, objet, detail, date, specialite).save()