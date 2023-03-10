from django.urls import path

from drama_datas import views

urlpatterns = [
    path("new/", views.drama_data_new, name="drama_data_new"),
    path("<int:drama_data_id>/", views.drama_data_detail, name="drama_data_detail"),
    path("<int:drama_data_id>/edit/", views.drama_data_edit, name="drama_data_edit"),
    path("<int:drama_data_id>/delete/", views.drama_data_delete, name="drama_data_delete"),
    path("company/new/", views.company_new, name="company_new"),
    path("company/<int:company_id>/", views.company_detail, name="company_detail"),
    path("company/<int:company_id>/edit/", views.company_edit, name="company_edit"),
    path("companies/", views.all_companies, name="all_companies"),
    path("cast/<int:drama_data_id>/new/", views.cast_new, name="cast_new"),
    path("all_actors/", views.all_actors, name="all_actors"),
    path("actor/new/", views.actor_new, name="actor_new"),
    #path("actor/<int:actor_id>")
    path("actor/<int:actor_id>/edit", views.actor_edit, name="actor_edit"),
]