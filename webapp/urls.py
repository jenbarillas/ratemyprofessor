from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'loginTest/', views.loginTest, name='loginTest'),
	url(r'profilePage/', views.profilePage, name='profilePage'),
	url(r'searchPage/', views.searchPage, name='searchPage'),
	url(r'professorSearchPage/', views.professorSearchPage, name='professorSearchPage'),
	url(r'courseSearchPage/', views.courseSearchPage, name='courseSearchPage'),
    url(r'^$', views.homepage, name='homepage'),
]