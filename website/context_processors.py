NAV_PRIMARY = [
    {"label": "Our Business", "url_name": "our-business"},
    {"label": "Our Investment Criteria", "url_name": "investment-criteria"},
    {"label": "Our Team", "url_name": "our-team"},
    {"label": "Our Portfolio", "url_name": "our-portfolio"},
    {"label": "Our Impact", "url_name": "our-impact"},
    {"label": "News & Insights", "url_name": "news"},
    {"label": "Contact Us", "url_name": "contact"},
]

NAV_ITEMS = NAV_PRIMARY + [
    {"label": "Investor Data Room", "url_name": "investor-data-room"},
]


def site(request):
    return {
        "nav_items": NAV_ITEMS,
        "nav_primary": NAV_PRIMARY,
        "office_address": "18 Pall Mall, London SW1Y 5LU",
        "office_phone": "+44 20 7430 5945",
        "office_email": "info@prefequity.com",
    }
