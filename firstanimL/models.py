from django.db import models
# from easymode.i18n.decorators import I18n
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User


# Create your models here.

# @I18n('banner', 'first_title','first_box', 'second_title', 'second_box')
class Front(models.Model):
    banner = RichTextField(blank=True, null=True)
    first_title = models.CharField(max_length=255, default="CATTLE HEALTH")
    first_box = RichTextField(blank=True, null=True)
    second_title = models.CharField(max_length=255, default="CATTLE EXAMINATIONS")
    second_box = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.banner

    def get_absolute_url(self):
        if settings.LANGUAGE_CODE == 'en':
            return redirect('/')
        else:
            return redirect('/{settings.LANGUAGE_CODE}')


class Observation(models.Model):
    animl_id = models.TextField()
    observe_date = models.DateField()
    examine_back = RichTextField()
    examine_front = RichTextField()
    examine_rest = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.examine_back


class Symptoms(models.Model):
    fever = models.IntegerField()
    diff_breathing = models.IntegerField()
    distend = models.IntegerField()
    discomfort = models.IntegerField()
    bellowing = models.IntegerField()
    lethargy = models.IntegerField()
    appetite = models.IntegerField()
    ocular = models.IntegerField()
    nasal = models.IntegerField()
    oral_lesions = models.IntegerField()
    diarrhea = models.IntegerField()
    decreasing_milk = models.IntegerField()
    abortion = models.IntegerField()
    stillborn = models.IntegerField()
    weak_calf = models.IntegerField()
    fetal = models.IntegerField()
    swollen_test = models.IntegerField()
    skin_lesions = models.IntegerField()
    bold_plaques = models.IntegerField()
    hair = models.IntegerField()
    mouth_blisters = models.IntegerField()
    foot_blisters = models.IntegerField()
    weight_loss = models.IntegerField()
    frothing = models.IntegerField()
    lameness = models.IntegerField()
    late_abortion = models.IntegerField()
    jaundice = models.IntegerField()
    depressed_appetite = models.IntegerField()
    fertility = models.IntegerField()
    rubbing = models.IntegerField()
    hair_loss = models.IntegerField()
    biting = models.IntegerField()
    scratching = models.IntegerField()
    depression = models.IntegerField()
    coordination = models.IntegerField()
    isolation = models.IntegerField()
    salivation = models.IntegerField()
    facial_paralysis = models.IntegerField()
    blood_poisoning = models.IntegerField()
    anaemia = models.IntegerField()
    weight_gain = models.IntegerField()
    swelling_udders = models.IntegerField()
    hardness_udders = models.IntegerField()
    redness_udders = models.IntegerField()
    watery_milk = models.IntegerField()
    clots_milk = models.IntegerField()
    mobility = models.IntegerField()
    stillbirth = models.IntegerField()
    coughing = models.IntegerField()
    nose_pus = models.IntegerField()
    condition_loss = models.IntegerField()
    rumination = models.IntegerField()
    rapid_heart = models.IntegerField()
    crepitation = models.IntegerField()
    painful_swelling = models.IntegerField()
    painless_swelling = models.IntegerField()
    prostration = models.IntegerField()
    strange_behaviour = models.IntegerField()
    mounting = models.IntegerField()
    restlessness = models.IntegerField()
    swelling_head = models.IntegerField()
    inflammation_eyes = models.IntegerField()
    swelling_mouth = models.IntegerField()
    ulcers_mouth = models.IntegerField()
    tiredness = models.IntegerField()
    teeth_grinding = models.IntegerField()
    dark_urine = models.IntegerField()
    anorexia = models.IntegerField()

    def __str__(self):
        return self.fever


