from django.contrib import admin

from .models import *
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    # Display the following fields in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'contact_number')

    # Add a search bar to search these fields
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Add filters for these fields
    list_filter = ('first_name',)

    # Specify the order of fields in the detail view
    fields = ('username', 'email', 'password', 'first_name', 'last_name',  'contact_number')

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

# Registering models with their respective admins
admin.site.register(CustomUser, AccountAdmin)
admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)