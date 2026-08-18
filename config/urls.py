from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from website import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("favicon.ico", views.favicon, name="favicon"),
    path("", include("website.urls")),
]

handler400 = "website.views.bad_request"
handler403 = "website.views.permission_denied"
handler404 = "website.views.page_not_found"
handler500 = "website.views.server_error"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
