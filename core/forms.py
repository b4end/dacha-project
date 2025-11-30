from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Settlement

class SignUpForm(UserCreationForm):
    """
    Форма регистрации (подачи заявки).
    """
    first_name = forms.CharField(label="Имя", max_length=150, required=True)
    last_name = forms.CharField(label="Фамилия", max_length=150, required=True)
    phone = forms.CharField(label="Номер телефона", max_length=20, required=True, help_text="Для связи и одобрения заявки")
    settlement = forms.ModelChoiceField(
        queryset=Settlement.objects.all(), 
        label="Ваш поселок",
        empty_label="Выберите поселок..."
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('settlement', 'username', 'first_name', 'last_name', 'phone')

# --- ИЗМЕНЕНИЯ ЗДЕСЬ ---

class UserInfoForm(forms.ModelForm):
    """
    Форма ТОЛЬКО для текстовых данных (Имя, Фамилия, Телефон)
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone']

class UserAvatarForm(forms.ModelForm):
    """
    Форма ТОЛЬКО для загрузки аватарки
    """
    class Meta:
        model = User
        fields = ['avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
        }