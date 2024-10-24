import csv

def odczytaj_csv(nazwa_pliku):
    suma_czasu = 0
    
    try:
        with open(nazwa_pliku, mode='r', newline='', encoding='utf-8') as plik_csv:
            reader = csv.reader(plik_csv, delimiter=';')
            
            # Pomijamy nagłówki
            next(reader)
            
            # Przetwarzamy kolejne wiersze
            for wiersz in reader:
                model = wiersz[0]  # Model z pierwszej kolumny
                czas = int(wiersz[2].replace('s', ''))  # Usuwamy 's' i konwertujemy na liczbę
                
                # Sumujemy czas tylko dla modelu 'A'
                if model == 'A':
                    suma_czasu += czas

        print(f"Suma czasu dla modelu A w pliku {nazwa_pliku}: {suma_czasu}s")
        return suma_czasu
    
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie istnieje!")
        return 0
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return 0

# Przykład użycia
odczytaj_csv('Dane.csv')
