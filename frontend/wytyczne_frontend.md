# Wytyczne frontend – kalkulator ubezpieczeń (Link4)

Projekt ma na celu stworzenie prostego interfejsu użytkownika do kalkulacji ubezpieczenia komunikacyjnego przy użyciu API Link4.

---

## 🎯 1. Widok: Formularz kalkulacji ubezpieczenia

**Tytuł strony:** Kalkulator ubezpieczenia samochodu

### Pola formularza:

| Nazwa pola           | Typ       | Walidacja                                          | Opis                          |
|----------------------|-----------|----------------------------------------------------|-------------------------------|
| Data rozpoczęcia     | `date`    | Wymagane, nie wcześniejsza niż dziś               | np. `2025-09-15`              |
| Numer rejestracyjny  | `text`    | Wymagane, max 20 znaków, litery i cyfry           | np. `WX12345`                 |
| Typ ubezpieczenia    | `select`  | Wymagane, wartości: OC / OC + AC                  | `11 = OC`, `13 = OC + AC`     |

**Przycisk:** `Oblicz składkę`

---

## 📤 2. Dane wysyłane do backendu

Dane przesyłane w formacie JSON (POST):

```
POST /api/link4/calculate
Content-Type: application/json

{
  "start_date": "2025-09-15",
  "license_plate": "WX12345",
  "insurance_formula": 11
}
```

---

## 📥 3. Dane zwracane przez backend

```
{
  "calculation_id": "7dbb4a9e-8187-43f0-b41c-c570b1f4a8e3",
  "premium": 1234.56
}
```

---

## ✅ 4. Widok po przesłaniu formularza

Po otrzymaniu wyniku wyświetlamy:

- **Nagłówek:** `Twoja składka wynosi: 1 234,56 zł`
- **calculation_id** – mniejszą czcionką (opcjonalnie)
- **Przycisk:** `Nowa kalkulacja`

---

## 🎨 Wytyczne projektowe (dla Figma)

| Element             | Styl |
|---------------------|------|
| Font główny         | Inter, Open Sans, Roboto |
| Kolory              | Stonowane z akcentem dla przycisku |
| Layout              | Jednokolumnowy, responsywny |
| Walidacja błędów    | Komunikaty przy polach z błędami |
| Loader              | Spinner / pasek ładowania po kliknięciu przycisku |

---

## 🧠 Uwagi dodatkowe

- Brak logowania
- Można wdrożyć jako aplikację SPA lub stronę HTML z JS (fetch/axios)
- Możliwość osadzenia jako iframe lub komponent w innej stronie
- Wersja MVP – tylko obsługa Link4