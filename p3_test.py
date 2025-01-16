import pytest

from p3 import (
    karakterek_szama,
    szavak_szama,
    sorok_szama,
    r_betuk_szama,
    lorem_szavak_szama,
    leggyakoribb_karakter,
    leghosszabb_sor_hossza,
    Teglalap,
    Negyzet,
    Kocka,
    string_fajlba,
    szaz_szam_fajlba,
    elso_karakter_a_fajlban,
    utolso_karakter_a_fajlban,
    szamok_osszege_a_fajlban,
    szamok_atlaga_a_fajlban,
    paros_szamok_szama_a_fajlban,
    paratlan_szamok_szama_a_fajlban,
    pozitiv_szamok_szama_a_fajlban,
    negativ_szamok_szama_a_fajlban,
    legkisebb_szam_a_fajlban,
    legnagyobb_szam_a_fajlban,
    parosok_a_fajlbol,
    paratlanok_a_fajlbol,
    pozitiv_a_fajlbol,
    negativok_a_fajlbol,
    leggyakoribb_szam_a_fajlban,
    harommal_oszthato_szamok_a_fajlban,
    neggyel_oszthato_szamok_a_fajlban
)

def test_karakterek_szama():
    assert karakterek_szama("lorem.txt") == 18047

def test_szavak_szama():
    assert szavak_szama("lorem.txt") == 2304

def test_sorok_szama():
    assert sorok_szama("lorem.txt") == 82

def test_r_betuk_szama():
    assert r_betuk_szama("lorem.txt") == 790

def test_lorem_szavak_szama():
    assert lorem_szavak_szama("lorem.txt") == 27

def test_leggyakoribb_karakter():
    assert leggyakoribb_karakter("lorem.txt") == "i"

def test_leghosszabb_sor_hossza():
    assert leghosszabb_sor_hossza("lorem.txt") == 304

def test_Teglalap():
    assert Teglalap(3, 4).oldal1 == 3
    assert Teglalap(3, 4).oldal2 == 4
    assert Teglalap(3, 4).kerulet() == 14
    assert Teglalap(3, 4).terulet() == 12

def test_Negyzet():
    assert Negyzet(3).kerulet() == 12
    assert Negyzet(3).terulet() == 9

def test_Kocka():
    assert Kocka(3).terfogat() == 27
    assert Kocka(3).felszin() == 54

def test_string_fajlba():
    assert string_fajlba("csacska macska", "szoveg.txt") == None
    assert open("szoveg.txt").read().strip() == "csacska macska"

def test_szaz_szam_fajlba():
    assert szaz_szam_fajlba("szazas.txt") == None
    assert sum([int(i) for i in open("szazas.txt")]) == 5050

def test_elso_karakter_a_fajlban():
    assert elso_karakter_a_fajlban("lorem.txt") == "L"

def test_utolso_karakter_a_fajlban():
    assert utolso_karakter_a_fajlban("lorem.txt") == "."

def test_szamok_osszege_a_fajlban():
    assert szamok_osszege_a_fajlban("szamok1.txt") == 16

def test_szamok_atlaga_a_fajlban():
    assert szamok_atlaga_a_fajlban("szamok1.txt") == 1.0

def test_paros_szamok_szama_a_fajlban():
    assert paros_szamok_szama_a_fajlban("szamok1.txt") == 10

def test_paratlan_szamok_szama_a_fajlban():
    assert paratlan_szamok_szama_a_fajlban("szamok1.txt") == 6

def test_pozitiv_szamok_szama_a_fajlban():
    assert pozitiv_szamok_szama_a_fajlban("szamok1.txt") == 10

def test_negativ_szamok_szama_a_fajlban():
    assert negativ_szamok_szama_a_fajlban("szamok1.txt") == 4

def test_legkisebb_szam_a_fajlban():
    assert legkisebb_szam_a_fajlban("szamok1.txt") == -6

def test_legnagyobb_szam_a_fajlban():
    assert legnagyobb_szam_a_fajlban("szamok1.txt") == 4

def test_parosok_a_fajlbol():
    assert parosok_a_fajlbol("szamok1.txt") == [4, 2, 4, 2, 0, -4, -6, 0, 4, 4]

def test_paratlanok_a_fajlbol():
    assert paratlanok_a_fajlbol("szamok1.txt") == [3, 1, 3, 1, -1, -1]

def test_pozitiv_a_fajlbol():
    assert pozitiv_a_fajlbol("szamok1.txt") == [4, 3, 2, 1, 4, 3, 2, 1, 4, 4]

def test_negativok_a_fajlbol():
    assert negativok_a_fajlbol("szamok1.txt") == [-1, -1, -4, -6]

def test_leggyakoribb_szam_a_fajlban():
    assert leggyakoribb_szam_a_fajlban("szamok1.txt") == 4

def test_harommal_oszthato_szamok_a_fajlban():
    assert harommal_oszthato_szamok_a_fajlban("szamok1.txt") == [3, 3, 0, -6, 0]

def test_neggyel_oszthato_szamok_a_fajlban():
    assert neggyel_oszthato_szamok_a_fajlban("szamok1.txt") == [4, 4, 0, -4, 0, 4, 4]
