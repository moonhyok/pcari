from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
from pcari.models import  QuantitativeQuestion, QualitativeQuestion, Rating, UserProgression, Comment, CommentRating, GeneralSetting, UserData
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import logout

import json
import random

# !IMPORTANT! YOU MUST COMMENT OUT THE FOLLOWING GLOBAL VARIABLES
# IF YOU MAKE CHANGES TO models.py
QUAN_QUESTIONS = list(QuantitativeQuestion.objects.all())
QUAL_QUESTIONS = list(QualitativeQuestion.objects.all())
QUAN_COUNT = QuantitativeQuestion.objects.all().count()
QUAL_COUNT = QualitativeQuestion.objects.all().count()

Q_COUNT = QUAN_COUNT + QUAL_COUNT

random.shuffle(QUAN_QUESTIONS)
random.shuffle(QUAL_QUESTIONS)

TEXT = GeneralSetting.objects.all()[0].get_text()


def switch_language(request):
    global TEXT 
    TEXT= GeneralSetting.objects.all()[0].get_text(TEXT['translate'])
    try:
        progression = UserProgression.objects.all().filter(user=request.user)[0]
        if progression.num_rated <= Q_COUNT:
            progression.num_rated -= 1
            progression.save()
    except:
        pass
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def landing(request):
    # logout(request)
    description = TEXT['landing_description'] % len(User.objects.all())
    context = {
    'translate':TEXT['translate'], 
    'landing_description':description, 
    'more_info':TEXT['more_info'],
    'short_description':TEXT['short_description'],
    'begin':TEXT['begin_button']
    }
    return render(request, 'landing.html', context)

def create_user(request):

    #User Authentication
    uid = User.objects.all().count()
    new_user = User.objects.create_user('%d' % uid,'%d@example.com' % uid,'%d' % uid)
    new_user.save()
    
    user = authenticate(username=new_user.username, password=new_user.username)
    
    login(request,user)

    #Data Initialization
    progression = UserProgression(user = user)
    progression.landing = True
    
    q = QUAN_QUESTIONS[progression.num_rated]

    progression.save()

    question_of = TEXT['question_of'] % (progression.num_rated+1,Q_COUNT)

    context = {
    'translate':TEXT['translate'], 
    'question_description':TEXT['question_description'], 
    'feedback_description':TEXT['feedback_description'], 
    'skip':TEXT['skip_button'],
    'question_of':question_of,
    'question': q.question if TEXT['translate'] == "Tagalog" else q.tagalog_question,
    'scale_description':TEXT['scale_description'],
    'qid': q.qid, 
    'rating':True
    }
    return render(request, 'rating.html', context)

def rate(request, qid):
    user = request.user
    try:
        rating = Rating(user = user, qid = qid)
    except:
        rating = Rating.objects.all().filter(user=user,qid=qid)


    try:
        rating.score = request.POST['choice']
        rating.save()
    except:
        pass

    if rating.score == "Skip" or rating.score == "Laktawan":
        rating.score = -1
        rating.save()

    # if rating.score == "Submit" or rating.score == "Ipasa":
    #     rating.response = request.POST['comment']

    progression = UserProgression.objects.all().filter(user=user)[0]
    progression.rating = True
    progression.num_rated += 1
    progression.save()

    print progression.num_rated
    print "num rated \n"

    if progression.num_rated < Q_COUNT:
        if progression.num_rated < QUAN_COUNT:
            q = QUAN_QUESTIONS[progression.num_rated]
            qualitative = False
        else:
            q = QUAL_QUESTIONS[progression.num_rated-QUAN_COUNT]
            qualitative = True

        question_of = TEXT['question_of'] % (progression.num_rated+1,Q_COUNT)

        context = {
        'translate':TEXT['translate'], 
        'question_description':TEXT['question_description'], 
        'feedback_description':TEXT['feedback_description'], 
        'skip':TEXT['skip_button'],
        'question_of':question_of,
        'question': q.question if TEXT['translate'] == "Tagalog" else q.tagalog_question,
        'scale_description':TEXT['scale_description'],
        'qid': q.qid, 
        'rating':True
        }
        return render(request, 'rating.html', context)

    return personal(request)

def review(request):
    user = request.user
    if not UserData.objects.all().filter(user=user).exists():
        try:
            int(request.POST['age'])
            if request.POST['barangay'] == "" or request.POST['age'] == "" or request.POST['gender'] == "":
                context = {
                'error':"Please enter the following data",
                'about':TEXT['about'],
                'rate_more':TEXT['rate_more'],
                'suggest_own':TEXT['suggest_own'],
                'next':TEXT['next_button'],
                'age':TEXT['age'],
                'gender':TEXT['gender'],
                'male':TEXT['male'],
                'female':TEXT['female'],
                'select':TEXT['select'],
                'translate':TEXT['translate']
                }
                return render(request, 'personal_data.html', context)
        except:    
            context = {
                'error':"Please enter a valid age",
                'about':TEXT['about'],
                'rate_more':TEXT['rate_more'],
                'suggest_own':TEXT['suggest_own'],
                'next':TEXT['next_button'],
                'age':TEXT['age'],
                'gender':TEXT['gender'],
                'male':TEXT['male'],
                'female':TEXT['female'],
                'select':TEXT['select'],
                'translate':TEXT['translate']
                }
            return render(request, 'personal_data.html', context)    

        userdata = UserData(user=user, age=request.POST['age'], barangay=request.POST['barangay'], gender=request.POST['gender'])
        userdata.save()

    progression = UserProgression.objects.all().filter(user=user)[0]
    progression.review = True
    progression.save()
    q = QuantitativeQuestion.objects.all()
    r = Rating.objects.all().filter(user=user)
    user_ratings = map(lambda x: (x.qid,x.score), r)
    user_ratings.sort(key=lambda x: x[0])

    if TEXT['translate'] == "Tagalog":
        tag = map(lambda x: (x.tag,x.qid,user_ratings[x.qid-1][1]), q)
    else:
        tag = map(lambda x: (x.tagalog_tag,x.qid,user_ratings[x.qid-1][1]), q)

    context = {
    'translate':TEXT['translate'],
    'language':True if TEXT['translate'] == "English" else False,
    'graph_description':TEXT['graph_description'],
    'next':TEXT['next_button'],
    'more_info':TEXT['more_info'],
    'tags':tag,
    'n':q.count()
    }
    return render(request, 'review.html', context)

def help(request):
    context = {
    'about':TEXT['about'],
    'rate_more':TEXT['rate_more'],
    'suggest_own':TEXT['suggest_own'],
    'exit':TEXT['exit'],
    'translate':TEXT['translate']
    }
    return render(request, 'help.html', context)

def personal(request):
    user = request.user
    progression = UserProgression.objects.all().filter(user=user)[0]
    progression.personal_data = True
    progression.save()
    context = {
    'about':TEXT['about'],
    'rate_more':TEXT['rate_more'],
    'suggest_own':TEXT['suggest_own'],
    'next':TEXT['next_button'],
    'age':TEXT['age'],
    'gender':TEXT['gender'],
    'male':TEXT['male'],
    'female':TEXT['female'],
    'select':TEXT['select'],
    'translate':TEXT['translate']
    }
    return render(request, 'personal_data.html', context)

def bloom(request, done = False):
    user = request.user
    progression = UserProgression.objects.all().filter(user=user)[0]
    progression.bloom = True
    progression.save()

    # comments = map(lambda x: x.id, Comment.objects.all())
    comments = Comment.objects.all()
    if done:
        data = [{"cid":0,"x_seed":0,"y_seed":0,"shift":0,"n":0}]
    else:
        data = []

    # List of Data
    already_seen = map(lambda x: x.id, CommentRating.objects.all().filter(user=user))
    n = 1
    for c in comments:
        if n > 8:
            break
        if c.id in already_seen:
            continue
        data.append({"cid":c.id, "x_seed":random.random(), "y_seed":random.random(), "shift":random.random() * (1 + 1) - 1,"n":n })
        n += 1

    context = {
    'translate':TEXT['translate'],
    'bloom_description':TEXT['bloom_description'],
    'language':True if TEXT['translate'] == "English" else False,
    'comment_data':data,
    'done':done
    }
    return render(request, 'bloom.html', context)

def comment(request):
    user = request.user
    progression = UserProgression.objects.all().filter(user=user)[0]
    progression.comment = True
    progression.save()

    context = {
    'translate':TEXT['translate'], 
    'comment_description':TEXT['comment_description'],
    'post':TEXT['post_button']
    }
    return render(request, 'comment.html', context)

def logout(request):
    user = request.user
    progression = UserProgression.objects.all().filter(user=user)[0]
    progression.logout = True
    progression.save()

    c = Comment(user=user)
    try:
        c.comment = request.POST['comment']
        c.save()
        # logout(request)
    except:
        pass

    context = {
    'translate':TEXT['translate'],
    'share_description':TEXT['share_description'],
    'learn_more':TEXT['learn_more'],
    'exit':TEXT['exit']
    }
    return render(request, 'logout.html', context)

def get_comment(request):
    cid = request.GET.get("cid")
    c = Comment.objects.all().filter(id=cid)[0]
    # context = {'translate':TEXT['translate'],'comment': c.comment, 'cid': cid}
    context = {
    'translate':TEXT['translate'],
    'peer_evaluation_description':TEXT['peer_evaluation_description'], 
    'skip':TEXT['skip_button'],
    'cid':cid, 
    'comment':c.comment
    }
    return render(request, 'rating.html', context)

def rate_comment(request, cid):
    user = request.user
    progression = UserProgression.objects.all().filter(user=user)[0]
    progression.peer_rating = True
    progression.num_peer_rated += 1
    progression.save()
    cid = cid

    rating = CommentRating(user=user)
    rating.cid = cid
    try:
        score = request.POST['choice']
    except:
        score = -2

    if score == "Skip" or score == "Laktawan":
        score = -1

    rating.score = score

    rating.save()

    if progression.num_peer_rated >= 2:
        print "rate_comment peer>2"
        return bloom(request,done=True)

    return bloom(request)

def update_ratings(user):
    questions = QuantitativeQuestion.objects.all()
    ratings = Rating.objects.all().filter(user=user)
    for r in ratings:
        q = questions[r.qid-1]
        ave = (q.average_score * q.number_rated + r.score) / (q.number_rated + 1)
        q.average_score = ave
        q.number_rated += 1
        q.save()

    # for q in questions:

