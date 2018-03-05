from collections import defaultdict


class Bus:
    def __init__(self):
        self.rooms = defaultdict(set)

    def publish(self, nameRoom, **kwargs):
        for data in self.rooms[nameRoom]:
            data(**kwargs)

    def subscribe(self, nameRoom, data):
        self.rooms[nameRoom].add(data)

