#Ici nous ecrivons differentes fonctions pour simplifier le code cote
# view
from .models import RendezVous, Etablissement
from django.shortcuts import get_object_or_404

def checkRdvNumber(etablis, user, forms):
    #On filtre le nombre de rendez vous pour une date donnee dans 
    #le but de savoir combien il y a t-il, si c'est 10 le patient
    #ne pourra pas prendre de rendez-vous
    etablis = get_object_or_404(Etablissement, pk=etablis)
    objet = forms.cleaned_data.get('objet')
    detail = forms.cleaned_data.get('detail')
    date = forms.cleaned_data.get('date')
    specialite = forms.cleaned_data.get('specialite')
    numberRDV =  len(RendezVous.objects.filter(etablissement=etablis, date=date))
    if numberRDV == 10:
        print(specialite)
        print('Cette date est pleine')
    else: 
        print('Le nombre de rendez-vous est bas')
        print(specialite)
        RendezVous.objects.create(user=user, etablissement=etablis, objet=objet, detail=detail, date=date, specialite=specialite)