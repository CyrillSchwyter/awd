import sympy as sym
import numpy as npy
import matplotlib.pyplot as plt

# Verwendetes Modul fuer die Erstellung von Lambda-Funktionen
# aus mathematischen Funktionen
module = 'numpy'


def taylor_1(f, x0, symbol: sym.Symbol):
    """
    Berechnet T1 (Taylorpolynom ersten Grades)
    Entspricht der Tangente durch Punkt x0 der Funktion f
    :param f: funktion die angenaehert weden soll
    :param x0: Entwicklungstelle
    :param symbol: verwendetes Sympol z.B. x
    :return: taylorpolynom ersten Grades als lambda-Funktion
    """
    # f.subs(symbol, x0) ersetzt das symbol mit dem konkreten Wert
    # sym.diff errechnet die ableitung der funktion
    fx = f.subs(symbol, x0) + sym.diff(f, symbol).subs(symbol, x0) * (x - x0)
    # wandelt die expression in einen Lambda-Ausdruck um x -> y
    return sym.lambdify(symbol, fx, module)


# x als Symbol definieren fuer die Funktionsgleichungen
x = sym.symbols('x')
# Punkte auf der X-Achse (von -1 bis 5 in 0.1er Schritten
xs = npy.arange(-1, 8, 0.1)

# Definition der Funktion: f(x) = (x − 2)3 + 5
f1 = sym.sin(x)
# f1 = (x - 2) ** 3 + 5

# Funktion umwandeln in eine Lambda-Funktion
# (ermoeglicht das einfache berechnen des Funktionswertes)
f1_lambda = sym.lambdify(x, f1, 'numpy')
plt.plot(xs, f1_lambda(xs), label='f(x) = (x - 2)^3 + 5', color='green')
plt.plot(xs, taylor_1(f1, 1, x)(xs), 'r--', label='Erstes Taylorpolynom')
plt.title('Beispielfunktion ')
plt.legend()
plt.show()


def taylor_n(f, x0, n: int, symbol: sym.Symbol):
    """
    Berechnet Tn (Taylorpolynom n-ten Grades)
    :param f: funktion die angenaehert weden soll
    :param x0: Entwicklungstelle
    :param n: n-Taylorpolynom
    :param symbol: verwendetes Sympol z.B. x
    :return: taylorpolynom ersten Grades als lambda-Funktion
    """
    # f.subs(symbol, x0) ersetzt das symbol mit dem konkreten Wert
    # sym.diff errechnet die ableitung der funktion
    fx = f.subs(symbol, x0)
    for k in range(1, n + 1):
        fx = fx + sym.Rational(sym.diff(f, symbol, k).evalf(subs={symbol: x0}),
                               sym.factorial(k)) * (x - x0) ** k

    # wandelt die expression in einen Lambda-Ausdruck um x -> y
    return sym.lambdify(symbol, fx, module)


plt.ylim(-2, 2)
plt.plot(xs, f1_lambda(xs), label='f(x) = (x - 2)^3 + 5', color='green')
plt.plot(xs, taylor_n(f1, 1, 1, x)(xs), 'r--', label='Taylorpolynom 1ten Grades')
plt.plot(xs, taylor_n(f1, 1, 2, x)(xs), 'b--', label='Taylorpolynom 2ten Grades')
plt.plot(xs, taylor_n(f1, 1, 3, x)(xs), 'y--', label='Taylorpolynom 3ten Grades')
plt.plot(xs, taylor_n(f1, 1, 10, x)(xs), 'y--', label='Taylorpolynom 3ten Grades')
# plt.plot(xs, taylor_n(f1, 1, 3, x)(xs), 'm--', label='Taylorpolynom 4ten Grades')
plt.title('Beispielfunktion ')
plt.legend()
plt.show()
