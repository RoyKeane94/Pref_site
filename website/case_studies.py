CASE_STUDIES = [
    {
        "slug": "central-roofing-case-study",
        "name": "Central",
        "full_name": "Central Roofing Group",
        "company_slug": "central-roofing-group",
        "image": "website/img/case-studies/central.jpg",
        "image_alt": "A Central Roofing technician working on a commercial roof",
        "region": "West Midlands",
        "invested": "December 2021",
        "lead": "Regionally based provider of commercial roofing services",
        "card_summary": "Reducing emissions, improving employee wellbeing, and strengthening community involvement.",
        "stats": [
            {"value": "8.2%", "label": "Emissions reduced since the carbon plan"},
            {"value": "2050", "label": "Net zero carbon target"},
            {"value": "100%", "label": "Jobs above the living wage"},
            {"value": "£80k", "label": "Annual community contributions"},
        ],
        "sections": [
            {
                "title": "Reducing emissions and determining a path to net zero",
                "bullets": [
                    "Central adopted a carbon reduction plan in 2024 and are actively taking steps to move to net zero carbon emissions by 2050.",
                    "The carbon reduction plan was created with Elemental Consulting Group, who calculated the base-line emissions across the organisation measured using the Greenhouse Gas Protocol. Since creating their carbon reduction plan, Central has reduced its emissions by 8.2%.",
                ],
            },
            {
                "title": "Improving the focus on employee wellbeing",
                "bullets": [
                    "Since our investment, Central has established a group HR function and undertaken a full review of its employee recruitment policies, contracts and benefits.",
                    "Central has undertaken occupational health assessments on all employees and arranged follow-up appointments where issues were identified. These assessments are now being carried out on a regular basis, with mental health support now in place for all employees.",
                    "Central is a living wage employer with 100% of jobs being above the living wage.",
                ],
            },
            {
                "title": "Fostering a greater presence in the community",
                "bullets": [
                    "Management encourages strong community involvement across the organisation, having made annual donations and in-kind contributions to 45 community groups worth around £80,000 p.a. in the last twelve months.",
                ],
            },
        ],
    },
    {
        "slug": "parseq-case-study",
        "name": "Parseq",
        "full_name": "Parseq",
        "company_slug": "parabellum",
        "image": "website/img/case-studies/parseq.jpg",
        "image_alt": "Parseq colleagues collaborating in an office",
        "region": "Yorkshire",
        "invested": "December 2022",
        "lead": "Regionally based provider of business process outsourcing specialising in workflow solutions",
        "card_summary": "Cutting carbon emissions, creating good-quality jobs, and building a more diverse workplace.",
        "stats": [
            {"value": "18%", "label": "Scope 1 & 2 emissions cut in year one"},
            {"value": "400", "label": "FTEs, up from 220 at investment"},
            {"value": "100%", "label": "Waste diverted from landfill"},
            {"value": "4%", "label": "Median gender pay gap"},
        ],
        "sections": [
            {
                "title": "Reducing carbon emissions and delivering environmental sustainability",
                "bullets": [
                    "Parseq measures its carbon footprint and has delivered an 18% reduction in Scope 1 & 2 carbon emissions in the first full year after Prefequity’s investment. Owing to offsets, the company is now carbon positive.",
                    "In 2023 the company developed a comprehensive five-year sustainability plan with environmental auditors, with a particular focus on the lifecycle of the supply chain and raw materials, operations, energy, maintenance, transportation and waste management. In September 2024, Parseq achieved 100% diversion from landfill.",
                ],
            },
            {
                "title": "Creating new, good quality jobs",
                "bullets": [
                    "Since our investment, the Parseq workforce has increased from 220 to 400 FTEs through both acquisitive and organic growth.",
                    "Parseq has been recognised as a real living wage employer and 100% of Parseq jobs are at or above the living wage.",
                ],
            },
            {
                "title": "Delivering a diverse and supportive workplace",
                "bullets": [
                    "Parseq has a strong commitment to diversity and equal opportunities demonstrated by the workforce make-up of 228 male/172 female. At 4%, the median gender pay gap is down c.20% since investment and is significantly lower than the UK median of 14.8% (Source: ONS 2023).",
                    "Parseq ensures that staff have access to a great work environment including training and a comprehensive mental health support service.",
                ],
            },
        ],
    },
    {
        "slug": "now-education-case-study",
        "name": "Now Education",
        "full_name": "Now Education",
        "company_slug": "now-education",
        "image": "website/img/case-studies/now-education.jpg",
        "image_alt": "A classroom of students with a teacher",
        "region": "Midlands",
        "invested": "December 2023",
        "lead": "Regionally based recruiter of teachers and classroom assistants",
        "card_summary": "Creating high-quality jobs, tightening compliance, and strengthening standalone operations.",
        "stats": [
            {"value": "8%", "label": "Workforce growth in nine months"},
            {"value": "100%", "label": "Jobs above the living wage"},
            {"value": "APSCo", "label": "Member, with office-level compliance"},
            {"value": "New", "label": "Standalone finance function"},
        ],
        "sections": [
            {
                "title": "Delivering high quality jobs across the country",
                "bullets": [
                    "In the 9 months since our investment, Now has increased its workforce by 8% and is planning to grow at similar rates over the course of Prefequity's investment.",
                    "Now is a living wage employer with 100% of jobs being above the living wage.",
                ],
            },
            {
                "title": "Putting best-in-class procedures in place",
                "bullets": [
                    "Now attaches high importance to rigorous processes and ensures that all teachers are vetted. As a member of APSCo, Now ensures that it remains on top of the latest regulations and compliance best-practices delivered through continuous training.",
                    "Each office has its own compliance function, enabling more responsive interactions between compliance and consultants.",
                ],
            },
            {
                "title": "Strengthening operations for independent growth and success",
                "bullets": [
                    "Having grown rapidly in recent years, Now relied on the founder’s group for some support functions. As part of Prefequity’s investment, management undertook a detailed business review and implemented a plan to ensure systems, processes and controls robust on a standalone basis.",
                    "With external support provided via Prefequity, a new finance function has been established.",
                ],
            },
        ],
    },
]


def get_case_study(slug):
    return next((item for item in CASE_STUDIES if item["slug"] == slug), None)
