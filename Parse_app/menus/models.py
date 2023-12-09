import random
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=50,default='DefaultFirstName')
    last_name = models.CharField(max_length=50,default='DefaultLastName')
    contact_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.username}"
    
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        return self.question

class Category(BaseModel):
    category_name =  models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

    def __str__(self) -> str:
        return self.category_name
    
class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        random.shuffle(answer_objs)  
        data = []

        for answer_obj in answer_objs:
            data.append({
                'answer' : answer_obj.answer,
                'is_correct' : answer_obj.is_correct
            })

        return data
    
class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer