from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5


class ChoiceInline(admin.StackedInline):
    model = Choice
    fields = ('choice_content', 'is_correct')
    extra = 4

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'question_grade', 'get_lesson')
    list_filter = ['question_grade']
    search_fields = ['question_text']
    def get_lesson(self, obj):
        return obj.lesson.title
    get_lesson.short_description = 'Lesson'
    get_lesson.admin_order_field = 'order'   
 
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('get_question', 'choice_content', 'is_correct')
    list_filter = ['is_correct']
    search_fields = ['choice_content']
    def get_question(self, obj):
        return obj.question.question_text
    get_question.short_description = 'Question'
    get_question.admin_order_field = 'question_text'

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)