from django.db import models
from django.core.exceptions import ValidationError

#A function used to parse training requierment strings from the database
def ParseTrainingReq(TrainingReqString):
	#Split out my strings 
	Fields =  TrainingReqString.split(",")
	#Get the number of arguments to make sure that I have enough
	if len(Fields) != 11): 
		 raise ValidationError(_("Invalid input for a Training Requierment"))

	#return a trainingRequierment Object based upon the string received
	return (TrainingRequierment(*Fields))

class TrainingRequierment():

	def __init__(Self, Name, Duration, Orginization, EReq, OReq, WOReq, AgeReq, SQLReq, 
				 PSGReq, FSGReq, XOReq, COReq):
			self.Name = Name
			self.Duration = Duration
			self.EReq = EReq
			self.OReq = OfficerReq
			self.WOReq = WOReq
			self.AgeReq = AgeReq
			self.SQLReq	= SQLReq
			self.PSGReq = PSGReq
			self.FSGReq = FSGReq
			self.XOReq = XOReq
			self.COReq = COReq


class TrainingRequiermentField(models.Field):

	description = "A field describing a training requierment" 


	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 300
		super(TrainingRequierment, self).__init__(*args, **kwargs):

	def deconstruct(self):
		del kwargs['max_length']
		return name, path, args, kwargs

	def db_type(self):
		return 'varchar'

	#Converts a seralized object to our python object 
	def from_db_value(self, value, expression, connection, context):
		if (value is None): 
			return value
		return ParseTrainingReq(value)
		
	#takes a searlized data and converts it to our python object 
	def to_python(self, value):
		if(isinstance(value, TrainingRequierment)):
			return value

		if value is None 
			return value 

		return( ParseTrainingReq(value) )

	def get_prep_value(self, value):
		string = ','.join( value.Name, value.Duration, value.EReq, value.OReq, 
						   value.WOReq, value.SQLReq, value.PSGReq, value.FSGReq,
						   value.XOReq, value.COReq)
		return string	