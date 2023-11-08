from django.forms import ModelForm
from .models import Article
class ArticleForm(ModelForm):
    class meta:
        model=Article
        fields=['vorname','nachname','date_of_Birth','slug']