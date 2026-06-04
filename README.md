# LemurXOR

```markdown
# 🎭 Lemur XOR

Un outil en Python optimisé pour résoudre les défis de cryptographie "Lemur XOR" couramment rencontrés dans les compétitions de type Capture The Flag (CTF).

Lorsqu'une même clé secrète est utilisée pour chiffrer deux images différentes via une opération XOR, il est possible d'annuler cette clé en effectuant un XOR entre les deux images chiffrées, révélant ainsi les données cachées (souvent un drapeau).

## ✨ Fonctionnalités

* **Analyse RGB pure :** Effectue l'opération mathématique uniquement sur les pixels de l'image, préservant ainsi l'intégrité des en-têtes de fichiers.
* **Haute performance :** Utilise des calculs matriciels via `NumPy` pour un traitement quasi instantané, même sur des images haute résolution.
* **Support universel :** Gère automatiquement la conversion des canaux alpha (transparence) pour éviter les erreurs de dimensions matricielles.

## ⚙️ Prérequis

Assurez-vous d'avoir Python 3 d'installé, ainsi que les bibliothèques de manipulation d'images et de mathématiques :

```bash
pip install Pillow numpy

```

## Utilisation

1. Clonez ce dépôt.
2. Placez vos deux images chiffrées (par exemple `image1.png` et `image2.png`) dans le même répertoire que le script.
3. Exécutez le script :

```bash
┌──(venv)─(mavericks㉿kali)-[~/CTF/lemurXOR]
└─$ python3 lemur.py

```

Le script générera automatiquement un fichier `drapeau_revele.png` dans le répertoire courant contenant la superposition en clair des deux images.

## Sous le capot : La Mathématique du XOR

Ce script exploite les propriétés fondamentales de l'opérateur OU exclusif (XOR, noté ⨁).

Si nous avons deux images originales (I1 et I2) chiffrées avec la même clé (K) pour produire deux images chiffrées (C1 et C2) :

C1 = I1 ⨁ K
C2 = I2 ⨁ K

En effectuant un XOR entre les deux images chiffrées, la clé s'annule d'elle-même grâce à la propriété d'auto-inverse (K ⨁ K = 0) :


C1 ⨁ C2 = (I1 ⨁ K) ⨁ (I2 ⨁ K) = I1 ⨁ I2

Le résultat est une fusion visuelle des deux images d'origine, rendant le secret lisible à l'œil nu.

## Avertissement

Ce script a été développé à des fins éducatives et d'entraînement pour la cybersécurité offensive et défensive.
