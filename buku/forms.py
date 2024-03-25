from django import forms
from .models import BukuModel


# creating a form
class BukuForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = BukuModel

		# specify fields to be used
		fields = [
			"title_book",
			"description_book",
            "date_book",
            "author_book",
            "file_book",
		]


