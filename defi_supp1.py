prenom = input("saisir le prénom : " )
nom = input("saisir le nom : " )
notes = []

while len(notes) < 3:
    saisie = input("Entrez une note : ")
    if saisie.isdigit():
        note = float(saisie)

        if 0 <= note <= 20:
            notes.append(note)
            print(f"Note acceptee : {note}")
        else:
            print("La note doit être comprise entre 0 et 20, reessayez.")
    else:
        print("Ce n’est pas un nombre valide, reessayez.")


total = 0
nombre_notes = 0

for note in notes:
    total += note
    nombre_notes += 1

if nombre_notes > 0:
    moyenne = total/nombre_notes
else:
    moyenne = 0

print()
print("===========================")
print(f"Nom      : {nom}")
print(f"Prénom   : {prenom}")
print(f"Moyenne  : {moyenne:>6.2f}")