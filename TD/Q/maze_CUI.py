def main():
    maze = Maze(
        '''
        #####
        #O.G#
        #...#
        #S..#
        #####
        ''',
        {'.':-1,
         'O':-50,
         'G':100})


class Maze:
    def __init__(self, maze_map, reward_dict):
        self.maze_map = [line.strip() for line in maze_map.splitlines() if line.strip()]
        self.maze_size = (len(self.maze_map), len(self.maze_map[0]))
        self._reward_dict = reward_dict
    def _get_reward(self, x, y):
        block = self.maze_map[x][y]
        if block in self._reward_dict:
            return self._reward_dict[block]
        else:
            return 0
    def move(self, x, y, direction):
        # basic move
        if direction == 0:
            nx, ny = x, y - 1
        elif direction == 1:
            nx, ny = x + 1, y
        elif direction == 2:
            nx, ny = x, y + 1
        elif direction == 3:
            nx, ny = x - 1, y
        # exceptional move
        if self._get_material(nx, ny) == '#':
            nx, ny = x, y
        # return pos, reward, end_flag
        reward = self._get_reward(nx, ny)
        is_end = (self._get_material(nx, ny) in ('O', 'G'))
        return nx, ny, reward, is_end


if __name__ == '__main__':
    main()
