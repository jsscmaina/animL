"""animL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.conf.urls import url, re_path
from django.conf import settings
from django.conf.urls.static import static
from firstanimL import views



urlpatterns = [
    path('change_language/',
         views.change_language,
         name='change_language')
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path(_("disease/"), include("content.urls")),
    path(_('examine/'), include('examine.urls')),
    path(_('members/'), include('django.contrib.auth.urls')),
    path(_('members/'), include('members.urls')),
    path('', include('firstanimL.urls')),
    # url('predict', views.line_predict, name="predict"),
    url('export', views.export, name="export"),
    url('pdf', views.pdf_view, name="export_pdf"),
    # url('symptoms', views.symptom, name="symptom"),
    url('diagnose', views.diagnose, name="diagnose"),
    url('mastitis', views.mastitis, name="mastitis"),
    url(_('fever'), views.fever, name="fever"),
    url(_('get_fever'), views.get_fever, name="get_fever"),
    url('predict_image', views.predict_image, name="predict_image"),
    prefix_default_language=False
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

urlpatterns += (
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
