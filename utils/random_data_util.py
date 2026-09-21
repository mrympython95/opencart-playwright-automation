from faker import Faker
import random
import string

class RandomDataUtil:
    def __init__(self):
        self.fake = Faker()

    def get_first_name(self) -> str:
        return self.fake.first_name()

    def get_last_name(self) -> str:
        return self.fake.last_name()

    def get_email(self) -> str:
        return self.fake.email()

    def get_phone_number(self) -> str:
        return self.fake.phone_number()

    def get_password(self) -> str:
        return self.fake.password()

    def get_city(self) -> str:
        return self.fake.city()

    def get_postcode(self) -> str:
        return self.fake.postcode()

    def get_address(self) -> str:
        return self.fake.address()

    def get_random_numeric(self, length: int) -> str:
        return "".join(random.choice(string.digits)for _ in range(length))

    def get_random_alphanumeric(self, length: int) -> str:
        chars = string.ascii_letters + string.digits

        return "".join(
            random.choice(chars)
            for _ in range(length)
        )

    def get_uuid(self) -> str:
        return str(self.fake.uuid4())