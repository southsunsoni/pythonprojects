from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class meta:
        model=Article
        fields=['vorname','nachname','date_of_Birth','slug']