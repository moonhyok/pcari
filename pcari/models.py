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

    english_landing_description = models.CharField(max_length=500, default="Take a minute to see how prepared you are and join the %d others who have visited so far in an online discussion about preparedness.")
    english_question_description = models.CharField(max_length=500, default="Please select how strongly you agree with the following statement")
    english_graph_description = models.CharField(max_length=500, default="Here's how you compare with others")
    english_peer_evaluation_description = models.CharField(max_length=500, default="How helpful is this suggestion? ")
    english_comment_description = models.CharField(max_length=500, default="How could your Barangay help you better prepare for a disaster?")
    english_feedback_description = models.CharField(max_length=500, default="At the end you'll have a chance to give us more feedback")
    english_bloom_description = models.CharField(max_length=500, default="Each sphere below represents an idea proposed by another user")

    english_begin_button = "Begin"
    english_skip_button = "Skip"
    english_next_button = "Next"
    english_post_button = "Post"
    english_submit_button = "Submit"

    english_question_of = "Question %d of %d"
    tagalog_question_of = "Ika-%d ng %d katanungan"

    english_about_pcari = "About PCARI"
    tagalog_about_pcari = "Tungkol sa PCARI"

    english_rate_more_ideas = "Rate More Ideas"
    tagalog_rate_more_ideas = "Bigyan ng grado ang iba pang ideya"

    english_exit = "Exit"
    tagalog_exit = "Lumabas"

    english_more_info = "More Information"
    tagalog_more_info = "Iba pang impormasyon"

    english_suggest_own = "Suggest Your Own Idea"
    tagalog_suggest_own = "Magmungkahi ng iyong sariling ideya"

    english_share_description = "Please share Malasakit with your friends and family"
    tagalog_share_description = "Paki bahagi ang Malasakit sa inyong mga kaibigan at pamilya"

    english_learn_more = "Learn more about how to be prepared for a disaster"
    tagalog_learn_more = "Alamin ang iba pang impormasyon kung paano magiging handa sa isang sakuna"

    english_short_description = "A project by the CITRIS Connected Communities Initiative at UC Berkeley and the Philippine Commission on Higher Education through the Philippine-California Advanced Research Institutes Project."
    tagalog_short_description = "Isang proyekto ng CITRIS Connected Communities Initiative ng UC Berkeley, at ng Commission on Higher Education ng Pilipinas sa pamamagitan ng Philippine-California Advanced Research Institutes Project"

    english_scale_description = "0 (strongly disagree) to 9 (strongly agree)"
    tagalog_scale_description = "Mula 0 (hinding-hindi ako sumasang-ayon) hanggang 9 (lubos akong sumasang-ayon)"

    english_age = "Age"
    tagalog_age = "Susunod"

    english_gender = "Gender"
    tagalog_gender = "Edad"

    english_select = "Select"
    tagalog_select = "Pili ang"

    english_male = "Male"
    tagalog_male = "Lalaki"

    english_female = "Female"
    tagalog_female = "Babae"

    tagalog_landing_description = models.CharField(max_length=500, default="Maglaan ng isang minuto para tingnan kung gaano kayo kahanda, at sumali sa %d iba pa na bumisita sa isang onlayn na diskusyon tungkol sa kahandaan.")
    tagalog_question_description = models.CharField(max_length=500, default="Paki pili kung gaano kayo sumasang-ayon sa mga sumusunod na pangungusap")
    tagalog_graph_description = models.CharField(max_length=500, default="no translation provided")
    tagalog_peer_evaluation_description = models.CharField(max_length=500, default="Gaano ka halaga ang mungkahing ito?")
    tagalog_comment_description = models.CharField(max_length=500, default="Sa papaanong pamamaraan makakatulong ang inyong barangay upang higit na maging handa ka para sa isang kalamidad")
    tagalog_feedback_description = models.CharField(max_length=500, default="Sa dulo, mabibigyan ka ng pagkakataon na magbigay ng iyong mungkahing ideya")
    tagalog_bloom_description = models.CharField(max_length=500, default="Kumakatawan sa mungkahing ideya ng ibang tao ang bawat bilog sa ibaba")

    tagalog_begin_button = models.CharField(max_length=20, default="Simulan")
    tagalog_skip_button = models.CharField(max_length=20, default="Laktawan")
    tagalog_next_button = models.CharField(max_length=20, default="Susunod")
    tagalog_post_button = models.CharField(max_length=20, default="Ipasa")
    tagalog_submit_button = models.CharField(max_length=20, default="Isumite")


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
            'about': self.english_about_pcari,
            'more_info': self.english_more_info,
            'short_description': self.english_short_description,
            'scale_description': self.english_scale_description,
            'suggest_own': self.english_suggest_own,
            'exit': self.english_exit,
            'rate_more': self.english_rate_more_ideas,
            'share_description': self.english_share_description,
            'learn_more': self.english_learn_more,
            "age": self.english_age,
            "gender": self.english_gender,
            "select": self.english_select,
            "male": self.english_male,
            "female": self.english_female,
            'question_of' : self.english_question_of}
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
            'about': self.tagalog_about_pcari,
            'more_info': self.tagalog_more_info,
            'short_description': self.tagalog_short_description,
            'scale_description': self.tagalog_scale_description,
            'suggest_own': self.tagalog_suggest_own,
            'exit': self.tagalog_exit,
            'rate_more': self.tagalog_rate_more_ideas,
            'share_description': self.tagalog_share_description,
            'learn_more': self.tagalog_learn_more,
            "age": self.tagalog_age,
            "gender": self.tagalog_gender,
            "select": self.tagalog_select,
            "male": self.tagalog_male,
            "female": self.tagalog_female,
            'question_of' : self.tagalog_question_of}

class QuantitativeQuestion(models.Model):
    qid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500, default="")
    average_score = models.FloatField(default = 0)
    number_rated = models.IntegerField(default = 0)
    tag = models.CharField(max_length=50, default="")
    tagalog_tag = models.CharField(max_length=50, default="")
    tagalog_question = models.CharField(max_length=500, default="walang tagalog pagsasalin")

class QualitativeQuestion(models.Model):
    qid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500, default="")
    tagalog_question = models.CharField(max_length=500, default="walang tagalog pagsasalin")

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    age = models.IntegerField(default=0)
    barangay = models.CharField(max_length=500, default="")
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null = True)

# If a user does not rate a question, the score will be -2.
# If they choose to skip a question, the score will be -1.
# For qualitative questions, the score will remain -2.
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True)
    qid = models.IntegerField(default = -1)
    date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default = -2)
    response = models.CharField(max_length = 1000, default = "")
    accounted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'qid')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True)
    comment = models.CharField(max_length = 1000, default = "", null = True)
    tagalog_comment = models.CharField(max_length = 1000, default = "", null = True)
    date = models.DateTimeField(auto_now_add = True)
    average_score = models.FloatField(default = 0)
    number_rated = models.IntegerField(default = 0)
    tag = models.CharField(max_length=200, default = "", null=True)
    accounted = models.BooleanField(default=False)

class CommentRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True)
    cid = models.IntegerField(default = -1)
    score = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add = True)

class UserProgression(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add = True)
    landing = models.BooleanField(default=False)
    rating = models.BooleanField(default=False)
    num_rated = models.IntegerField(default=0)
    review = models.BooleanField(default=False)
    bloom = models.BooleanField(default=False)
    peer_rating = models.BooleanField(default=False)
    num_peer_rated = models.IntegerField(default=0)
    personal_data = models.NullBooleanField(default=False)
    comment = models.BooleanField(default=False)
    logout = models.BooleanField(default=False)
    completion_rate = models.IntegerField(default = 0)

class Progression(models.Model):
    landing = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    review = models.FloatField(default=0)
    bloom = models.FloatField(default=0)
    peer_rating = models.FloatField(default=0)
    comment = models.FloatField(default=0)
    logout = models.FloatField(default=0)

class FlaggedComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True)
    comment = models.CharField(max_length = 1000, default = "", null = True)
    tagalog_comment = models.CharField(max_length = 1000, default = "", null = True)
    date = models.DateTimeField(auto_now_add = False)
    average_score = models.FloatField(default = 0)
    number_rated = models.IntegerField(default = 0)
    tag = models.CharField(max_length=200, default = "", null=True)
