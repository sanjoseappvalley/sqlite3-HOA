class HOA:

    def __init__(self, first, last, address):
        self.first = first
        self.last = last
        self.address = address

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def addressunit(self):
        return self.address

    def __repr__(self):
        return f"{self.first} {self.last} owns unit {self.address}"
