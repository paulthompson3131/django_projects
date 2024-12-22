# Python program to read CSV file line by line 
# import necessary packages 
import csv
from menu.models import Menu  # Replace 'myapp' with your actual app name

def import_menus(file_path):
    with open(file_pathi,'r') as file: 
        reader = csv.DictReader(file) 
        for row in reader_obj: 
            print(row)
            Menu.objects.create(
                name=row['name'],
                heading=row['heading'],
                parent=row['parent'],
                )

if __name__ == '__main__':
    csv_file_path = r'/home/paulthompson3131/django_projects/mysite/menu/scripts/Menu.csv'
    import_menus(csv_file_path)
