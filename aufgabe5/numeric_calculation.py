import sympy as sym
import numpy as npy
from scipy import random


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

        xj = j * sym.Rational(b - a, n)

        bruch = sym.Rational(b - a, 2 * n)
        x0 = integrand.subs(variable, xj.subs(j, 0))
        xn = integrand.subs(variable, xj.subs(j, n))

        summe = sym.summation(integrand.subs(variable, xj.subs(j, i)), (i, 1, n - 1))

        return bruch * (x0 + xn + 2 * summe)


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

        bruch = sym.Rational(b - a, 6 * n)
        x0 = integrand.subs(variable, xs.subs(j, 0))
        xn = integrand.subs(variable, xs.subs(j, 2 * n))

        summe_1 = sym.summation(integrand.subs(variable, xs.subs(j, 2 * i)), (i, 1, n - 1))
        summe_2 = sym.summation(integrand.subs(variable, xs.subs(j, 2 * i - 1)), (i, 1, n))

        return bruch * (x0 + xn + 2 * summe_1 + 4 * summe_2)


class MonteCarlo(object):

    @staticmethod
    def calculate(integrand: sym.Function, variable: sym.Symbol, a: float, b: float, n: int):
        """
        Numerische Berechnung mittels der Monte-Carlo Methode

        :param integrand:
        :param variable:
        :param a: untere Integrationsgrenze
        :param b: obere Integrationsgrenze
        :param n: anzahl Zufallszahlen
        :return: numerische Loesung
        """

        zufalls_zahlen = npy.random.uniform(a, b, n)

        bruch = sym.Rational(b - a, n)

        summe = 0
        for k in zufalls_zahlen:
            summe = summe + integrand.subs(variable, k)

        return bruch * summe


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


class CyrcleRingVolumn(object):

    @staticmethod
    def calculate(calculation_strategy, r: float, d: float, n: int):
        """

        :param calculation_strategy: Berechnungsstrategy
        :param r: Radius des Kreisringes
        :param d: Innendurchmesser (Loch durch das man sehen kann)
        :param n: Anzahl Unterteilungen des Intervalls fuer die Berechnung
        :return: Volumen des Kreisringes
        """
        x = sym.Symbol('x')
        halbkreis = sym.sqrt(r ** 2 - x ** 2)
        versatz = sym.Rational(d, 2) + r
        oberer_halb_kreis = (halbkreis + versatz) ** 2
        unterer_halb_kreis = (-1 * halbkreis + versatz) ** 2
        oben = 2 * npy.pi * calculation_strategy.calculate(oberer_halb_kreis, x, 0, r, n)
        unten = 2 * npy.pi * calculation_strategy.calculate(unterer_halb_kreis, x, 0, r, n)
        result = oben - unten
        return result.evalf()


def run_test(radius: float, inner_durchmesser: float, intervalls: int):
    cyrcle_calculator = CyrcleRingVolumn()
    print("---------------- Next Test ------------------")
    print("testlauf mit: r = {} d = {} n = {}".format(radius, inner_durchmesser, intervalls))
    trapez_result = cyrcle_calculator.calculate(GreatTrapez(), radius, inner_durchmesser, intervalls)
    print('Resultat mit Great-Trapez:')
    print(trapez_result)
    sympson_result = cyrcle_calculator.calculate(GreatSimpson(), radius, inner_durchmesser, intervalls)
    print('Resultat mit Great-Simpson:')
    print(sympson_result)
    sympy_result = cyrcle_calculator.calculate(CalculationSympy(), radius, inner_durchmesser, intervalls)
    print('Resultat mit Sympy:')
    print(sympy_result)
    sympy_result = cyrcle_calculator.calculate(MonteCarlo(), radius, inner_durchmesser, intervalls)
    print('Resultat mit Monte Carlo:')
    print(sympy_result)
    print("\n")


# run_test(5, 20, 10)
# run_test(5, 20, 20)
run_test(5, 20, 30)
#
# run_test(10, 20, 10)
# run_test(10, 20, 20)
# run_test(10, 20, 30)
#
# run_test(10, 40, 30)


# # Monte Carlo
# ring_volum = CyrcleRingVolumn()
# monte_carlo = MonteCarlo()
# result = ring_volum.calculate(monte_carlo, 5, 20, 20)
# print('monte Carlo: {}'.format(result))
