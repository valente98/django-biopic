from django import forms
from PIL import Image, ImageFilter
from app.models import ImagePostModel


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


# class Likes(forms.):
# class LoginForm(forms.Form):

# class SignupForm(forms.Form):
#     Username = forms.CharField()
#     Email = forms.CharField()
#     Password = forms.CharField()