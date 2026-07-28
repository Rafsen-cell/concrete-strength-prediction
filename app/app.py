import pandas as pd
import numpy as np
import joblib
import streamlit as st
import plotly.express as px
from utils.predictor import predict_strength


st.title("🏗️Concrete Compressive Strength Predictor")
st.write("Estimate concrete compressive strength based on its mix design")
model = joblib.load(r".\models\concrete_strength_model.pkl")
st.divider()

with st.sidebar:
    st.title("🏗️ About")
    st.markdown("""
**Model**

Random Forest Regressor

**Dataset**


""")
    st.link_button(url="https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength",label="Concrete Compressive Strength", use_container_width=True)
    
    st.markdown("""**Author**

Muhammad Rafly Husen Batubara""")
    st.link_button(url="https://github.com/Rafsen-cell", label="GitHub", use_container_width=True)
    st.divider()

    

with st.sidebar:
    st.subheader("📈 Model Performance")
    st.metric("R\u00B2 Score", "0.908")
    st.metric("MAE", "3.604")
    st.metric("RMSE", "4.932")
    st.divider()

with st.sidebar:
    st.subheader("📝 Description")
    st.write(
        "Predict the compressive strength of concrete from its mix design using a machine learning model."
    )
    st.divider()


with st.sidebar:
    st.warning(
        "This prediction is an estimate based on historical data and should not replace laboratory testing"
    )


st.subheader("Prediction Mode")
mode = st.radio(
    "Choose a prediction mode:",
    ["Single Prediction", "Batch Prediction (CSV)"]
)

if mode == "Single Prediction":
    st.subheader("📝Input Concrete Mix")

    col1, col2 = st.columns(2)

    with col1:
        cement = st.slider("Cement (Kg/m\u00B3): ",
                        min_value=102.0,
                        max_value=540.0,
                        value=278.6
                        )
        slag = st.slider("Slag (Kg/m\u00B3): ",
                        min_value=0.0,
                        max_value=359.4,
                        value=72.0
                        )
        fly_ash = st.slider("Fly Ash (Kg/m\u00B3): ",
                            min_value=0.0,
                            max_value=200.1,
                            value=55.5
                            )
        water = st.slider("Water (Kg/m\u00B3): ",
                        min_value=121.8,
                        max_value=247.0,
                        value=182.1
                        )
    with col2:
        superplasticizer = st.slider("Superplasticizer (Kg/m\u00B3): ",
                                    min_value=0.0,
                                    max_value=32.2,
                                    value=6.0
                                    )
        coarse_agg = st.slider("Coarse Aggregate (Kg/m\u00B3): ",
                            min_value=801.0,
                            max_value=1145.0,
                            value=974.4
                            )
        fine_agg = st.slider("Fine Aggregate (Kg/m\u00B3): ",
                            min_value=594.0,
                            max_value=992.6,
                            value=772.7
                            )
        age = st.slider("Age (days): ",
                        min_value=1.0,
                        max_value=365.0,
                        value=45.8
                        )


    input_data = pd.DataFrame({
        "Cement": [cement],
        "BlastFurnaceSlag": [slag],
        "FlyAsh": [fly_ash],
        "Water": [water],
        "Superplasticizer": [superplasticizer],
        "CoarseAggregate": [coarse_agg],
        "FineAggregate": [fine_agg],
        "Age": [age]
    })



    if st.button("🚀 Predict Strength", use_container_width=True):
        prediction = predict_strength(input_data)
        st.divider()

        st.subheader("🎯 Prediction Result")
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"Predicted strength:{prediction[0]:.2f} MPa")
        with col2:
            if prediction < 20:
                strength = "Low Strength"
            elif prediction < 40:
                strength = "Normal Strength"
            elif prediction < 60:
                strength = "High Strength"
            else:
                strength = "Ultran High Strength"
            st.info(f"Classification: {strength}")


        summary = pd.DataFrame({
            "Features": [
                "Cement",
                "BlastFurnaceSlag",
                "FlyAsh",
                "Water",
                "Superplasticizer",
                "CoarseAggregate",
                "FineAggregate",
                "Age"
            ],
            "Value": [
                cement,
                slag,
                fly_ash,
                water,
                superplasticizer,
                coarse_agg,
                fine_agg,
                age
            ]

        })

        st.subheader("📋 Input Summary")
        st.dataframe(summary,use_container_width=True, hide_index=True)



        engineered_feature = input_data[[
            'WaterCementRatio',
            'TotalBinder',
            'WaterBinderRatio',
            'TotalAggregate',
            'FineAggregateRatio',
            'CoarseAggregateRatio',
            'CementRatio',
            'SCM',
            'SCMPercentage',
            'LogAge'
        ]]

        st.subheader("🟢 Engineered Features")
        table = engineered_feature.T
        table.columns = ["Value"]
        st.dataframe(table.style.format("{:.2f}"))



        importance = model.feature_importances_
        feature_names = [
        "Cement",
        "BlastFurnaceSlag",
        "FlyAsh",
        "Water",
        "Superplasticizer",
        "CoarseAggregate",
        "FineAggregate",
        "Age",
        "WaterCementRatio",
        "TotalBinder",
        "WaterBinderRatio",
        "TotalAggregate",
        "FineAggregateRatio",
        "CoarseAggregateRatio",
        "CementRatio",
        "SCM",
        "SCMPercentage",
        "LogAge"
        ]
        feature_df = pd.DataFrame({
            "Features": feature_names,
            "Importance": importance
        })

        st.subheader("📊 Feature Importance")
        feature_df_sorted = feature_df.sort_values(
        by="Importance",
        ascending=True
        )
        fig = px.bar(
            feature_df_sorted,
            x="Importance",
            y="Features",
            orientation="h",
        )
        st.plotly_chart(fig, use_container_width=True)

if mode == "Batch Prediction (CSV)":
    uploaded_file = st.file_uploader(
        "Upload a CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Preview")
        st.dataframe(df.head())
        

    if st.button("Predict CSV"):
        prediction = predict_strength(df)
        df["PredictedStrength"] = prediction

        st.subheader("Prediction Result")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download Prediction",
            csv,
            "predictions.csv",
            "text/csv"
        )



st.caption(
    "This prediction is generated by a machine learning model and is intended for educational purposes only. It should not replace laboratory testing."
)

st.markdown("""
<hr>
<div style='text-align: center; color: gray; font-size: 14px;'>
Develop by Muhammad Rafly Husen Batubara<br>
Powered by Streamlit | Scikit-learn | Python
</div>
""", unsafe_allow_html=True)