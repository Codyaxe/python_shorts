class Ewan():
    def __iter__(self, size):
        self.size = size
        self.a = -1
        return self
    def __next__(self):
        if self.a < self.size:
            x = self.a
            x += 1
            return x
        else:
            StopIteration

def even(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(even(10)))

#input output, looping, 