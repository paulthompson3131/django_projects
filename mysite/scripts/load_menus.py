import csv  # https://docs.python.org/3/library/csv.html

import datetime
from menu.models import Menu, MenuContent

def run():
    print("=== Menu Loader")

    Menu.objects.all().delete()
    MenuContent.objects.all().delete()
    print("=== Objects deleted")


    fhand = open('scripts/Menu.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header


    for row in reader:
        print(row)
        m = Menu(name=row[0], heading=row[1], parent = row[2])
        m.save()

        fhand2 = open('scripts/MenuContent.csv')
        reader2 = csv.reader(fhand2)
        next(reader2)  # Advance past the header
        for row2 in reader2:
            if row2[0] == row[0]:
                m.menucontent_set.create(form_url=row2[1], url_to_call=row2[2], label=row2[3])
                m.save()

    print("=== Menu Load Complete")




    print("=== Load Complete")
