from django.core.management.base import BaseCommand
from home.models import Student
from faker import Faker
class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        fk=Faker()
        for i in range(5):
            name=fk.name()
            email=fk.email()
            phno=fk.msisdn()[:10]
            while True:
                phno=fk.msisdn()[:10]
                break
            Student.objects.create(name=name,email=email,phno=phno)