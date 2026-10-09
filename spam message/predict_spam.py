
import joblib
from pathlib import Path

# Load the trained spam detection model
model_path = Path(__file__).with_name("spam_model.pkl")
model = joblib.load(model_path)

print("===================================")
print("     SPAM MESSAGE DETECTOR")
print("===================================")
print("Model loaded successfully!")

while True:
    message = input(
        "\nEnter a message (or type 'exit' to quit): "
    ).strip()

    if message.lower() == "exit":
        print("Thank you for using Spam Message Detector!")
        break

    if not message:
        print("Please enter a message.")
        continue

    try:
        prediction = model.predict([message])[0]
        label = str(prediction).strip().lower()

        if label in ("spam", "1"):
            print("Result: SPAM MESSAGE")
        elif label in ("ham", "not spam", "0"):
            print("Result: NOT SPAM")
        else:
            print(f"Prediction: {prediction}")

    except Exception as error:
        print("Prediction error:", error)
