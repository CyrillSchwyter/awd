import sympy as sym
import numpy as npy


class GreatTrapez(object):

    @staticmethod
    def calculate(integrand: sym.Function, variable: sym.Symbol, a: float, b: float, n: int):
        """
        Numerische Berechnung mittels der grossen Trapez-Formel

        :param integrand:
        :param variable:
        :param a: untere Integrationsgrenze
        :param b: obere Integrationsgrenze
        :param n: anzahl Aufteilungen des Invervalls
        :return: numerische Loesung
        """
        j, i = sym.symbols('j, i')

        xs = j * sym.Rational(b - a, n)

        summation = sym.summation(integrand.subs(variable, xs.subs(j, i)), (i, 1, n - 1))

        x0 = integrand.subs(variable, xs.subs(j, 0))
        xn = integrand.subs(variable, xs.subs(j, n))
        bruch = sym.Rational(b - a, 2 * n)
        return bruch * (x0 + xn + 2 * summation)


class GreatSimpson(object):

    @staticmethod
    def calculate(integrand: sym.Function, variable: sym.Symbol, a: float, b: float, n: int):
        """
        Numerische Berechnung mittels der grossen Simpson-Formel

        :param integrand:
        :param variable:
        :param a: untere Integrationsgrenze
        :param b: obere Integrationsgrenze
        :param n: anzahl Aufteilungen des Invervalls
        :return: numerische Loesung
        """
        j, i = sym.symbols('j, i')

        xs = j * sym.Rational(b - a, 2 * n)

        x0 = integrand.subs(variable, xs.subs(j, 0))
        xn = integrand.subs(variable, xs.subs(j, 2 * n))
        bruch = sym.Rational(b - a, 6 * n)
        summe_1 = sym.summation(integrand.subs(variable, xs.subs(j, 2 * i)), (i, 1, n - 1))
        summe_2 = sym.summation(integrand.subs(variable, xs.subs(j, 2 * i - 1)), (i, 1, n))
        return bruch * (x0 + xn + 2 * summe_1 + 4 * summe_2)


class CalculationSympy(object):

    @staticmethod
    def calculate(integrand: sym.Function, variable: sym.Symbol, a: float, b: float, n: int):
        """
        Integration mittels sympy

        :param integrand:
        :param variable:
        :param a: untere Integrationsgrenze
        :param b: obere Integrationsgrenze
        :param n: wird nicht benoetigt
        :return: numerische Loesung
        """
        integrate = sym.integrate(integrand, (variable, a, b))
        return integrate


class CyrcleRingVolumnCalculator(object):

    @staticmethod
    def calculate(calculation_strategy, r: float, d: float, n: int):
        x = sym.Symbol('x')
        halbkreis = sym.sqrt(r ** 2 - x ** 2)
        versatz = sym.Rational(d, 2) + r
        oberer_halb_kreis = (halbkreis + versatz) ** 2
        unterer_halb_kreis = (-1 * halbkreis + versatz) ** 2
        oben = 2 * npy.pi * calculation_strategy.calculate(oberer_halb_kreis, x, 0, r, n)
        unten = 2 * npy.pi * calculation_strategy.calculate(unterer_halb_kreis, x, 0, r, n)
        result = oben - unten
        return result.evalf()


cyrcleCalculator = CyrcleRingVolumnCalculator()

trapez_result = cyrcleCalculator.calculate(GreatTrapez(), 10, 20, 20)
print('trapez:')
print(trapez_result)

sympson_result = cyrcleCalculator.calculate(GreatSimpson(), 10, 20, 20)
print('sympson:')
print(sympson_result)

sympy_result = cyrcleCalculator.calculate(CalculationSympy(), 10, 20, 20)
print('numpy:')
print(sympy_result)
