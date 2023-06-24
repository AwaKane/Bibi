from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout
from .utils import checkRdvNumber
from django.db.models import Q

# Create your views here.
def homeView(request):
    etablissement_seached = ""

    if 'q' in request.GET:
        q = request.GET['q']
        
        multiple_q = Q(nom_etablissement__icontains=q)
        etablissement_seached = Etablissement.objects.filter(multiple_q)
    return render(request, "home.html", {'list_etablis':etablissement_seached})


def listEtablisView(request):
    etablissements = Etablissement.objects.all()
    return render(request, "patient/listEtablissement.html", {'etablissements': etablissements})


def detailEtablisView(request, etabli_id):
    etablis = get_object_or_404(Etablissement, pk=etabli_id)
    return render(request, "patient/detailEtablissement.html", {"etablis": etablis})


def detailRdvView(request, rendez_vous_id):
    rdv =  get_object_or_404(RendezVous, pk=rendez_vous_id)
    return render(request, "etablissement/detailRDV.html", {"item_rdv": rdv})


def ajoutEtablisView(request):
    if request.method == "POST":
        forms = Etablissement_form(request.POST)
        print(forms)
        print("request thow")
        if forms.is_valid():
            print("saving data")
            forms.save()
        else:
            print("echec de la requete")
    else:
        forms = Etablissement_form()
    return render(request, "ajoutEtablissement.html", {'forms': forms})


def listRdvView(request):
    rdvs = RendezVous.objects.all()
    return render(request, "etablissement/listRDV.html", {"rdvs": rdvs})


def rendezVousView(request, etabli_id):
    if request.method == "POST":
        forms = RendezVous_form(request.POST)
        if forms.is_valid():
            checkRdvNumber(etabli_id, request.user, forms)
    else:
        forms = RendezVous_form() 
    return render(request, "patient/createRDV.html", {'forms': forms})


def loginView(request):
    if request.method == "POST":
        form=Login_form(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            password=form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            print("user authentifier")
            if user:
                if user.personnel:
                    login(request, user)
                    return redirect("listRDV")
                else:
                    login(request, user)
                    return redirect("rendez_vous")
            else:
                print("user don't exist")
        else: 
            print(form.errors)
    else: 
        form = Login_form()
    return render(request, "auth/login.html", {"form": form})


# La view pour permettre le user de se deconnecter
def logoutView(request):
    """logout logged in user"""
    logout(request)
    return redirect("login")


#La view permettant au user de se connecter
def signup_view(request):
    if request.method == "POST":
        form = User_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = User_form()
    return render(request, 'auth/signup.html', {'form': form})


#La view permettant au user de se connecter
def ajoutUser_view(request):
    if request.method == "POST":
        form = User_form(request.POST)
        if form.is_valid():
            form.savePersonnel()
    else:
        form = User_form()
    return render(request, 'ajoutUser.html', {'form': form})