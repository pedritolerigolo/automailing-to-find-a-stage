import os
import openai
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Charger .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# --- FONCTION IA ---
def generer_phrase_personnalisee(nom_entreprise):
    """
    Génère 1-2 phrases personnalisées pour un e-mail via OpenAI.
    """
    prompt = f"""
    Tu es chargé de rédiger une phrase d’accroche pour une candidature de stage en développement web/logiciel.
    L'entreprise s'appelle {nom_entreprise}.
    Rédige 1 à 2 phrases courtes et professionnelles expliquant pourquoi cette entreprise est intéressante,
    ou invente un projet plausible si aucune info publique n'est disponible.
    """
    try:
        reponse = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.7
        )
        texte_genere = reponse.choices[0].message['content'].strip()
        return texte_genere
    except Exception as e:
        print(f"Erreur IA pour {nom_entreprise}: {e}")
        return "Je suis particulièrement intéressé par vos projets dans le développement web et logiciel."


# --- FONCTION D'ENVOI E-MAIL ---
def envoyer_mail_avec_pdf(
    destinataire_email, 
    objet, 
    corps_texte, 
    chemin_pdf, 
    sender_email, 
    sender_password,
    smtp_server, 
    smtp_port,
    nom_fichier_joint
):
    """Construit et envoie l'e-mail avec pièce jointe."""
    try:
        # Création du message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = destinataire_email
        msg['Subject'] = objet

        # Ajout du corps
        msg.attach(MIMEText(corps_texte, 'plain'))

        # Ajout de la pièce jointe
        with open(chemin_pdf, "rb") as f:
            piece_jointe = MIMEApplication(f.read(), _subtype="pdf")
            piece_jointe.add_header('Content-Disposition', 'attachment', filename=nom_fichier_joint)
            msg.attach(piece_jointe)

        # Connexion et envoi
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, destinataire_email, msg.as_string())
        server.quit()

        return True, f"Email envoyé avec succès à : {destinataire_email}"
    
    except Exception as e:
        return False, f"ERREUR lors de l'envoi à {destinataire_email} : {e}"
