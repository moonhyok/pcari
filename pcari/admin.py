from django.contrib import admin

# Register your models here.
from .models import QuantitativeQuestion, QualitativeQuestion, Rating, Comment, Progression, GeneralSetting


admin.site.register(QuantitativeQuestion)
admin.site.register(QualitativeQuestion)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Progression)
admin.site.register(GeneralSetting)

