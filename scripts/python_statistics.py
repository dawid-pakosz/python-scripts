import statistics

from openpyxl.worksheet.print_settings import PRINT_AREA_RE

# dataset
time =  [12,15,14,10,22,15,19,14,16,120,17,15,13,16,14]

from django.template.context_processors import static

# Calculate the harmonic mean of a dataset
harmonic_mean = statistics.harmonic_mean(time)
print(f'srednia harmoniczna: {harmonic_mean}')

# Jedziesz do pracy:
# Tam: 60 km/h (przez 10 km)
# Z powrotem: 30 km/h (przez te same 10 km)

# Pytanie: Jaka była średnia prędkość?
#   Zwykła średnia mówi: (60 + 30) / 2 = 45 km/h ← ŹLE!
#   Średnia harmoniczna mówi: 40 km/h ← DOBRZE!

# Dlaczego?
# Bo spędziłeś więcej czasu jadąc wolniej (30 km/h), więc to bardziej wpłynęło na całkowitą prędkość!


# Calculate the arithemtics mean (average) of a dataset
mean = statistics.mean(time)
print(f'srednia arytmetyczna: {mean}')          #szybka średnia (ale uważaj na błędy w danych)

# Calculate the median of a dataset
median = statistics.median(time)
print(f'mediana: {median}')                     #stabilna 'typowa wartość'

# Calculate the median of grouped data
median_grouped = statistics.median_grouped(time)
print(f'mediana grupowa: {median_grouped}')     # Dla danych już w przedziałach (10-15, 15-20, etc.)

# Calculate the high median of a dataset
median_high = statistics.median_high(time)
print(f'Mediana wysoka: {median_high}')


# Calculate the low median of a dataset
median_low = statistics.median_low(time)
print(f'Mediana niska: {median_low}')

# Find the mode of a dataset
mode_dataset = statistics.mode(time)
print(f'wartość, która pojawia się najczęsciej: {mode_dataset}')        #'co najczęściej' (fajne do dashboardów)

# Calculate the sample standard deviation of a dataset
standard_deviation = statistics.stdev(time)
print(f'Odchylenie standardowe: {standard_deviation}')  #Małe odchylenie = stabilny proces | Duże = nieprzewidywaln


# Calculate the sample variance of a dataset
variance_dataset = statistics.variance(time)
print(f'Odchylenie standardowe do kwadratu: {variance_dataset}')


# Calculate the quantile of a dataset
quantile_dataset = statistics.quantiles(time)
print(f'kwantyle: {quantile_dataset}')


# ==================================================================================================
# ==================================================================================================
# 1. Monitoring wydajnosci makr/procesów
#   - mean():        sredni czas wykonania
#   - median():      typowy czas
#   - stdev():       czy proces jest stabilny

# 2. Raportowanie:
#   - quantiles(n=20[18]):       95% raportów wykonuje się w X sekund
#   - mode():                    Najczęstrzy czas to X sekund

# 3. Wykrywanie problemów
#   - stdev():                  duża wartość, szukaj co spowalnia proces
#   - mean() vs median():       duża róznica = masz outliers

# 4. SLA i KPI:
#   - quantiles():              90% transakcji 2 < 30 sek
#   - median()                  mediana dla wyciągnięcia wniosków lepsza niż średnia mean()
# ==================================================================================================
# ==================================================================================================








