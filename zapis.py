import csv
import random

def zapisz_do_csv(nazwa_pliku):
    # Nagłówki do pliku CSV
    naglowki = ['Model', 'Wynik', 'Czas']
    
    # Generujemy losową linię danych
    model = random.choice(['A', 'B', 'C'])  # Wybór losowego modelu
    wynik = random.randint(0, 1000)          # Losowy wynik z zakresu 0-1000
    czas = random.randint(0, 1000)           # Losowy czas z zakresu 0-1000
    
    # Zapisujemy do pliku CSV
    with open(nazwa_pliku, mode='w', newline='', encoding='utf-8') as plik_csv:
        writer = csv.writer(plik_csv, delimiter=';')
        
        # Zapisujemy nagłówki
        writer.writerow(naglowki)
        
        # Zapisujemy losowe dane
        writer.writerow([model, wynik, f"{czas}s"])  # Dodajemy 's' do czasu

    print(f"Zapisano plik {nazwa_pliku} z danymi: Model={model}, Wynik={wynik}, Czas={czas}s")

# Przykład użycia
zapisz_do_csv('Dane.csv')
