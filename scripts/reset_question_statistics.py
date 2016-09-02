# Include this line at the beginning of every script.
import environment

from pcari.models import QuantitativeQuestion, Rating


questions = QuantitativeQuestion.objects.all()

for q in questions:
	q.average_score = 0
	q.number_rated = 0
	q.save()

ratings = Rating.objects.all().filter(accounted=True)

for r in ratings:
	r.accounted = False
	r.save()

