import dataclasses
import datetime
import decimal
import uuid

from django_templates_homework.enums import Currency


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class Message:
    text: str
    author_nickname: str
    likes_num: int
    reposts_num: int


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class BankTransaction:
    id: uuid.UUID
    amount: decimal.Decimal
    currency: Currency
    submitted_at: datetime.datetime
    receiver_id: uuid.UUID
    is_validated_by_receiver: bool
    can_be_fraud: bool
