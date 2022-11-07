#!/usr/bin/python3.10

import random


def main():

    # Initialise length, height of grid and the number of random moves.
    length = int(input('Enter length of grid: '))
    height = int(input('\nEnter height of grid: '))
    n_move = int(input('\nEnter number of movements: '))

    # Initialise grid state.
    grid = [['#'] * length for i in range(height)]   

    # Calculate centre points of both rows and columns.
    # Think of + within grid where points overlap to create centre point.
    centre_length = int(length/2)
    centre_height = int(height/2)

    # Determines if centre point can be created with given input.
    # If even, it adds 1 to given length and height to be able to assign a centre.
    # If odd, assigns centre point.
    if length % 2 == 0:
        length += 1
        print('\nGrid length must contain a centre point, therefore each rows length cannot be even.')
        print(f'Appending each rows length to: {length}.\n')
        grid[centre_height].insert(centre_length, 'C')
        for l in grid:
            if 'C' not in l:
                l.append('#')

    if height % 2 == 0:
        height += 1
        print('\nGrid height must contain a centre point, therefore the height of the grid cannot be even. ')
        print(f'Appending grid height to: {height}.\n')
        grid.append(['#'] * length)
        grid[centre_height][centre_length] = 'C'

    else:
        print('Grid size valid.')
        grid[centre_height][centre_length] = 'C'

    # Prints inital grid state with given centre point.
    print('\nInitial Grid:'); print_grid(grid)

    # Initialise dictionary to store move counts.
    move_count = {'Up': 0,
                  'Down': 0,
                  'Left': 0,
                  'Right': 0,
                  'Exceeded': 0}

    # Performs each move and then prints grid state after each move.
    for n in range(n_move):
        move_C(grid, length, height, move_count)
        print_grid(grid)

    # Prints total of each movements.
    for direction, value in move_count.items():
        print(f'{direction}: {value}')

    return


def move_C(grid, length, height, move_count):

    # Gets current position of 'C'.
    for i, lst in enumerate(grid):
        for j, c in enumerate(lst):
            if c == 'C':
                current_pos = [i, j] # current_pos[y, x]

    # Assigns each directtion to a list and selects one at random.
    directions = ['U', 'D', 'L', 'R']; random_direction = random.choice(directions)

    # Switch case for each direction.
    # Here the given direction is printed and it is validated whether completing the move
    # will force the 'C' off grid. If so, the move is passed.
    match random_direction:
        case 'U':
            print('Up:')
            if int(current_pos[0] - 1) < 0:
                print('Exceeds border. Passing...')
                move_count['Exceeded'] += 1
                pass
            else:
                grid[current_pos[0]][current_pos[1]] = '#'
                grid[int(current_pos[0])-1][current_pos[1]] = 'C'
                move_count['Up'] += 1

        case 'D':
            print('Down:')
            if int(current_pos[0] + 1) >= height:
                print('Exceeds Border. Passing...')
                move_count['Exceeded'] += 1
                pass
            else:
                grid[current_pos[0]][current_pos[1]] = '#'
                grid[int(current_pos[0])+1][current_pos[1]] = 'C'
                move_count['Down'] += 1

        case 'L':
            print('Left:')
            if int(current_pos[1] - 1) < 0:
                print('Exceeds border. Passing...')
                move_count['Exceeded'] += 1
                pass
            else:
                grid[current_pos[0]][current_pos[1]] = '#'
                grid[current_pos[0]][int(current_pos[1])-1] = 'C'
                move_count['Left'] += 1

        case 'R':
            print('Right')
            if int(current_pos[1] + 1) >= length:
                print('Exceeds border. Passing...')
                move_count['Exceeded'] += 1
                pass
            else:
                grid[current_pos[0]][current_pos[1]] = '#'
                grid[current_pos[0]][int(current_pos[1])+1] = 'C'
                move_count['Right'] += 1

    return move_count

# Make printing the grid pretty.
def print_grid(grid):

    for l in grid:
        print(''.join(l))
    print('')

    return


if __name__ == '__main__':
    main()
    
    





