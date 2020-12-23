import csv
from itertools import islice

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Victim

DATA_DIR = settings.BASE_DIR.parent / 'data'


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Customers
        customer_file_name = 'Ledger Orders (Buyers) only [Part %s of 8].txt'
        for i in range(1, 9):
            file = str(DATA_DIR / customer_file_name) % i
            with open(file) as f:
                reader = csv.reader(f, delimiter='|')
                try:
                    batch_size = 100
                    objs = (Victim(**{
                        'email': row[0],
                        'name': row[1],
                        'address_1': row[2],
                        'address_2': row[3],
                        'country': row[4],
                        'phone': row[5],
                    }) for row in reader)
                    while True:
                        batch = list(islice(objs, batch_size))
                        if not batch:
                            break
                        Victim.objects.bulk_create(batch, batch_size)
                except IndexError:
                    pass

        # Subscriptions
        email_file_name = 'All Emails (Subscription) [Part %s of 6].txt'
        for i in range(1, 7):
            file = str(DATA_DIR / email_file_name) % i
            with open(file) as f:
                for line in f:
                    email = line.strip()
                    try:
                        obj = Victim.objects.get(email__iexact=email)
                        obj.newsletter = True
                        obj.save()
                        self.stdout.write(self.style.SUCCESS('Updated %s' % obj))
                    except Victim.DoesNotExist:
                        obj = Victim.objects.create(**{
                            'email': email,
                            'newsletter': True,
                        })
                        self.stdout.write(self.style.SUCCESS('Added %s' % obj))
