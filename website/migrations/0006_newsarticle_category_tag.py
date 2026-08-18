from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_portfoliocompany_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsarticle",
            name="category",
            field=models.CharField(
                choices=[("news", "News"), ("insights", "Insights")],
                default="news",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="newsarticle",
            name="tag",
            field=models.CharField(
                blank=True,
                help_text="Optional label shown on cards, e.g. a portfolio company name.",
                max_length=80,
            ),
        ),
    ]
