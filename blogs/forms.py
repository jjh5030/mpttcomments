from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	parent_id = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'parent'}), required=False)

	class Meta:
		model = Comment
		fields = ('comment','parent')