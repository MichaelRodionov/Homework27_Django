import csv

from ads.models import Category, Advertisement


# ----------------------------------------------------------------
def convert_csv(file) -> list[dict]:
    """
    Convert a CSV file to list with dict
    :param file: CSV file
    :return: list of dict
    """
    with open(file, encoding='utf-8') as f:
        return [row for row in csv.DictReader(f)]


categories: list[dict] = convert_csv(file='./ads/data/categories.csv')
ads: list[dict] = convert_csv(file='./ads/data/ads.csv')


# ----------------------------------------------------------------
def fill_database() -> None:
    """
    Fill the database with data from CSV files
    :return: None
    """
    for category_ in categories:
        category = Category.objects.create(**category_)
        category.save()
    for ad_ in ads:
        if ad_['is_published'] == 'TRUE' or ad_['is_published'] == 'FALSE':
            ad_['is_published'] = ad_['is_published'].title()
        ad = Advertisement.objects.create(**ad_)
        ad.save()

