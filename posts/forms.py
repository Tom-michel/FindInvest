from dataclasses import field
from pyexpat import model
from django import forms
from .models import Projet, Commentaire, Reponse


class ProjetForm(forms.ModelForm):
	class Meta():
		model = Projet
		fields = [
			'title',
			'categorie',
			'media',
			'image',
			'investi',
			'description',
			'etudiant',
            
		]

# class ComForm(forms.ModelForm):
# 	class Meta():
# 		model = Commentaire
# 		fields = ['corps',]
# 		labels = {'corps': 'Commentaires'}
# 		widgets = {
# 			'corps': forms.Textarea(attrs={
# 				'class':'form-control',
# 				'rows':4,
# 				'cols':70,
# 				'placeholder':'Votre commentaire'
# 			})
# 		}

class RepForm(forms.ModelForm):
	class Meta():
		model = Reponse
		fields = ['corps',]
		labels = {'corps': 'Reponses'}
		widgets = {
			'corps': forms.Textarea(attrs={
				'class':'form-control',
				'rows':2,
				'cols':10,
				'placeholder':'Votre réponse'
			})
		}

