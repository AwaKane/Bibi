from django.urls import path
from . import views

urlpatterns=[
    path("home/", views.homeView, name="home"),
    path("list-etablissement/", views.listEtablisView, name="listEtablis"),
    path("etablissement/<int:etabli_id>", views.detailEtablisView, name="detail"),
    path("ajout-etablissement/", views.ajoutEtablisView, name="ajoutEtablis"),
    path("list-rendez-vous/", views.listRdvView, name="listRDV"),
    path("rendez-vous/", views.rendezVousView, name="rendez_vous"),
    path("rendez-vous/<int:rendez_vous_id>", views.detailRdvView, name="rendez_vous_detail"),
    path("login/", views.loginView, name="login"),
    path('logout/', views.logoutView, name='logout'),
    path("signup/",  views.signup_view, name="signup"),
]