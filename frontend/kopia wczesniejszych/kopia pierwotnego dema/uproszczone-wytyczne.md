Kalkulator Ubezpieczeń – Wytyczne Frontendowe
(Integracja z API Link4)

1. Widok: Formularz Kalkulacji
Tytuł strony: Kalkulator ubezpieczenia samochodu
Pola formularza:
Pole
Typ
Walidacja
Przykład
Uwagi
Data rozpoczęcia
date
Wymagane, ≥ dzisiejsza data
2025-09-15
Format: RRRR-MM-DD
Numer rejestracyjny
text
Wymagane, max 20 znaków (A-Z, 0-9)
WX12345
Bez spacji/znaków specjalnych
Typ ubezpieczenia
select
Wymagane, tylko: OC lub OC + AC
OC
Wartości API: 11 (OC), 13 (OC+AC)

Przycisk: "Oblicz składkę" (primary, akcentowany kolor)

2. Komunikacja z Backendem
Żądanie (POST)



POST /api/link4/calculate
Content-Type: application/json

{
  "start_date": "2025-09-15",
  "license_plate": "WX12345",
  "insurance_formula": 11  // 11 = OC, 13 = OC + AC
}



Odpowiedź (JSON)



json



{
  "calculation_id": "7dbb4a9e-8187-43f0-b41c-c570b1f4a8e3",
  "premium": 1234.56  // Kwota w PLN
}





3. Widok Wyniku Kalkulacji
Po pomyślnym obliczeniu wyświetl:
Nagłówek: "Twoja składka wynosi: 1 234,56 zł" (kwota sformatowana z przecinkiem jako separator tysięcy)
ID kalkulacji: 7dbb4a9e-... (małą czcionką, opcjonalnie)
Przycisk: "Nowa kalkulacja" (reset formularza)

4. Wytyczne Projektowe
Element
Szczegóły
Czcionka
Inter / Open Sans / Roboto (fallback)
Kolorystyka
Stonowana (szarości, biele) + akcent dla przycisku (np. niebieski)
Układ
Jednokolumnowy, responsywny (mobile-first)
Walidacja błędów
Komunikaty pod polami (czerwony tekst)
Loader
Spinner podczas ładowania (po kliknięciu przycisku)


5. Uwagi Techniczne
Brak autentykacji – aplikacja działa bez logowania.
Minimalna wersja (MVP) – tylko integracja z API Link4.
Możliwości wdrożenia:
Jako SPA (React/Vue) lub strona HTML + JS (fetch/axios).
Jako iframe lub komponent w istniejącej stronie.
Formatowanie kwoty: Użyj Intl.NumberFormat dla poprawnego wyświetlenia PLN:


javascript



  new Intl.NumberFormat('pl-PL', { style: 'currency', currency: 'PLN' }).format(1234.56)
  // Wynik: "1 234,56 zł"
  





6. Przykładowy Kod Frontendu (HTML/JS)
HTML



html



<form id="insuranceForm">
  <h1>Kalkulator ubezpieczenia samochodu</h1>

  <label for="startDate">Data rozpoczęcia:</label>
  <input type="date" id="startDate" required min="@minDate">

  <label for="licensePlate">Numer rejestracyjny:</label>
  <input type="text" id="licensePlate" required maxlength="20" pattern="[A-Za-z0-9]+">

  <label for="insuranceType">Typ ubezpieczenia:</label>
  <select id="insuranceType" required>
    <option value="11">OC</option>
    <option value="13">OC + AC</option>
  </select>

  <button type="submit">Oblicz składkę</button>
  <div id="loader" class="hidden">Ładowanie...</div>
</form>

<div id="result" class="hidden">
  <h2>Twoja składka wynosi: <span id="premium"></span></h2>
  <p class="small">ID kalkulacji: <span id="calculationId"></span></p>
  <button id="newCalculation">Nowa kalkulacja</button>
</div>



JavaScript (Fetch API)



javascript



document.getElementById('insuranceForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const loader = document.getElementById('loader');
  const form = e.target;

  // Pokazuj loader
  loader.classList.remove('hidden');

  try {
    const response = await fetch('/api/link4/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        start_date: form.startDate.value,
        license_plate: form.licensePlate.value,
        insurance_formula: parseInt(form.insuranceType.value)
      })
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.detail);

    // Wyświetl wynik
    document.getElementById('premium').textContent =
      new Intl.NumberFormat('pl-PL', { style: 'currency', currency: 'PLN' }).format(data.premium);
    document.getElementById('calculationId').textContent = data.calculation_id;
    document.getElementById('result').classList.remove('hidden');
    form.reset();
  } catch (error) {
    alert(`Błąd: ${error.message}`);
  } finally {
    loader.classList.add('hidden');
  }
});

// Reset formularza
document.getElementById('newCalculation')?.addEventListener('click', () => {
  document.getElementById('result').classList.add('hidden');
});





7. Mockupy (Figma/Adobe XD)
Sugestie układu:
Formularz:
Pola w pionie, etykiety nad polami.
Przycisk na dole, wyrównany do lewej.
Wynik:
Kwota w dużym foncie, wyróżniona kolorem.
ID kalkulacji w szarym tekście (12px).


