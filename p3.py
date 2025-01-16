def karakterek_szama(fname):
    """ Visszatér a fájlban levő karakterek számával. A karakterekkel együtt.
    """
    pass # Írd a kódodat a következő sorokba!


#assert karakterek_szama("lorem.txt") == 18047

#------------------------------------------------------

def szavak_szama(fname):
    """ Visszatér a fájlban levő szavak számával """
    pass # Írd a kódodat a következő sorokba!


#assert szavak_szama("lorem.txt") == 2304

#------------------------------------------------------

def sorok_szama(fname):
    """ Visszatér a fájlban levő sorok számával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert sorok_szama("lorem.txt") == 82

#------------------------------------------------------

def r_betuk_szama(fname):
    """ Visszatér a fájlban levő 'r' betük számával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert r_betuk_szama("lorem.txt") == 790 

#------------------------------------------------------

def lorem_szavak_szama(fname):
    """ Visszatér a fájlban levő "lorem" szavak számával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert lorem_szavak_szama("lorem.txt") == 27 

#------------------------------------------------------

def leggyakoribb_karakter(fname):
    """ Visszatér a fájlban leggyakrabban előforduló karakterrel.
    """
    pass # Írd a kódodat a következő sorokba!

#assert leggyakoribb_karakter("lorem.txt") ==  "i"

#------------------------------------------------------

def leghosszabb_sor_hossza(fname):
    """ Visszatér a fájlban levő leghosszabb sor hosszával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert leghosszabb_sor_hossza("lorem.txt") == 304

#------------------------------------------------------

class Teglalap:   
    """1. Hozz létre egy osztályt Teglalap néven.
       2. A Teglalap osztály lehetővé teszi a téglalap oldalhosszúságainak tárolását.
       3. A Teglalap osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
       4. A Teglalap osztály rendelkezik egy terulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum területét."""
    pass # Írd a kódodat a következő sorokba!


#assert Teglalap(3, 4).oldal1 == 3
#assert Teglalap(3, 4).oldal2 == 4
#assert Teglalap(3, 4).kerulet() == 14
#assert Teglalap(3, 4).terulet() == 12

#------------------------------------------------------

class Negyzet:   
    """1. Hozz létre egy osztályt Negyzet néven.
       2. A Negyzet osztály lehetővé teszi a negyzet oldalhosszúságának tárolását.
       3. A Negyzet osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
       4. A Negyzet osztály rendelkezik egy terulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum területét."""
    pass # Írd a kódodat a következő sorokba!

#assert Negyzet(3).kerulet() == 12
#assert Negyzet(3).terulet() == 9

#------------------------------------------------------

class Kocka:   
    """1. Hozz létre egy osztályt Kocka néven.
       2. A Kocka osztály lehetővé teszi a kocka oldalhosszúságának tárolását.
       3. A Kocka osztály rendelkezik egy terfogat() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum térfogatát.
       4. A Kocka osztály rendelkezik egy felszin() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum felszínét."""
    pass # Írd a kódodat a következő sorokba!

#assert Kocka(3).terfogat() == 27
#assert Kocka(3).felszin() == 54

#------------------------------------------------------

def string_fajlba(string, fajlnev):
    """Az első paraméterként kapott sztringet fájlba írja."""
    pass # Írd a kódodat a következő sorokba!

#assert string_fajlba("csacska macska", "szoveg.txt") == None
#assert open("szoveg.txt").read().strip() == "csacska macska"

#------------------------------------------------------

def szaz_szam_fajlba(fajlnev):
    """Minden szám kerüljön új sorba. 1-tól 100-ig egyesével kiírja a számokat egy fájlba."""
    pass # Írd a kódodat a következő sorokba!

#assert szaz_szam_fajlba("szazas.txt") == None
#assert sum([int(i) for i in open("szazas.txt")]) == 5050

#------------------------------------------------------

def elso_karakter_a_fajlban(fajlnev):
    """ Visszatér egy szövegfájl első karakterével.
    """
    pass # Írd a kódodat a következő sorokba!

#assert elso_karakter_a_fajlban("lorem.txt") == "L"

#------------------------------------------------------

def utolso_karakter_a_fajlban(fajlnev):
    """ Visszatér egy szövegfájl utolsó karakterével
    """
    pass # Írd a kódodat a következő sorokba!

#assert utolso_karakter_a_fajlban("lorem.txt") == "."

#------------------------------------------------------

def szamok_osszege_a_fajlban(filename):
    """ Visszatér egy szövegfájlban levő számok összegével.
    """
    pass # Írd a kódodat a következő sorokba!

#assert szamok_osszege_a_fajlban("szamok1.txt") == 16

#------------------------------------------------------

def szamok_atlaga_a_fajlban(fajlnev):
    """ Visszatér egy szövegfájlban levő számok átlagával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert szamok_atlaga_a_fajlban("szamok1.txt") == 1.0

#------------------------------------------------------

def paros_szamok_szama_a_fajlban(fajlnev):
    """ Visszatér egy szövegfájlban levő páros számok számával.
    """
    pass # Írd a kódodat a következő sorokba!
        
#assert paros_szamok_szama_a_fajlban("szamok1.txt") == 10

#------------------------------------------------------

def paratlan_szamok_szama_a_fajlban(fajlnev):
    """Visszatér egy szövegfájlban levő páratlan számok számával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert paratlan_szamok_szama_a_fajlban("szamok1.txt") == 6

#------------------------------------------------------

def pozitiv_szamok_szama_a_fajlban(fajlnev):
    """  Visszatér egy szövegfájlban levő pozitiv számok számával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert pozitiv_szamok_szama_a_fajlban("szamok1.txt") == 10

#------------------------------------------------------

def negativ_szamok_szama_a_fajlban(fajlnev):
    """ Visszatér egy szövegfájlban levő negativ számok számával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert negativ_szamok_szama_a_fajlban("szamok1.txt") == 4

#------------------------------------------------------

def legkisebb_szam_a_fajlban(fajlnev):
    """ Visszatér egy szövegfájlban levő lekisebb számmal.
    """
    pass # Írd a kódodat a következő sorokba!

#assert legkisebb_szam_a_fajlban("szamok1.txt") == -6

#------------------------------------------------------

def legnagyobb_szam_a_fajlban(fajlnev):
    """ Visszatér egy szövegfájlban levő legnagyobb számmal.
    """
    pass # Írd a kódodat a következő sorokba!

#assert legnagyobb_szam_a_fajlban("szamok1.txt") == 4

#------------------------------------------------------

def parosok_a_fajlbol(fajlnev):
    """ Visszatér a szövegfájlban levő 
        páros számokkal mint listával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert parosok_a_fajlbol("szamok1.txt") == [4, 2, 4, 2, 0, -4, -6, 0, 4, 4]

#------------------------------------------------------

def paratlanok_a_fajlbol(fajlnev):
    """ Visszatér a szövegfájlban levő 
        páratlan számokkal mint listával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert paratlanok_a_fajlbol("szamok1.txt") == [3, 1, 3, 1, -1, -1]

#------------------------------------------------------

def pozitiv_a_fajlbol(fajlnev):
    """ Visszatér a szövegfájlban levő 
        pozitiv számokkal mint listával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert pozitiv_a_fajlbol("szamok1.txt") == [4, 3, 2, 1, 4, 3, 2, 1, 4, 4]

#------------------------------------------------------

def negativok_a_fajlbol(fajlnev):
    """ Visszatér a szövegfájlban levő 
        negativ számokkal mint listával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert negativok_a_fajlbol("szamok1.txt") == [-1, -1, -4, -6] 

#------------------------------------------------------

def leggyakoribb_szam_a_fajlban(fajlnev):
    """ Visszatér a szövegfájlban levő leggyakoribb számmal.
    """
    pass # Írd a kódodat a következő sorokba!

#assert leggyakoribb_szam_a_fajlban("szamok1.txt") == 4

#------------------------------------------------------

def harommal_oszthato_szamok_a_fajlban(fajlnev):
    """ Visszatér a szövegfájlban levő 
        hárommal osztható számok listájával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert harommal_oszthato_szamok_a_fajlban("szamok1.txt") == [3, 3, 0, -6, 0]

#------------------------------------------------------

def neggyel_oszthato_szamok_a_fajlban(fajlnev):
    """ Visszatér a szövegfájlban levő 
        neggyel osztható számok listájával.
    """
    pass # Írd a kódodat a következő sorokba!

#assert neggyel_oszthato_szamok_a_fajlban("szamok1.txt") == [4, 4, 0, -4, 0, 4, 4]