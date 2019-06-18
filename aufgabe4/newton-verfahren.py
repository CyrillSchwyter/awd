import sympy as sym
import numpy as npy
import matplotlib.pyplot as plt

module = 'numpy'


class NewtonCalculateExeption(Exception):
    def __init__(self, start: float):
        self.value = "Keine Loesung mit Startpunkt: " + str(start)

    def __str__(self):
        return repr(self.value)


def printfloat(number: float):
    rounded = round(number, 3)
    return str(rounded)


class NewtonVerfahren(object):
    """
    Fuer die Berechnung einer Nullstelle einer Funktion
    mit dem Newton-Verfahren
    """
    __precision: float
    __max_tries: int
    __symbol: sym.Symbol
    __doVisual: bool
    __tries: int
    __ableitung: sym.Function
    __funktion: sym.Function

    def __init__(self, symbol: sym.Symbol):
        """
        :param symbol: Beispiel x
        """
        self.__precision = 0.01
        self.__max_tries = 10
        self.__tries = 0
        self.__symbol = symbol
        self.__doVisual = False
        self.__range: tuple = (-10, 10)

    def set_visualization(self, visual: bool):
        """
        aktiviert die Visualisierung
        :param visual:
        """
        self.__doVisual = visual

    def set_max_tries(self, tries: int):
        self.__max_tries = tries

    def set_precision(self, precision: float):
        self.__precision = precision

    def set_visualization_range(self, start: int, end: int):
        """
        X-Bereich fuer die Visualisierung
        :param start:
        :param end:
        """
        self.__range = (start, end)

    def solve(self, f: sym.Function, start: float):
        """
        Sucht den nachsten Nullpunkt der uebergebenen Funktion vom gegebenen Starpunkt aus
        :param f: funktion
        :param start: startpunkt
        :return: duple (ergebnis, abweichung zu 0)
        """
        if self.__doVisual:
            self.__visualisiere(f, style='r', description='f(' + str(self.__symbol) + ')=' + str(f))

        self.__ableitung = f.diff(self.__symbol)
        self.__funktion = f
        self.__tries = 0
        current_point = start
        current_div = abs(f.evalf(subs={self.__symbol: current_point}))
        # wiederholen bis genauigkeit erreicht oder das Maximum der Versuche erreicht ist
        while current_div > self.__precision and self.__tries < self.__max_tries:
            current_point = self.__do_newton(f, current_point)
            result = self.__evaluate(current_point)
            current_div = abs(result)
            self.__tries = self.__tries + 1

        if self.__doVisual:
            self.__visual_result()
        return current_point, current_div

    def __do_newton(self, f: sym.Function, point: float):
        """
        :param f: Funktion deren Nullpunkt gesucht wird
        :param point: Punkt zu der die Tangente gesucht wird
        :return: Nullpunkt von der Tangente
        """
        # Tangente erstellen
        tangente: sym.Function = f.evalf(subs={self.__symbol: point}) + self.__ableitung.evalf(
            subs={self.__symbol: point}) * (self.__symbol - point)

        # Gleichung fuer die Bestimmung des Nullpunktes aufstellen
        gleichung = sym.Eq(tangente, 0)
        # Gleichung aufloesen
        result = sym.solve(gleichung)
        # Nullstelle gefunden
        if len(result) > 0:
            a = result[0]
            # [optionale] visualisierung des Zwischenergebnisses
            if self.__doVisual:
                text = 'Nr:' + str(self.__tries + 1) + " Xn:" + printfloat(
                    a) + " Abw: " + printfloat(self.__evaluate(a))
                self.__visualisiere(tangente, style='--', description=text)
            return a
        # Keine Nullstelle gefunden -> Verfahren ist gescheitert
        else:
            exeption = NewtonCalculateExeption(point)
            if self.__doVisual:
                plt.text(0, 0, exeption.value)
                plt.show()
            raise exeption

    def __evaluate(self, x_value):
        """
        Berechnet den Funktionswert
        :param x_value:
        :return: y wert
        """
        result = self.__funktion.evalf(subs={self.__symbol: x_value})
        return result

    def __visual_result(self):
        """
        Visualisiert das Ergebnis
        :return:
        """
        plt.ylim(self.__range[0] - 10, self.__range[1])
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.grid(True)
        plt.legend()
        plt.show()

    def __visualisiere(self, function: sym.Function, style: str = 'b--', description: str = ' '):
        """
        Visualisiert eine Funktion
        :param function: die visualisiert werden soll
        :param style: Style fuer die visualisierung
        :param description: beschriftung
        """
        xs = npy.arange(self.__range[0], self.__range[1], 0.1)
        function_as_lambda = sym.lambdify(self.__symbol, function, module)
        plt.plot(xs, function_as_lambda(xs), style, label=description)


# Testen
x = sym.symbols('x')
newton = NewtonVerfahren(x)
fx: sym.Function = -x ** 2 + 4
newton.set_visualization(True)
result = newton.solve(fx, 1)
print(result)

# x = sym.symbols('x')
# newton = NewtonVerfahren(x)
# fx: sym.Function = -x ** 2 + 4
# newton.set_visualization(True)
# result = newton.solve(fx, 0)
# print(result)

newton.set_precision(0.01)
newton.set_visualization_range(-5, 5)
solve = newton.solve(fx, 0.5)
print(solve)

x = sym.symbols('x')
newton = NewtonVerfahren(x)
f2: sym.Function = (x - 3) ** 5 - 10
newton.set_max_tries(14)
newton.set_visualization(True)
res = newton.solve(f2, 1)
print(res)
