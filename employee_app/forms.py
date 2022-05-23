from django import forms
from employee.models import Employee,Team
from .widget import DatePickerInput


#This is for manager Team
class TeamForm(forms.ModelForm):
    TEAM = forms.ChoiceField(choices=Team.TEAM_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Team
        fields = ('employe',)
    
        
# This is for employee
class EmployeeForm(forms.ModelForm):
    position = forms.ChoiceField(choices=Employee.POSITION_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Employee
        fields = "__all__"
        widgets={'hired_on': DatePickerInput(),
                   'birth_date': DatePickerInput(),
                  }