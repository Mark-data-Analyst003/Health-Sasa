
from django import forms

class CovidSymptomsForm(forms.Form):
    # Predefined list of COVID-19 symptoms
    symptoms = forms.MultipleChoiceField(
        choices=[
            ('fever', 'Fever'),
            ('cough', 'Cough'),
            ('fatigue', 'Fatigue'),
            ('difficulty_breathing', 'Difficulty Breathing'),
            ('headache', 'Headache'),
            ('sore_throat', 'Sore Throat'),
            ('loss_taste', 'Loss of Taste/Smell'),
            ('muscle_pain', 'Muscle Pain'),
            ('chills', 'Chills'),
            ('diarrhea', 'Diarrhea'),
        ],
        widget=forms.CheckboxSelectMultiple,  # Allows multiple checkboxes
        required=True,
        label="Select Symptoms"
    )
