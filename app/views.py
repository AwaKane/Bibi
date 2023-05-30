from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def homeView(request):
    return render(request, "home.html", {})


def listEtablisView(request):
    etablissements = Etablissement.objects.all()
    return render(request, "listEtablissement.html", {'etablissements': etablissements})

def detailEtablisView(request, etabli_id):
    etablis = get_object_or_404(Etablissement, pk=etabli_id)
    return render(request, "detailEtablissement.html", {"etablis": etablis})


def detailRdvView(request, rendez_vous_id):
    rdv =  get_object_or_404(RendezVous, pk=rendez_vous_id)
    return render(request, "detailRDV.html", {"item_rdv": rdv})


def ajoutEtablisView(request):
    if request.method == "POST":
        form = RendezVous_form(request.POST)
        
        if form.is_valid():
            form.save()
    else:
        form = RendezVous_form()
        
    return render(request, "ajoutEtablissement.html", {'forms': forms})


def listRdvView(request):
    rdvs = RendezVous.objects.all()
    return render(request, "listRDV.html", {"rdvs": rdvs})


def rendezVousView(request):
    if request.method == "POST":
        forms = RendezVous_form(request.POST)

        if forms.is_valid():
            forms.save()

    else:
        forms = RendezVous_form() 
    return render(request, "create_rdv.html", {'forms': forms})