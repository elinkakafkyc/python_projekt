import streamlit as st
from PIL import Image
# "/Users/eliskakafkova/Library/Mobile Documents/com~apple~CloudDocs/Datová analýza/04_Python/projekt/XY_pokus.py"
# streamlit run XY_pokus.py
# `KODY`
# dve mezery na konci textu jsou novej radek!!!
# pevna mezera st.markdown("<br>", unsafe_allow_html=True)
# vickrat za sebou st.markdown("<br><br>", unsafe_allow_html=True)
# mala mezera st.write("")
# oddelovace st.divider()
# nebo st.markdown("---")
# barevne boxy - st.success(), st.warning(), st.error(), st.info()





# NADPIS
st.title("Metr za milion: Mileniálské dilema")

# ÚVOD
st.header("Úvod")
st.write(
    """
    V rámci našeho projektu jsme se rozhodly podívat na jeden z nejpalčivějších problémů mladé generace – dostupnost vlastního bydlení v Praze. 
    Na základě dat z Srealit, statistik příjmů a predikcí vývoje cen a mezd jsme zjišťovaly, jestli si průměrný mladý pár může za několik let dovolit koupit vlastní byt.
    
    Naším cílem bylo nejen zjistit, jaká je současná situace, ale také ji zasadit do reálného příběhu – proto jsme vytvořily fiktivní pár Cecilku a Evžena a jejich sen o vlastním bytě v hlavním městě.
    """
)

st.divider() # rozdelovaci cara

# Sekce 1 - modelový páreček a byteček
st.header("1. Stanovení modelového scénáře")
st.write("Prvním krokem bylo nadefinování modelové situace, která by odpovídala realitě většiny mladých párů v Praze:")

# MODELOVÝ PÁREČEK
st.subheader("Modelový páreček:")
st.markdown(
    """
    - 👩 **Cecilka (29)** – učitelka na soukromé základní škole, bere mediánový hrubý měsíční příjem **45 120 Kč**
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
image = Image.open("parecek.png")
st.image(image, caption='Modelový páreček - Cecilka a Evžen s fenkou Bárou', use_container_width=True)

st.write("")

# MODELOVÝ BYTEČEK
st.subheader("Modelový byteček:")
st.markdown(
    """
    Cílem Cecilky a Evžena je do roku 2030 našetřit a koupit vlastní byt **2+kk nebo 2+1**, ideálně v širším centru nebo klidné části Prahy. Dispozice 2+kk je nejoblíbenější a nejčetnější v inzerátech prodejů nemovitostí, a 2+1 je její nejbližší alternativou. 
    Tuto dispozici si vybírají i proto, že zatím nemají děti a velikost bytu jim pro každodenní život plně vyhovuje.
    """
)

st.divider()  # rozdelovaci cara

# Sekce 2 - analytické otázky
st.header("2. Analytické otázky")
st.write("Na začátku jsme si položily následující klíčové otázky, které bude cílem zodpovědět:")
st.markdown(
        """
        **A. Jaké jsou průměrné ceny modelového bytu v různých částech Prahy?**  
       

        **B. Jak se ceny modelového bytu změnily za poslední roky? A jak se změnily mzdy?**  
       

        **C. Dosáhne modelový pár na hypotéku v roce 2030? 
        Jaké jsou jejich šance vzhledem k jejich mzdě a bude to dostačující i při rostoucí rodině?**  
    
        """
    )

    # Prostor pro další interaktivní prvky:
st.info("💡 Tip: Zkouška sirén.")

st.divider()  # rozdelovaci cara

# OBRÁZEK 2 - Hackathon 
# image = Image.open("hackathon.png")
# st.image(image, width = 300)

# Sekce 3 - datova priprava, hackathon

col1, col2 = st.columns([9, 1]) # 1 a 8 je pomer rozdeleni sirky tech sloupcu

with col1:
    st.header("3. Datová příprava a čištění aka první")

with col2:
    st.image("hackathon.png", width=300)


st.header("3. Datová příprava a čištění aka první")
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
st.markdown("[**Přesně tady!**](https://github.com/MichaelaKad/sql_projekt.git)")

