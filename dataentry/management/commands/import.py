from django.core.management.base import BaseCommand
import csv
from dataentry.models import Student


class Command(BaseCommand):
    help = 'import data from dataset'

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str,help='dataset name.')

    def handle(self,*args,**kwargs):
        
        file_path = kwargs['file_path']
        self.stdout.write(file_path)

        with open(file_path,'r') as f:
            dataset = csv.DictReader(f)
            for data in dataset:
                roll_no = data['roll_no']
                if not Student.objects.filter(roll_no=roll_no).exists():
                    Student.objects.create(student_name=data['name'],roll_no=data['roll_no'],age=data['age'])
                else:
                    self.stdout.write(self.style.WARNING(f'data with rollno {roll_no} already exists'))
        self.stdout.write(self.style.SUCCESS('imported dataset successfully!!!'))