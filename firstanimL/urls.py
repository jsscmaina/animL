from django.conf.urls import url
from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import FrontView, EditFrontView,\
    SymptomsView, ObservationView, AddObservationView, UpdateObservationView,\
    DeleteObservationView
from firstanimL import views


urlpatterns = [

    url('^$', FrontView.as_view(), name='home'),
    path('edit/<int:pk>', EditFrontView.as_view(), name='front_edit'),
    url('home', FrontView.as_view(), name='Home'),
    path(_('observation'), ObservationView.as_view(), name="observation"),
    path(_('add_observation'), AddObservationView.as_view(), name="add_observation"),
    path(_('save_observe'), views.save_observe, name="save_observe"),
    path(_('symptom'), views.individual_symptoms, name="individual_symptoms"),
    path('edit/update/<int:pk>', views.update, name="update"),
    path('edit_observation/update_observation/<int:pk>', views.update_observation, name="update_observation"),
    path('symptoms', SymptomsView.as_view(), name="symptom"),
    path('edit_observation/<int:pk>', UpdateObservationView.as_view(), name='edit_observation'),
    path('edit_observation/<int:pk>/delete', DeleteObservationView.as_view(), name='delete_observation'),
    # url('predict', views.predict, name="predict"),
    # url('symptoms', views.symptom, name="symptom"),
    # url('diagnose', views.diagnose, name="diagnose")
]
