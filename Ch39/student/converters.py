class RollNumberConverter:
    regex = '[0-9]{4}-[A-Za-z]{2,4}-[0-9]{3}'    # year - department - number

    def to_python(self, value):
        year = int(value[:4])
        if year < 2000:
            raise ValueError('too old')          # Django treats this as "no match", so 404
        return value.upper()                     # cs → CS

    def to_url(self, value):
        return value.upper()