import smtplib
import  argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os



parser = argparse.ArgumentParser(description="Un exemple de script Python acceptant des arguments.")

parser.add_argument('-e', '--email', type=str, required=True, help="Email.")
parser.add_argument('-f', '--file', type=str, required=True, help="Chemin du fichier PDF à joindre.")



args =parser.parse_args() 

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)

    server.login("richardmbakam1@gmail.com","ubgccqzmzkcinbit")

    print(".............connection reussi..........")

    recieve = args.email

# Construction du message
# Faut modifier le message pour les  differents postes

    message = (
                "Bonjour,\n\n" 
                "Je me permets de vous contacter suite à la récente publication de plusieurs offres de stage sur votre site internet et les différents job boards, que j’ai consultées avec grand intérêt. " 
                "Ces opportunités correspondent parfaitement à mon parcours et à mes compétences.\n\n" 
                "Actuellement étudiant à l’Université de Technologie de Troyes, je me spécialise dans la sécurité réseau, un domaine que j’ai approfondi au cours de ma formation et de diverses expériences professionnelles. " 
                "Convaincu de pouvoir contribuer efficacement à vos projets, je serais ravi de mettre à disposition mes compétences pour soutenir vos équipes et relever de nouveaux défis au sein de votre entreprise.\n\n" 
                "Vous trouverez en pièce jointe mon CV qui présente mon parcours en détail.\n" 
                "Je me tiens bien entendu à votre disposition pour un entretien, où nous pourrons discuter de la manière dont je pourrais intégrer et apporter une réelle valeur ajoutée à vos équipes.\n\n" 
                "Je vous remercie par avance de l’attention que vous porterez à ma candidature, et je vous prie d’agréer, Madame, Monsieur, l’expression de mes salutations distinguées.\n\n" 
                "Richanel Mbou\n" 
                "0781500681\n" 
                "richanelmbou@gmail.com") 



# Création du message MIME
    msg = MIMEMultipart()
    msg['From'] = "richardmakam1@gmail.com"
    msg['To'] = args.email
    msg['Subject'] = "Candidature spontanée aux offres de stage"

 # Ajouter le corps du message
    msg.attach(MIMEText(message, 'plain'))

# Ajouter la pièce jointe
    file_path = args.file
    if os.path.isfile(file_path):
       part = MIMEBase('application', 'octet-stream')
       with open(file_path, 'rb') as file:
          part.set_payload(file.read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
       msg.attach(part)
    else:
     print(f"Le fichier {file_path} n'existe pas.")


        
    server.sendmail("richardmbakam1@gmail.com", recieve, msg.as_string() )

    print("envoi............................ok")

except smtplib.SMTPException as e:
    print(f"Erreur SMTP : {e}")
except Exception as e:
    print(f"Erreur : {e}")
