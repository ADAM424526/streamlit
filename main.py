#import streamlit as st

#st.title("Éljenek a Bélák")

#szam1 = st.number_input("Szám1")
#st.write("Első szám:", szam1)

#szam2 = st.number_input("Szám2")
#st.write("Második szám:", szam2)

#művelet = st.text_input("művelet")
#if st.button("Művelet elvégzése"):
#    if művelet == ("+"):
#        result = szam1 + szam2
#        st.write("eredmény", result)

#    elif művelet == "*":
#        result = szam1 * szam2
#        st.write("eredmény", result)

#    elif művelet == "**":
#        result = szam1 ** szam2
#        st.write("eredmény", result)


#    elif művelet == "-":
#        result = szam1 - szam2
#        st.write("eredmény", result)

#    elif művelet == "//":
#        result = szam1 // szam2
#        st.write("eredmény", result)
    
#
#import streamlit as st

#st.title("Egyszerű Számológép")

#szam1 = st.number_input("Szám1")
#szam2 = st.number_input("Szám2")

#if st.button("Művelet"):
#    with st.expander("Összeadás"):
#        result_addition = szam1 + szam2
#        st.write(f"Eredmény (összeadás): {result_addition}")

#    with st.expander("Kivonás"):
#        result_subtraction = szam1 - szam2
#        st.write(f"Eredmény (kivonás): {result_subtraction}")

#    with st.expander("Szorzás"):
#        result_multiplication = szam1 * szam2
#        st.write(f"Eredmény (szorzás): {result_multiplication}")




#import streamlit as st

#st.title("Listabu")
#if 'lista' not in st.session_state:
    #st.session_state.lista = []
#adat = st.text_input("Adat")
#if st.sidebar.button("Hozzáad"):
    #st.session_state.lista.append(adat)
#if st.sidebar.button("Töröl"):
    #if st.session_state.lista:
        #st.session_state.lista.pop()
#st.write("Lista:", st.session_state.lista)

import streamlit as st
from collections import Counter

def leggyakoribb_szo(mondat):
    szavak = mondatszavak.split()
    szavak_szama = len(szavak)
    szavak_gyakorisaga = Counter(szavak)
    leggyakoribb_szavak = szavak_gyakorisaga.most_common(1)

    if leggyakoribb_szavak:
        return leggyakoribb_szavak[0][0]
    else:
        return "Nincs szó a szövegben"

def leggyakoribb_betu(mondat):
    karakterek = [betu.lower() for betu in mondatszavak if betu.isalpha()]
    karakterek_gyakorisaga = Counter(karakterek)
    leggyakoribb_karakter = karakterek_gyakorisaga.most_common(1)

    if leggyakoribb_karakter:
        return leggyakoribb_karakter[0][0]
    else:
        return "Nincs betű a szövegben"

mondatszoveg = st.text_input('Írj bele egy szöveget')

if st.button('Nagybetű'):
    st.write(str.upper(mondatszoveg))

if st.button('Szavak'):
    szavak_szama = len(mondatszoveg.split())
    st.write(f"{szavak_szama}")

if st.button('Betűk'):
    betuk_szama = len([betu for betu in mondatszoveg if betu.isalpha()])
    st.write(f"{betuk_szama}")

if st.button('Leggyakoribb szó'):
    leggyakoribb = leggyakoribb_szo(mondatszoveg)
    st.write(f'Leggyakoribb szó: {leggyakoribb}')

if st.button('Leggyakoribb betű'):
    leggyakoribb_betu = leggyakoribb_betu(mondatszoveg)
    st.write(f'Leggyakoribb betű: {leggyakoribb_betu}')


cam = st.camera_input("Kamera")
if cam:
    st.image(cam)