from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import pandas as pd
import joblib

from .models import Front, Symptoms, Observation
from .forms import FrontForm, SymptomsForm, ObserveForm
from .resources import SymptomsResource


# Create your views here.

# reloadModel = joblib.load('./models/RFModelforMPG.sav')
animalModel = joblib.load('./models/animals.sav')
cnn_model = load_model('./models/mastitis.h5')


class FrontView(ListView):
    model = Front
    template_name = 'index.html'


class AddFrontView(CreateView):
    model = Front
    form_class = FrontForm
    template_name = 'front/add_front_content.html'
    # fields = '__all__'


class AddObservationView(CreateView):
    model = Observation
    form_class = ObserveForm
    template_name = 'observation/add_observation.html'
    # fields = '__all__'


class SymptomsView(CreateView):
    model = Symptoms
    template_name = 'symptoms.html'
    fields = '__all__'


class EditFrontView(UpdateView):
    model = Front
    # form_class = FrontForm
    template_name = 'front/add_front_content.html'
    fields = '__all__'


class ObservationView(ListView):
    model = Observation
    template_name = 'observation/index.html'


class UpdateObservationView(UpdateView):
    model = Observation
    template_name = 'observation/update.html'
    # form_class = ObserveForm
    fields = ['animl_id', 'observe_date', 'examine_front', 'examine_back', 'examine_rest']


class DeleteObservationView(SuccessMessageMixin, DeleteView):
    model = Observation
    template_name = 'observation/delete_observation.html'
    success_url = reverse_lazy('observation')
    success_message = 'THE OBSERVATION HAS BEEN DELETED'


def update_observation(request, pk):
    observe = Observation.objects.get(pk=pk)
    form = ObserveForm(request.POST, instance=observe)
    if form.is_valid():
        form.save()
        messages.success(request, 'THE OBSERVATION HAS BEEN UPDATED')
    else:
        messages.warning(request, 'THE OBSERVATION HAS NOT BEEN SAVED')
    if settings.LANGUAGE_CODE == 'en':
        return redirect('/observation')
    else:
        return redirect('/{settings.LANGUAGE_CODE}/uchunguzi')
    # return redirect('/')


def save_observe(request):
    form = ObserveForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'THE OBSERVATION HAS BEEN SAVED')
    else:
        return redirect('/add_observation')
    if settings.LANGUAGE_CODE == 'en':
        return redirect('/observation')
    else:
        return redirect('/{settings.LANGUAGE_CODE}/uchunguzi')


def update(request, pk):
    front = Front.objects.get(pk=pk)
    form = FrontForm(request.POST, instance=front)
    if form.is_valid():
        form.save()
    if settings.LANGUAGE_CODE == 'en':
        return redirect('/')
    else:
        return redirect('/{settings.LANGUAGE_CODE}')
    # return redirect('/')


def export(request):
    symp_resource = SymptomsResource()
    dataset = symp_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="symptoms.csv"'
    return response


def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'observations.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="observations.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')


def individual_symptoms(request):
    return render(request, 'transition.html')


def fever(request):
    return render(request, 'fever.html')


def get_fever(request):
    if request.method == 'POST':
        fever_entered = request.POST.get('fever')
        print(fever_entered)
        if fever_entered > 39:
            temperature = 'HIGH FEVER'
        elif fever_entered < 37:
            temperature = 'SHIVERS'
        else:
            temperature = 'NORMAL'
    else:
        a = "HA"
    context = {
        'temp': temperature,
        'a': a,
    }

    return render(request, 'fever.html', context)


def index(request):
    title = _("Welcome")
    context = {'a': title}
    return render(request, 'index.html', context)


def change_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response


def symptom(request):
    fields = '__all__'
    context = {'a': 'Symptoms', 'fields': fields}
    return render(request, 'symptoms.html', context)


def observation(request):
    observations = Observation.objects.values('observe_date').annotate().order_by('observe_date')
    context = {
        "a": "SANTA TELL ME",
        "observations": observations,
    }
    return render(request, 'observation/index.html', context)


def mastitis(request):
    title = _("Welcome")
    context = {'a': title}
    return render(request, 'mastitis.html', context)


def predict_image(request):
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filename = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filename)

    img = image.load_img("models/Dataset/upload/" + filename, target_size=(200, 200))
    X = image.img_to_array(img)
    X = np.expand_dims(X, axis=0)
    images = np.vstack([X])

    val = cnn_model.predict(images)
    if val == 0:
        predicted_class = "Abnormal"
    else:
        predicted_class = "Normal"
    context = {
        "filePathName": filePathName,
        "filename": filename,
        "predicted_class": predicted_class,
    }
    return render(request, 'mastitis.html', context)


def showform(request):
    form = SymptomsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'symptoms.html', context)


def diagnose(request):
    st = {}
    form = SymptomsForm(request.POST)
    if form.is_valid():
        form.save()
    if request.method == 'POST':
        symp = {}
        symp['fever'] = request.POST.get('fever')
        symp['difficulty breathing'] = request.POST.get('diff_breathing')
        symp['distended left abdomen'] = request.POST.get('distend')
        symp['discomfort'] = request.POST.get('discomfort')
        symp['bellowing'] = request.POST.get('bellowing')
        symp['lethargy'] = request.POST.get('lethargy')
        symp['loss of appetite'] = request.POST.get('appetite')
        symp['ocular discharge'] = request.POST.get('ocular')
        symp['nasal discharge'] = request.POST.get('nasal')
        symp['oral lesions'] = request.POST.get('oral_lesions')
        symp['diarrhea'] = request.POST.get('diarrhea')
        symp['decreasing milk production'] = request.POST.get('decreasing_milk')
        symp['abortion'] = request.POST.get('abortion')
        symp['stillborn'] = request.POST.get('stillborn')
        symp['weak calf'] = request.POST.get('weak_calf')
        symp['retention of fetal membrane'] = request.POST.get('fetal')
        symp['swollen testicles'] = request.POST.get('swollen_test')
        symp['lesions on skin'] = request.POST.get('skin_lesions')
        symp['bold plaques'] = request.POST.get('bold_plaques')
        symp['tufts of hair coming off'] = request.POST.get('hair')
        symp['blisters in the mouth'] = request.POST.get('mouth_blisters')
        symp['blisters on feet'] = request.POST.get('foot_blisters')
        symp['weight loss'] = request.POST.get('weight_loss')
        symp['frothing of mouth'] = request.POST.get('frothing')
        symp['lameness'] = request.POST.get('lameness')
        symp['late abortion'] = request.POST.get('late_abortion')
        symp['jaundice'] = request.POST.get('jaundice')
        symp['depressed appetite'] = request.POST.get('depressed_appetite')
        symp['reduced fertility'] = request.POST.get('fertility')
        symp['rubbing'] = request.POST.get('rubbing')
        symp['hair loss'] = request.POST.get('hair_loss')
        symp['biting'] = request.POST.get('biting')
        symp['scratching'] = request.POST.get('scratching')
        symp['depression'] = request.POST.get('depression')
        symp['lack of coordination'] = request.POST.get('coordination')
        symp['isolation'] = request.POST.get('isolation')
        symp['salivation'] = request.POST.get('salivation')
        symp['facial paralysis'] = request.POST.get('facial_paralysis')
        symp['blood_poisoning'] = request.POST.get('blood_poisoning')
        symp['anaemia'] = request.POST.get('anaemia')
        symp['reduced live weight gain'] = request.POST.get('weight_gain')
        symp['swelling in udders'] = request.POST.get('swelling_udders')
        symp['hardness of udders'] = request.POST.get('hardness_udders')
        symp['redness or pain in udders'] = request.POST.get('redness_udders')
        symp['watery milk'] = request.POST.get('watery_milk')
        symp['clots in milk'] = request.POST.get('clots_milk')
        symp['reduced mobility'] = request.POST.get('mobility')
        symp['stillbirth'] = request.POST.get('stillbirth')
        symp['coughing'] = request.POST.get('coughing')
        symp['pus from nose'] = request.POST.get('nose_pus')
        symp['progressive loss of condition'] = request.POST.get('condition_loss')
        symp['suspended rumination'] = request.POST.get('rumination')
        symp['rapid heart rates'] = request.POST.get('rapid_heart')
        symp['crepitation swelling'] = request.POST.get('crepitation')
        symp['painful swelling'] = request.POST.get('painful_swelling')
        symp['painless swelling'] = request.POST.get('painless_swelling')
        symp['prostration'] = request.POST.get('prostration')
        symp['strange behaviour'] = request.POST.get('strange_behaviour')
        symp['mounting others'] = request.POST.get('mounting')
        symp['restlessness'] = request.POST.get('restlessness')
        symp['swelling of head and neck'] = request.POST.get('swelling_head')
        symp['inflammation of the eyes'] = request.POST.get('inflammation_eyes')
        symp['swelling in mouth'] = request.POST.get('swelling_mouth')
        symp['ulcers in mouth'] = request.POST.get('ulcers_mouth')
        symp['tiredness'] = request.POST.get('tiredness')
        symp['grinding teeth'] = request.POST.get('teeth_grinding')
        symp['dark coloured urine'] = request.POST.get('dark_urine')
        symp['anorexia'] = request.POST.get('anorexia')
        for s in symp.items():
            if s[1] is None:
                symp[s[0]] = 0
            st['s'] = s[1]
        symp = pd.DataFrame({'x': symp}).transpose()
        score = animalModel.predict(symp)
        summary = animalModel.predict_proba(symp)
        context = {'a': 'Diagnosis', 'symp': symp, 'st': score, 'summary': summary}
        return render(request, 'symptoms.html', context)


def line_predict(request):
    global temp, temp2
    if request.method == 'POST':
        # temp = {'cylinders': request.POST.get('cylinderVal'), 'displacement': request.POST.get('dispVal'),
        #         'horsepower': request.POST.get('hrsPwrVal'), 'weight': request.POST.get('weightVal'),
        #         'acceleration': request.POST.get('accVal'), 'model year': request.POST.get('modelVal'),
        #         'origin': request.POST.get('originVal')}
        temp = {}
        temp['cylinders'] = request.POST.get('cylinderVal')
        temp['displacement'] = request.POST.get('dispVal')
        temp['horsepower'] = request.POST.get('hrsPwrVal')
        temp['weight'] = request.POST.get('weightVal')
        temp['acceleration'] = request.POST.get('accVal')
        temp['model_year'] = request.POST.get('modelVal')
        origin = request.POST.get('originVal')
        print(origin)
        temp['origin'] = int(origin)
        temp2 = temp.copy()
        temp['model year'] = temp['model_year']
        print(temp.keys(), temp2.keys())
        # del temp2['model_year']

    testDtaa = pd.DataFrame({'x': temp}).transpose()
    scoreval = animalModel.predict(testDtaa)[0]
    context = {'scoreval': scoreval, 'temp': temp, 'test': testDtaa}
    return render(request, 'index.html', context)
