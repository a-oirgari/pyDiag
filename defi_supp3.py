def calculer_moyenne(notes):
    if len(notes) == 0:
        print("Attention : aucune note fournie.")
        return None

    total = 0
    nombre_notes = 0

    for note in notes:
        total += note
        nombre_notes += 1

    return total / nombre_notes


def appreciation(moyenne):
    if moyenne < 10:
        return "Insuffisant"
    elif 10 <= moyenne < 12:
        return "Passable"
    elif 12 <= moyenne < 16:
        return "Bien"
    else:
        return "Tres bien"


def construire_resultats(etudiants):
    resultats = {}

    for etudiant in etudiants:
        nom = etudiant["nom"]
        notes = etudiant["notes"]

        moyenne = calculer_moyenne(notes)

        if moyenne is not None:
            resultats[nom] = {
                "moyenne": moyenne,
                "mention": appreciation(moyenne)
            }

    return resultats

def classer_etudiants(resultats):

    classement = sorted(
        resultats.items(),
        key=lambda element: element[1]["moyenne"],
        reverse=True
    )

    return classement


def trouver_echecs(resultats):

    echecs = [
        (nom, informations["moyenne"])
        for nom, informations in resultats.items()
        if informations["moyenne"] < 10
    ]

    return echecs


def regrouper_par_mention(resultats):

    groupes = {}

    for nom, informations in resultats.items():

        mention = informations["mention"]

        if mention not in groupes:
            groupes[mention] = []

        groupes[mention].append(nom)

    return groupes



def detecter_doublons(noms):

    noms_uniques = set()

    for nom in noms:

        if nom in noms_uniques:
            return True

        noms_uniques.add(nom)

    return False


def fusionner_groupes(groupe_a, groupe_b):

    fusion = {}

    for nom, informations in groupe_a.items():
        fusion[nom] = informations

    for nom, informations in groupe_b.items():

        if nom not in fusion:

            fusion[nom] = informations

        else:
            print(f"Conflit détecté pour {nom}.")

            fusion[nom] = [
                fusion[nom],
                informations
            ]

    return fusion


etudiants = [
    {"nom": "Karim", "notes": [12, 15, 9]},
    {"nom": "Sara", "notes": [18, 17, 16]},
    {"nom": "Lina", "notes": [6, 8, 5]},
]


resultats = construire_resultats(etudiants)

print(" Résultats  ")

for nom, informations in resultats.items():

    moyenne = informations["moyenne"]
    mention = informations["mention"]

    print(f"{nom:<10} {moyenne:>.2f} {mention}")



classement = classer_etudiants(resultats)

print()
print(" Classement  ")

position = 1

for nom, informations in classement:

    print(
        f"{position}. {nom:<10} "
        f"{informations['moyenne']:>.2f}"
    )

    position += 1


echecs = trouver_echecs(resultats)

print()
print(" Étudiants en échec ")

for nom, moyenne in echecs:
    print(f"{nom:<10} {moyenne:>.2f}")


print()
print(" Groupes par mention  ")

groupes_mentions = regrouper_par_mention(resultats)

print(groupes_mentions)


print()
print(" Détection des doublons  ")

noms = ["Karim", "Sara", "Lina", "Karim"]

if detecter_doublons(noms):
    print("Attention, il y a des doublons !")
else:
    print("Aucun doublon détecté.")


print()
print(" Fusion des groupes  ")

groupe_a = {
    "Karim": {
        "moyenne": 12.0,
        "mention": "Bien"
    }
}

groupe_b = {
    "Karim": {
        "moyenne": 15.0,
        "mention": "Bien"
    },
    "Sara": {
        "moyenne": 17.0,
        "mention": "Tres bien"
    }
}

groupe_fusionne = fusionner_groupes(groupe_a, groupe_b)

print(groupe_fusionne)