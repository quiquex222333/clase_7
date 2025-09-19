from faker import Faker
fake = Faker("es_ES")

def random_address():
    return {
        "first": fake.first_name(),
        "last": fake.last_name(),
        "zip": fake.postcode()[:5]
    }
