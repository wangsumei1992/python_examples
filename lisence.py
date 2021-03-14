import uuid
import sys

class Lisence:

    def __init__(self, count):
        self.count = count

    def create(self):
        res = []
        for i in range(0, self.count):
            res.append(str(uuid.uuid4()))
        return res

if __name__ == "__main__":
    print(sys.argv[0])
    if len(sys.argv) != 2:
        count = 10
    else:
        count = int(sys.argv[-1])
    for l in Lisence(int(count)).create():
        print(l)
