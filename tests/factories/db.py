import uuid

import factory.fuzzy

from app import db
from app.db.registry import registry
from tests.utils import AsyncSQLAlchemyFactory


class DemoModelFactory(AsyncSQLAlchemyFactory):
    uid = factory.LazyFunction(uuid.uuid4)
    type_ = factory.Faker("pystr", min_chars=10, max_chars=128)

    class Meta:
        # pylint: disable=unnecessary-lambda-assignment
        model = db.DemoModel
        async_alchemy_get_or_create = ("uid",)
        async_alchemy_session_factory = lambda: registry.session
