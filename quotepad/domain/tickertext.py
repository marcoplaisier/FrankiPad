from uuid import UUID


class TickerText:
    def __init__(self, id: UUID, text: str, active: bool):
        self.id = id
        self.text = text
        self.active = active

    @classmethod
    def from_dict(cls, adict):
        return cls(
            id=adict['id'],
            text=adict['text'],
            active=adict['active']
        )
