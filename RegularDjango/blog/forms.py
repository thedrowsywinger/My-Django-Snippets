from django import forms

from blog.models import BlogUploaderModel

from ckeditor.widgets import CKEditorWidget

class UploadingForm(forms.ModelForm):

	class Meta:
		model = BlogUploaderModel
		fields = [
			'author',
			'title',
			'header_image',
			'body',
			'abstract',
			'keywords',
			'category'
		]

	def __init__(self, *args, **kwargs):

		super(UploadingForm,self).__init__(*args, **kwargs)
		self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})
		self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
		self.fields['header_image'].widget.attrs.update({'class': 'form-control'})
		self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Body'})
		self.fields['abstract'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Abstract'})
		self.fields['keywords'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Keyword'})
		self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Category'})
		# self.fields['issue_date'].widget.attrs.update({'class': 'form-control'})
