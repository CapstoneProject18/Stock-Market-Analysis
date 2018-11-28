import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search.settings')

import django
# Import settings
django.setup()

from myapp.models import Product
from faker import Faker

fake = Faker('en_GB')

def populate(N=5):

	for _ in range(N):
		name=fake.name()
		description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
		p, c = Product.objects.get_or_create(name=name, description=description )
		p.save()

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(50)
    print('Populating Complete')