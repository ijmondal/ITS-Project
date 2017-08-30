
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from website import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^households/', views.HouseholdsList.as_view()),
    url(r'^points/', views.PointsList.as_view()),
    url(r'^members/', views.MembersList.as_view()),
    url(r'^farms/', views.FarmsList.as_view()),
    url(r'^farmPoints/', views.Farm_pointsList.as_view()),
    url(r'^cropping/', views.CroppingList.as_view()),
    url(r'^crops/', views.CropsList.as_view()),
    url(r'^seasons/', views.SeasonsList.as_view()),
    url(r'^wells/', views.WellsList.as_view()),
    url(r'^yields/', views.YieldsList.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)


