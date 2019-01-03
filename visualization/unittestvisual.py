from django.core.management import call_command
from django.test import TestCase
from elasticsearchapp.models import Companies



class IntegrationTestUsers(TestCase):
    # def test_search_users_in_elasticsearch(self):
    #     c = Companies.objects.create(id = 372,
    #         compnumber= 372,
    #         ticker="AIG",
    #         longname="American International Group Inc",
    #         shortname="American International Group",
    #         country="USA")
    #     c = Companies.objects.create(id = 76258,
    #         compnumber=76258,
    #         ticker="CB",
    #         longname="Chubb Ltd",
    #         shortname="Chubb Ltd",
    #         country="CHE")
    
    def test_details_page_status_code(self):
        response = self.client.get('/company/',{'company_name':'AAPL','start_date':'','end_date':''})
        self.assertEquals(response.status_code, 200)

    def test_search_page_status_code_cmpny(self):
        response = self.client.get('/twitter/')
        self.assertEquals(response.status_code, 200)
    
    
    def test_search_page_status_code_shortName(self):
        response = self.client.get('/compare/')
        self.assertEquals(response.status_code, 200)

    # def test_search_page_value_shortName(self):
    #     response = self.client.get('/companies/search/',{'arg':'Chubb Ltd'})
    #     self.assertIsNotNone(response)