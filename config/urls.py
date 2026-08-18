from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
]

handler400 = "website.views.bad_request"
handler403 = "website.views.permission_denied"
handler404 = "website.views.page_not_found"
handler500 = "website.views.server_error"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
