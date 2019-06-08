import matplotlib.pyplot as plt
import numpy as npy
from aufgabe1 import csvread as csvread

# Funktionsgraph Lineare Funktion
xs = npy.arange(-1, 10, 0.1)  # X-Achsenwerte -1, -0.9, -0.8, ... 10
ys = -0.5 * xs + 3  # Funktionswerte fuer jedes X berechnen

plt.plot(xs, ys, color='b', linewidth=2, label="f(x) = -0.5x + 3")
plt.title('Lineare Funktion')
plt.xlabel('X-Achse')
plt.ylabel('y = f(x)')
# X Werte der Achsenbeschriftung festlgen
plt.xticks(npy.arange(-1, 10, 1))
# Abszisse und Ordinate dicher und schwarz zeichnen
plt.axhline(linewidth='2', color='black')
plt.axvline(linewidth='2', color='black')
# Koordinaten Gitter anzeigen
plt.grid(True)
# Legende anzeigen
plt.legend()
# Zeichnen des Plot
plt.show()

# Funktionsgraph Quadratische Funktion
xs = [x for x in range(-100, 100)]
ys = [pow(x, 2) for x in xs]

plt.plot(xs, ys, color='b', label='x^2', marker='o')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quadratische Funktion')
plt.legend()
plt.show()

# Wachstunmsfunktion
xs = [x * 2 for x in range(-25, 25)]
ys = [pow(1.1, x) for x in xs]
plt.plot(xs, ys, color='g', label='1.1^x')
plt.title('Wachstungsmfunktion')
plt.legend()
plt.show()

# ---------------- Teilaufgabe Mehrere Funktionsgraphen --------------------------------

# mehrere Sinusfunktionen in einem Plot
# Funktionen
xs = npy.arange(0, 5, 0.1)
fxs = npy.sin(xs)
gxs = 2 * npy.sin(xs)
hxs = npy.sin(xs + 1)
plt.plot(xs, fxs, 'm', label='f(x) = sin(x)')
plt.plot(xs, gxs, 'b', label='g(x) = 2 * sin(x)')
plt.plot(xs, hxs, 'g', label='g(x) = sin(x + 1)')

# Gestaltung
# Abszisse und Ordinate dicher und schwarz zeichnen
plt.axhline(linewidth='2', color='black')
plt.axvline(linewidth='2', color='black')
plt.title('Sinus-Funktionen')
plt.grid(True)
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.legend()
plt.show()


# -------------------- Ende Teilaufgabe mehrere Funktionsgraphen --------------------------------


#  ------------------- Graphik auf CSV eingelesen ----------------------------

def get_ticks(counts_values: int, amount_statistics: int):
    """
    Berechnet die X-Achsenpositionen fuer die Balken eines Balkendiagrammes
    :param counts_values: werte pro angezeigte Statisik
    :param amount_statistics: anzahl verschie
    :return: zweidimensionales array mit den positionen fuer die balken
    """
    result = []
    for x in range(amount_statistics):
        newlist = []
        result.append(newlist)
    div = -1
    counts_divider: int = counts_values * amount_statistics
    for x in range(counts_divider):
        div = (div + 1) % amount_statistics
        result[div].append(x)

    return result


def geburen_darstellen(anzahl_vorjahre: int, cantone: [], colors: []):
    """
    Zeichnet ein Balkendiagramm der Geburten pro Jahr der ausgewaehlten Kantone und
    der gewaehlten Vorjahre

    :param anzahl_vorjahre:
    :param cantone:
    :param colors:
    :return:
    """
    # Breite der Anzeige dynaisch bestimmen
    breite = 0.4 * len(cantone) * anzahl_vorjahre
    plt.figure(figsize=(breite, 4))
    plt.title('Geburten pro Jahr')
    plt.ylabel('Anzahl Geburten')

    # Daten mittels entwickelter Funktion in PVA1 auslesen
    file_with_nums = csvread.convert_to_int(csvread.read_csv_file('totalGeburten.csv'))
    # Balkenbezeichnungen auslesen (Jahre die angezeigt werden)
    jahre = file_with_nums[0][-anzahl_vorjahre:]
    # x positionen Berechnen fuer die anzahl vergleich Balken
    ticks = get_ticks(len(jahre), len(cantone))
    # Der mittlere Balken soll die Jahresbeschriftung ahben (bei gerade ist es halte der mehr rechts)
    xlabel_pos: int = int(len(cantone) / 2)
    plt.xticks(ticks[xlabel_pos], jahre, rotation=90)

    # Zeichnen der Balken
    for x in range(len(cantone)):
        # Bezeichnungen der Kantone
        plt.bar(ticks[x], file_with_nums[cantone[x]][-anzahl_vorjahre:], label=file_with_nums[cantone[x]][0],
                align='center',
                width=0.8,
                color=colors[x])
    # Anzeige der Legende
    plt.legend()
    # Jetzt gehts los -> Diagram wird gezeichnet
    plt.show()


geburen_darstellen(5, [5, 6, 7, 3, 2], ['b', 'g', 'y', 'r', 'm'])


# Tortendiagramm
# Handelspartner in Europa der Schweiz und ihr Exportvolumen
def euro_handelspartner_der_schweiz(jahr: str):
    plt.figure(figsize=(8, 8))
    plt.title('Export der Schweiz in europaeiche Laender im Jahr {0}'.format(jahr))
    # Daten mittels entwickelter Funktion in PVA1 auslesen
    file_with_nums = csvread.convert_to_int(
        csvread.read_csv_file('export_handelspartner_europa.csv'))
    # Index zum angefragten Jahr suchen
    index_land = file_with_nums[0].index(jahr)
    # labels -> laender -> erste Spalte des zweidimensionalen arrays
    labels = [x[0] for x in file_with_nums[1:]]
    # Daten -> wert pro land -> werte des gesuchten index_land
    daten = [x[index_land] for x in file_with_nums[1:]]

    # Zeichnen des Kuchens
    plt.pie(daten, labels=labels, colors=['g', 'm',
                                          'b', 'olive',
                                          'y', 'b',
                                          'r', 'c',
                                          'navy', 'lime', 'cyan'])
    plt.show()


# Zeichnen des Kuchendiagrammes fuer das Jahr 2017
euro_handelspartner_der_schweiz('2017')

plt.hist([9, 12, 12, 12, 8, 8], [6, 10, 12, 14])
plt.show()


def historgam_tagestemperaturen(jahr: str):
    # Histogramm maximale Temperatur der Messstation Dozwil
    # Daten einlesen und in werte in float umwandeln
    plt.figure(figsize=(8, 4))
    plt.title('Histogramm max. Tagesdeperaturen Gemeinde Dozwil Jahr {}'.format(jahr))
    plt.xlabel('Temperaturen in ℃')
    plt.ylabel('Anzahl Tage')
    messdaten = csvread.convert_to_float(
        csvread.read_csv_file('maxtempdatendozwil.csv'));
    # nur daten eines jahres weriter verarbeiten
    daten_jahr = list(filter(lambda x: jahr in x[0], messdaten))
    # maximale Tageadeperaturen
    max_tages_temp = [x[1] for x in daten_jahr]
    max_tages_temp_sorted = list(sorted(max_tages_temp))
    temp_klassen = npy.array(range(-4, 32, 1))
    plt.hist(max_tages_temp_sorted, temp_klassen, color='g')
    plt.show()


historgam_tagestemperaturen('2014')



# Mehrere Graphen in einem Plot
xs = [x for x in range(-10, 10)]
# Lineare Funktion 1
fx = [0.5 * x + 3 for x in xs]
plt.plot(xs, fx, 'g-.', label='0.5x + 3')
#  Lineare Funktion 2
gx = [-1 * x + 7 for x in xs]
# plt.plot(xs, gx, label='-1x + 7', marker='o', color='green')
plt.title('Strichpunktierte Linie')
plt.legend()

plt.show()
