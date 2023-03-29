import json

from main import logger
from time import sleep
import pandas as pd


"""Exercise 2"""
logger.info('Completing task 2...')
sleep(2)


def main():
    data = pd.read_csv('distr/covid_19_data.csv')

    cases_by_country = data.groupby('Country/Region')['Confirmed'].max().to_dict()
    print(json.dumps(cases_by_country, indent=4, sort_keys=True))


main()
