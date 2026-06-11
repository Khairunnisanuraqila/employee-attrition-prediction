import streamlit as st
import joblib
import numpy as np

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon="📊",
    layout="wide"
)

# ======================
# LOAD MODEL
# ======================
model = joblib.load("model.pkl")

# ======================
# CUSTOM CSS
# ======================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.metric-card {
    background: #1E293B;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

.metric-title {
    color: #94A3B8;
    font-size: 14px;
}

.metric-value {
    color: white;
    font-size: 30px;
    font-weight: bold;
}

.result-success {
    background-color: #064E3B;
    padding: 20px;
    border-radius: 15px;
    color: white;
}

.result-danger {
    background-color: #7F1D1D;
    padding: 20px;
    border-radius: 15px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ======================
# SIDEBAR
# ======================
with st.sidebar:

    st.title("📚 Project Info")

    st.markdown("""
### Kelompok

👩 Aqila - KNN

👩 Shara - SVM

👩 Fataya - Random Forest

---

### Dataset

Employee Attrition Dataset

---

### Best Model

🌲 Random Forest

Accuracy: **91.00%**
""")

# ======================
# HEADER
# ======================
st.title("📊 Employee Attrition Prediction")

st.markdown("""
Prediksi kemungkinan seorang karyawan keluar dari perusahaan menggunakan Machine Learning.
""")

st.divider()

# ======================
# KPI CARDS
# ======================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Total Employee</div>
        <div class="metric-value">10,000</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Attrition</div>
        <div class="metric-value">903</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Attrition Rate</div>
        <div class="metric-value">9.03%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Best Model</div>
        <div class="metric-value">RF</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ======================
# MODEL COMPARISON
# ======================
st.subheader("📈 Model Comparison")

comparison = {
    "Model": ["KNN", "SVM", "Random Forest"],
    "Accuracy": ["90.85%", "90.95%", "91.00%"]
}

st.table(comparison)

st.divider()

# ======================
# INPUT FORM
# ======================
st.subheader("👤 Employee Information")

col1, col2 = st.columns(2)

with col1:
    monthly_income = st.number_input(
        "Monthly Income",
        min_value=0,
        value=5000
    )

    age = st.number_input(
        "Age",
        min_value=18,
        value=30
    )

    years_at_company = st.number_input(
        "Years At Company",
        min_value=0,
        value=3
    )

with col2:
    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=0.0,
        value=5.0
    )

    training_hours = st.number_input(
        "Training Hours Last Year",
        min_value=0,
        value=10
    )

# ======================
# PREDICTION BUTTON
# ======================
if st.button(
    "🔍 Predict Attrition",
    use_container_width=True
):

    data = np.array([
        [
            monthly_income,
            distance_from_home,
            age,
            training_hours,
            years_at_company
        ]
    ])

    prediction = model.predict(data)

    st.write("")
    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.markdown("""
        <div class="result-danger">
            <h2>⚠ HIGH ATTRITION RISK</h2>
            <p>
            Employee has a high probability
            of leaving the company.
            </p>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result-success">
            <h2>✅ LOW ATTRITION RISK</h2>
            <p>
            Employee is likely to stay
            in the company.
            </p>
        </div>
        """, unsafe_allow_html=True)