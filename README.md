# AI-Based Electricity Fraud Detection and Inspection Prioritization System

End-to-end project: 
SGCC electricity consumption data 
-> preprocessing -> feature engineering 
-> ML fraud model -> rule engine 
-> risk scoring 
-> Streamlit app 
-> SQL/Power BI.

## Setup
1. Put the downloaded SGCC CSV in `data/raw/`.
2. Update `DATA_FILE` in `config.py` with the exact filename.
3. Install dependencies: `pip install -r requirements.txt`
4. Train: `python -m src.pipeline`
5. Run: `streamlit run app/app.py`
