from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from website import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("favicon.ico", views.favicon, name="favicon"),
    path("", include("website.urls")),
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT},
        name="media",
    ),
]

handler400 = "website.views.bad_request"
handler403 = "website.views.permission_denied"
handler404 = "website.views.page_not_found"
handler500 = "website.views.server_error"
