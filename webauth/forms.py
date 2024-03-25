from django import forms
from .models import BookModel


# creating a form
class BookForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = BookModel

		# specify fields to be used
		fields = [
			"title",
			"author",
		]
