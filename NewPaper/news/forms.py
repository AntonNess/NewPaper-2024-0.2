from django import forms
from django.core.exceptions import ValidationError
from django.forms import Textarea
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Post, Author
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
   title = forms.CharField(min_length=4)
   class Meta:
       model = Post
       fields = ['title', 'author', 'postCategory', 'text',]

   def clean(self):
       cleaned_data = super().clean()
       title = cleaned_data.get("title")
       text = cleaned_data.get("text")

       if title == text:
           raise ValidationError(
               "Описание не должно быть идентично названию."
           )

       return cleaned_data


class UsersForm(forms.ModelForm):
   class Meta:
       model = User
       fields = '__all__'
#       widgets = {
##           'name': Textarea(attrs={'cols':80, 'rows': 20})
#       }

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'prodected_page.html'

#   def clean(self):
#       cleaned_data = super().clean()
 #      title = cleaned_data.get("title")
 #      text = cleaned_data.get("text")

 #      if title == text:
 #          raise ValidationError(
 #              "Описание не должно быть идентично названию."
  #         )

 #      return cleaned_data

#form = PostForm()

#article = Post.objects.get(pk=1)
#form = PostForm(instance=article)