def calculer_moyenne(notes):
    if len(notes) == 0:
        print("Attention : aucune note fournie.")
        return None

    total = 0
    nombre_notes = 0

    for note in notes:
        total += note
        nombre_notes += 1

    return total/nombre_notes

def calculer_moyenne_ponderee(notes, coefficients):
    if len(notes) == 0:
        print("Attention : aucune note fournie.")
        return None

    if len(notes) != len(coefficients):
        print("Erreur : le nombre de notes et de coefficients doit être identique.")
        return None

    total_pondere = 0
    total_coefficients = 0

    for i in range(len(notes)):
        total_pondere += notes[i] * coefficients[i]
        total_coefficients += coefficients[i]

    return total_pondere / total_coefficients


def appreciation(moyenne):
    if moyenne < 10:
        return "Insuffisant"
    elif 10 <= moyenne < 12:
        return "Passable"
    elif 12 <= moyenne < 16:
        return "Bien"
    else:
        return "Tres bien"


def moyenne_groupe(etudiants):
    if len(etudiants) == 0:
        print("Attention: aucun étudiant fourni.")
        return None

    total_moyennes = 0
    nombre_etudiants = 0

    for etudiant in etudiants:
        moyenne = calculer_moyenne(etudiant["notes"])

        if moyenne != None:
            total_moyennes += moyenne
            nombre_etudiants += 1

    if nombre_etudiants == 0:
        print("Attention : aucun étudiant ne possède de note.")
        return None

    return total_moyennes / nombre_etudiants


def somme_recursive(notes):
    if len(notes) == 0:
        return 0

    return notes[0] + somme_recursive(notes[1:])


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


print()
print("Tests supplémentaires   ")


notes = [14, 10, 18]
coefficients = [3, 2, 1]

moyenne_ponderee = calculer_moyenne_ponderee(notes, coefficients)

print(f"Moyenne ponderee : {moyenne_ponderee:.2f}")


moyenne_classe = moyenne_groupe(etudiants)

print(f"Moyenne du groupe : {moyenne_classe:.2f}")

notes_vides = []

moyenne_vide = calculer_moyenne(notes_vides)

print(f"Moyenne avec liste vide : {moyenne_vide}")


notes_recursive = [12, 15, 9, 18]

somme = somme_recursive(notes_recursive)

print(f"Somme recursive : {somme}")