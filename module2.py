def calculer_moyenne(notes):
    total = 0
    nombre_notes = 0

    for note in notes:
        total += note
        nombre_notes += 1

    if nombre_notes == 0:
        return 0

    return total/nombre_notes

def appreciation(moyenne):
    if moyenne < 10:
        return "Insuffisant"
    elif 10 <= moyenne < 12:
        return "Passable"
    elif 12 <= moyenne < 16:
        return "Bien"
    else:
        return "Tres bien"

etudiants = [
    {"nom": "Karim", "notes": [12, 15, 9]},
    {"nom": "Sara", "notes": [18, 17, 16]},
    {"nom": "Lina", "notes": [6, 8, 5]},
]


meilleur_etudiant = None
dernier_etudiant = None

meilleure_moyenne = None
pire_moyenne = None

for etudiant in etudiants:

    nom = etudiant["nom"]
    notes = etudiant["notes"]

    moyenne = calculer_moyenne(notes)
    mention = appreciation(moyenne)

    print(f"{nom:<10} {moyenne:>.2f} {mention}")

    if meilleure_moyenne == None or moyenne > meilleure_moyenne:
        meilleure_moyenne = moyenne
        meilleur_etudiant = nom

    if pire_moyenne == None or moyenne < pire_moyenne:
        pire_moyenne = moyenne
        dernier_etudiant = nom

print(f"Meilleur etudiant : {meilleur_etudiant}")
print(f"dernier etudiant : {dernier_etudiant}")

