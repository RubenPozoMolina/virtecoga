from virtecoga.position import Position


class LivingBeing:
    code: int = None
    position: Position = None
    content: str = None

    def __init__(self, code: int, position: Position, content:str):
        self.code = code
        self.position = position
        self.content = content
