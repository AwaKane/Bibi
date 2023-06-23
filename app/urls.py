from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    path("", views.homeView, name="home"),
    path("list-etablissement/", views.listEtablisView, name="listEtablis"),
    path("etablissement/<int:etabli_id>", views.detailEtablisView, name="detail_etablis"),
    path("ajout-etablissement/", views.ajoutEtablisView, name="ajoutEtablis"),
    path("list-rendez-vous/", views.listRdvView, name="listRDV"),
    path("etablissement/<int:etabli_id>/rendez-vous/", views.rendezVousView, name="rendez_vous"),
    path("rendez-vous/<int:rendez_vous_id>", views.detailRdvView, name="rendez_vous_detail"),
    path("login/", views.loginView, name="login"),
    path('logout/', views.logoutView, name='logout'),
    path("signup/",  views.signup_view, name="signup"),
    path("ajout-user/",  views.ajoutUser_view, name="ajout-user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)