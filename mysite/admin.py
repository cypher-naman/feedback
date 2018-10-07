from django.contrib import admin

# Register your models here.
from .models import Teacher, Subject, Section, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'rollno', 'batch', 'Section_name','teacher_name', 'teacher_subject', 'Punctuality', 'Subject_knowledge','Behaviour', 'Method_of_teaching', 'Audibility','Syllabus_coverage',)
    # for (a,b) in list_display:
    #     print(a,b)
    # class Meta:
    #     model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Section)
