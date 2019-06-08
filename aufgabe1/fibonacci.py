"""
Semesterarbeit Teil 1a: Rekursion mit Python anhand der Fibonacci-Folge
"""
import time


class FibonacciNaiv:
    """
    Teilaufgabe 1: Implementieren Sie eine Python-Funktion fib(n) , die die n-te Fibonacci-Zahl bestimmt.
    f0 := 0
    f1 := 1
    fn := fn-1 + fn-2 fuer n >= 2
    """

    def __init__(self):
        self.__count = 0

    def __fib__(self, n: int):
        """
        Berechnet die n-te Fibonacci-Zahl
        :param n: n-te Fibonacci Zahl die berechnet werden soll
        :return: Resultat der n-te Fibunacci-Zahl
        """
        self.__count += 1

        if n <= 1:
            return n
        else:
            return self.__fib__(n - 1) + self.__fib__(n - 2)

    def fib(self, n: int):
        """
        Berechnet die n-te Fibonacci-Zahl
        :param n: n-te Fibonacci Zahl die berechnet werden soll
        :return: t-te fibunacci-Zahl
        """
        return self.__fib__(n)

    def fib_count(self, n: int):
        """
        Berechnet die n-te Fibunacci-Zahl
        :param n: n-te Fibonacci Zahl die berechnet werden soll
        :return: Tuple (n-te Fibunacci, Ergebnis, Anzahl Aufrufe der Funktioon)
        """
        self.__count = 0
        result = (n, self.__fib__(n), self.__count)
        return result

    def fib_time(self, n: int):
        """
        :param n: n-te Fibonacci Zahl die berechnet werden soll
        :return: Tuple (dauer der Berechnung in NanoSec, fibonacci-Zahl)
        """
        begin = time.time_ns()
        fib = self.fib(n)
        end = time.time_ns()
        duration = end - begin
        return duration, fib


class FibonacciImproved:
    """
    Klasse mit einer verbesserten Implementierung.
    Nutz eine Map um bereits bekannte Fibonacci-Zahlen zu merken
    """
    def __init__(self):
        # berechnete Folgenglieder
        self.knownFib = {0: 0, 1: 1}

    def fib(self, n: int):
        """
        :param n: n-te Fibonacci Zahl die berechnet werden soll
        :return: t-te fibunacci-Zahl
        """
        # schon berechnet? wenn ja aus dem Speicher laden
        if n in self.knownFib:
            return self.knownFib[n]
        else:
            res = self.fib(n - 1) + self.fib(n - 2)
            # resultat in den Speicher laden
            self.knownFib[n] = res
            return res

    def fib_time(self, n: int):
        """
        :param n: n-te Fibonacci Zahl die berechnet werden soll
        :return: Tuple (dauer der Berechnung in NanoSec, fibonacci-Zahl)
        """
        begin = time.time_ns()
        fib = self.fib(n)
        end = time.time_ns()
        duration = end - begin
        return duration, fib


naiv_Fibonacci = FibonacciNaiv()
# Teilaufgabe 1
print("Teilaufgabe 1:")
print(naiv_Fibonacci.fib(3))
print(naiv_Fibonacci.fib(4))
print(naiv_Fibonacci.fib(5))


# Teilaufgabe 2 und 3
print("Teilaufgabe 2 und 3 Anzahl Aufrufe von fib(n) der naiven Implementierung")

print(naiv_Fibonacci.fib_count(3))
print(naiv_Fibonacci.fib_count(4))
print(naiv_Fibonacci.fib_count(5))
print(naiv_Fibonacci.fib_count(6))
print(naiv_Fibonacci.fib_count(7))
print(naiv_Fibonacci.fib_count(8))
print(naiv_Fibonacci.fib_count(9))
print(naiv_Fibonacci.fib_count(10))
print(naiv_Fibonacci.fib_count(11))
print(naiv_Fibonacci.fib_count(12))
print(naiv_Fibonacci.fib_count(13))
print(naiv_Fibonacci.fib_count(14))
print(naiv_Fibonacci.fib_count(15))
print(naiv_Fibonacci.fib_count(16))

# Teilaufgabe 4
print("Teilaufgabe 4 Zeitmessung von fib(n)")
print(naiv_Fibonacci.fib_time(4))
print(naiv_Fibonacci.fib_time(5))
print(naiv_Fibonacci.fib_time(6))
print(naiv_Fibonacci.fib_time(7))
print(naiv_Fibonacci.fib_time(8))
print(naiv_Fibonacci.fib_time(20))
print(naiv_Fibonacci.fib_time(30))

# Teilaufgabe 5
print("Teilaufgabe 5 Zeitmessung von fib(n) mit verbesserter Klasse")
improved_Fibonacci = FibonacciImproved()
print(improved_Fibonacci.fib_time(4))
print(improved_Fibonacci.fib_time(5))
print(improved_Fibonacci.fib_time(6))
print(improved_Fibonacci.fib_time(7))
print(improved_Fibonacci.fib_time(8))
print(improved_Fibonacci.fib_time(20))
print(improved_Fibonacci.fib_time(30))


