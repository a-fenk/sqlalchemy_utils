from sqlalchemy import TypeDecorator, String


class StrEnum(TypeDecorator):
    def __init__(self, enumtype, str_max_len: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._enumtype = enumtype
        self.impl = String(length=str_max_len)

    def process_bind_param(self, value, dialect):
        if value:
            return value.value if not isinstance(value, int) else value
        else:
            return None

    def process_result_value(self, value, dialect):
        return self._enumtype(value) if value is not None else None
