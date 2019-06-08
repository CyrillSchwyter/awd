import csv


def read_csv_file(csv_file: str):
    """
    List ein CSV-File ein und uebernimmt die Daten in eine zweidimensionale Python-Liste
    :param csv_file:
    :return: zweidimensionale Python-Liste
    """
    result: list = []
    with open(csv_file, newline="") as csvfile:
        rowreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in rowreader:
            result.append(row)
    return result


def convert_to_int(csv_list_with_strings: list):
    """
    Aufbereitung einer zweidimensionalen Python-Liste mit Titel-Zeile und Row-Bezeichnung
    Der Daten-Inhalt wir in Integer-Werte umgewandelt
    :param csv_list_with_strings: alle Daten sind im String-Format auch den Daten-Bereich
    :return: zweidimensionale Pyton-Liste mit Titel-Zeile und Row-Bezeichnung. Daten-Content im Integer-Format
    """
    # spalten-Bezeichnungen hinzufuegen
    result: list = [csv_list_with_strings[0]]

    # Datenbereich aufbereiten -> Ort bleibt String Anzahl Geburten zu Zahl umwandeln
    for row in csv_list_with_strings[1:]:
        data_row: list = [row[0]]
        counts = [int(s) for s in row[1:]]
        data_row.extend(counts)
        result.append(data_row)
    return result


def convert_to_float(csv_list_with_strings: list):
    """
    Aufbereitung einer zweidimensionalen Python-Liste mit Titel-Zeile und Row-Bezeichnung
    Der Daten-Inhalt wir in Integer-Werte umgewandelt
    :param csv_list_with_strings: alle Daten sind im String-Format auch den Daten-Bereich
    :return: zweidimensionale Pyton-Liste mit Titel-Zeile und Row-Bezeichnung. Daten-Content im Integer-Format
    """
    # spalten-Bezeichnungen hinzufuegen
    result: list = [csv_list_with_strings[0]]

    # Datenbereich aufbereiten -> Ort bleibt String Anzahl Geburten zu Zahl umwandeln
    for row in csv_list_with_strings[1:]:
        data_row: list = [row[0]]
        counts = [float(s) for s in row[1:]]
        data_row.extend(counts)
        result.append(data_row)
    return result


def convert_to_dictionary(python_list: list):
    """
    Konvertiert ein zweidimensionale Python-Liste in ein zweidimensionales Dictionary
    Die Keys sind jeweils die Titel-Zeile und die Row-Bezeichnungen (Index[0] einer Daten-Row
    :param python_list: zweidimensionale Python-Liste
    :return: zweidimensionales Dictionary
    """
    columns = python_list[0][1:]
    dict_result = {}
    for i in range(1, len(python_list)):
        ort = python_list[i][0]
        row = python_list[i][1:]
        zipobj = zip(columns, row)
        dict_result[ort] = dict(zipobj)

    return dict_result


file = read_csv_file('totalGeburten.csv')
print(file)

file_with_nums = convert_to_int(file)
print(file_with_nums)

dic = convert_to_dictionary(file_with_nums)
print(dic)



