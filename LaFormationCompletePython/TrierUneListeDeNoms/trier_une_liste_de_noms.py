# liste_caracteres = ["¯", "«", "©", "¨", "Ã"]
# result = []
# with open("prenom.txt", "r") as f:
#     words = f.read().split()
#     for word in words:
#         for caractere in liste_caracteres:
#             word = word.strip(".,¨")
#             word = word.replace(caractere, "")
#         result.append(word)
#         result.sort()
#
#     for elmt in result:
#         print(elmt)

# Correction
with open("prenom.txt", "r") as f:
    lines = f.read().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]
with open("prenom_final.txt", "w") as f:
     f.write("\n".join(sorted(prenoms_final)))