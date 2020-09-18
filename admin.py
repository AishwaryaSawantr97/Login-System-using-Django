from django.contrib import admin
from .models import Tutorial
from django.utils import timezone


Tutorial.objects.all()
new_tutorial=Tutorial(tutorial_title="To be",tutorial_content="...or not to be",tutorial_published=timezone.now())
new_tutorial.save()


class TutorialAdmin(admin.ModelAdmin):
    fields= ["tutorial_title",
             "tutorial_published",
             "tutorial_content"]

    fieldsets= [
        ("Title/date",{"fields": ["tutorial_title", "tutorial_published"]}),
        ('Content',{"fields":["tutorial_content"]})
    ]


admin.site.register(Tutorial)

