import environment

from pcari.models import QuantitativeQuestion, Rating, CommentRating, Comment

def comment_update():
	comments = Comment.objects.all()

	for comment in comments:
		ratings = CommentRating.objects.all().filter(cid=comment.id, accounted=False)
		current_ave = comment.average_score * comment.number_rated
		for rating in ratings:
			if rating.score == -1 or rating.score == -2:
				continue
			if rating.accounted == True:
				continue
			current_ave += rating.score
			rating.accounted = True
			rating.save()
			comment.number_rated += 1
		if comment.number_rated == 0:
			continue
		comment.average_score = (current_ave+0.0)/(comment.number_rated+0.0)
		comment.save()

def se_update():
	comments = Comment.objects.all()
	for comment in comments:
		if comment.number_rated == 0:
			continue
		ratings = CommentRating.objects.all().filter(cid=comment.id)
		var = 0
		ave = comment.average_score
		for rating in ratings:
			if rating.score == -1 or rating.score == -2:
				continue
			var += (rating.score - ave + 0.0)**2 / (comment.number_rated + 0.0)
		comment.se = (sqrt(var) + 0.0) / (sqrt(comment.number_rated) + 0.0)
		comment.save()