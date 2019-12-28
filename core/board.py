import random

class Board:
    def __init__(self, size, natoms):
        self.size = size
        self.atoms = set()
        atom = self.atom(natoms)
        while True:
            try:
                self.atoms.add(next(atom))
            except StopIteration:
                break

    def step(self, start_dir, start_pos):
        if not self.valid_start_dir(start_dir):
            raise ValueError
        if not self.valid_start_pos(start_pos):
            raise ValueError
        if not type(start_dir) is tuple:
            raise TypeError
        if not type(start_pos) is tuple:
            raise TypeError
        
        position = start_pos
        direction = start_dir

        while self.in_bounds(position[0], position[1]) or position == start_pos:
            direction = self.update_direction(direction)
            #if not direction:
                #raise AbsorbError
            position = tuple([sum([p, d]) 
                for p, d in zip(position, direction)])
            yield position

    def atom(self, natoms):
        pass

    def valid_start_dir(self, d):
        pass

    def valid_start_pos(self, p):
        pass

    def in_bounds(self, p):
        pass

    def update_direction(self, d):
        pass

class RectBoard(Board):
    def atom(self, natoms):
        if natoms <= 0:
            raise ValueError
        count = 0

        random.seed()
        while count < natoms:
            a = (random.randint(0,self.size), random.randint(0, self.size))
            if a in self.atoms:
                continue
            count += 1
            yield a
        
    def in_bounds(self, *args):
        for arg in args:
            if arg < 0 or arg >= self.size - 1:
                return False
        return True

    def valid_start_dir(self, d):
        if d[0] == 0 or d[1] == 0 and abs(sum(d)) == 1:
            return True
        return False

    def valid_start_pos(self, p):
        for i, n in enumerate(p):
            if n == -1 or n == self.size + 1:
                return self.in_bounds(p[i-1])
 
if __name__ == "__main__":
    board = RectBoard(size=8, natoms=4)
    print(board.atoms)
    step = board.step((1, 0), (-1, 0)) 
    while True:
        try:
            print(next(step))
        except StopIteration:
            print('Done')
            break        