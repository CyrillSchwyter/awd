from numpy import *

# Array von Numpy
zahlen = array([1, 2, 3, 4, 5, 6])
ergebnis = sin(zahlen)
print(ergebnis)

# Matrizen
# erzeugen
M1 = array([[1, 2, 3], [1, 2, 5]])
# typ der matrize ermittelt 2 x 3 (zwei Zeilen, drei Spalten)
print(M1.shape)

# Nullermatrize (3 x 3)
M2 = zeros((3, 3))
print(M2)

# Matrix mit nur 1sen erstellen
M3 = ones((4, 5))
print(M3)

# arange fuer eine Sequenz von Zahlen, auch Gleitkomme (analog range diese kann aber nur Ganzahlen)
print('Sequenz von Zahlen')
sequenz = arange(0.1, 1.5, 0.1)
print(sequenz)

# Rechnen mit Sequenzen
a = arange(10, 20, 1)
b = arange(0, 10, 1)
c = a - b
print(c)

a = array([10, 0, -1])
b = array([1, 2, 3])
c = a * b
print(c)

# Matrize
# Wenn wirklich die Matrizenberechnung genommen werden muss
M1 = array([[1, 2, 3],
            [4, 5, 6]])

M2 = ones(2, 3)


