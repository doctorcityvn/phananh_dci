from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    Type_id = forms.CharField(label="ID",max_length=30,initial=1)
    codepatientp = forms.CharField(label="Code:",max_length=254,initial="BN" )
    namepatient = forms.CharField(label="Họ tên: ",max_length=2000,initial="Nguyễn")
    age = forms.CharField(label="Tuổi: ",max_length=2000,initial="40")
    place = forms.CharField(label="Địa chỉ: ",max_length=2000,initial="Thanh Xuân")
    city = forms.CharField(label="City: ",max_length=2000,initial="Hà Nội")



    def clean(self):
        cleaned_data = super(ContactForm, self).clean()



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    bio = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', 'bio', 'location',)
