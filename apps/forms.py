

from django import forms


class PhoneForm(forms.Form):
    tel = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'detailinfo__wrappers-input',
                "placeholder":'+7'
            }
        )
    )

class FormEmail(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'app-form-control',
                "placeholder":'имя'
            }
        )
    )
    tel = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'app-form-control',
                "placeholder":'+7'
            }
        )
    )
    des = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'app-form-control',
                "placeholder":'Вопрос'
            }
        )
    )