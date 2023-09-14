import os
import shutil

# Chemin du dossier source contenant les 4 sous-dossiers
dossier_source = r''

# Chemin du dossier de destination où vous voulez fusionner les images
dossier_destination = r''

# Vérification et création du dossier de destination s'il n'existe pas déjà
if not os.path.exists(dossier_destination):
    os.makedirs(dossier_destination)

# Fonction pour fusionner les images des sous-dossiers dans le dossier de destination
def fusionner_images(dossier_source, dossier_destination):
    numero_image = 1
    for sous_dossier in os.listdir(dossier_source):
        if os.path.isdir(os.path.join(dossier_source, sous_dossier)):
            for image in os.listdir(os.path.join(dossier_source, sous_dossier)):
                # Vérifier si le nom du fichier correspond au format "Image_<numéro>.jpg"
                if image.startswith('Image_') and (image.endswith('.jpg') or image.endswith('.JPG') or image.endswith('.jpeg') or image.endswith('.JPEG') or image.endswith('.png') or image.endswith('.PNG') ):
                    nouveau_nom = f'Image_{numero_image}.jpg'
                    chemin_source = os.path.join(dossier_source, sous_dossier, image)
                    chemin_destination = os.path.join(dossier_destination, nouveau_nom)
                    shutil.copy(chemin_source, chemin_destination)
                    numero_image += 1

# Appel de la fonction pour fusionner les images
fusionner_images(dossier_source, dossier_destination)
