```python
import pickle
from pathlib import Path

MODEL_PATH = Path(__file__).with_name("spam_model.pkl")

try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    message = input("Enter a message: ").strip()

    if not message:
        print("Error: Please enter a message.")
    else:
        prediction = model.predict([message])
        print("Prediction:", prediction[0])

except FileNotFoundError:
    print("Error: spam_model.pkl was not found.")
except Exception as e:
    print("Error:", e)
py -c "import pickle; f=open('spam_model.pkl','rb'); print(pickle.load(f))"