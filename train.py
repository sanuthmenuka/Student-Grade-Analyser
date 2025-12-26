# Install/upgrade to latest versions first
# pip install --upgrade scikit-learn pandas numpy xgboost joblib

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Load your data
# Replace this with your actual data loading code
df = pd.read_csv('student_habits_performance_cleaned.csv')  # or however you load your data

# Define features
numeric_features = [
    "age", "study_hours_per_day", "social_media_hours",
    "sleep_hours", "attendance_percentage"
]
categorical_features = ["gender", "part_time_job"]

# Prepare X and y
X = df[numeric_features + categorical_features]
y = df['exam_score']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create preprocessor
categorical_transformer = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# Create and train pipeline
pipe = Pipeline([
    ("preprocess", preprocessor),
    ("model", RandomForestRegressor(n_estimators=200, random_state=42))
])

print("Training model...")
pipe.fit(X_train, y_train)

# Save the model with the NEW scikit-learn version
joblib.dump(pipe, 'student_performance_model.pkl')
print("✅ Model saved successfully with current scikit-learn version!")

# Test it works
from sklearn.metrics import mean_absolute_error, r2_score
y_pred = pipe.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.3f}")