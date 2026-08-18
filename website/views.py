from pathlib import Path

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.paginator import Paginator
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, render

from .case_studies import CASE_STUDIES, get_case_study
from .models import HomepageSlide, NewsArticle, PortfolioCompany, TeamMember


def favicon(request):
    path = finders.find("website/img/favicon.ico")
    if not path:
        fallback = Path(settings.STATIC_ROOT) / "website" / "img" / "favicon.ico"
        path = str(fallback) if fallback.exists() else None
    if not path:
        raise Http404()
    return FileResponse(open(path, "rb"), content_type="image/x-icon")


def home(request):
    return render(
        request,
        "website/home.html",
        {
            "portfolio": PortfolioCompany.objects.filter(
                status__in=[
                    PortfolioCompany.Status.CURRENT,
                    PortfolioCompany.Status.REALISED,
                ]
            ),
            "news": NewsArticle.objects.filter(featured_on_home=True)[:3],
            "slides": HomepageSlide.objects.filter(is_active=True),
        },
    )


def page(request, template, extra=None):
    context = extra or {}
    return render(request, template, context)


def our_business(request):
    return render(
        request,
        "website/pages/business.html",
        {"news": NewsArticle.objects.all()[:3]},
    )


def investment_criteria(request):
    return page(request, "website/pages/criteria.html")


def our_team(request):
    return page(
        request,
        "website/pages/team.html",
        {"team": TeamMember.objects.all()},
    )


def our_portfolio(request):
    deal_types = (
        PortfolioCompany.objects.order_by("transaction_type")
        .values_list("transaction_type", flat=True)
        .distinct()
    )

    return render(
        request,
        "website/pages/portfolio.html",
        {
            "companies": PortfolioCompany.objects.all(),
            "deal_types": deal_types,
            "status_choices": PortfolioCompany.Status.choices,
        },
    )


def portfolio_detail(request, slug):
    company = get_object_or_404(PortfolioCompany, slug=slug)
    related = PortfolioCompany.objects.exclude(pk=company.pk)[:3]
    return render(
        request,
        "website/pages/deal.html",
        {"company": company, "related": related},
    )


def our_impact(request):
    return page(request, "website/pages/impact.html", {"case_studies": CASE_STUDIES})


def case_study(request, slug):
    study = get_case_study(slug)
    if not study:
        raise Http404()

    company = None
    if study.get("company_slug"):
        company = PortfolioCompany.objects.filter(slug=study["company_slug"]).first()

    related = [item for item in CASE_STUDIES if item["slug"] != slug]
    return render(
        request,
        "website/pages/case_study.html",
        {"study": study, "company": company, "related_studies": related},
    )


def news(request):
    paginator = Paginator(NewsArticle.objects.all(), 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return page(
        request,
        "website/pages/news.html",
        {"articles": page_obj, "page_obj": page_obj},
    )


def news_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)
    related = NewsArticle.objects.exclude(pk=article.pk)[:3]
    return render(
        request,
        "website/pages/article.html",
        {"article": article, "related": related},
    )


def investor_data_room(request):
    return page(request, "website/pages/data_room.html")


def contact(request):
    return page(request, "website/pages/contact.html")


def terms(request):
    return page(request, "website/pages/terms.html")


def privacy(request):
    return page(request, "website/pages/privacy.html")


ERROR_LINKS = [
    ("Home", "home"),
    ("Our Business", "our-business"),
    ("Our Portfolio", "our-portfolio"),
    ("News & Insights", "news"),
    ("Contact Us", "contact"),
]


def _error(request, template, status, extra=None):
    context = {"error_links": ERROR_LINKS, **(extra or {})}
    return render(request, template, context, status=status)


def bad_request(request, exception):
    return _error(
        request,
        "400.html",
        400,
        {"error_path": request.path},
    )


def permission_denied(request, exception):
    return _error(request, "403.html", 403)


def page_not_found(request, exception):
    return _error(
        request,
        "404.html",
        404,
        {"error_path": request.path},
    )


def server_error(request):
    return _error(request, "500.html", 500)
