from flask import Flask, render_template, request
import pandas as pd
import joblib


class NonNegativeRegressor:
    def __init__(self, model):
        self.model = model

    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict(self, X):
        predictions = self.model.predict(X)
        predictions[predictions < 0] = 0
        return predictions


app = Flask(__name__)

# Load trained model
model_pipeline = joblib.load("gbm_housing_model.joblib")


@app.route("/")
def home():
    return render_template("page.html")


@app.route("/result", methods=["POST"])
def predict():
    try:

        def check_value(field_name, minimum=None, maximum=None):
            value = float(request.form[field_name])

            if minimum is not None and value < minimum:
                raise ValueError(f"{field_name} must be at least {minimum}")

            if maximum is not None and value > maximum:
                raise ValueError(f"{field_name} must not exceed {maximum}")

            return value

        # Collect user inputs
        user_inputs = {
            "Number_of_Rooms": [check_value("Number_of_Rooms", 1, 10)],
            "Site_Area_sqm": [check_value("Site_Area_sqm", 50, 1000)],
            "Built_Area_sqm": [check_value("Built_Area_sqm", 30, 800)],
            "Property_Years": [check_value("Property_Years", 0, 50)],
            "Type_of_Nearest_Road": [request.form["Type_of_Nearest_Road"]],
            "Housing_Typology": [request.form["Housing_Typology"]],
            "Land_Value_Grading": [request.form["Land_Value_Grading"]],
            "Construction_Materials": [request.form["Construction_Materials"]],
            "Proximity_to_CBD_km": [check_value("Proximity_to_CBD_km", 0)],
            "Proximity_to_Bus_Station_km": [check_value("Proximity_to_Bus_Station_km", 0)],
            "Proximity_to_Schools_km": [check_value("Proximity_to_Schools_km", 0)],
        }

        # Convert input to DataFrame
        input_df = pd.DataFrame(user_inputs)

        # Predict
        predicted_price = model_pipeline.predict(input_df)[0]

        # Prevent negative output
        predicted_price = max(0, predicted_price)

        prediction_text = f"Estimated House Value: {predicted_price:,.2f} ETB"

        return render_template("page.html", prediction_text=prediction_text)

    except Exception as e:
        print("ERROR:", e)

        return render_template(
            "page.html",
            prediction_text=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)