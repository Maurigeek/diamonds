
"""Dessiner des diamants de différentes tailles."""

def main():
  print("Diamants")

  # Afficher les diamants des tailles 0 à 6 :
  for diamondSize in range(0, 6):
    {displayOutlineDiamond(diamondSize)} 
    print() # Afficher une nouvelle ligne.
    {displayFilledDiamond(diamondSize)}
    print() # Afficher une nouvelle ligne.


def displayOutlineDiamond(size):

  # Affichez la moitié supérieure du diamant :
  for i in range(size):
    print(' ' * (size - i - 1), end='') # Espace côté gauche.
    print('/', end='') # Côté gauche du diamant.
    print(' ' * (i * 2), end='') # Intérieur du diamant.
    print('\\') # Côté droit du diamant.

  # Affichez la moitié inférieure du diamant :
  for i in range(size):
    print(' ' * i, end='') # Espace côté gauche.
    print('\\', end='') # Côté gauche du diamant.
    print(' ' * ((size - i - 1) * 2), end='')  # Intérieur du diamant.
    print('/') # Côté droit du diamant.

def displayFilledDiamond(size):

  # Affichez la moitié supérieure du diamant :
  for i in range(size):
    print(' ' * (size - i - 1), end='') # Espace de gauche.
    print('/' * (i + 1), end='') # Moitié gauche du diamant.
    print('\\' * (i + 1))  # Moitié droite du diamant.
  
  # Affichez la moitié inférieure du diamant :
  for i in range(size):
    print(' ' * i, end='') # Espace de gauche.
    print('\\' * (size - i), end='') # Côté gauche du diamant.
    print('/' * (size - i)) # Côté droit du diamant.


# Si ce programme a été exécuté (au lieu d'être importé), lancez le jeu :
if __name__ == '__main__':
  main()

