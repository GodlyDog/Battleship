class Ship():
    type : str
    position : tuple([tuple([int, int]), tuple([int, int])])
    status : int
    size : int
    def __init__(self, type: str, position: tuple([tuple([int, int]), tuple([int, int])])):
        self.type = type
        self.position = position
        self.status = 0
        self.size = 0
        if type == "Carrier":
            self.size = 5
        if type == "Battleship":
            self.size = 4
        if type == "Submarine":
            self.size = 3
        if type == "Destroyer":
            self.size = 2
        
    def hit(self) -> int:
        self.status += 1
        if self.status == self.size:
            return 1
        else:
            return 0