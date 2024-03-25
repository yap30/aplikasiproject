from django.forms import ModelForm
from django import forms
from validasi.models import *

# define the class of a form
class PostForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Post	 

        # Custom fields
        fields =["name", "gender", "email", "message", "username", "password", "upload_photo" ]
        widgets = {
            'password': forms.PasswordInput(),
        }
    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(PostForm, self).clean()
        
        # extract the username and text field from the data
        name = self.cleaned_data.get('name')
        username = self.cleaned_data.get('username')
        message = self.cleaned_data.get('message')

        #conditions to be met for the username length
        if name:
            if len(name) > 20:
                self._errors['name'] = self.error_class([
                'Maximum 20 characters required'])
        if username:
             if len(username) > 10:
                 self._errors['username'] = self.error_class([
                 'Maximum 10 characters required'])

        if username == name:
            self._errors['username'] = self.error_class([
                'username tidak boleh sama dengan nama'])
        if message:
            if len(message) <10:
                self._errors['text'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        #return any errors if found
        return self.cleaned_data



