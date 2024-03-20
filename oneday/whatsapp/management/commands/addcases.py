from django.core.management.base import BaseCommand
from whatsapp.models import Case
from pandas import read_csv, concat


class Command(BaseCommand):
    help = "Add data."
    filepaths = [r"C:\Users\User\MaDoIS\data\cases.tsv", r"C:\Users\User\MaDoIS\data\other.tsv"]

    def handle(self, *args, **options):
        count = 0
        cases = concat(objs=[read_csv(self.filepaths[0]), read_csv(self.filepaths[1])], ignore_index=True)
        for index in cases.index:
            print(cases["name"][index])
            case = Case(name=cases["name"][index], url=cases["url"][index], pattern=cases["pattern"][index])
            case.save()
            count += 1

        self.stdout.write(
            self.style.SUCCESS('Successfully added: %s.' % count)
        )
