
import inspect, sys, csv, os, re
from datetime import datetime

import logging

from django.core.management.base import BaseCommand
from tweetlocator.models import TweetCountry

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Imports countries for us in TweetLocator App.'

    def add_arguments(self, parser):
        parser.add_argument('source_file', nargs='+', type=int)

    def handle(self, *args, **options):

            def get_rows(rdr):
                i= iter(rdr)
                for row in i:
                    yield row

            csv_obj = csv.reader(open('countries.csv','r'), quoting=csv.QUOTE_ALL)

            csv_titles = csv_obj.next() #Grab the headers!

            import pdb; pdb.set_trace()

            countries = [self.convert_line_to_country(csv_titles, row) for row in get_rows(csv_obj)]

            self.stdout.write('Successfully imported %s Countries' % str(len(countries)))

    def convert_line_to_country(self, top_row, country_row):
        # TODO: check if the country already exists - this might be an update - what is unique and permanent?
        country_dict = self.convert_line_to_dict(top_row, country_row)


        try:
            country = TweetCountry.objects.get(iso_code=country_dict['iso_code'])

        except TweetCountry.DoesNotExist:
            country = TweetCountry(**country_dict)
            country.save()

        else:
            logger.debug("TweetCountry: %s already exists" % country.name)

        return country


    def convert_line_to_dict(self, top_row, country_row):
        # TODO: shim the top row line titles to the django object names, zip to a dict
        return dict(zip(top_row,country_row))
