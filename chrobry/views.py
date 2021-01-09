from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from chrobry.models import *


def index(request):
	context = {
	"hospital_list": Hospital.nodes.all(),
	"doctor_list": Doctor.nodes.all(),
	"patient_list": Patient.nodes.all()
	}
	return render(request,'template_index.html',context)


def view_hospital(request):
	hospital_name = request.GET['hospital_choosment']
	if not hospital_name:
		return
	hospital = Hospital.nodes.get(name=hospital_name)
	return {
	'title':f'Dane {hospital_name}',
	'dataset':[
	{
		'title' : 'Doktorzy',
		'data':hospital.doctors.all()
	},
	{
		'title' : 'Pacjęci Hospitalizowani',
		'data':hospital.patients.all()
	}
	],
		'selected' : hospital
	}

def view_doctor(request):
	doctor_name = request.GET['doctor_choosment'].split()
	if not doctor_name:
		return
	doctor_last_name = doctor_name[1]
	doctor_name = doctor_name[0]
	doctor = Doctor.nodes.get(name=doctor_name,last_name=doctor_last_name)
	return {
	'title':f'{doctor.name} {doctor_last_name}',
	'dataset':[
	{
		'title' : 'Zabiegi',
		'data':doctor.treatments.all()
	},
	{
		'title' : 'Pracuje w',
		'data' : doctor.work.all()
	},	
	{
		'title' : 'Dokonywane zabiegi',
		'data' : doctor.treatments.all()
	}
	],
		'selected' : doctor
	}

def view_patient(request):
	patient_id = request.GET['patient_choosment']
	if not patient_id:
		return
	patient = Patient.nodes.get(NFZ_ID=patient_id)
	return {
	'title':f'Pacjent {patient.name} {patient.last_name}',
	'dataset':[
	{
		'title' : 'Hospitalizowany w ',
		'data':patient.hospitalized.all()
	},
	{
		'title' : 'Zabiegi',
		'data':patient.treatments.all()
	}
	],
		'selected' : patient
	}

def view_treatment(request):
	treatment_id = request.GET['treatment_choosment']
	if not treatment_id:
		return
	treatment= Treatment.nodes.get(T_ID=treatment_id)
	return {
	'title':f'Zabieg {treatment.T_ID}',
	'dataset':[
	{
		'title' : 'Dokonywany na ',
		'data':treatment.patient.all()
	},
	{
		'title' : 'Dokonywany przez ',
		'data':treatment.doctor.all()
	},
	{
		'title' : 'w szpitalu',
		'data':treatment.hospital.all()
	}
	],
	'selected' : treatment
	}




def view(request):
	if 'hospital_choosment' in request.GET:
		context = view_hospital(request)
	elif 'doctor_choosment' in request.GET:
		context = view_doctor(request)
	elif 'patient_choosment' in request.GET:
		context = view_patient(request)
	elif 'treatment_choosment' in request.GET:
		context = view_treatment(request)

	return render(request,'template_view.html',context)