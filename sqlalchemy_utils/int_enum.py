from sqlalchemy import TypeDecorator, Integer


class IntEnum(TypeDecorator):
    impl = Integer

    def __init__(self, enumtype, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if value is not None:
            return value.value if not isinstance(value, int) else value
        else:
            return None

    def process_result_value(self, value, dialect):
        return self._enumtype(value) if value is not None else None
