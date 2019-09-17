from django.core.management.base import BaseCommand
from rest_test.models import ShoeColor, ShoeType

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'adding shoe colors and types to the database'

    def _create_shoe_color(self):
        col1 = ShoeColor(color_name='Red')
        col1.save()

        col2 = ShoeColor(color_name='Orange')
        col2.save()

        col3 = ShoeColor(color_name='Yellow')
        col3.save()

        col4 = ShoeColor(color_name='Green')
        col4.save()

        col5 = ShoeColor(color_name='Blue')
        col5.save()

        col6 = ShoeColor(color_name='Indigo')
        col6.save()

        col7 = ShoeColor(color_name='Violet')
        col7.save()

        col8 = ShoeColor(color_name='White')
        col8.save()

        col9 = ShoeColor(color_name='Black')
        col9.save()

    def _create_shoe_type(self):
        type1 = ShoeType(style='sneaker')
        type1.save()

        type2 = ShoeType(style='boot')
        type2.save()

        type3 = ShoeType(style='sandal')
        type3.save()

        type4 = ShoeType(style='dress')
        type4.save()

        type5 = ShoeType(style='other')
        type5.save()

    def handle(self, *args, **options):
        self._create_shoe_color()
        self._create_shoe_type()