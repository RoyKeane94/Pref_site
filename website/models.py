from django.db import models
from django.urls import reverse


class PortfolioCompany(models.Model):
    class Status(models.TextChoices):
        CURRENT = "current", "Current"
        REALISED = "realised", "Realised"

    name = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    sector = models.CharField(max_length=80)
    head_office = models.CharField(max_length=80)
    transaction_type = models.CharField(max_length=80)
    invested_on = models.DateField()
    status = models.CharField(max_length=20, choices=Status.choices)
    summary = models.TextField()
    quote = models.TextField(blank=True)
    quote_attribution = models.CharField(max_length=160, blank=True)
    company_quote = models.TextField(blank=True)
    company_quote_attribution = models.CharField(max_length=160, blank=True)
    image = models.ImageField(
        upload_to="portfolio/",
        blank=True,
        help_text="Hero and card image for this deal.",
    )
    logo = models.ImageField(
        upload_to="portfolio/logos/",
        blank=True,
        help_text="Company logo, shown on portfolio cards and the deal page.",
    )
    featured_on_home = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("portfolio-detail", kwargs={"slug": self.slug})

    def summary_parts(self):
        paragraphs = [part.strip() for part in self.summary.split("\n\n") if part.strip()]
        if len(paragraphs) <= 1:
            return "", paragraphs
        return paragraphs[0], paragraphs[1:]


class NewsArticle(models.Model):
    class Category(models.TextChoices):
        NEWS = "news", "News"
        INSIGHTS = "insights", "Insights"

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=120, default="Johnny Carew Pole")
    published_on = models.DateField()
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.NEWS,
    )
    tag = models.CharField(
        max_length=80,
        blank=True,
        help_text="Optional label shown on cards, e.g. a portfolio company name.",
    )
    excerpt = models.TextField(blank=True)
    body = models.TextField(
        blank=True,
        help_text="Full article. If blank, the excerpt is shown on the article page.",
    )
    image = models.ImageField(
        upload_to="news/",
        blank=True,
        help_text="Hero and card image for this article.",
    )
    featured_on_home = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"slug": self.slug})


class TeamMember(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=160)
    bio = models.TextField()
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class HomepageSlide(models.Model):
    title = models.CharField(
        max_length=160,
        blank=True,
        help_text="Optional caption shown on the homepage carousel.",
    )
    alt_text = models.CharField(
        max_length=160,
        help_text="Describe the image for accessibility.",
    )
    image = models.ImageField(upload_to="carousel/")
    link_url = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional link, e.g. /our-portfolio/ilektra/ or a full URL.",
    )
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "id"]
        verbose_name = "Homepage carousel slide"
        verbose_name_plural = "Homepage carousel slides"

    def __str__(self):
        return self.title or self.alt_text or f"Slide {self.pk}"
