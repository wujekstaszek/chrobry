from neomodel  import StringProperty,DateTimeProperty,UniqueIdProperty,IntegerProperty,RelationshipTo,RelationshipFrom
from neomodel.cardinality import *
from django_neomodel import DjangoNode
from django.forms import ModelForm

class Hospital(DjangoNode):
	hid = IntegerProperty(required=True)
	name = StringProperty(required=True)
	addres = StringProperty(required=True)
	doctors = RelationshipFrom("Doctor","WORKS",cardinality=ZeroOrMore)
	patients = RelationshipFrom("Patient","HOSPITALIZED",cardinality=ZeroOrMore)
	treatments = RelationshipFrom("Treatment","TAKE PLACE",cardinality=ZeroOrMore)
	def __str__(self):
		return f'{self.hid} - {self.name}'
	def details(self):
		return (('Adres: ',self.addres),)
	def url(self):
		return f'/view?hospital_choosment={self.name.replace(" ","+")}'


class Doctor(DjangoNode):
	name = StringProperty(required=True)
	last_name = StringProperty(required=True)
	PWZ_ID = IntegerProperty(required=True)
	spec = StringProperty()
	work = RelationshipTo("Hospital","WORKS",cardinality=OneOrMore)
	treatments = RelationshipFrom("Treatment","TREAT",cardinality=ZeroOrMore)
	def __str__(self):
		return f"{self.PWZ_ID} - {self.name} {self.last_name}"
	def details(self):
		return (('Numer PWZ:',self.PWZ_ID),('Specjalizacja: ',self.spec),)
	def url(self):
		return f'/view?doctor_choosment={self.name}+{self.last_name}'



class Patient(DjangoNode):
	name = StringProperty(required=True)
	last_name = StringProperty(required=True)
	NFZ_ID = IntegerProperty(required=True)
	addres = StringProperty(required=True)
	phone = IntegerProperty()
	hospitalized = RelationshipTo("Hospital","HOSPITALIZED",cardinality=ZeroOrOne)
	treatments = RelationshipTo("Treatment","HAS/HAD SCHEDULDED",cardinality=ZeroOrMore)
	def __str__(self):
		return f"{self.NFZ_ID} - {self.name} {self.last_name}"
	def details(self):
		a=[('Numer NFZ:',self.NFZ_ID),('Adres: ',self.addres),]
		if self.phone:
			a.append(('Telefon: ', self.phone))
		return a
	def url(self):
		return f'/view?patient_choosment={self.NFZ_ID}'



class Treatment(DjangoNode):
	T_ID = IntegerProperty(required=True)
	date = DateTimeProperty(required=True)
	description = StringProperty(required=True)
	patient = RelationshipFrom("Patient","HAS/HAD SCHEDULDED",cardinality=One)
	doctor = RelationshipTo("Doctor","TREAT",cardinality=One)
	hospital = RelationshipTo("Hospital","TAKE PLACE",cardinality=One)
	def __str__(self):
		return f"{self.date} - {self.description}"
	def details(self):
		return (('Data: ',self.date),)
	def url(self):
		return f'/view?treatment_choosment={self.T_ID}'








# Create your models here.
