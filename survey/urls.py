from django.conf.urls import patterns, url

from .views import SurveyVoteView, SurveyListView


urlpatterns = [
    url(r'^vote$', SurveyVoteView.as_view(), name="survey-vote"),
    url(r'^archives$', SurveyListView.as_view(), name="survey-list"),
]
