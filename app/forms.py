from django import forms
from PIL import Image, ImageFilter
from app.models import ImagePostModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImagePostModel
        fields = ('uploaded_by', 'image', 'caption')


class Filters(forms.Form):
    choice = {
        'BLUR': 'Blur',
        'CONTOUR': 'Contour',
        'DETAIL': 'Detail',
        'EDGE_ENHANCE': 'Edge Enhance',
        'EDGE_ENHANCE_MORE': 'Edge Enhance More',
        'EMBOSS': 'Emboss',
        'FIND_EDGES': 'Find Edges',
        'SMOOTH': 'Smooth',
        'SMOOTH_MORE': 'Smooth More',
        'SHARPEN': 'Sharpen'
    }
    Filter_Choice = forms.ChoiceField(choices=(choice.items()))

    def filters(self):
        return {
            'BLUR': ImageFilter.BLUR,
            'CONTOUR': ImageFilter.CONTOUR,
            'DETAIL': ImageFilter.DETAIL,
            'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
            'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
            'EMBOSS': ImageFilter.EMBOSS,
            'FIND_EDGES': ImageFilter.FIND_EDGES,
            'SMOOTH': ImageFilter.SMOOTH,
            'SMOOTH_MORE': ImageFilter.SMOOTH_MORE,
            'SHARPEN': ImageFilter.SHARPEN
        }.get(self.cleaned_data['Filter_Choice'], None)


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=50)

    def __init__(self, post=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.post = post

    def save(self):
        return self.post.comments_set.create(
            comment=self.cleaned_data['comment'])


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )