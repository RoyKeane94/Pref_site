from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from website import views


def serve_media(request, path):
    return serve(request, path, document_root=str(settings.MEDIA_ROOT))


urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve_media, name="media"),
    path("admin/", admin.site.urls),
    path("favicon.ico", views.favicon, name="favicon"),
    path("", include("website.urls")),
]

handler400 = "website.views.bad_request"
handler403 = "website.views.permission_denied"
handler404 = "website.views.page_not_found"
handler500 = "website.views.server_error"
