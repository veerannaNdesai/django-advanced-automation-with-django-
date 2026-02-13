from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'some grettings from the admin!'  

    def add_arguments(self, parser):
        parser.add_argument('ingredients',type=list,help='displays the ingredients.')      

    def handle(self,*args,**kwargs):
        

        ingredients = kwargs['ingredients']
        reversed = ingredients[::-1]

        result = ''.join(reversed)

        self.stdout.write(self.style.WARNING(f'these are the ingredients \n{result}'))

    

    
