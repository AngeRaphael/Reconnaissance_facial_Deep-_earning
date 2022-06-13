import cv2
import glob
import os

def crop():
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    path = "./images/*.*"
    
    img_list = glob.glob(path)
    
    
    ok = True
    
    try:
        for file in img_list[0:len(img_list)]:
            
            img_list = glob.glob(path)

            nom = str(img_list[0]).replace(path,"")
            
            nom = str(nom)[9:len(nom)]
                
            if nom.endswith(".jpeg"): nom = nom[0:len(nom)-5]
            if nom.endswith(".png"): nom = nom[0:len(nom)-4]
            if nom.endswith(".jpg"): nom = nom[0:len(nom)-4]
            
            img = cv2.imread(file, 1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade.detectMultiScale(gray,1.3,5)
            
            try:
                for (x,y,w,h) in faces:
                    
                    roi_color  = img[y:y+h, x: x+ w]
                    
                    resized = cv2.resize(roi_color, (128,128))
                    cv2.imwrite("./known_faces/"+str(nom)+".jpg", resized)
                
                
                files = glob.glob('./images/*')
                
                # for f in files:
                #     os.remove(f)
                                
            except:
                print("Aucune face détecté")
                
                ok = "Aucune face détecté"
    except:
        ok = False
            
    return ok
