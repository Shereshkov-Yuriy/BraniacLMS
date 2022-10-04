from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("courses_list/", views.CoursesPageView.as_view(), name="courses"),
    path("courses_list/<int:pk>/", views.CoursesDetailView.as_view(), name="courses_detail"),
    path("doc_site/", views.DocSitePageView.as_view(), name="docs"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("news/<int:pk>/", views.NewsPageDetailView.as_view(), name="news_detail"),
]
