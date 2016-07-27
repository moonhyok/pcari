from django.contrib import admin

# Register your models here.
from .models import Question, Rating, Comment, Progression


admin.site.register(Question)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Progression)
# admin.site.register(BarDescription)
# admin.site.register(MergingDescription)
# admin.site.register(DustDescription)
# admin.site.register(LensDescription)
# admin.site.register(TidalDescription)
# admin.site.register(EllipticalDescription)
# admin.site.register(SpiralDescription)

# admin.site.register(Introduction)

# admin.site.register(Elliptical)
# admin.site.register(Spiral)
# admin.site.register(Edge)
# admin.site.register(Bulge)
# admin.site.register(Bar)
# admin.site.register(Merging)
# admin.site.register(Dust)
# admin.site.register(Lens)
# admin.site.register(Tidal)
# admin.site.register(UserSession)
# admin.site.register(PrePostTest)
# admin.site.register(Participant)