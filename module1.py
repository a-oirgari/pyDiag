nom = "Oirgari"
prenom = "Abderrahman"
notes = [12, 15, 18]

total = 0
nombre_notes = 0

for note in notes:
    total += note
    nombre_notes += 1

if nombre_notes > 0:
    moyenne = total/nombre_notes
else:
    moyenne = 0

print(f"{nom:<10} moyenne : {moyenne:>6.2f}")