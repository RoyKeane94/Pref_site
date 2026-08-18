from django.contrib import admin
from django.utils.html import format_html

from .models import HomepageSlide, NewsArticle, PortfolioCompany, TeamMember


def admin_thumb(image):
    if not image:
        return "—"
    return format_html(
        '<img src="{}" alt="" style="height:48px;width:80px;object-fit:cover;border-radius:2px;" />',
        image.url,
    )


@admin.register(PortfolioCompany)
class PortfolioCompanyAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "logo_thumb", "name", "sector", "status", "invested_on", "featured_on_home")
    list_filter = ("status", "sector")
    list_display_links = ("thumbnail", "name")
    prepopulated_fields = {"slug": ("name",)}
    fields = (
        "name",
        "slug",
        "logo",
        "image",
        "sector",
        "head_office",
        "transaction_type",
        "invested_on",
        "status",
        "summary",
        "company_quote",
        "company_quote_attribution",
        "quote",
        "quote_attribution",
        "featured_on_home",
        "display_order",
    )

    @admin.display(description="Image")
    def thumbnail(self, obj):
        return admin_thumb(obj.image)

    @admin.display(description="Logo")
    def logo_thumb(self, obj):
        return admin_thumb(obj.logo)


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "title", "published_on", "featured_on_home")
    list_display_links = ("thumbnail", "title")
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        "title",
        "slug",
        "image",
        "category",
        "tag",
        "author",
        "published_on",
        "excerpt",
        "body",
        "featured_on_home",
    )

    @admin.display(description="Image")
    def thumbnail(self, obj):
        return admin_thumb(obj.image)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "display_order")


@admin.register(HomepageSlide)
class HomepageSlideAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "title", "alt_text", "is_active", "display_order")
    list_editable = ("is_active", "display_order")
    list_display_links = ("thumbnail", "title")
    ordering = ("display_order", "id")

    @admin.display(description="Image")
    def thumbnail(self, obj):
        return admin_thumb(obj.image)
