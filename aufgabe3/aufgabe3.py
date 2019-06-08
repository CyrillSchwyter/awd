import sympy as sym
import numpy as npy
import matplotlib.pyplot as plt

# Ausgangslage:
# Linere Steiung der Anlaufstrecke
# vorskizziert Stützpunkte

x = sym.symbols('x')

f1 = anlauf = sym.Rational(17, 4) * x
f1_lampda = sym.lambdify(x, f1, 'numpy')

plt.xticks(npy.arange(0, 100, 5))
plt.yticks(npy.arange(0, 100, 5))

# Steigung
plt.title("Ausgangslage der Achterbahn")
xsSteigung = npy.arange(0, 22, 1)
ysSteigung = f1_lampda(xsSteigung)
plt.plot(xsSteigung, ysSteigung, label='Anlaufstrecke f1(x)', color='green')

# Stuetzpunkte
xsStuetzpunkte = npy.array([40, 50, 65, 85])
xyStuetzpunkte = npy.array(([65, 40, 20, 15]))
plt.plot(xsStuetzpunkte, xyStuetzpunkte, label='Stützpunkte', marker='o', color='red', linestyle='None')
plt.xlabel('Strecke horizontal in Meter')
plt.ylabel("Höhe in Meter")
plt.legend()
plt.show()

# Bestimmung der Auslaufkurse mit Hilfe der Stuetzpunke
A = sym.Matrix([[40 ** 3, 40 ** 2, 40, 1],
                [50 ** 3, 50 ** 2, 50, 1],
                [65 ** 3, 65 ** 2, 65, 1],
                [85 ** 3, 85 ** 2, 85, 1]])

b = sym.Matrix([65, 40, 20, 15])
solve = A.solve(b)

f2 = solve[0] * x ** 3 + solve[1] * x ** 2 + solve[2] * x + solve[3]
f2_lampda = sym.lambdify(x, f2, 'numpy')

xsAblaufkurve = npy.arange(32, 85, 1)
xyAblaufkurve = f2_lampda(xsAblaufkurve)
plt.title("Mit Auslaufkurve")
plt.plot(xsStuetzpunkte, xyStuetzpunkte, label='Stützpunkte', marker='o', color='red', linestyle='None')
plt.plot(xsSteigung, ysSteigung, label='Anlaufstrecke f1(x)', color='green')
plt.plot(xsAblaufkurve, xyAblaufkurve, label='Auslaufkurve f2(x)', color='red', linestyle='--')
plt.xlabel('Strecke horizontal in Meter')
plt.ylabel("Höhe in Meter")
plt.legend()
plt.show()


# Bestimmung eines Splines zwischen der Anlaufstrecke und der Auslaufkurve
a, b, c, d, e, f = sym.symbols('a b c d e f')
# Die Funktion des Splines ist eine Funktion der 5.Ordnung: Prototyp einer solchen Funktion
f3_proto = a * x ** 5 + b * x ** 4 + c * x ** 3 + d * x ** 2 + e * x + f
# erste Ableitung des Prototyp
f3_proto_1 = f3_proto.diff(x)
# zweite Ableitung des Prototyp
f3_proto_2 = f3_proto_1.diff(x)

# erste Ableitung von f1(x)
f1_1 = f1.diff(x)
# zweite Ableitung von f1(x)
f1_2 = f1_1.diff(x)

# erste Ableitung von f2(x)
f2_1 = f2.diff(x)
# zweite Ableitung von f2(x)
f2_2 = f2_1.diff(x)

# Anschlusspunkte
x1 = 20
x2 = 40
# Gleichungssystem mit 6 Variablen
gleichungsSystem = [sym.Eq(f3_proto.subs(x, x1), f1.subs(x, x1)),
                    sym.Eq(f3_proto.subs(x, x2), f2.subs(x, x2)),
                    sym.Eq(f3_proto_1.subs(x, x1), f1_1.subs(x, x1)),
                    sym.Eq(f3_proto_1.subs(x, x2), f2_1.subs(x, x2)),
                    sym.Eq(f3_proto_2.subs(x, x1), f1_2.subs(x, x1)),
                    sym.Eq(f3_proto_2.subs(x, x2), f2_2.subs(x, x2))
                    ]

koeffizienten = sym.solve(gleichungsSystem)
ziel_funktion = f3_proto.subs(
    [(a, koeffizienten.get(a)),
     (b, koeffizienten.get(b)),
     (c, koeffizienten.get(c)),
     (d, koeffizienten.get(d)),
     (e, koeffizienten.get(e)),
     (f, koeffizienten.get(f))])

f3_lambda = sym.lambdify(x, ziel_funktion, 'numpy')
zielxs = npy.arange(20, 40, 1)

zielys = f3_lambda(zielxs)
plt.title("Mit Verbindungstück")
plt.plot(xsStuetzpunkte, xyStuetzpunkte, label='Stützpunkte', marker='o', color='red', linestyle='None')
plt.plot(xsSteigung, ysSteigung, label='Anlaufstrecke f1(x)', color='green')
plt.plot(xsAblaufkurve, xyAblaufkurve, label='Auslaufkurve f2(x)', color='red', linestyle='--')
plt.plot(zielxs, zielys, label="Verbindung f3(x)", color='blue')
plt.xlabel('Strecke horizontal in Meter')
plt.ylabel("Höhe in Meter")
plt.legend()
plt.show()