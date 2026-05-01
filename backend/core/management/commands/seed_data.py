from django.core.management.base import BaseCommand
from core.models import (
    County, Leader, AgendaItem, NewsCategory, NewsArticle,
    Testimonial, SiteSettings
)


class Command(BaseCommand):
    help = 'Seed initial YR27 data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding YR27 data...')

        # Counties (all 47)
        counties_data = [
            ('Mombasa', '001'), ('Kwale', '002'), ('Kilifi', '003'), ('Tana River', '004'),
            ('Lamu', '005'), ('Taita-Taveta', '006'), ('Garissa', '007'), ('Wajir', '008'),
            ('Mandera', '009'), ('Marsabit', '010'), ('Isiolo', '011'), ('Meru', '012'),
            ('Tharaka-Nithi', '013'), ('Embu', '014'), ('Kitui', '015'), ('Machakos', '016'),
            ('Makueni', '017'), ('Nyandarua', '018'), ('Nyeri', '019'), ('Kirinyaga', '020'),
            ('Murang\'a', '021'), ('Kiambu', '022'), ('Turkana', '023'), ('West Pokot', '024'),
            ('Samburu', '025'), ('Trans-Nzoia', '026'), ('Uasin Gishu', '027'),
            ('Elgeyo-Marakwet', '028'), ('Nandi', '029'), ('Baringo', '030'),
            ('Laikipia', '031'), ('Nakuru', '032'), ('Narok', '033'), ('Kajiado', '034'),
            ('Kericho', '035'), ('Bomet', '036'), ('Kakamega', '037'), ('Vihiga', '038'),
            ('Bungoma', '039'), ('Busia', '040'), ('Siaya', '041'), ('Kisumu', '042'),
            ('Homa Bay', '043'), ('Migori', '044'), ('Kisii', '045'), ('Nyamira', '046'),
            ('Nairobi', '047'),
        ]
        for name, code in counties_data:
            County.objects.get_or_create(name=name, code=code)
        self.stdout.write(f'  ✓ {len(counties_data)} counties created')

        # National Leaders
        leaders_data = [
            ('Yussuf Mugane', 'convener', 'National Convener', 'national', 1),
            ('Alex Kiorop', 'chairperson', 'Chairperson', 'national', 2),
            ('Onesmus Nyaga', 'deputy_chairperson', 'Deputy Chairperson', 'national', 3),
        ]
        for name, position, title, level, order in leaders_data:
            Leader.objects.get_or_create(
                full_name=name,
                defaults={
                    'position': position,
                    'custom_title': title,
                    'level': level,
                    'order': order,
                    'is_active': True,
                }
            )
        self.stdout.write(f'  ✓ {len(leaders_data)} leaders created')

        # Agenda Items
        agenda_data = [
            ('Youth Employment & Job Creation', 'youth-employment', 'briefcase',
             'Creating 2 million jobs for young Kenyans through targeted programs and economic reforms.'),
            ('Digital Economy & Innovation', 'digital-economy', 'laptop',
             'Building tech hubs, coding bootcamps, and digital infrastructure across all 47 counties.'),
            ('Education & Skills Training', 'education-skills', 'graduation',
             'Free TVET training, university bursaries, and practical skills development programs.'),
            ('Hustler Fund & Youth Enterprise', 'hustler-fund', 'chart',
             'Expanding Hustler Fund access and providing mentorship for young entrepreneurs.'),
            ('Agriculture & Agribusiness', 'agriculture', 'seedling',
             'Modern farming techniques, subsidized inputs, and market access for young farmers.'),
            ('Housing & Urban Development', 'housing', 'home',
             'Affordable housing for youth and urban renewal projects creating employment.'),
            ('Healthcare & Wellness', 'healthcare', 'heart',
             'Universal health coverage and mental health support programs for young Kenyans.'),
            ('National Unity & Cohesion', 'national-unity', 'users',
             'Building bridges across ethnic, regional, and political divides through youth exchange programs.'),
        ]
        for title, slug, icon, desc in agenda_data:
            AgendaItem.objects.get_or_create(
                slug=slug,
                defaults={
                    'title': title,
                    'icon': icon,
                    'short_description': desc,
                    'is_active': True,
                }
            )
        self.stdout.write(f'  ✓ {len(agenda_data)} agenda items created')

        # News Categories
        categories = ['Movement News', 'Events', 'Press Releases', 'Opinion', 'County Updates']
        for cat in categories:
            NewsCategory.objects.get_or_create(
                name=cat,
                defaults={'slug': cat.lower().replace(' ', '-')}
            )
        self.stdout.write(f'  ✓ {len(categories)} news categories created')

        # Testimonials
        testimonials = [
            ('James Mwangi', 'Nairobi', 'YR27 gave me a platform to lead. Today I coordinate over 500 youth in my ward.',
             'Ward Mobilizer'),
            ('Faith Wanjiku', 'Nakuru', 'Through YR27 skills training, I started my own digital marketing agency.',
             'Youth Entrepreneur'),
            ('Brian Ochieng', 'Kisumu', 'YR27 is not about politics alone — it\'s about building our generation\'s future.',
             'Campus Leader'),
        ]
        for name, loc, quote, role in testimonials:
            Testimonial.objects.get_or_create(
                name=name,
                defaults={'location': loc, 'quote': quote, 'role': role, 'is_active': True}
            )
        self.stdout.write(f'  ✓ {len(testimonials)} testimonials created')

        # Site Settings
        SiteSettings.objects.get_or_create(pk=1, defaults={
            'site_name': 'YR27 – Youths for Ruto 2027',
            'tagline': 'Youth Power. National Power. 2027 – Ruto Tena.',
            'email': 'info@yr27movement.co.ke',
            'phone': '+254 XXX XXX XXX',
        })
        self.stdout.write('  ✓ Site settings created')

        self.stdout.write(self.style.SUCCESS('\n🎉 YR27 data seeded successfully!'))