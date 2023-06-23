class Picture:
    def __init__(self, path, idx):
        self.path = path
        self.rating = 0
        self.idx = idx

    def plus_one(self):
        self.rating += 1
    
    def minus_one(self):
        self.rating -= 1
    