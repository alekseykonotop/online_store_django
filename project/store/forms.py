from django import forms
from .models import Article, Feedback
from ckeditor.widgets import CKEditorWidget


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['published', 'title', 'content', 'products', ]


PRODUCT_RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label='Имя')
    text = forms.CharField(label='Отзыв', widget=forms.widgets.Textarea())
    rating = forms.ChoiceField(label='Оценка', choices=PRODUCT_RATING, widget=forms.RadioSelect())

    class Meta:
        model = Feedback
        exclude = ['product']
