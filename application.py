from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import PIL.Image as Image
import io
from crop_image import crop
from easy_facial_recognition import run_reco
import glob

application = Flask(__name__)

CORS(application)

@application.route('/')
def Home():

    
    return 'Face Recognition!'

#convertir base64 en fichier image
def convert_and_save(b64_string, nom):
    string = bytes(b64_string, "UTF-8")
    b = base64.b64decode(string)

    image = Image.open(io.BytesIO(b))

    image.save("images/{}.png".format(nom))
    
    
#Enregistrer les images capturer dans le dossier image
@application.route('/save_image', methods=["POST"])
def save_image():
    
    data = request.get_json(force=True)    

    Image = data["base64"]
    nom = data["nom"]
    ok = True

    print("Image")

    print(Image)
    print(nom)
    
    try:
        convert_and_save(str(Image).replace("data:image/jpeg;base64,",""),nom)
    except:
        ok = False
    return jsonify({"ok":ok})


#Crop les images et les insérer dans le dossier know image avec leur nom
@application.route('/launch_crop')
def launch_crop():

    ok = True
    try:
        val = crop()
    except:
        ok = False
    return jsonify({"ok":ok,"resultat":val})


#Lancer la reconnaissances
@application.route('/launch_recog')
def launch_recog():
    ok = True
    try:
        val = run_reco()
    except:
        ok = False
    return jsonify({"ok":ok,"resultat":"val"})


if __name__ == '__main__':
    application.run(debug=True)