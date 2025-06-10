import os

import django
from django.utils import timezone
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from entries.models import Entry

fake = Faker()
for _ in range(22):
    naive_dt = fake.date_time_this_year()
    aware_dt = timezone.make_aware(naive_dt, timezone.get_current_timezone())
    Entry.objects.create(
        title=fake.sentence(nb_words=6),
        content=fake.paragraph(nb_sentences=5),
        date_created=aware_dt,
    )

print("22 fake entries created!")
