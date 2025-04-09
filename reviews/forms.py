# reviews/forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Review

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        label="Рейтинг",
        help_text="Введите значение от 0 до 5."
    )

    class Meta:
        model = Review
        fields = ["rating", "comment"]