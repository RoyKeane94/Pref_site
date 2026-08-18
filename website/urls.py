from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("our-business/", views.our_business, name="our-business"),
    path("investment-criteria/", views.investment_criteria, name="investment-criteria"),
    path("our-team/", views.our_team, name="our-team"),
    path("our-portfolio/", views.our_portfolio, name="our-portfolio"),
    path("our-portfolio/<slug:slug>/", views.portfolio_detail, name="portfolio-detail"),
    path("our-impact/", views.our_impact, name="our-impact"),
    path("our-impact/<slug:slug>/", views.case_study, name="case-study"),
    path("news/", views.news, name="news"),
    path("news/<slug:slug>/", views.news_detail, name="news-detail"),
    path("investor-data-room/", views.investor_data_room, name="investor-data-room"),
    path("contact-us/", views.contact, name="contact"),
    path("terms-and-conditions/", views.terms, name="terms"),
    path("privacy-policy/", views.privacy, name="privacy"),
]
