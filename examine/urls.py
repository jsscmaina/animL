from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import ExamineView, ExamineDetailView
from . import views

urlpatterns = [
    path('', ExamineView.as_view(), name='examine_index'),
    path(_('<int:pk>'), ExamineDetailView.as_view(), name='examine_detail'),
    path(_("search/"), views.examine_search, name="examine_search"),

]