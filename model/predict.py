import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# === Load the model
model_path = os.path.join("model", "crop_health_model.h5")
model = tf.keras.models.load_model(model_path)

# === Prediction function
def predict_crop_health(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]
    result = "Healthy" if prediction > 0.5 else "Unhealthy"
    return result, float(prediction)

# === Run from command line
if __name__ == "__main__":
    test_image = "test_leaf.jpg"  # Put any test image in AgroScan root

    if os.path.exists(test_image):
        result, confidence = predict_crop_health(test_image)
        print(f"✅ Prediction: {result} ({confidence:.2f})")
    else:
        print("⚠️ test_leaf.jpg not found.")
