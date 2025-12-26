# Student Academic Performance Predictor

A Streamlit web application that uses machine learning to predict student academic performance based on lifestyle and demographic factors.

## Overview

This application predicts a student's academic performance score (0-100) by analyzing:
- Demographics (gender, age)
- Study habits (hours per day)
- Social media usage
- Sleep patterns
- Attendance percentage
- Part-time job status

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Input Parameters

- **Gender**: Male or Female
- **Age**: 15-25 years
- **Study Hours per Day**: 0-12 hours
- **Social Media Hours**: 0-12 hours per day
- **Sleep Hours**: 4-12 hours per day
- **Attendance**: 0-100%
- **Part-time Job**: Yes or No

## Prediction Results

The app provides instant feedback:
- **85+**: Excellent performance
- **70-84**: Good performance
- **60-69**: Average performance
- **<60**: Below average

## Requirements

- Python 3.8+
- Streamlit 1.28.0
- Pandas 2.1.0
- Scikit-learn 1.3.0
- XGBoost 2.0.0
- Joblib 1.3.2
- NumPy 1.24.3

## Model

The application requires a trained model file: `student_performance_model.pkl`

This file should be placed in the project root directory before running the app.

## License

MIT License
