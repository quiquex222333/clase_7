from faker import Faker

fake = Faker("es_ES")
for _ in range(10):
    print(fake.first_name(), fake.last_name(), fake.postcode()[:5])
# print(fake.first_name(), fake.last_name(), fake.postcode()[:5])