import uuid

import factory.fuzzy

from app.models import CreateDemoScheme, DemoScheme


class CreateDemoSchemeFactory(factory.Factory):
    type = factory.Faker("pystr", min_chars=10, max_chars=128)

    class Meta:
        model = CreateDemoScheme


class DemoSchemeFactory(factory.Factory):
    uid = factory.LazyFunction(uuid.uuid4)
    type_ = factory.Faker("pystr", min_chars=10, max_chars=128)

    class Meta:
        model = DemoScheme
