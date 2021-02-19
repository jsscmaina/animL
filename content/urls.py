from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _
# from .views import SearchResultsView

urlpatterns = [
    path("", views.content_index, name="content_index"),
    path(_("search/"), views.content_search, name="content_search"),
    path("<int:pk>/", views.content_detail, name="content_detail"),
    path("<category>/", views.content_category, name="content_category"),
    path("observation/", views.observe_form)
    # path("search/", SearchResultsView.as_view(), name='search'),

]
