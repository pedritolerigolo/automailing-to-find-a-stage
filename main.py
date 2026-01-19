import os
from contact import CONTACTS
from ia import generer_phrase_personnalisee, envoyer_mail_avec_pdf
from dotenv import load_dotenv

# Charger .env
load_dotenv()

# --- CONFIGURATION GLOBALE ---
SENDER_EMAIL = "martin.cozic@etu.univ-nantes.fr"
SENDER_PASSWORD = os.getenv("SMTP_PASSWORD")  # mot de passe universitaire
SMTP_SERVER = "smtp.univ-nantes.fr"  # à confirmer avec l'info de l'université
SMTP_PORT = 587

PDF_A_JOINDRE = "CV_Martin_COZIC.pdf"
NOM_FICHIER_DESTINATAIRE = "CV_Martin_COZIC.pdf"
OBJET_MAIL = "Candidature spontanée — Stage développement (avril–juin 2026)"


def construire_email_complet(nom_contact, phrase_ia):
    """Renvoie le corps complet du mail à envoyer, avec la phrase générée par l'IA."""
    corps = f"""Bonjour {nom_contact},

Actuellement en deuxième année de BUT Informatique à l'IUT de Nantes, je suis à la recherche d'un stage de 8 à 12 semaines à partir de mi-avril 2026.

Je suis particulièrement intéressé par les projets liés au développement logiciel et web, des domaines dans lesquels je souhaite mettre en pratique et approfondir mes compétences.

{phrase_ia}

Mes études et projets personnels m’ont permis de développer une base technique solide et polyvalente :

• Développement Java et Kotlin (architecture MVC, JavaFX, design patterns)
• Développement web (PHP/CodeIgniter, MySQL, applications dynamiques)
• Automatisation avec Python (API Google Sheets pour alertes e-mail)
• Maîtrise de HTML/CSS, JavaScript, PHP et outils collaboratifs Git/GitLab/GitHub
• Connaissances en bases de données (MySQL, Oracle), environnement Linux et IDE modernes (VS Code, IntelliJ)

Curieux, rigoureux et motivé, je serais ravi de contribuer à vos projets tout en consolidant mes compétences au sein de votre équipe.

Vous trouverez mon CV en pièce jointe. Je reste disponible pour tout complément d’information ou pour un entretien à votre convenance.

Bien cordialement,

Martin Cozic
06 02 16 50 44
martin.cozic@etu.univ-nantes.fr
"""
    return corps


def lancer_campagne():
    print("--- Lancement de la Campagne d'E-mailing IA ---")
    
    if not os.path.exists(PDF_A_JOINDRE):
        print(f"ERREUR FATALE : Le fichier PDF '{PDF_A_JOINDRE}' est introuvable. Arrêt.")
        return

    for contact in CONTACTS:
        email = contact.get('email')
        nom = contact.get('nom', 'Client')

        print(f"\nTraitement du contact : {nom} <{email}>...")

        # Génération de la phrase IA
        phrase_ia = generer_phrase_personnalisee(nom)

        # Construction du mail complet
        corps_mail = construire_email_complet(nom, phrase_ia)

        # Envoi du mail
        

    print("\n--- Campagne terminée ---")


if __name__ == "__main__":
    lancer_campagne()
