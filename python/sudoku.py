# coding: utf-8

#----------------------------------- Import -----------------------------------

from pprint import pprint
from random import shuffle
from copy import deepcopy

#---------------------------------- Fonction ----------------------------------

def print_grid(g):
    """Affiche la grille g.

    Args:
        g (list): Grille de sudoku.
    """
    for i,line in enumerate(g):
        if i%3 == 0 and i != 0:
            print(' ' + '─'*17)
        
        for j,c in enumerate(line):
            if j%3 == 0 and j != 0:
                print('|',end='')
            else:
                print(' ',end='')
            
            if c == 0:
                print(' ',end='')
            else:
                print(c,end='')
        
        print()


def alea_grid():
    """Génère une grille aléatoire (fausse).

    Return:
        (list): Grille.
    """
    l = [0,0,0,1,2,3,4,5,6,7,8,9]
    g = []

    for i in range(9):
        shuffle(l)
        g.append(l[:9])

    return g


def get_coords(n):
    """Renvoie les coordonnées associées à l'entier n.

    Args:
        n (int): Entier (< 81)

    Return:
        (tuple): Coordonnées (x,y).
    """
    return divmod(n,9)


def get_line(g,i):
    """Renvoie la i-ème ligne de la grille g.

    Args:
        g (list): Grille de sudoku.
        i (int): Numéro de ligne.

    Return:
        (list): Ligne.
    """
    return g[i]


def get_column(g,j):
    """Renvoie la j-ème colonne de la grille g.

    Args:
        g (list): Grille de sudoku.
        i (int): Numéro de ligne.

    Return:
        (list): Colonne.
    """
    return [line[j] for line in g]


def get_case_coords(i,j):
    """Renvoie les coordonées de la case de la cellule (i,j).

    Args:
        i (int): Coordonnée entière.
        j (int): Coordonnée entière.

    Return:
        (tuple): Coordonnées de la case.
    """
    return ((i//3),(j//3))


def get_case(g,i,j):
    """Renvoie la case dela grille contenant la cellule (i,j).

    Args:
        g (list): Grille de sudoku.
        i (int): Coordonnée entière.
        j (int): Coordonnée entière.

    Return:
        (list): Case.
    """
    I,J = get_case_coords(i,j)
    
    return [g[3*I+i][3*J+j] for j in range(3) for i in range(3)]


def free_numbers(g,i,j):
    """Renvoie la liste des numéros disponibles pour la cellule (i,j).

    Args:
        g (list): Grille de sudoku.
        i (int): Coordonnée entière.
        j (int): Coordonnée entière.

    Return:
        (list): Numéros libres.
    """
    if(g[i][j] != 0):
        return []

    n = set([1,2,3,4,5,6,7,8,9])

    return list(n - set(get_line(g,i) + get_column(g,j) + get_case(g,i,j)))


def solve(g):
    """Résout le sudoku par récursivité.

    Args:
        g (list): Grille de sudoku.

    Return:
        (list): Sudoku résolu.
    """
    G = deepcopy(g)

    def solve_rec(n):
        """Fonction récursive de résolution du sudoku.

        Args:
            n (int): Entier associé à une cellule.

        Return:
            (bool): True si le sudoku est résolu.
        """
        if n >= 81:
            return True

        i,j = get_coords(n)

        if G[i][j] != 0:
            return solve_rec(n+1)


        F = free_numbers(G,i,j)

        for f in F:
            G[i][j] = f

            if solve_rec(n+1):
                return True

        G[i][j] = 0

        return False

    solve_rec(0)

    return G





#------------------------------------ Main ------------------------------------

g = [
    [0,0,0, 0,0,0, 0,1,6],
    [3,0,0, 0,0,1, 0,9,7],
    [0,9,6, 0,0,0, 4,2,8],

    [7,0,9, 0,6,8, 0,0,0],
    [6,0,0, 3,0,4, 0,0,9],
    [0,0,0, 2,5,0, 7,0,4],

    [2,6,5, 0,0,0, 9,4,0],
    [9,7,0, 4,0,0, 0,0,1],
    [4,3,0, 0,0,0, 0,0,0],
]
s = [
    [5,8,7, 9,4,2, 3,1,6],
    [3,2,4, 6,8,1, 5,9,7],
    [1,9,6, 7,3,5, 4,2,8],

    [7,4,9, 1,6,8, 2,3,5],
    [6,5,2, 3,7,4, 1,8,9],
    [8,1,3, 2,5,9, 7,6,4],

    [2,6,5, 8,1,7, 9,4,3],
    [9,7,8, 4,2,3, 6,5,1],
    [4,3,1, 5,9,6, 8,7,2],
]

print_grid(g)
print()

G = solve(g)

print_grid(G)

print("\nAm I the boss ?","Yes Mister !" if s == G else "Nop")