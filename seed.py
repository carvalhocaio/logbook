import os
from datetime import timedelta

import django
from django.utils import timezone

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from faker import Faker

from entries.models import Entry

fake = Faker()


def clear_entries():
    """Clear all existing entries from the database."""
    Entry.objects.all().delete()
    print("Cleared all existing entries.")


def create_entries(count=15):
    """Create sample entries using Faker."""
    entries_created = 0

    for _ in range(count):
        # Generate varied creation dates over the past 3 months
        days_ago = fake.random_int(min=1, max=90)
        created_date = timezone.now() - timedelta(days=days_ago)

        entry = Entry.objects.create(
            title=fake.sentence(nb_words=fake.random_int(min=3, max=8)).rstrip(
                "."
            ),
            content=fake.text(max_nb_chars=fake.random_int(min=200, max=1000)),
            date_created=created_date,
        )
        entries_created += 1
        print(f"Created entry {entries_created}: {entry.title}")

    print(f"\nSuccessfully created {entries_created} entries.")


def main():
    print("LogBook Entry Seeder")
    print("===================")

    # Optional: Clear existing entries
    if input("Clear existing entries first? (y/N): ").lower().strip() == "y":
        clear_entries()

    # Create new entries
    create_entries(15)

    total_entries = Entry.objects.count()
    print(f"\nTotal entries in database: {total_entries}")


if __name__ == "__main__":
    main()
