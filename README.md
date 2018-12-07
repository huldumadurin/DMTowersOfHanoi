# Recursive Towers of Hanoi
A short Python program to recursively solve the Towers of Hanoi puzzle for any reasonable number of disks.

## Dependencies:
Requires Python3 and PyGame to be installed:
On windows:
```
python -m pip install pygame
```

## Usage:
To visualize a solution of the Towers of Hanoi with 3 disks, run
```
python HanoiTowers.py
```

To do so with <i>n</i> disks, run
```
python HanoiTowers.py [n]
```
Where <i>n</i> is an integer. Values less than 1 are clamped to 1, which makes for a very boring solution.

## Limitations:
On my machine, this seems to work fine up to 995 disks. Higher values cause the program to crash almost immediately, due to reaching Python's default maximum recursion depth of 1000 nested calls.

## Results:
### 3 disks
![Towers of Hanoi with 3 disks](https://github.com/huldumadurin/DMTowersOfHanoi/blob/master/Hanoi3.gif?raw=true "3 Disks")

### 8 disks
![Towers of Hanoi with 8 disks](https://github.com/huldumadurin/DMTowersOfHanoi/blob/master/Hanoi8.gif?raw=true "8 Disks")

### 50 disks...
![Towers of Hanoi with 8 disks](https://github.com/huldumadurin/DMTowersOfHanoi/blob/master/Hanoi50.gif?raw=true "50 Disks")