from collections import Counter
saraksts = [
    "sveiki", "labdien", "sveiki", "labdien", "sveiki", "kaijas",
    "cienījamais", "dzīvot", "cienījamais", "mūsdienu",
    "mūsdienu", "cienījamais", "kukurūza", "māja",
    "sveiciens", "dzīvot", "mūsdienu", "dzīvot", "sveiciens", "māja"
]
analize = Counter(saraksts)
for vards in analize:
    print(vards)
