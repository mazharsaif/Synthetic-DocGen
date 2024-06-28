import random

with open(rf"..\data\random_texts\company_names.txt") as fp:
    company_names = fp.read().split('\n')

def get_random_company_name():
    return random.choice(company_names)
