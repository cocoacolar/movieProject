from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    MBTI_CHOICES = [
        ('ISTJ', 'ISTJ'),
        ('ISFJ', 'ISFJ'),
        ('INFJ', 'INFJ'),
        ('INTJ', 'INTJ'),
        ('ISTP', 'ISTP'),
        ('ISFP', 'ISFP'),
        ('INFP', 'INFP'),
        ('INTP', 'INTP'),
        ('ESTP', 'ESTP'),
        ('ESFP', 'ESFP'),
        ('ENFP', 'ENFP'),
        ('ENTP', 'ENTP'),
        ('ESTJ', 'ESTJ'),
        ('ESFJ', 'ESFJ'),
        ('ENFJ', 'ENFJ'),
        ('ENTJ', 'ENTJ'),
    ]

    # blank=True 속성으로 빈값도 입력받을 수 있게끔 설정. null과는 다름.
    mbti = models.CharField(blank=True, choices=MBTI_CHOICES, max_length=4) 
    