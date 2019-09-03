class Piece:
    def __init__(self, format):
        self.format = format
        self.crown = False

    def has_crown(self):
        return self.crown

    def __repr__(self):
        return self.format
