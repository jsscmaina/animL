from django.shortcuts import render
from examine.models import Guide
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _

# Create your views here.


class ExamineView(ListView):
    model = Guide
    template_name = 'examine/index.html'


class ExamineDetailView(DetailView):
    model = Guide
    template_name = 'examine/detail.html'


def index(request):
    guides = Guide.objects.all()
    title = _("Examine")
    context = {
        "guides": guides,
        "title": title,
    }
    return render(request, 'examine/index.html', context)


def examine_search(request):
    query = request.GET.get('q')
    guides = Guide.objects.filter(Q(title__icontains=query))
    context = {
        "guides": guides,
    }
    return render(request, "examine/search.html", context)

