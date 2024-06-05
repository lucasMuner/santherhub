import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    pattern = re.compile(r'^\(\d{2}\) \d{5}-\d{4}$')

    if not pattern.match(value):
        raise ValidationError(
            ('O número de telefone deve estar no formato (xx) xxxxx-xxxx.'),
            code='invalid_phone_number'
        )