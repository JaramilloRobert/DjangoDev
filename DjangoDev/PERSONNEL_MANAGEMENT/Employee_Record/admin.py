from django.contrib import admin

# Register your models here.
from .models import Employee_Record, Orginization, TrainingRequierment


class EmployeeRecordsAdmin(admin.ModelAdmin):

	#define how the admin will look 
	list_display = ["Rank", "Last_Name", "First_Name", "Orginization"]
	list_display_links = ["Last_Name"]
	list_filter = ["Rank", "Orginization"]
	class Meta:
		model = Employee_Record


class TrainingRequiermentAdmin(admin.ModelAdmin):
	list_display = ["Training_Name", "Training_Duration"]
	class Meta: 
		model = TrainingRequierment

	


#Now make sure that our employee record shows uo on the admin site
admin.site.register(Orginization)
admin.site.register(TrainingRequierment, TrainingRequiermentAdmin)
admin.site.register(Employee_Record, EmployeeRecordsAdmin)
