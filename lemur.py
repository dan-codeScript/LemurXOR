from PIL import Image
import numpy as np

def main():
    # 1. Charger les deux images chiffrées (remplace par tes noms de fichiers)
    # Convertir explicitement en 'RGB' pour ignorer la transparence (canal Alpha) éventuelle
    try:
        img1 = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png").convert('RGB')
        img2 = Image.open("flag_7ae18c704272532658c10b5faad06d74.png").convert('RGB')
    except FileNotFoundError:
        print("Erreur : Assure-toi que les images sont dans le même dossier que le script.")
        return

    # 2. Convertir les images en matrices NumPy pour la manipulation mathématique
    matrice1 = np.array(img1)
    matrice2 = np.array(img2)

    # Vérification de sécurité : les images doivent avoir la même taille
    if matrice1.shape != matrice2.shape:
        print(f"Attention : Les images n'ont pas la même taille ! ({matrice1.shape} vs {matrice2.shape})")
        return

    # 3. La magie opère : XOR bit à bit sur l'ensemble des matrices RVB
    matrice_resultat = np.bitwise_xor(matrice1, matrice2)

    # 4. Reconvertir la matrice mathématique en véritable image visuelle
    image_finale = Image.fromarray(matrice_resultat)

    # 5. Afficher et sauvegarder le résultat
    image_finale.show()
    image_finale.save("drapeau_revele.png")
    print("[+] L'image a été générée et sauvegardée sous 'drapeau_revele.png'.")

if __name__ == "__main__":
    main()
