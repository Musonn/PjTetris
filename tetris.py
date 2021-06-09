class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Tetris():
    def Check(self):
        pass


class Tetrismino():
    def __init__(self, data):
        self.prev = data  # prev origin at left up corner be (0,0)

    def Left(self):
        self.location = list(self.prev)
        self.location[0] -= 1
        if Check():
            self.prev = tuple(self.location)


    def Right(self):
        self.location = list(self.prev)
        self.location[0] += 1
        if Check():
            self.prev = tuple(self.location)

    def Down(self):
        self.location = list(self.prev)
        self.location[1] += 1
        if Check():
            self.prev = tuple(self.location)


class I_block(Tetrismino):
    def __init__(self, data):
        super().__init__(data)

    type = 'I'
    node_1 = Node(((0, 1), (1, 1), (2, 1), (3, 1)))
    node_2 = Node(((2, 0), (2, 1), (2, 2), (2, 3)))

    node_1.next = node_2
    node_2.next = node_1


I = I_block((4,0))
# print(I.node_1.next.next.data)
I.Down()
print(I.prev)
