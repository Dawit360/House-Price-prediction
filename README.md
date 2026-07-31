🏠 AI House Price Prediction App (Multi-Model Pipeline)

An advanced Machine Learning web application that predicts house prices using multiple models and selects the best performer. Built with Flask + Scikit-learn, this project demonstrates a full end-to-end ML pipeline, from data preprocessing to deployment.

---

🚀 Features

- 🤖 Multiple ML models integrated in one pipeline
- 📊 Automatic model comparison & selection
- 🌐 Interactive Flask web application
- 🔒 Input validation (no invalid/negative values)
- 📉 Safe predictions (no negative outputs)
- ⚡ Fast and scalable architecture

---

🧠 Machine Learning Pipeline (End-to-End)

This project follows a complete ML workflow:

1. Data Processing

- Handles missing values
- Separates:
  - Numerical features
  - Categorical features

2. Feature Engineering

- StandardScaler → for numerical data
- OneHotEncoder → for categorical data

3. Column Transformer

Combines preprocessing steps into a single pipeline:

ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), NUM_COLS),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CAT_COLS)
    ]
)

---

🤖 Models Used (All Integrated)

The system trains and compares multiple models:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor (Final Selected Model)
- Support Vector Regressor (SVR)
- K-Nearest Neighbors (KNN)

---

🏆 Model Selection

- All models are trained on the same dataset
- Performance evaluated using:
  - R² Score
  - Mean Squared Error (MSE)
- The best-performing model is selected automatically

✔ Final Model Used:

GradientBoostingRegressor (n_estimators=100, random_state=42)

---

⚙️ Unified Training Module

All models are integrated into a single training module:

models = {
    "Linear": LinearRegression(),
    "Ridge": Ridge(),
    "Lasso": Lasso(),
    "Tree": DecisionTreeRegressor(),
    "RF": RandomForestRegressor(),
    "GBM": GradientBoostingRegressor(),
    "SVR": SVR(),
    "KNN": KNeighborsRegressor()
}

for name, model in models.items():
    pipe = Pipeline([
        ("preprocess", preprocessor),
        ("model", model)
    ])
    
    pipe.fit(X_train, y_train)
    score = pipe.score(X_test, y_test)
    
    print(f"{name}: {score}")

---

🌐 Web Application Flow

1. User inputs property data:
   
   - Rooms
   - Area (site & built)
   - Property age
   - Materials
   - Location distances

2. Flask:
   
   - Validates inputs
   - Converts to DataFrame

3. Model:
   
   - Loads saved pipeline (".joblib")
   - Predicts price

4. Output:
   
   - Displays predicted house price instantly

---

🏗️ Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS
- ML Library: Scikit-learn
- Data Handling: Pandas
- Model Saving: Joblib

---

📂 Project Structure

AI-House-Price-App/
│
├── Dataset/
│   └── houses_improved.csv
│
├── Model/
│   └── gbm_housing_model.joblib
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
└── README.md

---

▶️ How to Run

1.Clone Repository 

gitclone https://github.com/Dawit360/House-Price-prediction


cd House-Price-prediction 

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask application (no training required)
python app.py

Then open your browser:

http://127.0.0.1:5000/

Important Notes

Ensure that model.joblib is located in the same directory as app.py

Verify that the model is loaded correctly in your application:

import joblib
model = joblib.load("model.joblib"

---

📊 Example Prediction

Input:

Rooms: 3
Built Area: 120 sqm
Age: 5 years

Output:

Estimated Price: 3,200,000 ETB

---

🔐 Safety Features

- Prevents negative inputs
- Handles unseen categories
- Avoids negative predictions using model wrapper

---

📈 Future Improvements

- Add Deep Learning model (Neural Network)
- Deploy to cloud (Render / Railway / AWS)
- Add real-time dataset updates
- Improve UI/UX design

---

👨‍💻 Author

Dawit Birhanu

- 🎓 Computer Science & Finance Background
- 🤖 Passionate about AI & Data Science

---

⭐ Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork it
- 🚀 Share it
