from collections import Counter
saraksts = [
    "sveiki", "labdien", "sveiki", "labdien", "sveiki", "kaijas",
    "cienījamais", "dzīvot", "cienījamais", "mūsdienu",
    "mūsdienu", "cienījamais", "kukurūza", "māja",
    "sveiciens", "dzīvot", "mūsdienu", "dzīvot", "sveiciens", "māja"
]
analize = Counter(saraksts)
for vards, skaits in analize.items():   
    print(f"Simbolu virkne {vards} sarakstā sastopama = {skaits}")

    ##Lieto .items() tad, kad Tev ir jāsaskaita vai jāsaglabā lietas pārī (piemēram, ar Counter), un tas paņem gan pašu vārdu, gan tā skaitu vienlaicīgi, lai abus varētu uzreiz izmantot ciklā.