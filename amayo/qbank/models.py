from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

#Q-bank segment

class qBank(models.Model):
    questionId = models.CharField(max_length=100)
    questionText = models.TextField()
    options = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    yearOfStudy = models.IntegerField()
    unit = models.CharField(max_length=100)
    questionType = models.CharField(max_length=100)


""" Course, Topic, and Resource models for organizing course content
class Course(models.Model):
    name = models.CharField(max_length=100) # Name of the course
    description = models.TextField() # Description of the course

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100) # Name of the topic
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Course that the topic belongs to

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100) # Name of the resource
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Topic that the resource belongs to
    description = models.TextField(blank=True) # Description of the resource (optional)
    file = models.FileField(upload_to='course_resources/', blank=True) # File upload field for the resource (optional)
    link = models.URLField(blank=True) # Link to additional resources (optional)

    def __str__(self):
        return self.name


# Models for different types of questions
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Course that the question belongs to
    question_type = models.CharField(max_length=100, choices=[
        ('MCQ', 'Multiple Choice Question'),
        ('SAQ', 'Short Answer Question'),
        ('IVQ', 'Image/Video Question'),
    ]) # Type of the question (Multiple Choice, Short Answer, or Image/Video)
    text = models.TextField() # Text of the question
    answer = models.TextField(blank=True) # Answer to the question (optional)
    file = models.FileField(upload_to='image_video_questions/', blank=True) # File upload field for the question (optional)

    def __str__(self):
        return self.text


class MultipleChoiceQuestion(models.Model):
    text = models.TextField() # Text of the question
    correct_answer = models.TextField() # Correct answer to the question
    explanation = models.TextField() # Explanation for the correct answer
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Course that the question belongs to

    def __str__(self):
        return self.text


class ShortAnswerQuestion(models.Model):
    text = models.TextField() # Text of the question
    answer = models.TextField() # Answer to the question
    discussion = models.TextField(blank=True) # Discussion or additional information about the question (optional)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Course that the question belongs to

    def __str__(self):
        return self.text


class ImageVideoQuestion(models.Model):
    text = models.TextField() # Text of the question
    file = models.FileField(upload_to='image_video_questions/') # File upload field for the question
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Course that the question belongs to

    def __str__(self):
        return self.text

#stores the answer given by a user to a particular question
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"



#stores the comment posted by a user to a particular question
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"

#store the results of a user's attempt at a question
class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    passed = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"


#Research segment.

#stores the introduction to research, with a title and content field
class ResearchIntroduction(models.Model):
    title = models.CharField(max_length=100) # Title of the research introduction
    content = models.TextField() # Content of the research introduction

    def __str__(self):
        return self.title


#stores the different categories of research topics, with a name and an optional description field
class ResearchCategory(models.Model):
    name = models.CharField(max_length=100) # Name of the research category
    description = models.TextField(blank=True) # Description of the research category (optional)

    def __str__(self):
        return self.name


#stores research resources
class ResearchResource(models.Model):
    name = models.CharField(max_length=100) # Name of the research resource
    description = models.TextField(blank=True) # Description of the research resource (optional)
    category = models.ForeignKey(ResearchCategory, on_delete=models.CASCADE) # Category that the resource belongs to
    link = models.URLField(blank=True) # URL for the resource (optional)
    file = models.FileField(upload_to='research_resources/', blank=True) # File upload field for the resource (optional)

    def __str__(self):
        return self.name


#stores research methodologies
class ResearchMethodology(models.Model):
    name = models.CharField(max_length=100) # Name of the research methodology
    description = models.TextField(blank=True) # Description of the research methodology (optional)
    category = models.ForeignKey(ResearchCategory, on_delete=models.CASCADE) # Category that the methodology belongs to

    def __str__(self):
        return self.name


#stores data analysis methods
class DataAnalysis(models.Model):
    name = models.CharField(max_length=100) # Name of the data analysis method
    description = models.TextField(blank=True) # Description of the data analysis method (optional)
    category = models.ForeignKey(ResearchCategory, on_delete=models.CASCADE) # Category that the method belongs to

    def __str__(self):
        return self.name

#store student research projects.
class StudentResearch(models.Model):
    title = models.CharField(max_length=100) # Title of the student research project
    authors = models.CharField(max_length=200) # Author(s) of the student research project
    abstract = models.TextField() # Abstract of the student research project
    file = models.FileField(upload_to='student_research/', blank=True) # File upload field for the student research project (optional)
    category = models.ForeignKey(ResearchCategory, on_delete=models.CASCADE) # Category that the project belongs to

    def __str__(self):
        return self.title



#Memoir segment

#store Amayo's storylife and gallery
class AmayoLifeStory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    birth_date = models.DateField(default=date(1999, 5, 15))
    death_date = models.DateField(default=date(2022, 1, 2))
    bio = models.TextField()
    gallery = models.ImageField(upload_to='amayo_gallery/')

    def __str__(self):
        return self.name

#stores philosophy quotes, files,images and personal knowledge
class Philosophy(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    personal_note = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.author}: {self.quote}'
        """