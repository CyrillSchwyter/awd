import numpy as npy
import sympy as sym


class NumericCalculatorBase(object):
    """
    Basis einer Numerischen Kalkulation
    """
    def __init__(self, symbol: sym.Symbol):
        """
        Konstruktor
        :param symbol: mit welchem gerechnet wird. meist 'x'
        """
        self.symb = symbol

    def get_symbol(self):
        """
        Gibt das Symbol zurueck
        :return: symbol meist 'x'
        """
        return self.symb

    def eval(self, func: sym.Function, argument):
        """
        Berechnet den Funktionswert
        :param func: funktion die ausgewertet werden soll
        :param argument: wert der der Funktion uebergeben wird
        :return: funktionswert
        """
        result = func.evalf(subs={self.symb: argument})
        return result


class Trapez(NumericCalculatorBase):
    """
    Berechnet die Integration einer Funktion mit Hilfe der Trapezregel
    """
    def __init__(self, symbol: sym.Symbol):
        super().__init__(symbol)

    def calc(self, integrand: sym.Function, a: float, b: float):
        result = sym.Rational(b - a, 2) * (
                super().eval(integrand, a) + super().eval(integrand, b))
        return result


class Sympson(NumericCalculatorBase):
    """
    Berechnet die Integration einer Funktion mit Hilfe der Simpsonschen Regel
    """
    def __init__(self, symbol: sym.Symbol):
        super().__init__(symbol)

    def calc(self, integrand: sym.Function, a: float, b: float):
        """
        Integriert mit Hilfe der Simpsonschen Regel

        :param integrand: funktion die integriert wird
        :param a: untere integrationsvariable
        :param b:
        :return:
        """
        rat_1 = sym.Rational(b - a, 6)
        rat_2 = sym.Rational(a + b, 2)

        result = rat_1 * (
                super().eval(integrand, a) + 4 * super().eval(integrand, rat_2) + super().eval(integrand, b))
        return result


class CircleVolumCalculator(object):
    """
    Berechnet das Volumen eines Kreises mit Hilfe einer Implementierung
    eines NumericCalculators
    """
    def __init__(self, numeric_calculator):
        self.calculator = numeric_calculator
        self.delta_target = 0.2
        self.x = numeric_calculator.get_symbol()
        self.r = sym.Symbol('r')
        self.kreis_function = sym.sqrt(self.r ** 2 - self.x ** 2)

    def set_delta_target(self, delta: float):
        self.delta_target = delta

    def calculate(self, radius: float):
        function = self.kreis_function.subs(self.r, radius)
        a = radius * -1
        b = radius
        width = b - a
        n = int(round(width / self.delta_target))
        # recalculate real delta
        delta = (b - a) / n
        summe = 0
        for i in range(0, n):
            summe = summe + self.calculator.calc(function, a + i * delta, a + (i + 1) * delta)
        return 2 * summe


class CircleRingCalculator(object):

    def __init__(self, circle_volumn_valculator):
        self.calc = circle_volumn_valculator

    def calculate(self, outside_radius: float, inner_radius: float):
        return self.calc.calculate(outside_radius) - self.calc.calculate(inner_radius)

    def set_delta_target(self, delta: float):
        self.calc.set_delta_target(delta)


class DirectRingCalculator(object):

    @staticmethod
    def calculate(outside_radius: float, inner_radius: float):
        return outside_radius ** 2 * npy.pi - inner_radius ** 2 * npy.pi

    def set_delta_target(self, delta: float):
        return


class CalculatorComparator(object):

    def __init__(self, trapez, simpson, direkt_function):
        self.direct_function = direkt_function
        self.simpson = simpson
        self.trapez = trapez

    def calculate(self, outside_radius: float, inner_radius: float, delta: float):
        print('------------------ new Test-Run -------------------------')
        print('Calculate: outside-radius: ' + str(outside_radius) + ' inner-radius: ' + str(inner_radius))
        print('used delta: ' + str(delta))
        self.trapez.set_delta_target(delta)
        self.simpson.set_delta_target(delta)
        direct_value = self.direct_function.calculate(outside_radius, inner_radius)
        simpson_value = self.simpson.calculate(outside_radius, inner_radius)
        trapez_value = self.trapez.calculate(outside_radius, inner_radius)
        print('real-value: '+str(direct_value))
        self.log('trapez', trapez_value, direct_value)
        self.log('simpson', simpson_value, direct_value)

    def log(self, calculator_name: str, calc_value: float, real_value: float):
        diff = real_value - calc_value
        proz_diff = diff / real_value
        print(calculator_name + ' value: ' + str(calc_value) + ' diff: ' + str(diff) + ' proz_diff: ' + str(proz_diff))


volum_calculator_simpson = CircleVolumCalculator(Sympson(sym.Symbol('x')))
print('volumCalculator_with_simpson ' + str(volum_calculator_simpson.calculate(4)))

volum_calculator_trapez = CircleVolumCalculator(Trapez(sym.Symbol('x')))
print('volumCalculator_with_trapez ' + str(volum_calculator_trapez.calculate(4)))

circle_ring_simpson = CircleRingCalculator(volum_calculator_simpson)
circle_ring_trapez = CircleRingCalculator(volum_calculator_trapez)
print(circle_ring_simpson.calculate(4, 10))

comparator = CalculatorComparator(circle_ring_trapez, circle_ring_simpson, DirectRingCalculator())
comparator.calculate(12, 5, 2)
comparator.calculate(12, 5, 1.5)
comparator.calculate(12, 5, 1)
comparator.calculate(12, 5, 0.5)
comparator.calculate(12, 5, 0.2)

comparator.calculate(24, 5, 0.2)
# comparator.calculate(24, 5, 1.5)
# comparator.calculate(24, 5, 1)
# comparator.calculate(24, 5, 0.5)
# comparator.calculate(24, 5, 0.2)
