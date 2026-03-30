#Codigo principal del modelo
#https://github.com/rajpurkarlab/cheXpert-test-set-labels

import pandas as pd
import numpy as np
import cv2
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.utils import resample


# ------------------------
# 1. RUTAS
# ------------------------
IMAGE_FOLDERS = [
    r"E:\archive\images_001\images",
    r"E:\archive\images_002\images",
    r"E:\archive\images_003\images",
    r"E:\archive\images_004\images",
    r"E:\archive\images_005\images",
    r"E:\archive\images_006\images",
    r"E:\archive\images_007\images",
    r"E:\archive\images_008\images",
    r"E:\archive\images_009\images",
    r"E:\archive\images_010\images",
    r"E:\archive\images_011\images",
    r"E:\archive\images_012\images",
]
IMAGES_PATH = r"E:\archive\images_001\images"
CSV_PATH = r"E:\archive\Data_Entry_2017.csv"

# ------------------------
# 2. CARGAR CSV
# ------------------------
df = pd.read_csv(CSV_PATH)

print("Columnas:", df.columns)
print("Total registros:", len(df))

# ------------------------
# 3. CREAR CLASIFICACIÓN BINARIA
# ------------------------
df['label'] = df['Finding Labels'].apply(
    lambda x: 0 if x == "No Finding" else 1
)

df = df[['Image Index', 'label']]
df = df.sample(1000)  

from sklearn.utils import resample

df_major = df[df.label == 1]
df_minor = df[df.label == 0]

df_minor_up = resample(df_minor, replace=True, n_samples=len(df_major), random_state=42)

df = pd.concat([df_major, df_minor_up])

print("Balance:")
print(df['label'].value_counts())

# ------------------------
# 4. FUNCIÓN PARA PROCESAR IMÁGENES
# ------------------------
def procesar_imagen(nombre_img):
    
    for folder in IMAGE_FOLDERS:
        path = os.path.join(folder, nombre_img)
        
        if os.path.exists(path):
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            
            if img is None:
                return None
            
            img = cv2.resize(img, (224, 224))
            img = img / 255.0
            
            mean = np.mean(img)
            std = np.std(img)
            
            return [mean, std]
    
    return None

# ------------------------
# 5. CREAR DATASET FINAL
# ------------------------
X = []
y = []

for _, row in df.iterrows():
    features = procesar_imagen(row['Image Index'])
    
    if features is not None:
        X.append(features)
        y.append(row['label'])

X = np.array(X)
y = np.array(y)

print("Datos procesados:", X.shape)

# ------------------------
# 6. TRAIN / TEST
# ------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------
# 7. MODELO LOGÍSTICO
# ------------------------
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train, y_train)
# ------------------------
# 8. EVALUACIÓN
# ------------------------
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred, zero_division=0))
