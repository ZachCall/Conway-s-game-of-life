# Conways-game-of-life
Implementation of Conway's game of life using Numpy and Pygame


This was simple implementation of the famous Game of Life, created in 1970 by John Conway.

The game is represented by an infinite grid, which are represented by cells. The cells can either be alive or dead, represented by 1 or 0. The cells follow these basic rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

This application keeps track of the current generation of cells, as well as having a start, stop, exit, clear and toggle grid button.
