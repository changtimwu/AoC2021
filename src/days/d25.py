from typing import List
import copy


class Map(object):
    SMap = List[List[str]]

    def __init__(self, smap: SMap):
        self.smap = smap
        self.h = len(smap)
        self.w = len(smap[0])

    def east_next(self, x: int) -> int: return (x+1) % self.w

    def south_next(self, y: int) -> int: return (y+1) % self.h

    def onestep_east(self) -> bool:
        moved = False
        omap = copy.deepcopy(self.smap)
        # scan every column
        for x in range(self.w):
            nx = self.east_next(x)
            for y in range(self.h):
                if omap[y][x] != '>':
                    continue
                if omap[y][nx] == '.':  # check if the right side is clean
                    moved = True
                    self.smap[y][nx] = '>'
                    self.smap[y][x] = '.'
        return moved

    def onestep_south(self) -> bool:
        moved = False
        omap = copy.deepcopy(self.smap)
        # scan every row
        for y in range(self.h):
            ny = self.south_next(y)
            for x in range(self.w):
                if omap[y][x] != 'v':
                    continue
                if omap[ny][x] == '.':  # check if the below side is clean
                    moved = True
                    self.smap[ny][x] = 'v'
                    self.smap[y][x] = '.'
        return moved

    def onestep(self) -> bool:
        moved1 = self.onestep_east()
        moved2 = self.onestep_south()
        return moved1 or moved2

    def display(self):
        for m in self.smap:
            print(''.join(m))


astr = '''
...>...
.......
......>
v.....>
......>
.......
..vvv..
'''
bstr = '''
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
'''

cstr = '''
>.>vv.....v.v.vvvv..>..>>....v.>>>>>v.>..>v.vv......vv>>.>.>.>v.>..>>.v>..vv.>>.>..v.>>..vvv.>.>>v.>>.>v.v..v.v.>....>..>....>.v>>>.>>..v..
..>v..>..>vv..vv.v..>>..v...vv..>.v>vv...>.>vvv>>>>>....v>v..v......v>.v..vv>.>.v..>...v>v.v.>.vv>..>v......vv>>vv>..v.v>vv.>v.>..vvvvv.>v>
>>.>v....>>vv.vv...v..>.....v.>>..>.v>>>v..>vv..>>..v.v..v.>.v>..v.v>...v..v>..v>>.vv.v>>>>.>...v.v.v>.vvv.v.vv.v..vv>....v.....v.....v.>>.
v...>.>v>v>>..v..>..v.>v>vv>.v.v.....>v..>.>....>....>vv.vv.>....>vvv>..vv....>>>...v....v.v..>....>..vv>.>>.vvv>v>v.vv.>.....v>..v...>v.>v
..>.......>vv.v..vvv>.vv.v.v.v>.>v>>.....v.v.v>.....v.v.vvv>..v...>v>>.......>>>vvv>>.>....vvvv>>v>>.v.v.>..v.v>..v.v>....>..>v......v>v.>.
>vvv.v..v>vv.v......v..>.vv...v........>.>.>..v>.>>...v.vv>..>v.v>.>.v.v.>>.>>..>.>>.v>.v..>>..>vvv..>>.v.vv.>v.>v...v>.v..v.vv..v...>v..>.
v...>v>>..v..>>v>vv.>>..>>v.v>.>v>.>..vvvv>.>>v.vv.>..v.>...vv..v.>.>v...>v.v>..v.vv>..>>......vvv>..>>>>vv>......v.>.>>>>>>>.v.>..v.>..>v>
.v>.>.>vv>>.>>...v>v>>.v>.>.v..vv>v.>v>v>v.>....vv>.>.v>.v....vv..>..v..v.v>.>...>..v.v....>.vvv.vv..v>v....vv...v...v..>.>.....vvv>vv..v..
.....vv.vv.v..v>.>v..>>.v.>..v.v....>>v..>.v...>..v.>.v.v>.>..>....>>.....>vv.v..vv>v.>>...>.......v.>.vv...v.>..>.....>>v.>vv....>..vv.>.>
.vv.v.v>.>.v...>.v..>.vv.....v.>.v>.>v>>...v>.v>.>v>>......>.>>v>..v>.>v>.......>.>...>v..>...>..>.>.>>v.v..>..>..v>>.v.v..>>v.>.>>>>....>v
vv...v>>.vv>...v.vv..>......v>.>>v.>>vv.>>vv..vv.v...v.>>>v>.v.>>v.v..vv>vv.>....>>>v>>v.......v..>.......v.>..>....v..v..>.>v....v...vvv..
....>>.v>v........>>..v..v...>..v...>v..v>>...v.>.v.>>>.......v.>>v.v>>.v.v..>v.>..>..>>..>.vvv>...>>>v.v...v.>..>>v.>>>v.>..v>...v...v..>.
.>.>.>>..>>.....vv..>v...vv.v....vv..v.v>v....>.v.>>....>.v.>.>.v.....vv..v.>.....>>>.>>.vv.v>...vv..>.>>v....>.>.>.v..vv.v>.>>...>>v..v.>.
>..>.>..>v.v....>.....v>v....>.v..vv.v>......>v..v...v.>v.v.>.>>.vvvvv..>>>.v>.>...v...v...>.vv>..>..>.>..>..v>>>>v>.....v.v..>>vv.vvv..vv.
.>>>.>.v>>v>v>>v>.>.....v>>v>>v>..>.>>.>...>>.>.vvv....vv....>vvv>..v..>.>.>vvvv.>vv...>...>>>>.v.>..vv..v.v..v.>..v.v>.v.>..>..v>.....>>.v
.v>.v.vv.v>...>vv>..>vvv.>vv..>.vv..v.v..v>..>..>v>>>.....>>..vvvv>vv......>..>..vv>v.>v.v.v..v..v>v>>.>....v>.>.v..v.>>.v>..>v.vv..>..v.vv
..v>v.v....v.v.v....v>.>...v.>.>v.vv>v....v.>...>>v.v>.>>.v...v>>v.>>v.v.>v.>vv.>.v..v>>..>.v.>>..vv>..vv>.v>.....>..vv.v...v>.>.vv.>>v.>.>
.v.>.>>..>>.v>v...>>..v.>.v..>.v>>v>>.v>v>.>.....>>...>..>v>>........v..>>.v..>..>v>..v.v.>..v>.>..>..v.v.v.>>v.vvv..>>>>>>.........v.v..v.
>>..vv...>....>...vv.v.>..v.v.v>>v>.>..>.v...v...v...vvv..v>.....>>v..>.>...>...v>.>v...v...>v....>>v...vv........>....v>......>.v.>..>.>..
..>v.v....>>.>..v.>>.>.v>..>v.vvv..>.>..v..>..v.v..v......v....>v.>vv..v.>.vv..>>>.>.>.>>.....vv..v...>>v.>v.v.vv.vvv>..v..v.vv>vvv>vv>....
.>>v.vv...vv.>v>vv.>...v.v.>v..>.>>.v.>>..v...>v.>v..>>.v...v.>v.v..vv>>>...>>..>.v..v>..vv.v...v.>vv.>>>.vvv...>v...v.....vvv.....vvvv.v.>
.v>.vv>>.>.vv.>>.>.>....v...v..v>.>.vv>.v..v..>v>..>>>v.v..vv....>..>v..vv.>..>..vv>..v...v..v.....>>.>..v.>v.v.v..v..v..vvv.v...>....>>v.v
v>....v.v>....>..>v.v...>>v..>v>.vvv..v..v.v>>.v..>.vvv..v.v..>>>>v>v...v..>...v..vvv>.>>>vv>>v..>.>.v.>......>..v>.v>>v>v.>..v.>>.v.v.....
.>..v>v.>v..v>>.>....>vv>v.vv>.vv.>v...v.>.>...vvv..>>..>vvv......>>>.v.v..v...>..>vvvv.>.>>.v.v>>.vv.>>v..>v>v>..>v...v.v>>.>>....v.v.>.>.
...>..>.v.>.>.v...vv>.v.....v.v..>v>v..v.>.>..>..>.>..v.v.v.>.v.>v..>.vv.v>>.v>...>.>v.....vv..v>v..v........v.v..vv>vv.>vv>v.v.....vv..vv>
.......vv>v...>>v...>v..>v..>.>>v.>>.>>v.v>..v.vv..>>>.>..>..>v.>v...>>>v..v.v>v.v.>.v.vv.v.v..vvvv.vv.vv>>>>....>.>.>...>..v...>v>..vvv..v
.v....v.vv.>v.>.v.>>.v.>..........v>...>>>>....v>....>>v...v....v...v>vv.....>v.>.vv>>>..v>vvv>..>.vv..>...v.v..>.>...v..v.>vv..v.>vvv>>v.v
..>>vv.v.>.....v>...>v..>..>.>.v........v>..v>>..v....v.v.v....>v>vv>..v...v.>.v>...>.>>.vv....v...v>v.v>vv....>v>v.>..vv>.>.v..>v>>v>vv...
...>v>>>..........>..vv..>>.v...>..>>........v..v.v>..>.vv.>vvv..>vv..>v.v...v..vvvv.>.v>..vv>.v..>v>>.>.>>v>>vv..v>>>.vvvv..>.v.v.........
.>.>>v>v>v>.>..v.>v.>.vv...>......>.>v....vv>.>..>.>.v..v..>v.>>.v..v.>....vv.v>.v.>....>>.>>.v>.v>v.vvv....>.>..v>.v.vv.>>......>.>.>...v.
v..>..>>>.v.>.>>.>v>>.vv>.>v..vv.v..>....v.v.>v...>..vv..v>v>.>>...v>..>v.v.v>>>v.>.>.vv>.v>..vv...>v...v>...>v>v>.v>v....v>vv...v.>>>>>.v.
.v.>.v...>..vv>......>>..>v.v.....v>.v...>...v.v..v>.....v.v.v>>>>....v..>.....>.vv>.>v...v>.v.>>.>vvv>v.>.v.vv>...>..>.>.vv>v....>v.>..v..
>..>.>v.>v..>.>v>..>....>vv.v>v.v..>v..v.v.vvv.>v.vv.v>.v...>...v.......>v.......>v>v.v.>...>.......v>v.v...>vv.v>.v>v>..>>>.>>.vvv..>>v...
.v>>>v....vvv.>v.>.>>v>v...>.v.v.....v>.....>.>>v.>>vv..>.v.vvv....>>v.>v>.v>vvv>>>..>>.v.vv>v>.....>>.v.v.>....v...>..v>.>vv.>.v.v...v.>..
....>>...v..>>v...>>>.>.>>..v>.vv....v....>>.>.>..>...vv..>>v.>.v..v.vv.v..vv.>>.v...>>.>.>....>.>vvv.....v....>>v.>....vv..v..>.>v>.>...v.
.vv.>.>v...vvv....v....v.>..>.v>>.>.v...>.>>.vvv...>.v.>...v.vv..v>>.>..v.>..>...v..v..v.v>v.vv.>v>.v>.v>v...>>.>>>v>>>..v.v..>..>.v>.v.>v.
>v..v..v.vv.>vv.v..>.>v..v.v.>..v....v.v>.v...v>.>>vvvv>.vv.v>..v.>v>.>v>>.v>>>>.vv..>vv>v..>>...v..v....v..v>...>...vv.v>...>v...>.>..v.v.
>>.v.>v>.vv..vvv......v>>..>>.vv.vv>.v...>>.>.>.v>v..>>v>>.>....>.v.v.v>....v.v>>..>..v>......>.>.v>.v..v>....>v....v.vv...v>vv>.v....>v.>>
>v...>>.>.>v>v...>....>.vv....v..v>.....vv..>vv>v....>.>..vv..vv.v.v>>.>.vv>vvv>..vv..>.>.vv..v..>.>v.>.v.>>>..>>..>>>>.vvv...>.>....v.v..v
>.>.>..vv.v..v>v.>.>>>v>v>..v..>...>>..>vv>v..v>v.vv>>>..vv.>.>vvv>.v....>...v.>v>.>....>vv>...v>>vv.v..v.>.v>..vvv>>.>v>.....>>>..v.>.v.vv
vvvv>v..v>v.>vv.>.v..v..>.>....v.v....>v>.v>.>.>...>v..>v...vvv..v.v...>>..>..>>>...v>>>.>.v.>.>...>..>.v.>v..vvvvv.>v>>.v>..v.>v..vv>..>>>
...>v>.>v...>>>vv..>vv.v.v..vvv....>..>.>.v>>vv...>....v.v>.v.>..v.>.>>...v...v>v>>.....v>>vv...v..>...v.>...>v>....vvv.v....vv.>...>..vv..
......v..>..v>v.v....>.v.v>..v>..>v...vvv.v.v.>>vv.....>..v.v.v....>v.>v....>.>..>>.>...v...>...v..>v>>>.>.vv..>vv>.>v.....>..v.>>..v>..v..
.>v.>...vvv>..v..v..>...>.>>.>..>v.>..v>....v>>v..v.vv....v..vv......v>>>..v>v>.>...>v>>v>.v.v>.vvvv..v...v..>>..>>>...>..>>>>...v..v>v.v.v
..v..>v.....vv.v....v.vv.>.vv>.v>>.v.>v>v.vv..v.vv.>.....v.>.vv.>.>..v...v.v.vv.>v...v>.>>.>.>.>.>...>..vv.v..v.v.>v..>v...vv>v.v..>.v.v>.>
...v..v>>>...vv>vv.v.>...v>>.>.>v>>v.v>vv>v>......>.....v..v..v>>>v..>>.>>v.>v..vv......>.....vvvv.v>.>.vv...>...v...v>...v..v>v.vv.v>..>>v
v.>vv>>v.v.v.>v...v.....v.>>..v.>>v>>.v.........v..vvv..>...>.>>.>v...>>.v.v.>>..>v>v..v...vv>.>>..v.>.>v.v.>>>.vv.vv.v.>.v.>>>..>>..v>>.>.
....>.....vv...v.>.v>>>>.......v....>>>>>..>....v...>....v>....>v..>>..v.>.>...v>v........>.>v..v>.v>>..vv>>>v>...vv.>..>>v.v..v.v.>..v>vv.
>>v.vv..vv..>>.>.v..vvv.v>...>>.>>.>v.v...>v......vv..vv....v...>v..>..v.v>.vv>>......v.>.v>v.v.>>v>v>.v.vv....v...v.v.>....>v>>v....>v..v>
v...>v.>.v>v>.vv...>...v.v.>.>>>v.>>...>>>v>..v.v...v.vv..v>.....>...>.>.v.>...>.>...>..vv..>>>vv>.v>v.>>..v>v>.vv..>v....vvvv.>.>>..>..v..
..v..>>.vv>.>v.>.v.>..>..>>v>v..v>>>...v>v>>v.>>..v.>v>>v...v..>v.v>.>.>>.>..v.v>v>.v...>v...>v>>...v.v>v..vv.....v>..>v..v......vvv.....>>
.....>..>.....>...>v..>..>..v..>...v..v..vvv..vv>v>...v>........>..v..>..>v.>vv>...>..vvv>.>>>.....v.>>.v>.v>.>..v>>.>..v..vv>>.v.vv.>...>v
>>.v>v.>>.>>v>>.vv.v.>.>.v..>vvv..vv..vv>v>.v..v..>>.v>..v...vv..vvvv>.v..>.>vv>.v>v>>.....v>v>>..>...>...v...v>>v.>..>..vv.v>....v>..vv...
....>>.>..v..vv.v....>.v>.v>v>..>v>>.v>>v.vv.v.v>>vv>>>>.>v>.>.v..>v.>vv>>..>..v>>v..>>.>..vv>>>.>..>.v>v>..v.vv...>>..vvv...>>.>.vv.v>v.>>
.v.vv>.v...>.>>>.>...v.v>>>.>...>>..>>.vv..v...v>..>v>..vvv>.>.....>v.v.vv.v>>>.>..vv.v.v..v.>>.vvvv>.>v>.>v..>..>vv.>>.....v.>v..v.vv.v>..
..v..v....v...>.vv..v..>......>>>>v.v..v.vv>......vv>..>v.v>...>.>v...>>.>>v.v.>>.>.>.>..>>..v....v>.>>>vv>......v.......vv.>...v.>...>v...
.>.vvv.v....>vv.>>>...vv>v.vv.v>>>>.v.>v.v....v>..>.v.>>vv.>vv....>.......>...v.>>v.v.>>.>.>vv.vv...v>..v>>>......>>.v.>v.v.>.>..v.>.>....v
.>..v...>>>>.>..v...>>.vvvv.>v>.....>>vv...v....>.>>.vv>.v..vvvv....v........>v.v....>vv.v.>..v>..v...>.>..>v.vv>.v..vv.>..>.vv.>.v...>.>>v
v>..vv>..>..vv>..>v..v>vvv..>v>v.v.....v.>vv.>...>.>v.v>>..>v..v.v...v>.....v.>..>>v.v..>>>...>...vvv...>.....v>.......>vv.>..vv.>.>.v>v>v>
...v>v>.>.v.>..>....v..>.v.v>v.vv.>.v..>>..v.vv>v>....v>>.>>.v>.v....>>vv.v.v>.v.>.v>v.>.>.v..>>v..>>.v>v>>.v.>v.>..vvv.>....>>>v.>..>v.>..
..v.v..v..>..v>>...>...>>.v>.vv.>...v.vv>.>..v.>v...v..v.>...v.v...>.v.>>...>>..>.v..>>.v>v....>.>.>>vv....vv...v..>>.>>.>>vv.....>v.....v.
>.>>.v..>>.vv.v>>.vvv>....v.....v..>....>>.v.v>vv>>..>v...>.v>.v.v.>.v.>>..>>...vv>.>>.>.v.>..>v.v.>.>v.v>>v>..>.v>v.>vv.>v>.>.vvv.>.>...>.
v.v.v..vvv..>..vvv..v....v....>.v....v..>..>.>v...v.vv>.>v..v.v>>.v.>>>>.v>.>....v..v>vv..v.v>..vv.v.v..>v...v.v.>..>..v..>>>...>..v.v.v.>v
.>..>....>v.v..vv..>.v.v>...v.vvv.>...>.vv>.vv...........vv.vv.>..vv...>vv.v.vv>v..>v..>.v.>...>.v>.v.....v>.>>>.v>vv....>>v..v>.v..>v..>.>
..v>.......>.>.vv>>.>.vv>.vv...>>v.>.>v>.v>>.vv.vv.v>>..v>..>.v.v.>vvv.>vv...v>...>..vv...v>v>.v>.>...>>>.>.v>v>>v.>.v>......>.>.v>....v...
.vv.v>.v...>vv.v..>...v..>..>>.vv....>v>>>v>v...>.v>>..>..v..v.>>v>..>>v..>..>v.>..>v.v.>.v.vv>.>.vv.>vv..v..>..>vv.....>>...>...>v>>.v..>.
.>.>..vv>>v>.v..v>..v>>>.>..>.>v..>..v...vv.....v..vvv.>.>.vv..v.vvvvvvv..v>>>.v...>......v..vvv.v.>>.....>.>.v......>.>>>..v>.>>>...>..>>v
>vv.>...>vv>v>.v.>>v...>....>>..>>.v..v>vv...>>>>....vv.vv>.vv>...v.>>....>>>>.....>v.vv.vv..>.vv....v.v>vvvv..vv..>...v>v.>vv.v......>v>>.
>>v.>>..v.>>.v.>.>.v.v...>.>>v..>.>>v..>>>.>..>>...>>.>...v>v..vv>...v.>..v..>...>v...>v>.v>>v>.>.v..v...v.v>.v>...vv..v>vv..vv>.v.......v.
..vv....v....v.>v....>..v.>.v.>..vv>v>.vvv.....>........>>v>vv>..v....v.v>...>.vv>.v.>vv.....v.v>vv>>v>.v>...>..>.>vv.>>>>>v>.>.v..v..v..>v
v.......>..vvv.>..>>v>......>v>v...vv..v..>v...v>>vv>.>.>...v...v>>vv.>.>>..vv.>>vv...v>v.v.>v.v......>......>>v>...>>>.>v.....vv>...>>.v..
v.v>>vv>.>v>.v.>v.v....v.>v>v..vv....v..v>.>>>.>v...v>.....v.>v...>vvv>>.>v...>..>...vv>>>>....>.v.>vvv.....v..>.v.>v>.v.....v>v>.>.vvv>>>v
.v>>..v.v.v.v.vv...v.>.v.vv.vvv>>.v>>>.v.v>v>.vv.>>v>v.>..>v.....v.......>.>.vv.>...>v.v...v...>.>.>...>>v.v..>>.vv..>...vvvv.>.v>..v..vv..
..v....>vv.>>v>>..>v..>v.>v>.v>>v.>.v.>>.>.....>..>..v..v..>..>vv........vv.>v>.v...v.>.>...v..v.v.>>...v>v.v..v.v>.>>...v>.>.v..v.>..v>...
vvvv...>..v.>>..v..>>.v.>>.v..v>.>vv>..>v>>>..v>....>..>.v>>>>.....vv>v..>..>v>vv.v.>v>..>vv.vv...v.v.vv.v>.v.vvv>..>.vv.v..vvv..>v>v.v.v..
.>vv.>v..v>..v>...v.v>...>.>v..v>...vvv....v...v..>>>....>..vv>....>.>.vv.>.....v.>.>....>>.>.vvvv>.>.>.>..>>>....>.vv...>>..v>.>.v.....v>.
vv>>..v>.....v>.v.v.........>.>.>...v>>.v......v>..v>..v.vvv..v...v.vv>v...>v>>v>.v....vv.>>.>v>...>.>v.>..vv......v..>v.>vv..v.v..v...vv..
>v.>..v>...>v.v>.v.vv..>....>..>.v..>>>v>>..>..>v.>v..>>..v....vv..>.>>>>>.v.>vvv.....v.>>>.v.v..>.v.v.v..>>v.>>vv>>....vv...vv>>.v.v.>vv.>
v>>.v.>....>>..v>>.>.>.......v..vv...>...vv.v>>>>v>...v>vv...vv...>....>>>.>..>.v.v.>>.v.v>vv..v>..vvv.>...>...v.v..v>v>.>.....vvv..v>.v.>.
..>.>v>>>..>v...>>v.v.v..v.v>>.v>..>.v>v>.>...v.>..>.v.>>.vvv>.>>>.>...>v.v...v.>....v...vv.v>..>.>..v.>.>.v.>.v.v..>>....>v>..>.v>..v.vv.>
vv.>>v.v>>vvv.....v.v>..>v>.vv.>>vv>....v....v..v.>>.>vv>..v.vv....v...v>>>.vvv..v>>.>v>>v.v...v.>>>>v>>.v.>>vvv..v.vvv.vv...>>..>>..v.>.v.
v....v.v>>.>v..>.....v.v>...vv...v.....v>>v..>vv>...>v...vv..>>v.>>.vv..v>.>>..>>.v..v....>>.v.>>.....v.>>...v..>v>vv...>>>.v>..>.v.vv.>v>v
........vv>>vv.>v.>...v.>v.>>.>........vv..>.>..>>>.v.>v..>.>>.v.>..>v...>.v>>.>..>v>.v.v.v.>...>.vv.v.>>.>vv..>...v>vvv>.>..vv.>v.>v.>..v>
.v>>vv.>>>.>..v>v>v....>.....>>>.>>.....>v>.v.>v>>vv>..>...>>v.vv>vv>v..v>>>v..>v..vv...vvv.....v.v>v..>v..>v..v>>v>.v>..>.v...vvv.>.v.v.>>
.v>>>.v..vv.....v>v....>v...vv..v.>>.>.>..v.>...v...v..v>.>v.>>v.vv....v>v.v....>.>>>...>..vvvv>.v..>.>>.>vvv..>.......>v>v..>....>..vv>.v.
>.....v..vvv.v.>>>..>v>>vv>.>..v.>>.v......>vv.v>.vvv>vv..vv>...v...vvv.>>....vv>>.v>vv>.....>v.>..v..v..>>.......v.>v..>v..v....>>v..v.v.v
>.>vv>.>.>v.....v>>....>.>v>>vv.v>vv..>>>>>.>.v...>>v...>.vv.>vv.v>....>......vv.v.>......v>v....v.....>..>>.v.>.>>>v.>.v>v>..>.v..v>>v>vvv
...>.>.>.v>.>v.>....v..>..>..>.>..v>vvv.>...>>>.v..v...v..>>vv>.v.v..v>>.>...v>.v......v.v>>vv..v.v.vvv...vv>v.>.>>v....vv.v..>>.v.vvv>v.>>
>>.v.>v...>..vv>>v.>...>...>...>v.v.....v..>..v>v...>.>..>.>..vv...>..>v..>>>>>....>.>v.>..v..>.>v>v.v...v>>......vv..>.v..>.>.>.....>v>v.>
v>.v....v..>v.v.>>....v....>....>>.v>..>.v..>.>..v>>.v..>>..v..v>>v>v.vv...>>...vv.v.>.>>.>.....>..v.v...>.v.vv..v.v.vvv>.>.>v.v.vv>v.vv>.v
..>>.v..>>....>..vv.>.v..>>.>.>.>v.>..>..>..>v..v..v>v.v..>.>>.>...>>>....>.>>..vvv.v>v..v...vv..vv.vv>v..>v..v..v>v>.>...>v....>>.>.....vv
v.v...v.>>....v.>v.v....>.>.>...>>..vvv>..v>>v..>>.vvv.>v....>>..>>v>>>>v..vv>v.v..>v>>v>.>>v...>.>v>.>>.v..v>.>>vvv>..v.>..v......v>>>..>v
v>.>.vv.>>vv...>.>.v.vv.v>.v>v...vv.>vvv.>v...v.v..v>.vv>.>v.v...>.>..>v>.>..v..>.>v>..>.>v.>>>>>.>.v>.vvvv..v.vv.>.>...>.v>v.v....>.>>.>.v
>...v.v...vv........>>vv...vv.v>...>.>>>>>.>.v>>vv>..v.>v.>>v>>.v..>>..vv..>....>...v.v>.v.>..>..>>v...v.>>v...>....>.v..>.>>v.v.>.v>vv....
.vv..v>>>.v.v.vv.v>>..vv>.v>v>.>...v>v.......v....>>v..>.>.vv.v>.>.v.v..v..vv......>...>..v....>>>...v.v>..>>v....>.vv..v......v.>...v...v.
>.>....>.v>..>.>>.>v>..v.>.vv...........vvv>...>v.v>>...v>vv....v.>..>>>.>..>.v.v..>vv>..>v>vvvvv.v.>...v..>.vv.vv....>>v...v.v...>v...>.>.
.>.v...v>.v..>.>v....>..>>.v.v.v...>.>.vv..v.v.....>>..vv>.>.v..>..>.>>.>>>v..>.>..vv...>....>..v.v.v.>>vv>v..vv....v.v.vv.....v.>..v......
>..>>>v>>v>>..>>.>vvv..v..v....>v...>.v..v..v>>>..v.>...vvv..v>>v...>>>..>>..>.v..>>.>>.v>.........>..vv.>.v>>v.vv>.>.>.vv>>....v...>..>>v.
..>vv..>vvvv.v>.v.>..v.v..v.vv>>>vvv.v>.v.>>..v.v..v>>vv..vvv.....v>.>..v>vv....v..>.>.v>..>.....v.v.>>vvvv..v..v>v..v>v>>>>.v.>v...v..v>..
>>...>.....v.>...v>..>.vv.v....>.>.>v...>v>.>vv.v.vv.......v>.>.>.vvvv>....v.>..>v..>v.>>>...v>v>>........>>...v>.....>v>v..>.vv.>..v......
>v.v..>...>>...>...v.vv..>v>....v.v.>v.v.v..v>.>>v...>.v>...>.vv..vv.v..>....v>>.v..v>vv...>v.>....v.>..v>...v.v.>>>vv.>.>..>...>v.v.>vv.>>
>v.v>.vvv>...>>v>>>v>v...>..>.vv>.>vv>v....vvv........v>v.>v...>>v>.v..v.>...v>.>..>>..v.....v...>.v.vv>v.v....>.v..>vv.v.>>..vv>....v...v.
>>>>.>...>v.v..>>.>>.>>...v>v.v..>>...>v>>v..v...>..>.vv>>>...v.v.>.>v..v.v>>vvv.v>>>>.....v.>..>.v.vv.v>....>.v>....>.vv.>vv..v.v..vv.v..v
v.v>vv..vv...>.......vv.>v..v..v....>.>.>..v>.vv>.>.>.vv.>>v.v.>v>>..>.>>>.vv.>vv>v>.v.>vv.v>>vvvv>.vvv>>>...v>v.v>..>.....>.>>..v.>v......
..v.....>vv.v...>..v.v....>>>..v...>.......v.>....>.>..vvv>v>..vv>v>v...>..>>..v>.....>>.>.vv>...>vv.vv>>..........vvv.>vv...>>.v...v..v>>.
....>.v..>.>v.......v.vv>>>v.vvv.....v>>.vv>.>.>...v>.v.>vvvvv.>v>.v.v>>....>>...>....>.v...>.......>.>v>>vv..>...>......>....vv.v.v.>.v.>v
...>v>.v.>v..v>>.>.v>vvv.v>v>.v>v..>..v...v.v>.......>v.>..v.v.>...>>..>.>v.>>v..>.v>v...vv..vv...>v..>.>...>.v.>v.v....v.v..vv.>>....>v>..
...>.v...v.>..>..>v>v>v>.>>v..>....v.>.....>v>..>>>>.v..vv>v.v..vv>.v>>.vv..>>..vv.>>...v.>v.vvv.v>.>.>.>v.v>.>.v.>.....v..........v.>>..>v
v>.v>.v.>vv>>vvvv>.>v.>.>.>.>vv.vv>.>vv..>...>...v>v>v>...>....>....>>.>>....>v..vv.vv...>.v..>.v..>.v>v>v>.>..v..>...>..>v...>>.>>v>..>.>.
>v.>.v.>.vv>...v>.>..v.v.v...>v.>.>.>v>>>.....v..vv..vv...>.>>.>>>.v>...vv>v.v.>.>v....>>>vv.>.>>v.vv.vv>>v..v>>>>v..v.vv>vvvvv.v..v...v...
.>..>.>..v..>>>.v..v..>>.>...>..>>.v..v.>>.>>.>.>>v.>v.>.....>v.v..>..v.v>..>>>..v........>vv>.v.v.v.v....vvv.vv>..>>v...vv.>...>.v..v.v.v>
..>.v>..>..>v>.v.>v>>...vv>>>>..>.vv.v...vv.vv.>>>>.>>.....v.vv.v.>>v>>.>v.>>.>>>>.v>>vv>..v.....v>>.vv>..v.v.>..>v>..vv>...>.>v.>vv..>..v>
>v.v>.v...v>>.vv>.vv>v>.>vv...>v>.>v>.vvvvv....>.>.vv...>.....v..vvv>v..v.v.v.v>>vv.v...v....v.>..>.v.v..>..v>>..>v......v..>vv.v...v...>..
..>v>>v>>v.v....v.>>v.v.>.v.>>.vvv.v>v.>..>>>>.........>..v.vv>.vv>>.>v...>>>>vv....>>vv....>.v>v>v>v.....>.>>>.>.v>..>.......v.>>>>vvv.>.v
>>>>>vv...v.>.vvv...>...>.v..v..>....>>.v>v..v.v>...>>v.>.>.v>......>>>>>vvv.>.>.>vv...>>v..vvv...>v..v.v>v...v>v>..>>vv>v.....>...v>.v.vv.
.v...v.v>v...>.v.>..>v.v...v>...>v.v.>>...>>>>vv.v>>.>..>.>.v>..vv.v>vv....v>>>....>v>>v>.v.v.....v>v..>>...v>>v.>...v...v>v>vv..>>.v>>>v.v
.v..>>vv.>>>.>v..>..v.v>.>vv...>....vv>.>vv...>v>....v.vv.>........>......v.vv>...>vv.vv..v.v>v.>..v...>.vv>vvv..v......>.>.vv.v...>..vv...
.v.....>>..v.>>>>v..v>>>>.>>......vv.vv.....>.v.vv>>v>.>..>....v>..>>.>v..vv.>v.vv..v>........v>....>..v>v>v.v>>v..vv>.v.>.v....>.vvv...>>v
.>..v..v..v....>v.v>...v.vv>v>.v.v>>..>v.vvv>...>>.v...v.....>vv.>.v>...>>.>v>vv...v>.>v>v...vv>.....v...>.>>>.>v..>vv.vv.v>.v.vvv.vv>v>...
>>.v..>.v.v.>.vv..v.v..v..v.vv.v.vv.v>v.>.vv>..v>.>v>..v.>v.>........>>>.v.>v>....v.>........>>.v...v..>vv..>.vvv.vvv....vvv.>.v>.>>..>>.v.
...>...v.>>v>.vv>.vv>..>....vv..vvv....>.>..v>.>>..v....>.>>>.v>>vv.>....>.>.v..>>>.v>.>.>...vv.>..>..>..>..>>.>>>...>.>vv....>...>.>>>...>
.........vv>>>v.v>.>v>vvv>v>..>..v>>>..>>.v>>>.>......>.vv.....>.v.....>....>..v......v>..v..>...>....v.v>....>>.>.>v.vv..v.v.>..>v.>..>..>
v..v>......v.>....vv.>v...>.vv>>v.v.>.>..v>>vv.v.v>v..>.vv....>..vv....>>..v...vv..v.>vv.>...>..v.>...v..>v.>.v.vv.....v..>.vv.>.vvvv...>v>
..v..v>.>>v>.vvvv>.v.....>v>vv.>.>v...>.v....v.>vv...>>...vv.v..v.>v.vv..>..>.>..>v>.>v..vvv>.v..v.v>...vv.v>.v>.v>>..>v.v>vvvvv.>.....>v>.
v>.>.v.>..>>>..v>..vvv..v>>.>..>>>v....>v.>...>.v>...>....>>..v>v>...>>.....>>v..v>>.>.>>.>v......v.v.v>v.>.>.v>>.v>>>v>>>v....v>>..v.vv>.v
>..v....>.vv>v..>vv>>>.>vvv>v..vv>.>>...vv>v..>.vv.>>..>..>....>>.......v..........>...v>>v>.vv..>>.>..>.vv>..v>..>vv...vvv..>.v>.vv>.vvv.v
.>>.v....v...>..v.v>.>.>v>.>v.v..v>.v.v..>v>...v.v>..v>v...>...vvv.>.vv>v>...v.v..v...>>.>.v.vv..>>>>v.>v>v.v.v.>v...v.>v.>v.vvvvv.....v>v>
>>vv.v.>vv...>>v..v...>>..vv>.>v.>>.>v.......>>v>v.v>v.>.>..v.......v>>>v..>>>.>..>v..>vvv..>..>.>>v>>>..v.>.vv..v.>.v.>>>..>>v.>>..>>...>.
>>..v..>..>v....v....>vvvv>.v.>...v.v.>v.>vv....>.>>>.v>v>.....>>v>.>>>>vvvv.>vv>vv>.....>>vv>..>>....v..>v.>v.v>>v>vv>....>v.v>>.v>...v...
..>>..v>v.>...v>....>v.>...>...>...>..v.v..v>.>>..>.>v...>>.v.>>.v.v..v..>.v.>...>v.v>v>>>.>.vv.v>>.vv...>v>>>..v>.v...>>vvv.v..>..v....>..
v>v>.>vv.>>>>vvv>.>v>>..>..v>.>.vv>>v.v>>.v>>.v>>.>.......>>>v>.>>.>>v>...vv>vv..>>>.v>.v>..vvv..>...>...v>v>...vv>>.>.vv>>>.>.>v>....>>v>>
...>>v>>v.>..v.v..v.v>v>>>..>..vvv..vv>.v.....>.vv.vvv.....>vv>v.v>v...>vv..v..vv.>.vv>...v.v>.v>>v.vv....v...>v...>>.v>v.vvv>v>>v>....>...
>>v..v.vv.>..vv.>>>>..>v>vv..v..v.>>>.vv..v.v...>>......vv>.....vv..>..>....>......>v.>.....vv.>>v....>.v>>..>.>....vv..>v>.>>>>.v>v...>vv>
v.v>v>v....>v..>.v..>>...v.v.v..>>>.....>v......v....>>>..v....>.v.>>>v.v.v.>v>.>v.....>>vv>.>v..v...>v..>>>.>>v.v..>>.>.v....>v>>>v..>v>.v
>>v.....v>v...>>vv>>.v>.v>..>...>..>.>.v........v.>.vvv....v.>>v>..vv..v.v>vv>.>..v>>v>v.v.>v>..v>v....v....>.>.>v>..v.v>>v>.>.v.vvv.v..v.v
>..>..>>.>...v>>vv...v.v>..v..>vv..>.>..v>>>v>.....v>v.vv.>vv>vv>>...>....>.v.vv...v.....>.>.....vv.....v..>>.v.>v....vv>.v...v....v>.vv...
v.>..>.>..>>.....v.>>......v>vv>v.vv>.>>v.vv.>.>>.vv...v.v..>vv...v.vvvvv..v>v.....>v.v..>..v...>.v..vv>.v.v.>v..>.......v....vv...>vv.v>>>
'''

inputmapstr = cstr
inputmap = [list(s) for s in inputmapstr.split('\n') if len(s) > 0]
m = Map(inputmap)
print('Initial state:')
m.display()
for i in range(1000):
    moved = m.onestep()
    print(f'After step {i+1}:')
    # m.display()
    if not moved:
        break
print('done')
