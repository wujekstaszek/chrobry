from neomodel  import StringProperty,DateTimeProperty,UniqueIdProperty,IntegerProperty,RelationshipTo,RelationshipFrom
from neomodel.cardinality import *
from django_neomodel import DjangoNode

class Hospital(DjangoNode):
	hid = IntegerProperty(required=True)
	name = StringProperty(required=True)
	addres = StringProperty(required=True)
	doctors = RelationshipFrom("Doctor","WORKS",cardinality=ZeroOrMore)
	patients = RelationshipFrom("Patient","HOSPITALIZED",cardinality=ZeroOrMore)
	treatments = RelationshipFrom("Treatment","TAKE PLACE",cardinality=ZeroOrMore)



class Doctor(DjangoNode):
	name = StringProperty(required=True)
	last_name = StringProperty(required=True)
	PWZ_ID = IntegerProperty(required=True)
	spec = StringProperty()
	work = RelationshipTo("Hospital","WORKS",cardinality=OneOrMore)
	treatments = RelationshipFrom("Treatment","TREAT",cardinality=ZeroOrMore)



class Patient(DjangoNode):
	name = StringProperty(required=True)
	last_name = StringProperty(required=True)
	NFZ_ID = IntegerProperty(required=True)
	addres = StringProperty(required=True)
	phone = IntegerProperty()
	hospitalized = RelationshipTo("Hospital","HOSPITALIZED",cardinality=ZeroOrOne)
	treatments = RelationshipTo("Treatment","HAS/HAD SCHEDULDED",cardinality=ZeroOrMore)


class Treatment(DjangoNode):
	date = DateTimeProperty(required=True)
	description = StringProperty(required=True)
	patient = RelationshipFrom("Patient","HAS/HAD SCHEDULDED",cardinality=One)
	doctor = RelationshipTo("Doctor","TREAT",cardinality=One)
	hospital = RelationshipTo("Hospital","TAKE PLACE",cardinality=One)








# Create your models here.
