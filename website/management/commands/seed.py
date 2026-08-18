from datetime import date
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from website.models import HomepageSlide, NewsArticle, PortfolioCompany, TeamMember


PORTFOLIO = [
    {
        "name": "Ilektra",
        "slug": "ilektra",
        "sector": "Business services",
        "head_office": "Tamworth",
        "transaction_type": "Growth capital",
        "invested_on": date(2024, 11, 1),
        "status": "current",
        "summary": "Ilektra is a Midlands-based group that designs, installs and maintains sensory technology in the built environment. It operates through Daemon Fire & Security and Custom Technology Solutions. Prefequity's investment will allow the group to strengthen its market position by making selective add-on acquisitions.",
        "quote": "Ilektra is a great example of the kind of business we back with its high level of repeat revenue and deeply experienced management. We look forward to partnering with the Ilektra team as they continue to develop the business.",
        "quote_attribution": "Theo Dickens, Managing Partner at Prefequity",
        "company_quote": "This investment from Prefequity is a significant milestone for Ilektra as it gives us the flexible, non-dilutive funding that is necessary to deliver the next phase of our growth strategy.",
        "company_quote_attribution": "Mayamiko Kachingwe, Board Director of Ilektra",
        "featured_on_home": True,
        "display_order": 1,
        "image_source": "Ilektra_banner.webp",
        "logo_source": "logos/IlektraCombinedAdjustedLogo.webp",
    },
    {
        "name": "KBH",
        "slug": "kbh",
        "sector": "TMT",
        "head_office": "London",
        "transaction_type": "Buy-out",
        "invested_on": date(2025, 11, 1),
        "status": "current",
        "summary": "KBH is a leading out-of-home advertising business specialising in the rail and cinema sectors, led by Ian Reynolds. It is the exclusive provider of on-train advertising for the majority of UK train operating companies, and manages a growing portfolio of digital screens in cinema foyers.",
        "quote": "KBH exemplifies the type of business we seek to support. It holds a dominant and defensible position in a niche market with attractive growth opportunities and is led by a highly committed and experienced management team.",
        "quote_attribution": "Johnny Carew Pole, Partner at Prefequity",
        "company_quote": "The investment from Prefequity marks an important milestone for KBH, providing the flexible funding required to drive the next phase of our growth strategy, as we explore new formats and bolster existing ones.",
        "company_quote_attribution": "Ian Reynolds, Managing Director of KBH",
        "featured_on_home": True,
        "display_order": 2,
        "image_source": "KBHPicture.webp",
        "logo_source": "logos/KBHLogo.webp",
    },
    {
        "name": "Now Education",
        "slug": "now-education",
        "sector": "Business services",
        "head_office": "Birmingham",
        "transaction_type": "Buy-out",
        "invested_on": date(2023, 12, 1),
        "status": "current",
        "summary": "Now Education is one of the UK's leading suppliers of staff for primary, secondary and SEND schools across England and Wales. Founded in 2010, it supplies around 1,600 supply staff to more than 800 schools per week.",
        "quote": "The combination of excellent management, strong cash generation, diverse customer base, publicly funded revenues and stable market demand all provide excellent downside protection for our investment.",
        "quote_attribution": "Johnny Carew Pole, Partner at Prefequity",
        "company_quote": "Prefequity’s approach to investment has allowed me the opportunity to take control of Now Education and Gary to realise his share value. The Prefequity team are pragmatic, forward-thinking people with a keen eye for detail.",
        "company_quote_attribution": "Alex Westwood, Managing Director at Now Education",
        "featured_on_home": True,
        "display_order": 3,
        "image_source": "NE_Blog-Post-Image_Blog-3_Body_v0.2.webp",
        "logo_source": "logos/NOWEducationAdjustedLogo.webp",
    },
    {
        "name": "Central Roofing Group",
        "slug": "central-roofing-group",
        "sector": "Construction",
        "head_office": "Hereford",
        "transaction_type": "Buy-out",
        "invested_on": date(2021, 12, 1),
        "status": "current",
        "summary": "Central Roofing Group is a premium provider of commercial roofing services operating from five branches across England and Wales, with over 35 years' heritage serving education, healthcare, local authorities and specialist private-sector projects.",
        "quote": "Prefequity’s investment benefits from robust downside protection, with the ageing roofs of the UK’s schools and hospitals offering a steady stream of future work for Central, and also participates in the significant upside opportunity as the business expands nationwide.",
        "quote_attribution": "Nick Petrusic, Senior Partner at Prefequity",
        "company_quote": "The directors are delighted to have selected Prefequity as a partner for the next chapter of our journey. We found the structure of Prefequity’s investment particularly attractive as it introduces finance on the right terms to support the next stage of the business’ growth.",
        "company_quote_attribution": "James Broady, Managing Director at Central Roofing Group",
        "featured_on_home": True,
        "display_order": 4,
        "image_source": "CentralGroupPicture2.webp",
        "logo_source": "logos/CentralAdjustedLogo.webp",
    },
    {
        "name": "HCI",
        "slug": "hci",
        "sector": "Financial services",
        "head_office": "Brighton",
        "transaction_type": "Growth capital",
        "invested_on": date(2018, 10, 1),
        "status": "current",
        "summary": "Established in 2000, HCI is a Brighton-based provider of private medical insurance to expatriates in over 120 countries. It acts as an MGA for third-party carriers that bear the insurance risk.\n\nFollowing its original investment of growth capital in 2018, Prefequity provided follow-on investment in 2021 to fund a management buy-out and to allow the founders to exit.",
        "quote": "We are delighted to be partnering with HCI. The management team has built a strong franchise in a niche segment of the health insurance market that enjoys a high level of recurring revenue, above-inflation price increases and favourable demographics.",
        "quote_attribution": "Theo Dickens, Managing Partner at Prefequity",
        "company_quote": "The Prefequity team delivered a flexible funding package that was a creative alternative to a traditional private-equity structure. We look forward to working together over the next few years as we continue to grow HCI.",
        "company_quote_attribution": "Shane Younger, CEO at HCI",
        "featured_on_home": True,
        "display_order": 5,
        "image_source": "HCIGroupBanner.webp",
        "logo_source": "logos/HCIAdjustedLogo.webp",
    },
    {
        "name": "Parabellum",
        "slug": "parabellum",
        "sector": "TMT",
        "head_office": "Yorkshire",
        "transaction_type": "Growth capital",
        "invested_on": date(2022, 12, 1),
        "status": "current",
        "summary": "Parabellum is a family office operating as a global private equity firm with deep expertise in the IT and software sectors. It looks to grow companies both organically and through acquisition, leveraging its management experience and track record.\n\nPortfolio companies include ieDigital, a developer of mid-market digital banking platforms; Advanco, a specialist in track-and-trace serialisation software for the pharmaceutical industry; and Parseq, a trusted business process outsourcer specialising in workflow solutions.",
        "quote": "Parabellum has a diverse portfolio of companies that benefit from sticky revenue streams, strong cash generation, long-standing customer relationships and significant barriers to entry that together provide substantial downside protection for us.",
        "quote_attribution": "Johnny Carew Pole, Partner at Prefequity",
        "featured_on_home": True,
        "display_order": 6,
        "image_source": "black_and_white_image.webp",
        "logo_source": "logos/ParabellumAdjustedLogo.webp",
    },
    {
        "name": "CaviTech Solutions",
        "slug": "cavitech-solutions",
        "sector": "Industrials",
        "head_office": "Blackpool",
        "transaction_type": "Refinancing",
        "invested_on": date(2017, 7, 1),
        "status": "realised",
        "summary": "Lancashire-based CaviTech Solutions designs and manufactures complex high-precision injection moulds for the personal-care and medical sectors. Formed in 1955, the company has continually invested in the latest technology and processes to build a strong market position in its chosen sectors.\n\nCaviTech’s highly automated manufacturing capability enables it to build repeatable series of interchangeable moulds that are delivered to market-leading customers around the world.",
        "quote": "We are delighted with the performance of our investment in CaviTech. It’s further evidence of our ability to deliver high double-digit returns to investors with strong downside protection by identifying and backing first-class businesses.",
        "quote_attribution": "Theo Dickens, Managing Partner at Prefequity",
        "company_quote": "The Prefequity team delivered a flexible funding package that closely met our objectives and our timetable.",
        "company_quote_attribution": "Chris Smith, Managing Director at CaviTech",
        "featured_on_home": False,
        "display_order": 7,
        "image_source": "CavitechBanner.webp",
        "logo_source": "logos/CaviTechAdjustedLogo.webp",
    },
    {
        "name": "TLC Marketing Worldwide",
        "slug": "tlc-marketing",
        "sector": "Business services",
        "head_office": "London",
        "transaction_type": "Growth capital",
        "invested_on": date(2017, 8, 1),
        "status": "realised",
        "summary": "TLC Marketing Worldwide is the award-winning specialist promotional agency that runs innovative campaigns for global consumer brands. Headquartered in London, the company runs over 500 campaigns each year out of its network of 19 offices covering every continent.\n\nCampaigns are designed to bring brands “alive” by offering consumer experiences that drive acquisition, retention and loyalty. Clients include 60 of Fortune’s Top 100 brands.",
        "quote": "We are delighted with the performance of our investment in TLC Marketing. It’s further evidence of our ability to deliver high double-digit returns to investors with downside protection by identifying and backing first-class owner-managers.",
        "quote_attribution": "Theo Dickens, Managing Partner at Prefequity",
        "company_quote": "I’d like to thank our partners at Prefequity for the significant contribution they have made to the business, which has been a major driver of our growth in recent years. The capital and advice provided by Prefequity have played a vital part in our ongoing success story.",
        "company_quote_attribution": "Nick True, Chairman of TLC Marketing Worldwide",
        "featured_on_home": False,
        "display_order": 8,
        "image_source": "TLCBanner.webp",
        "logo_source": "logos/TLCAdjustedLogo.webp",
    },
    {
        "name": "WH Good",
        "slug": "wh-good",
        "sector": "Business services",
        "head_office": "Lancashire",
        "transaction_type": "Buy-out",
        "invested_on": date(2019, 11, 1),
        "status": "realised",
        "summary": "WH Good is a family-run provider of mechanical and electrical engineering services based in Haslingden, Lancashire, serving utilities, airports, local government, manufacturing and process industries since 1922.",
        "quote": "The management team has built a strong franchise in the M&E sector that enjoys a high level of recurring revenue from repair & maintenance expenditure, backed by long-term framework agreements.",
        "quote_attribution": "Nick Petrusic, Senior Partner at Prefequity",
        "company_quote": "The Prefequity team delivered a bespoke funding package that was a creative alternative to a traditional lending structure. We look forward to working together over the next few years as we continue to grow WH Good and deliver value for our customers and shareholders.",
        "company_quote_attribution": "Paul Sumner, Director at W H Good",
        "featured_on_home": False,
        "display_order": 9,
        "image_source": "WHGoodBanner.webp",
        "logo_source": "logos/WHGoodAdjustedLogo.webp",
    },
    {
        "name": "WPI Group",
        "slug": "wpi-group",
        "sector": "Construction",
        "head_office": "Cheshire",
        "transaction_type": "Buy-out",
        "invested_on": date(2018, 7, 1),
        "status": "realised",
        "summary": "WPI Group is a long-established provider of civil engineering, groundwork and surfacing services to housebuilders in North West England. Established in 1979, the company benefits from deep market experience and embedded relationships with blue-chip housebuilders and construction firms.\n\nAs one of the region’s largest civil engineering businesses, it has a reputation for high-quality on-time delivery of groundworks and detailed knowledge of local ground conditions.",
        "quote": "We are delighted with the performance of our investment in WPI. It’s further evidence of our ability to deliver attractive double-digit returns to investors with downside protection by identifying first-class businesses and backing them with robust capital structures.",
        "quote_attribution": "Nick Petrusic, Senior Partner at Prefequity",
        "featured_on_home": False,
        "display_order": 10,
        "image_source": "WPIBanner.webp",
        "logo_source": "logos/WPIAdjustedLogo.webp",
    },
]

NEWS = [
    {
        "title": "Ilektra completes third acquisition since Prefequity's investment",
        "slug": "ilektra-third-acquisition",
        "published_on": date(2026, 1, 20),
        "category": "news",
        "tag": "Ilektra",
        "image_source": "Ilektra_banner.webp",
        "excerpt": "Ilektra continues its buy-and-build programme, completing a third add-on acquisition since Prefequity's growth capital investment.",
        "featured_on_home": True,
    },
    {
        "title": "Prefequity backs MBO of KBH On-Train Media",
        "slug": "prefequity-backs-mbo-kbh",
        "published_on": date(2025, 12, 1),
        "category": "news",
        "tag": "KBH",
        "image_source": "KBHPicture.webp",
        "excerpt": "Prefequity has backed the management buy-out of KBH, a leading out-of-home advertising business specialising in rail and cinema.",
        "featured_on_home": True,
    },
    {
        "title": "The importance of liquidity risk in private markets",
        "slug": "liquidity-risk-private-markets",
        "published_on": date(2025, 9, 11),
        "category": "insights",
        "tag": "Prefequity",
        "image_source": "NE_Blog-Post-Image_Blog-3_Body_v0.2.webp",
        "excerpt": "An insight into how liquidity risk shapes private market investing, and why structured capital can offer a more resilient alternative.",
        "featured_on_home": True,
    },
    {
        "title": "British Business Bank makes new £15m commitment to a separately managed account with Prefequity",
        "slug": "british-business-bank-15m-sma",
        "published_on": date(2025, 7, 29),
        "category": "news",
        "tag": "Prefequity",
        "image_source": "HCIGroupBanner.webp",
        "excerpt": "The British Business Bank has committed a further £15 million to a separately managed account alongside Prefequity Credit Opportunities II LP.",
        "featured_on_home": False,
    },
    {
        "title": "Prefequity provides follow-on investment to support Ilektra",
        "slug": "ilektra-follow-on",
        "published_on": date(2025, 6, 24),
        "category": "news",
        "tag": "Ilektra",
        "image_source": "Ilektra_banner.webp",
        "excerpt": "Follow-on capital to support Ilektra as it continues to strengthen its market position through selective add-on acquisitions.",
        "featured_on_home": False,
    },
    {
        "title": "Simon Orange joins Prefequity as Senior Adviser to bolster Northern network",
        "slug": "simon-orange-senior-adviser",
        "published_on": date(2025, 5, 7),
        "category": "news",
        "tag": "Prefequity",
        "image_source": "black_and_white_image.webp",
        "excerpt": "Manchester-based entrepreneur Simon Orange joins Prefequity as Senior Adviser, focused on the North of England.",
        "featured_on_home": False,
    },
    {
        "title": "Prefequity announces the first close of Fund II",
        "slug": "fund-ii-first-close",
        "published_on": date(2024, 5, 22),
        "category": "news",
        "tag": "Prefequity",
        "image_source": "CentralGroupPicture2.webp",
        "excerpt": "Prefequity Credit Opportunities II LP has reached a first close, targeting £150 million to continue providing senior secured loans with equity upside.",
        "featured_on_home": False,
    },
    {
        "title": "Prefequity builds on its success as it exits WPI Group",
        "slug": "exit-wpi-group",
        "published_on": date(2024, 3, 27),
        "category": "news",
        "tag": "WPI Group",
        "image_source": "WPIBanner.webp",
        "excerpt": "The exit was achieved via a refinancing after almost six years of partnership with WPI Group.",
        "featured_on_home": False,
    },
]

TEAM = [
    {
        "name": "Theo Dickens",
        "role": "Managing Partner",
        "bio": "Theo is Managing Partner and a member of the Investment Committee. He has over 25 years' experience in debt and equity investment. Prior to founding Prefequity, he worked in leveraged finance and investment banking with Morgan Grenfell, Morgan Stanley and Merrill Lynch. He also spent three years in mid-market private equity with NPIL. Theo's past and present board seats include Ilektra, CaviTech, TLC Marketing and HealthCare International.",
        "display_order": 1,
    },
    {
        "name": "Nick Petrusic",
        "role": "Senior Partner",
        "bio": "Nick is Senior Partner and a member of the Investment Committee. He has over 30 years' experience in senior and mezzanine debt and commercial lending. From 1990, he spent 10 years financing mid-market buy-out transactions with NatWest. He then worked at GSC, latterly as head of its European business, before continuing as European head at Black Diamond. Nick's past and present board seats include WPI, WH Good and Central.",
        "display_order": 2,
    },
    {
        "name": "Johnny Carew Pole",
        "role": "Partner",
        "bio": "Johnny is a Partner at Prefequity. He has invested in lower-mid market UK companies for over 20 years. Before Prefequity, he was an Investment Director at CapitalSource and Eternity Capital and a partner at Cairneagle Associates. He started his career at Mercer Oliver Wyman. Johnny's past and present board seats include HealthCare International, Parabellum and Now Education.",
        "display_order": 3,
    },
    {
        "name": "Tom Barratt",
        "role": "Investment Manager",
        "bio": "Tom is an Investment Manager at Prefequity. Before joining Prefequity, Tom spent three years in Rothschild & Co's mid-market team advising on both debt and equity transactions. He started his career at KPMG in their Complex and International Restructuring team, where he trained as an ICAEW Chartered Accountant.",
        "display_order": 4,
    },
    {
        "name": "Philip Williams",
        "role": "Finance Director",
        "bio": "Philip is Prefequity's Finance Director. He is an ICAEW Chartered Accountant with over 10 years of experience in financial services. Before joining Prefequity, Philip spent four years at Duke Street as the number two in finance and operations. He started his career at Moore Kingston Smith.",
        "display_order": 5,
    },
    {
        "name": "Simon Orange",
        "role": "Senior Adviser",
        "bio": "Simon is a Senior Adviser to Prefequity focused on the North of England. Simon is a well-known Manchester-based entrepreneur and co-owner of Sale Sharks. Since founding CorpAcq in 2006, Simon has been a pivotal figure in the Manchester investment arena and recently led CorpAcq's investment from TDR Capital.",
        "display_order": 6,
    },
]


SLIDES = [
    {
        "filename": "london.jpg",
        "title": "London",
        "alt_text": "Central London at dusk",
        "link_url": "",
        "display_order": 1,
    },
    {
        "filename": "workshop.jpg",
        "title": "UK industry",
        "alt_text": "Precision manufacturing workshop",
        "link_url": "/our-portfolio/",
        "display_order": 2,
    },
    {
        "filename": "architecture.jpg",
        "title": "Built environment",
        "alt_text": "Contemporary commercial architecture",
        "link_url": "",
        "display_order": 3,
    },
    {
        "filename": "partnership.jpg",
        "title": "Partnership",
        "alt_text": "Management team in discussion",
        "link_url": "/our-business/",
        "display_order": 4,
    },
]


class Command(BaseCommand):
    help = "Seed the SQLite database with Prefequity site content."

    def handle(self, *args, **options):
        PortfolioCompany.objects.all().delete()
        NewsArticle.objects.all().delete()
        TeamMember.objects.all().delete()

        for item in PORTFOLIO:
            image_source = item.pop("image_source", "")
            logo_source = item.pop("logo_source", "")
            company = PortfolioCompany.objects.create(**item)
            self._attach_portfolio_file(company, "image", image_source)
            self._attach_portfolio_file(company, "logo", logo_source)
        for item in NEWS:
            image_source = item.pop("image_source", "")
            article = NewsArticle.objects.create(**item)
            self._attach_news_image(article, image_source)
        for item in TEAM:
            TeamMember.objects.create(**item)

        slides_created = self._seed_slides()

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {len(PORTFOLIO)} companies, {len(NEWS)} articles, {len(TEAM)} team members, {slides_created} carousel slides."
            )
        )

    def _seed_slides(self):
        if HomepageSlide.objects.exists():
            return 0

        source_dir = Path(__file__).resolve().parents[2] / "static" / "website" / "img" / "carousel"
        created = 0
        for item in SLIDES:
            path = source_dir / item["filename"]
            if not path.exists():
                continue
            slide = HomepageSlide(
                title=item["title"],
                alt_text=item["alt_text"],
                link_url=item["link_url"],
                display_order=item["display_order"],
                is_active=True,
            )
            with path.open("rb") as handle:
                slide.image.save(item["filename"], File(handle), save=True)
            created += 1
        return created

    def _attach_portfolio_file(self, company, field_name, filename):
        if not filename:
            return False

        base_dir = Path(__file__).resolve().parents[3]
        path = base_dir / "media" / "portfolio" / filename
        if not path.exists():
            return False

        field = getattr(company, field_name)
        with path.open("rb") as handle:
            field.save(path.name, File(handle), save=True)
        return True

    def _attach_news_image(self, article, filename):
        if not filename:
            return False

        base_dir = Path(__file__).resolve().parents[3]
        search_dirs = [
            base_dir / "media" / "portfolio",
            base_dir / "website" / "static" / "website" / "img",
        ]
        for directory in search_dirs:
            path = directory / filename
            if not path.exists():
                continue
            with path.open("rb") as handle:
                article.image.save(filename, File(handle), save=True)
            return True
        return False
