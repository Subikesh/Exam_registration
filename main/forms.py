from django import forms
from .models import Register, Subject, Subject_attempts

class RegisterForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		# Retrieving the request instance from Register view to get the current user
		self.request = kwargs.pop('request')
		super(RegisterForm, self).__init__(*args, **kwargs)

		subject_query = Subject.objects.filter(Semester__lte = self.request.user.student.Semester).\
	        filter(Department= self.request.user.student.Department).\
	        exclude(pk__in= self.request.user.registrations.values('Subjects')).\
	        exclude(Sub_code__in = Subject_attempts.objects.\
	            filter(Student = self.request.user).\
	            filter(Passed = True).values('Sub_code'))
		self.fields['Subjects'].queryset = subject_query

	class Meta:
		model = Register 
		fields = ['Subjects']

	Subjects = forms.ModelMultipleChoiceField(
		queryset = Subject.objects.all() ,
		widget = forms.CheckboxSelectMultiple
	)