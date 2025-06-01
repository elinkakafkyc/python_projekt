import streamlit as st
from streamlit_ace import st_ace
from PIL import Image
import json


#nazev zalozky a ikonka, uzky layout a otevreny sidebar defaultne
st.set_page_config(
    page_title="Metr za milion",
    page_icon="🏠",
    layout="centered",  
    initial_sidebar_state="expanded"
)


# nastaveni barvy sidebaru f4dbe5 puvodne 
base = "light"
primaryColor = "#ffffff"
st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)


# pomocne poznamky 
# "/Users/eliskakafkova/Library/Mobile Documents/com~apple~CloudDocs/Datová analýza/04_Python/projekt/XY_pokus.py"
# streamlit run XY_pokus.py
# `KODY`
# dve mezery na konci textu jsou novej radek
# pevna mezera st.markdown("<br>", unsafe_allow_html=True)
# vickrat za sebou st.markdown("<br><br>", unsafe_allow_html=True)
# mala mezera st.write("")
# oddelovace st.divider()
# nebo st.markdown("---")
# barevne boxy - st.success(), st.warning(), st.error(), st.info()
#editor kodu themes: monokai, github, tomorrow night, pastel_on_dark, dracula, merbivore_soft,solarized_dark,twilight
# nase barvena paletka:
#f4a2c3 ruzova
#c89fca sv fialova
#613F75 tm fial
#568ea3 modra
#ECD444 zluta

# sidebar kapitoly neww
st.sidebar.markdown("## 📚 Kapitoly", unsafe_allow_html=True)

st.sidebar.markdown("""
<style>
.sidebar-button {
    display: block;
    padding: 6px 10px;
    margin: 3px 0;
    background-color: #c89fca;
    color: black !important;
    text-decoration: none !important;
    border-radius: 8px;
    font-weight: 500;
    font-size: 14px;
    transition: background-color 0.2s ease;
}
.sidebar-button:hover {
    background-color: #f4a2c3;
}
.sidebar-sub {
    margin-left: 20px;
    font-size: 13px;
}
.bullet::before {
    content: "• ";
    margin-right: 4px;
}
</style>

<a class="sidebar-button" href="#uvod">Úvod</a>
<a class="sidebar-button sidebar-sub bullet" href="#nastroje-a-postupy">Nástroje a postupy</a>
<a class="sidebar-button" href="#stanoveni-modeloveho-scenare">1. Stanovení modelového scénáře</a>
<a class="sidebar-button sidebar-sub bullet" href="#modelovy-parecek">Modelový páreček</a>
<a class="sidebar-button sidebar-sub bullet" href="#modelovy-bytecek">Modelový byteček</a>
<a class="sidebar-button" href="#analyticke-otazky">2. Analytické otázky</a>
<a class="sidebar-button" href="#datova-priprava-a-cisteni-aka-prvni">3. Datová příprava a čištění aka první Hackathon</a>
<a class="sidebar-button" href="#prvni-analyzy-a-vizualizace">4. První analýzy a vizualizace</a>
<a class="sidebar-button" href="#samostatna-prace-michaela-kaderova">5. Samostatná práce – Michaela Kaderová</a>
<a class="sidebar-button" href="#samostatna-prace-eliska-kafkova">6. Samostatná práce – Eliška Kafková</a>
<a class="sidebar-button" href="#zaverecna-analyza-a-vizualizace-na-druhem-hackathonu">7. Závěrečná analýza a vizualizace</a>
<a class="sidebar-button sidebar-sub bullet" href="#predikce-cen-bytu-v-roce-2030">Predikce cen bytů v roce 2030</a>
<a class="sidebar-button sidebar-sub bullet" href="#scenar-1-bez-materske-dovolene-pouze-s-fenkou-barou">Scénář 1: Bez mateřské dovolené</a>
<a class="sidebar-button sidebar-sub bullet" href="#scenar-2-s-materskou-dovolenou">Scénář 2: Vliv mateřské dovolené</a>
<a class="sidebar-button" href="#shrnuti-a-prinos">8. Shrnutí a přínos</a>
""", unsafe_allow_html=True)


# pokus o sidebar a kapitoly puvodni
# st.sidebar.markdown("## 📚 Kapitoly")
# st.sidebar.markdown("""

# - [Úvod](#uvod)  
# - [1. Stanovení modelového scénáře](#stanoveni-modeloveho-scenare)  
#      - [Modelový páreček](#modelovy-parecek)  
#      - [Modelový byteček](#modelovy-bytecek)  
# - [2. Analytické otázky](#analyticke-otazky)  
# - [3. Datová příprava a čištění aka první Hackathon](#datova-priprava-a-cisteni-aka-prvni)  
# - [4. První analýzy a vizualizace](#prvni-analyzy-a-vizualizace)  
# - [5. Samostatná práce – Michaela Kaderová](#samostatna-prace-michaela-kaderova)  
# - [6. Samostatná práce – Eliška Kafková](#samostatna-prace-eliska-kafkova)  
# - [7. Závěrečná analýza a vizualizace](#zaverecna-analyza-a-vizualizace-na-druhem-hackathonu)  
#      - [Predikce cen bytů v roce 2030](#predikce-cen-bytu-v-roce-2030)  
#      - [Scénář 1: Bez mateřské dovolené](#scenar-1-bez-materske-dovolene-pouze-s-fenkou-barou)  
#      - [Scénář 2: Vliv mateřské dovolené](#scenar-2-s-materskou-dovolenou)  
# - [8. Shrnutí a přínos](#shrnuti-a-prinos)  
# """, unsafe_allow_html=True)


# odkazy na github sidebar
st.sidebar.markdown("""
                    **📌 Odkazy na GitHub:** 
                    """)
st.sidebar.markdown("[ **❄️ SQL kódy**](https://github.com/MichaelaKad/sql_projekt.git)")

st.sidebar.markdown("[ **🐼 Python kódy 🐍**](https://github.com/elinkakafkyc/python_projekt)")

st.sidebar.markdown("[ **🗝️ Streamlit appka**](https://github.com/elinkakafkyc/python_projekt/blob/main/XY_pokus.py)")

#barevna paleta interaktivni    

barvy = {
    "Růžová": "#f4a2c3",
    "Světle fialová": "#c89fca",
    "Tmavě fialová": "#613F75",
    "Modrošedá": "#568ea3",
    "Žlutá": "#ECD444"
}

# vyber barvy
vybrana_barva = st.sidebar.radio("**Prohlédni si barvy z naší palety!**", list(barvy.keys()), horizontal=True)

# ziskani kodu
hex_kod = barvy[vybrana_barva]

# zobrazeni barvy
st.sidebar.markdown(f"""
<div style="width:250px; height:50px; background-color:{hex_kod}; border-radius:10px; border:1px solid #aaa;"></div>
""", unsafe_allow_html=True)




# NADPIS A AUTORI
st.title("Metr za milion: Mileniálské dilema")

st.subheader("*Eliška Kafková  &  Michaela Kaderová*") 
st.markdown("*Mentoři: **Eliška Valterová  &  Jakub Červinka***")



# if st.button("🔔 Zobraz toast"):
#     st.toast("Tohle je toasťáček! 🥳")

# # 🎧 Vtipný zvuk
# if st.button("🔊 Zahraj zvuk"):
#     st.audio("https://www.myinstants.com/media/sounds/that-was-easy.mp3", autoplay=True)


# st.image("https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif", caption="Točím se jak Streamlit komponenty 😄")


# ÚVOD
st.header("Úvod")
st.write(
    """
    V rámci našeho projektu jsme se rozhodly podívat na jeden z nejpalčivějších problémů mladé generace – dostupnost vlastního bydlení v Praze. 
    Na základě dat z Srealit, statistik příjmů a predikcí vývoje cen a mezd jsme zjišťovaly, jestli si průměrný mladý pár může za několik let dovolit koupit vlastní byt.
    
    Naším cílem bylo nejen zjistit, jaká je současná situace, ale také ji zasadit do reálného příběhu – proto jsme vytvořily fiktivní pár Cecilku a Evžena a jejich sen o vlastním bytě v hlavním městě.
    """
)
#obrazek uvod
st.image("images/uvod.png", use_container_width=True)
st.write()  

# nastroje a postupyy
st.subheader("🛠️ Nástroje a postupy")
st.markdown("""V projektu jsme využily širokou škálu nástrojů a technologií, se kterými jsme se během Digitální akademie (i mimo ni) seznámily. 
         Data o realitních inzerátech jsme získaly díky **Apify** a zpracovávaly je v **Keboole** pomocí **SQL (Snowflake)**.
           Datový model jsme vytvořily pomocí nástroje **Lucidchart**. Pro analytickou a statistickou část jsme pracovaly v **Pythonu** (hlavně za použití Jupyter Notebooků) s využitím knihoven jako pandas, seaborn, scipy, numpy, statsmodels či matplotlib. 
           Výstupy jsme vizualizovaly v **Tableau**, kde jsme si vyzkoušely i tvorbu predikce (Tableau Forecast) vývoje cen.
             Ke generování obrázků a ikonek ve zvolené paletě barev, kterou jsme si navrhly pomocí nástroje **Coolors** jsme využily **ChatGPT**. Pro náš článek jsme následně vytvořily tuto aplikaci za pomocí knihovny **streamlit** a její publikaci provedly přes **Streamlit Cloud**. 
             Kódy i aplikaci jsme sdíleli skrze **GitHub**, na nějž naleznete odkazy na této stránce pod výpisem kapitol. 
             Grafické úpravy a finální prezentaci jsme připravovaly v nástrojích **Figma** a **Canva**, pro společný brainstorming a přípravu struktury naší data story pak nástroj **Miro**.
         
""")
# schematko z figmy kvalitnejsi
st.image("images/schema_kvalita.png", use_container_width=True)


st.divider() # rozdelovaci caraaa

# Sekce 1 - modelový páreček a byteček
st.header("Stanovení modelového scénáře")
st.write("Prvním krokem bylo nadefinování modelové situace, která by odpovídala realitě většiny mladých párů v Praze:")

    # MODELOVÝ PÁREČEK
st.subheader("Modelový páreček:")
st.markdown(
    """
    - 👩 **Cecilka (29)** – učitelka na soukromé základní škole, má mediánový hrubý měsíční příjem **45 120 Kč**
    - 👨 **Evžen (30)** – elektrikář ve větší firmě, má mediánový hrubý měsíční příjem **52 397 Kč**
    - 💸 **Celkové čisté příjmy**: cca **76 000 Kč / měsíc**
    - 🏠 **Žijí spolu v nájemním bytě 2+kk**, za který platí **22 000 Kč** vč. poplatků (průměrný nájem v této kategorii dispozic bytů)
    - 🐶 **Domácí mazlíček**: fenka Bára
    - 🔒 **Pevné měsíční výdaje**: cca **46 110 Kč**
    - 📉 **Volné prostředky k úspoře**: cca **29 890 Kč / měsíc**
    """
)

    # OBRÁZEK 1 - MODELOVÝ PÁREČEK

st.write("")
image = Image.open("images/parecek.png")
st.image(image, caption='Modelový páreček - Cecilka a Evžen s fenkou Bárou', use_container_width=True)

st.write("")

    # MODELOVÝ BYTEČEK
st.subheader("🏡 Modelový byteček:")
st.markdown(
    """
    Cílem Cecilky a Evžena je do roku 2030 našetřit a koupit vlastní byt **2+kk nebo 2+1**, ideálně v širším centru nebo klidné části Prahy. Dispozice 2+kk je nejoblíbenější a nejčetnější v inzerátech prodejů nemovitostí, a 2+1 je její nejbližší alternativou. 
    Tuto dispozici si vybírají i proto, že zatím nemají děti a velikost bytu jim pro každodenní život plně vyhovuje.
    """
)

st.divider()  # rozdelovaci cara

# Sekce 2 - analytické otázky
st.header("👉 Analytické otázky")
st.write("*Na začátku jsme si položily následující klíčové otázky, které bude cílem zodpovědět:*")
st.markdown(
        """
        **A. Jaké jsou průměrné ceny modelového bytu v různých částech Prahy?**  
       

        **B. Jak se ceny modelového bytu změnily za poslední roky? A jak se změnily mzdy?**  
       

        **C. Dosáhne modelový pár na hypotéku v roce 2030? 
        Jaké jsou jejich šance vzhledem k jejich mzdě a bude to dostačující i při rostoucí rodině?**  
    
        """
    )



st.divider()  # rozdelovaci cara


# Sekce 3 - datova priprava, hackathon

st.header("Datová příprava a čištění aka první")
st.image("images/hackathon.png", width=300)
st.write("*Data o realitních inzerátech jsme získaly od **Apify** a nahrály do **Kebooly**, " \
"kde jsme provedly první transformace:*")
st.markdown(
        """
  
1. Vybraly jsme relevantní sloupce  
2. Data omezily jen na **Prahu**  
3. Opravily jsme nesoulad mezi názvy městských částí a GPS souřadnicemi (pomocí číselníku z ČSÚ a mentorky Elišky)  
4. Vyfiltrovaly jsme pouze byty **2+kk a 2+1** na prodej a odstranily zbývající irelevantní informace  
5. Vytvořily jsme čitelný formát datumu a také sloupce rok, měsíc, kvartál  
6. Došlo i na opravu rozbitého sloupce s užitnou plochou – napojily jsme správná data z původní tabulky  

*Podrobný postup spolu s SQL kódy jsou dostupné na Githubu:* 
        """
    ) 

# odkaz na GITHUB míša

st.markdown("[**📌 Přesně tady!**](https://github.com/MichaelaKad/sql_projekt.git)")
st.write()  

if st.button("❄️ Cecilka říkala, že Snowflake je romantika. Tak tady to máš."):
    st.snow()

st.markdown("""Z vyčištěných dat jsme následně mohly začít tvořit první SQL dotazy – 
            například pro výpočet průměrné ceny za m² podle jednotlivých městských částí, 
            což bude klíčový podklad pro zodpovězení naší první otázky.""")  
  
# SQL kodik

code = '''
SELECT
    "MC_spravne",
    ROUND(AVG("data_price"/"plocha")) AS "prumerna_cena_na_m2"
FROM "vycistena_tabulka_oprava_2"
WHERE 
        "data_price" IS NOT NULL
    AND "data_price" != ''
    AND "plocha" IS NOT NULL
    AND "plocha" != ''
    AND YEAR = 2024
GROUP BY "MC_spravne"
ORDER BY "prumerna_cena_na_m2" DESC;

'''

st_ace(
    value=code,
    language="sql",
    theme="pastel_on_dark",
    readonly=True,
    height=300
)

#sql kodik basics
st.code("""SELECT
    "MC_spravne",
    ROUND(AVG("data_price"/"plocha")) AS "prumerna_cena_na_m2"
FROM "vycistena_tabulka_oprava_2"
WHERE 
        "data_price" IS NOT NULL
    AND "data_price" != ''
    AND "plocha" IS NOT NULL
    AND "plocha" != ''
    AND YEAR = 2024
GROUP BY "MC_spravne"
ORDER BY "prumerna_cena_na_m2" DESC;""", language="sql")

#sql kodik varianta
code = '''
SELECT
    "MC_spravne",
    ROUND(AVG("data_price"/"plocha")) AS "prumerna_cena_na_m2"
FROM "vycistena_tabulka_oprava_2"
WHERE
    "data_price" IS NOT NULL
    AND "data_price" != ''
    AND "plocha" IS NOT NULL
    AND "plocha" != ''
    AND YEAR = 2024
GROUP BY "MC_spravne"
ORDER BY "prumerna_cena_na_m2" DESC;
'''

st.markdown(f"""
<div style="
    background-color: #f8f8f8;  /* světlé pozadí */
    color: #333;                /* tmavý text */
    padding: 12px;
    border-radius: 8px;
    font-family: monospace;
    font-size: 14px;
    line-height: 1.5;
    overflow-x: auto;
    white-space: pre;
    border: 1px solid #ccc;
">
{code}
</div>
""", unsafe_allow_html=True)




#datovy model obrazek

st.markdown("""V mezičase jsme pomocí nástroje LucidChart postupně tvořily **datový model:**""")  

st.image("images/model.png", caption='Datový model naší situace', use_container_width=True)


st.divider()  # rozdelovaci cara


# sekce 4 - prvni analýzy a vizualizace
st.header("📊 První analýzy a vizualizace")
st.markdown("""
Nyní jsme již mohly odpovědět na naši první otázku:    
               
👉 ***Jaké jsou aktuální průměrné ceny za m² v jednotlivých částech Prahy (2024)?***  
       
📍 Výsledky jsme zobrazily **v mapě městských částí.** Jak se dalo čekat, nejvyšší ceny za m² jsou v úplném centru města,
             ale ani okrajové části Prahy již nezůstávají pozadu.
            Zřejmě se zde nárazově promítají nové developerské projekty vznikající v těchto lokalitách, což průměrné ceny zvyšuje.
""")

# VIZUALIZACE MAPA CENY V JEDNOTLIVYCH CASTECH 2024
st.image("images/mapa.png", caption='Cena za m² v jednotlivých částech Prahy pro rok 2024', use_container_width=True)


st.divider()  # rozdelovaci cara

# sekce 5 - samostatna prace Misa Kaderova
st.header("🤵‍♀️ Samostatná práce - Michaela Kaderová")
st.write("*Míša se zaměřila na vývoj **cen nemovitostí a průměrných mezd v čase:***")
st.markdown(
"""
- Nejprve získala data o mzdách z ISPV. 
Zaměřila se pouze na data pro hlavní město Prahu a vybrala věkové kategorie 20-29 a 30-39 let. 
Dále rozdělila data podle pohlaví a omezila je na období let 2016-2024.
Z těchto údajů následně vypočítala jak mediánové, tak průměrné mzdy pro obě věkové skupiny dohromady. 
Tím vznikl souhrnný přehled o vývoji mzdové úrovně mladé generace v Praze za posledních několik let.
- Dále připravila data o inflaci. Data byla čerpána z Českého statistického úřadu – konkrétně se jednalo o průměrnou roční míru inflace ve stejném časovém rozmezí.
- Všechna tato data následně spojila s hlavním datasetem realit v Keboole
- Na závěr v Tableau vytvořila graf vývoje cen a mezd v Praze v letech 2016-2024
  
Díky tomu jsme mohly odpovědět **na druhou otázku:**  
  
👉 ***Jak se ceny modelového bytu změnily za poslední roky? A jak se změnily mzdy?*** 
   
...a potvrdily tak výrazné zhoršení dostupnosti bydlení pro mladé. 
 Je zřejmé, že růst mediánových mezd v posledních letech nestačil držet krok s výrazným zdražováním nemovitostí.

        """
    )

# VIZUALIZACE CENY BYTŮ ZA POSLEDNÍ ROKY
st.write()
st.image("images/mzdy_ceny.png", caption='Růst průměrné ceny za m² vs. růst mediánové mzdy', use_container_width=True)


st.divider()  # rozdelovaci

# sekce 6 - samostatna prace - Eliska kafkova
st.header("💁‍♀️ Samostatná práce – Eliška Kafková")
st.write("*Eliška se zaměřila na **predikce mezd, spoření a měsíční výdaje párečku.***")
st.markdown(
"""
- Vzhledem k předchozímu vývoji mezd byla zvolena lineární regrese 
(ano, víme že hodnot by bylo potřeba více pro lepší přesnost, ale člověk si zkrátka musí umět poradit)  
    - Predikce mzdy Evžena i Cecilky do roku 2030  
    - Odhad měsíčních výdajů poměrově rostoucích společně se mzdou  
    - Výpočet naspořených peněz  
    - Totéž pro druhou variantu s mateřskou dovolenou  
- Zároveň předpřipravila šablonu pro tuhle streamlit appku  
 
    
*Podrobný postup spolu s Python kódy jsou dostupné na Githubu:* 
        """
    )


# odkaz na GITHUB Eliška
st.markdown("[**📌 Přesně tady!**](https://github.com/elinkakafkyc/python_projekt.git)")
st.write()
#dopsat nazev kodu
#vlozeni kodu z ipynb

with open("01_predikce_mzdy_evzen.ipynb", "r", encoding="utf-8") as evzen:
    nb = json.load(evzen)

    # Posbírej všechny kódové buňky
all_code = []
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        code = "".join(cell["source"])
        all_code.append(code)

    # Sloučení všeho do jednoho stringu
full_code = "\n\n \n\n".join(all_code)

    # Zobrazení jako jedna scrollovatelná, barevná buňka
st_ace(value=full_code, language="python", theme="pastel_on_dark", readonly=True, height=300, key="readonly_code")
    # Popisek kodu



st.divider()  # rozdelovnik

# sekce 7 - zaverecna analyza a vizualizace na druhem hackathonu
st.header("📈 Závěrečná analýza a vizualizace na druhém Hackathonu")
st.subheader("Predikce cen bytů v roce 2030")
st.markdown(
"""
Z dostupných dat jsme spočítaly průměrnou velikost bytu o dispozici 2+kk a 2+1, která se nejvíce blížila potřebám páru. 
Výsledek byl **58 m²** – tuto hodnotu jsme následně použily pro další výpočty.  
  
S využitím Tableau jsme vytvořily prediktivní model vývoje cen za m² v jednotlivých částech Prahy. 
Pro každou městskou část jsme predikované ceny vynásobily hodnotou 58 m², čímž jsme získaly odhadovanou **cenovku bytu v roce 2030.** 
        """
    )

st.write()

# VIZUALIZACE nejdražších částí prahy top 5 a predikce do 2030
st.image("images/ceny_bytu_24_30.png", caption='5 nejdražších částí Prahy v roce 2024 a jejich predikce pro rok 2030', use_container_width=True)

st.markdown(
    """
Graf znázorňuje pět nejdražších městských částí Prahy v roce 2024 a jejich predikovanou cenovku bytu v roce 2030.
 Zatímco u většiny lokalit očekáváme pokračující růst cen, výjimku tvoří Praha 1, kde naše predikce naznačuje mírný pokles ceny. 
Tento vývoj může naznačovat nasycení trhu v centru města nebo rostoucí zájem o jiné atraktivní městské části, kde vznikají nové developerské projekty a nabízejí modernější bydlení v dostupnějších lokalitách.

      
Nyní se již můžeme věnovat našim závěrečným otázkám:
   
👉 ***Dosáhne modelový pár na hypotéku v roce 2030? 
Jaké jsou jejich šance vzhledem k jejich mzdě a bude to dostačující i při rostoucí rodině?***

Výsledky jsme zobrazily v mapě, kde byly zvýrazněny čtvrti, ve kterých by měl pár reálnou šanci na koupi bytu podle dvou scénářů:
 bez mateřské a s mateřskou dovolenou. 

""")


# scenar 1!
st.subheader(
    """
***Scénář 1: Bez mateřské dovolené pouze s fenkou Bárou***
""")
st.markdown(
    """
**Odhadované příjmy v roce 2030:**  
  
- Cecilka: 46 998 Kč (čistého)  
- Evžen: 56 764 Kč (čistého)  
 **→ Celkem: 103 762 Kč měsíčně**  
   
**Měsíční potenciál pro hypotéku:**  
  
- Po odečtení výdajů a bez nájmu (který již nebudou tou dobou platit):  
 → Mají navíc **62 809 Kč měsíčně**  
 → Bezpečná výše měsíční splátky: **~40 000 Kč měsíčně**  
   
**Naspořené prostředky :**  
  
- Celkově: **2 969 338 Kč**  
- Reálně lze použít na hypotéku: **2 500 000 Kč** (zbytek jako rezerva)  
  
**Možnosti páru:**  
  
- Hypotéka na **30 let** (u AirBank, protože i banku můžete mít rádi)  
- Půjčka **7,5 mil. Kč**  
- Celková cena nemovitosti: **10 mil. Kč**  
- **Limitující nebyl potřebný základ pro žádost o hypotéku (10 % z ceny nemovitosti při věku žadatele do 36 let), 
ale její měsíční splátka.**  
  
🟣  *V mapě jsme **růžově** vyznačily městské části, kde lze za tuto cenu v roce 2030 koupit byt 2+kk nebo 2+1.*


"""
)

st.image("images/mapa_bez_materske.png", caption='Vyznačené části Prahy, kde Evžen s Cecilkou dosáhnou na pořízení vysněného bytu.', use_container_width=True)

# scenar 2

st.subheader(
    """
***Scénář 2: S mateřskou dovolenou***
""")
st.markdown(
    """
    Zohlednily jsme i variantu, kdy Cecilka v určitém období (2027) odejde na mateřskou a po návratu zpět do práce 
    pobírá mzdu ekvivalentní jako ve stejném čase v předchozím scénáři.  
    
**Příjmy (po návratu z mateřské):**  
  
- Cecilka: 46 998 Kč (čistého)  
- Uvažovaly jsme 70% mateřskou a poté vyčerpání rodičovského příspěvku, délka mateřské dovolené klasicky v délce 3 let
- Evžen: 56 764 Kč (čistého)  
 **→ Celkem: 103 762 Kč měsíčně** 
  → Stejné úspory a kapacita pro splácení jako v předchozím scénáři **(~40 000 Kč měsíčně)**  
   
**Naspořené prostředky:**  
  
- Nižší úspory z důvodu výpadku/snížení příjmu: **1 931 026 Kč**
- Reálně lze použít na hypotéku: **1 500 000 Kč** (zbytek jako rezerva)  
  
**Možnosti páru:**  
  
- Hypotéka na **30 let** (u AirBank, protože i banku můžete mít rádi)  
- Půjčka **7,5 mil. Kč**  
- Celková cena nemovitosti: **9 mil. Kč**  
- **Limitující opět nebyl potřebný základ pro žádost o hypotéku, 
ale její měsíční splátka.**  
- **V této situaci by jim však postupem času byt 2+kk nebo 2+1 nestačil,
 a navíc by jim rostly měsíční výdaje, které zde zatím nebyly zohledněné** (výdaje se zvyšovaly pouze poměrem se mzdou).
  
🟣  *Opět jsme **růžově** zobrazily dostupné městské části v mapě – kde se v roce 2030 očekává, že za tuto částku půjde koupit příslušný byt.*


"""
)

st.image("images/mapa_materska.png", caption='Vyznačené části Prahy, kde Evžen s Cecilkou dosáhnou na pořízení 2+kk nebo 2+1 po mateřské.', use_container_width=True)


st.divider()  # rozdelovnaci cara

st.header("🌎 Shrnutí a přínos")
st.markdown("""
Obě simulace ukázaly, že pokud bude pár schopen spořit, 
vyhnout se dlouhodobé pracovní neschopnosti a udrží si stabilní příjem, **je pořízení bytu v určitých čtvrtích Prahy reálné.**  
  
*Zásadní roli hraje:*
- **výše naspořených prostředků,**  
- **schopnost dlouhodobě spořit a udržet výdajový režim na uzdě,**
- **úroková sazba a ochota banky úvěr poskytnout.**  
              
Za zvážení by samozřejmě stály i další scénáře – například zůstat v nájmu při potřebě většího bytu, nebo nákup menšího bytu jako investičního. 
Tyto varianty však vzhledem k časovým možnostem přenecháváme budoucím generacím datařek.  
              
Z hlediska analytické práce jsme v této fázi spojily veškeré připravené datové podklady, 
využily jsme prediktivní i vizualizační nástroje a převedly jsme čísla do praktického scénáře reálného života.
To považujeme za hlavní přínos našeho projektu.


""")



st.image("images/materska.png", use_container_width=True)
st.caption("Modelový páreček v roce 2030: Cecilka, Evžen, fenka Bára a nový člen rodiny – malý Albert. " \
"Teď už potřebují nejen hypotéku, ale i o trochu větší botník.")
if st.button("🎈 Albert trvá na balónkové rozlučce!"):
    st.balloons()









