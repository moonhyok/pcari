from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User

# IMPORTANT: Create only one instance
class GeneralSetting(models.Model):
    LANGUAGE_CHOICES = (
    ('English', 'English'),
    ('Tagalog', 'Tagalog'),
    )

    default_language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES, default="English")

    english_landing_description = models.CharField(max_length=500, default="Join others to amplify Philippine's collective intelligence")
    english_question_description = models.CharField(max_length=500, default="Please grade Philippine government's effectiveness on:")
    english_graph_description = models.CharField(max_length=500, default="The plots below show the average trend of the ratings.")
    english_peer_evaluation_description = models.CharField(max_length=500, default="How important is this issue?")
    english_comment_description = models.CharField(max_length=500, default="Please write your comment below")
    english_feedback_description = models.CharField(max_length=500, default="At the end you'll have a chance to give us more feedback")
    english_bloom_description = models.CharField(max_length=500, default="Each sphere below represents an idea proposed by another user")

    english_begin_button = "Begin"
    english_skip_button = "Skip"
    english_next_button = "Next"
    english_post_button = "Post"
    english_submit_button = "Submit"

    english_question_word = "Question"
    english_of_word = "of"

    tagalog_landing_description = models.CharField(max_length=500, default="Tagalog Landing")
    tagalog_question_description = models.CharField(max_length=500, default="Tagalog Question")
    tagalog_graph_description = models.CharField(max_length=500, default="Tagalog Graph Description")
    tagalog_peer_evaluation_description = models.CharField(max_length=500, default="Tagalog Peer Evaluation")
    tagalog_comment_description = models.CharField(max_length=500, default="Tagalog Comment Description")
    tagalog_feedback_description = models.CharField(max_length=500, default="Tagalog Feedback Description")
    tagalog_bloom_description = models.CharField(max_length=500, default="Tagalog Bloom Description")

    tagalog_begin_button = models.CharField(max_length=20, default="Magsimula")
    tagalog_skip_button = models.CharField(max_length=20, default="Laktawan")
    tagalog_next_button = models.CharField(max_length=20, default="Susunod")
    tagalog_post_button = models.CharField(max_length=20, default="Koreo")
    tagalog_submit_button = models.CharField(max_length=20, default="Ipasa")

    tagalog_question_word = "Tanong"

    tagalog_of_word = "mula sa"

    def get_text(self, language = None):
        if language == None:
            language = self.default_language

        translate = {"English":"Tagalog","Tagalog":"English"}[language]

        if language == "English":
            return {'translate' : translate,
            'landing_description' : self.english_landing_description,
            'question_description' : self.english_question_description,
            'graph_description' : self.english_graph_description,
            'peer_evaluation_description' : self.english_peer_evaluation_description,
            'comment_description' : self.english_comment_description,
            'feedback_description' : self.english_feedback_description,
            'bloom_description' : self.english_bloom_description,
            'begin_button' : self.english_begin_button,
            'skip_button' : self.english_skip_button,
            'next_button' : self.english_next_button,
            'post_button' : self.english_post_button,
            'submit_button' : self.english_submit_button,
            'question_word' : self.english_question_word,
            'of_word' : self.english_of_word}
        else:
            return {'translate':translate,
            'landing_description' : self.tagalog_landing_description,
            'question_description' : self.tagalog_question_description,
            'graph_description' : self.tagalog_graph_description,
            'peer_evaluation_description' : self.tagalog_peer_evaluation_description,
            'comment_description' : self.tagalog_comment_description,
            'feedback_description' : self.tagalog_feedback_description,
            'bloom_description' : self.tagalog_bloom_description,
            'begin_button' : self.tagalog_begin_button,
            'skip_button' : self.tagalog_skip_button,
            'next_button' : self.tagalog_next_button,
            'post_button' : self.tagalog_post_button,
            'submit_button' : self.tagalog_submit_button,
            'question_word' : self.tagalog_question_word,
            'of_word' : self.tagalog_of_word}

class QuantitativeQuestion(models.Model):
    qid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500, default="")
    average_score = models.IntegerField(default = 0)
    tagalog_question = models.CharField(max_length=500, default="walang tagalog pagsasalin")

class QualitativeQuestion(models.Model):
    qid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500, default="")
    tagalog_question = models.CharField(max_length=500, default="walang tagalog pagsasalin")


# If a user does not rate a question, the score will be -2.
# If they choose to skip a question, the score will be -1.
# For qualitative questions, the score will remain -2.
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True)
    qid = models.IntegerField(default = -1)
    date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default = -2)
    response = models.CharField(max_length = 1000, default = "")

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True)
    comment = models.CharField(max_length = 1000, default = "", null = True)
    tagalog_comment = models.CharField(max_length = 1000, default = "", null = True)
    date = models.DateTimeField(auto_now_add = True)
    average_score = models.IntegerField(default = 0)
    number_rated = models.IntegerField(default = 0)
    tag = models.CharField(max_length=200, default = "", null=True)

class CommentRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True)
    cid = models.IntegerField(default = -1)
    score = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add = True)

class UserProgression(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True)
    date = models.DateTimeField(auto_now_add = True)
    landing = models.BooleanField(default=False)
    rating = models.BooleanField(default=False)
    num_rated = models.IntegerField(default=0)
    review = models.BooleanField(default=False)
    bloom = models.BooleanField(default=False)
    peer_rating = models.BooleanField(default=False)
    num_peer_rated = models.IntegerField(default=0)
    comment = models.BooleanField(default=False)
    logout = models.BooleanField(default=False)
    completion_rate = models.IntegerField(default = 0)

class Progression(models.Model):
    landing = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    review = models.IntegerField(default=0)
    bloom = models.IntegerField(default=0)
    peer_rating = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    logout = models.IntegerField(default=0)
