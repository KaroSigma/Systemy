def analizuj_tabele_decyzyjna(nazwa_pliku, separator=','):
    wiersze = []
    
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            for linia in plik:
                linia = linia.strip()
                if linia:
                    wiersze.append(linia.split(separator))
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {nazwa_pliku}")
        return

    if not wiersze:
        print("Plik jest pusty.")
        return

    liczba_kolumn = len(wiersze[0])
    statystyki_kolumn = [{} for _ in range(liczba_kolumn)]

    for wiersz in wiersze:
        for i in range(liczba_kolumn):
            wartosc = wiersz[i].strip()
            
            if wartosc in statystyki_kolumn[i]:
                statystyki_kolumn[i][wartosc] += 1
            else:
                statystyki_kolumn[i][wartosc] = 1

    print(f"Wyniki analizy pliku: {nazwa_pliku} ---")
    for i in range(liczba_kolumn):
        nazwa_kolumny = f"Atrybut {i + 1}" if i < liczba_kolumn - 1 else "Decyzja (ostatnia kolumna)"
        
        unikalne_wartosci = list(statystyki_kolumn[i].keys())
        liczba_unikalnych = len(unikalne_wartosci)
        
        print(f"\n{nazwa_kolumny}:")
        print(f"Możliwe wartości (łącznie {liczba_unikalnych}): {', '.join(unikalne_wartosci)}")
        print("Liczba wystąpień: ")
        
        for wartosc, ilosc in statystyki_kolumn[i].items():
            print(f"    * '{wartosc}': {ilosc} raz(y)")

analizuj_tabele_decyzyjna('gielda.txt', separator=',')