from django import forms
from .models import Front, Symptoms, Observation

# from ckeditor.fields import RichTextField


class FrontForm(forms.ModelForm):
    class Meta:
        model = Front
        fields = ('banner', 'banner_sw', 'first_title', 'first_title_sw', 'first_box', 'first_box_sw',
                  'second_title', 'second_title_sw', 'second_box', 'second_box_sw')

        # widgets = {
        #     'banner': forms.Textarea(attrs={'class': 'form-control w-100'}),
        #     'first_title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'first_box': forms.Textarea(attrs={'class': 'form-control'}),
        #     'second_title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'second_box': forms.Textarea(attrs={'class': 'form-control'}),
        # }


class ObserveForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ('animl_id', 'observe_date',
                  'examine_front', 'examine_back', 'examine_rest', 'author')
        widgets = {
            'animl_id': forms.TextInput(attrs={'class': 'form-control', 'colspan': 2}),
            'observe_date': forms.DateInput(attrs={'class': 'form-control', 'colspan': 2}),
            'examine_front': forms.Textarea(attrs={'class': 'form-control', 'colspan': 2}),
            'examine_back': forms.Textarea(attrs={'class': 'form-control', 'colspan': 2}),
            'examine_rest': forms.Textarea(attrs={'class': 'form-control', 'colspan': 2}),
        }


class SymptomsForm(forms.ModelForm):
    class Meta:
        model = Symptoms
        fields = ('fever', 'diff_breathing', 'distend', 'discomfort', 'bellowing',
                  'lethargy', 'appetite', 'ocular', 'nasal',
                  'oral_lesions', 'diarrhea', 'decreasing_milk', 'abortion',
                  'stillborn', 'weak_calf', 'fetal',
                  'swollen_test', 'skin_lesions', 'bold_plaques',
                  'hair', 'mouth_blisters', 'foot_blisters',
                  'weight_loss', 'frothing', 'lameness', 'late_abortion',
                  'jaundice', 'depressed_appetite', 'fertility', 'rubbing',
                  'hair_loss', 'biting', 'scratching', 'depression',
                  'coordination', 'isolation', 'salivation',
                  'facial_paralysis', 'blood_poisoning', 'anaemia',
                  'weight_gain', 'swelling_udders', 'hardness_udders',
                  'redness_udders', 'watery_milk', 'clots_milk',
                  'mobility', 'stillbirth', 'coughing', 'nose_pus',
                  'condition_loss', 'rumination',
                  'rapid_heart', 'crepitation', 'painful_swelling',
                  'painless_swelling', 'prostration', 'strange_behaviour',
                  'mounting', 'restlessness', 'swelling_head',
                  'inflammation_eyes', 'swelling_mouth', 'ulcers_mouth',
                  'tiredness', 'teeth_grinding', 'dark_urine',
                  'anorexia')
