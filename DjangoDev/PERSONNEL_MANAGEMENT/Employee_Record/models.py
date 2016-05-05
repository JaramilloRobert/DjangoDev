from __future__ import unicode_literals
from django.db import models
import ast

DEFAULT_ORG = -1


# Create your models here.
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class ListModel(models.Model):
    test_list = ListField()




#create a employee record here 
class Employee_Record(models.Model):
    First_Name = models.CharField(max_length=120)
    Last_Name = models.CharField(max_length=120)
    Middile_Initial = models.CharField(max_length=120)
    Rank = models.CharField(max_length=120, default="CIV")
    Orginization = models.ForeignKey('Orginization', default=1)
    #Training = ListField([2,2,2])
    def __str__(self):
        return "Employee Record"


#Orginization model. 
class Orginization(models.Model):
    Platoon = models.CharField(max_length =120)
    Company = models.CharField(max_length=120)
    Battalion = models.CharField(max_length=120)
    Brigade = models.CharField(max_length=120)
    Division = models.CharField(max_length=120)
    Corp = models.CharField(max_length=120)

    #TrainingRequierment = TrainingRequierment()
    #Training_Requierments = models.ManyToManyField('TrainingRequierment')
    #Training = ListField([2,2,2])
    def __str__(self):
        return (self.Company + self.Platoon)



#Training Model
class TrainingRequierment(models.Model): 
    Training_Name  = models.CharField(max_length=256)
    Training_Duration = models.PositiveSmallIntegerField()
    #Orginization = models.ManyToManyField('Orginization')

    #Enlisted Ranks 
    PV1_Requiered = models.BooleanField()
    PV2_Requiered = models.BooleanField()
    PFC_Requiered = models.BooleanField()
    SPC_Requiered = models.BooleanField()
    CPL_Requiered = models.BooleanField()
    SGT_Requiered = models.BooleanField()
    SSG_Requiered = models.BooleanField()
    SFC_Requiered = models.BooleanField()
    MSG_Requiered = models.BooleanField()
    FIRST_SGT_Requiered = models.BooleanField()
    SGM_Requiered = models.BooleanField()
    CSM_Requiered = models.BooleanField()
    SMA_Requiered = models.BooleanField()

    #Warrant Ranks 
    WO1_Requiered = models.BooleanField()
    CW2_Requiered = models.BooleanField()
    CW3_Requiered = models.BooleanField()
    CW4_Requiered = models.BooleanField()
    CW5_Requiered = models.BooleanField()

    #Officer Ranks
    SECOND_LT_Requiered = models.BooleanField()
    FIRST_LT_Requiered = models.BooleanField()
    CPT_Requiered = models.BooleanField()
    MAJ_Requiered = models.BooleanField()
    LTC_Requiered = models.BooleanField()
    COL_Requiered = models.BooleanField()
    BG_Requiered = models.BooleanField()
    MG_Requiered = models.BooleanField()
    LTG_Requiered = models.BooleanField()
    GEN_Requiered = models.BooleanField()
    GA_Requiered = models.BooleanField()

    #Civilian Ranks 
    GS1_Requieres =  models.BooleanField()
    GS2_Requieres =  models.BooleanField()
    GS3_Requieres =  models.BooleanField()
    GS4_Requieres =  models.BooleanField()
    GS5_Requieres =  models.BooleanField()
    GS6_Requieres =  models.BooleanField()
    GS7_Requieres =  models.BooleanField()
    GS8_Requieres =  models.BooleanField()
    GS9_Requieres =  models.BooleanField()
    GS10_Requieres =  models.BooleanField()
    GS11_Requieres =  models.BooleanField()
    GS12_Requieres =  models.BooleanField()
    GS13_Requieres =  models.BooleanField()
    GS14_Requieres =  models.BooleanField()
    GS15_Requieres =  models.BooleanField()

    def __str__(self):
        return self.Training_Name
