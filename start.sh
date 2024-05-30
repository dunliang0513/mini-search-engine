#!/bin/bash
export OMP_NUM_THREADS=1

echo "Installing required Python packges."
pip install -r requirements.txt

echo "Running index.py with Python 3."
python3 index.py

echo "Start Streamlit app"
streamlit run app.py