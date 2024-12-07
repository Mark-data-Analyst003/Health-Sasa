from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Consultation, SymptomsInput
from .forms import CovidSymptomsForm  

# Home page
def home(request):
    return render(request, 'index.html')

# Consultation creation
@login_required(login_url='accounts:login')
def consultation(request):
    if request.method == 'POST':
        consultation = Consultation(
            user=request.user,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            date=request.POST.get('date'),
            department=request.POST.get('department'),
            doctor=request.POST.get('doctor'),
            message=request.POST.get('message'),
        )
        consultation.save()
        messages.success(request, "Consultation successfully created.")
        return redirect('sasa_app:show_appointments')
    return render(request, 'consultation.html')

# COVID-19 symptoms checker
COVID_SYMPTOMS = [
    'fever', 'cough', 'fatigue', 'difficulty_breathing',
    'headache', 'sore_throat', 'loss_taste', 'muscle_pain',
    'chills', 'diarrhea'
]

def covid_diagnosis(selected_symptoms):
    high_risk_symptoms = {'fever', 'cough', 'difficulty_breathing', 'fatigue', 'loss_taste'}
    high_risk_count = sum(1 for symptom in selected_symptoms if symptom in high_risk_symptoms)
    return ("Positive" if high_risk_count >= 3 else "Negative", high_risk_count)

@login_required(login_url="accounts:login")
def symptomsChecker(request):
    form = CovidSymptomsForm()  
    if request.method == "POST":
        form = CovidSymptomsForm(request.POST)  
        if form.is_valid():
            selected_symptoms = form.cleaned_data['symptoms']
            sex = request.POST.get('sex')
            age = request.POST.get('age')
            country = request.POST.get('country')

            # Ensure all additional fields are filled
            if not all([sex, age, country]):
                messages.error(request, "All fields are required.")
                return render(request, 'symptoms_input.html', {'form': form})

            # Process the symptoms and get the diagnosis
            result, count = covid_diagnosis(selected_symptoms)
            messages.success(request, "Symptoms submitted successfully. We'll analyze your input.")

            # Render the results
            return render(request, 'results.html', {
                'result': result, 'count': count,
                'symptoms': selected_symptoms, 'sex': sex, 'age': age, 'country': country
            })

    # Render the form for symptoms
    return render(request, 'symptoms_input.html', {'form': form})

# Retrieve consultations
@login_required(login_url="accounts:login")
def retrieve_appointments(request):
    appointments = Consultation.objects.filter(user=request.user)
    return render(request, 'show_appointments.html', {'appointments': appointments})

# Delete appointment
def delete_appointment(request, id):
    appointment = get_object_or_404(Consultation, id=id)
    appointment.delete()
    messages.success(request, "Appointment successfully deleted.")
    return redirect("sasa_app:show_appointments")

# Update consultation
def edit_consultation(request, appointment_id):
    appointment = get_object_or_404(Consultation, id=appointment_id)
    if request.method == 'POST':
        for field in ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']:
            setattr(appointment, field, request.POST.get(field))
        appointment.save()
        messages.success(request, "Consultation updated successfully.")
        return redirect("sasa_app:show_appointments")

    return render(request, "edit_consultation.html", {'appointment': appointment})


def results(request):
    return render(request, 'results.html')


def retrieve_symptoms_input(request):
    symptoms_input = SymptomsInput.objects.all()
    return render(request, 'show_symptoms.html', {'symptoms_input': symptoms_input})
