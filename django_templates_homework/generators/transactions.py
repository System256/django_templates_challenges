import datetime
import decimal
import random
import uuid

from django_templates_homework.custom_types import BankTransaction
from django_templates_homework.enums import Currency


def generate_fake_transactions(num: int) -> list[BankTransaction]:
    return [_generate_transaction() for _ in range(num)]


def _generate_transaction() -> BankTransaction:
    is_validated_by_receiver = random.random() < 0.7
    can_be_fraud = False if is_validated_by_receiver else random.random() < 0.2

    return BankTransaction(
        id=uuid.uuid4(),
        amount=decimal.Decimal(random.randint(1, 100)),
        currency=random.choice(list(Currency)),
        submitted_at=(
            datetime.datetime(2023, 1, 1)
            + datetime.timedelta(seconds=random.randint(0, 365 * 24 * 60 * 60))
        ),
        receiver_id=uuid.uuid4(),
        is_validated_by_receiver=is_validated_by_receiver,
        can_be_fraud=can_be_fraud,
    )
