from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# form django.core.urlresolvers import reverse
# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=10)

    def __str__(self):
        return self.subject_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=30)

    def __str__(self):
        return self.teacher_name

class TeacherSubjectMapping(models.Model):
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher_name}-{self.subject_name}"

class Section(models.Model):
    Section_name = models.CharField(max_length=3)
    subject_name = models.ManyToManyField(TeacherSubjectMapping)
    def __str__(self):
        return self.Section_name

# S09 Naman Sharma 3215603116 Mr. Ashish MATHS 2016
class Feedback(models.Model):
    student_name = models.CharField(max_length=120, default='Naman Sharma')
    rollno = models.IntegerField(default='03215603116')

    Section_name = models.ForeignKey(Section, on_delete=models.CASCADE, default='S09')
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    teacher_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    batch = models.IntegerField(validators=[
        MaxValueValidator(2100),
        MinValueValidator(2000),
    ], default='2016')

    Punctuality = models.IntegerField(blank=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])
    Subject_knowledge = models.IntegerField(blank=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])
    Behaviour = models.IntegerField(blank=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])
    Method_of_teaching = models.IntegerField(blank=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])
    Audibility = models.IntegerField(blank=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])
    Syllabus_coverage = models.IntegerField(blank=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])

    def get_absolute_url(self):
        return "/detail/%s/" %(self.id)
        # return reverse("detail", kwargs ={"id":self.id})

    def __str__(self):
        return f"{str(self.Section_name)}-{str(self.teacher_name)}-{str(self.teacher_subject)}"
