
# Cecilka: 45 000 Kč hrubého -> čistá mzda přibližně 34 980 Kč
# Evžen:   52 000 Kč hrubého -> čistá mzda přibližně 41 020 Kč
# Celkem:  cca 76 000 Kč čistého 

# zustatek 29 890 Kč celkem -> rozdělíme podle poměru čistých mezd
import pandas as pd
# ciste mzdy
mzda_start_cecilka = 34980
mzda_start_evzen = 41020
uspora_spolecna = 29890
poměr_c = mzda_start_cecilka / (mzda_start_cecilka + mzda_start_evzen)
poměr_e = 1 - poměr_c


uspora_cecilka_start = uspora_spolecna * poměr_c
uspora_evzen_start = uspora_spolecna * poměr_e

# pomer uspory ke mzdam
podil_c = uspora_cecilka_start / mzda_start_cecilka
podil_e = uspora_evzen_start / mzda_start_evzen

# rocni prirustek mzdy z regresních modelů
rust_c = 2003
rust_e = 2624


mzdy_c = []
uspory_c = []
mzdy_e = []
uspory_e = []
celkem_c = 0
celkem_e = 0

mzda_c = mzda_start_cecilka
mzda_e = mzda_start_evzen
roky = list(range(2024, 2031))  

for rok in roky:
    rocni_uspora_c = mzda_c * podil_c * 12
    rocni_uspora_e = mzda_e * podil_e * 12

    mzdy_c.append(round(mzda_c))
    uspory_c.append(round(rocni_uspora_c))
    celkem_c += rocni_uspora_c

    mzdy_e.append(round(mzda_e))
    uspory_e.append(round(rocni_uspora_e))
    celkem_e += rocni_uspora_e

    mzda_c += rust_c
    mzda_e += rust_e


prehled_mezd_uspor = pd.DataFrame({
    "Rok": roky,
    "Mzda Cecilka (Kč/měsíc)": mzdy_c,
    "Roční úspora Cecilka (Kč)": uspory_c,
    "Mzda Evžen (Kč/měsíc)": mzdy_e,
    "Roční úspora Evžen (Kč)": uspory_e
})

print(prehled_mezd_uspor)

(round(celkem_c), round(celkem_e), round(celkem_c + celkem_e))
