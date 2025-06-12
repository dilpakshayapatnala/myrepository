import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌱", layout="centered")

st.title("🌱 Household Carbon Footprint Calculator")
st.markdown("Estimate your household's yearly carbon emissions and discover ways to reduce them.")

# -----------------------
# 🔹 User Inputs
# -----------------------
st.header("📥 Enter Your Household Data")

electricity = st.number_input("Monthly Electricity Use (kWh):", min_value=0.0, format="%.2f")
travel = st.number_input("Weekly Travel Distance by Car/Bus/Bike (km):", min_value=0.0, format="%.2f")
air_travel_count = st.number_input("No. of Flights in Last 3 Months:", min_value=0, step=1)
lpg_used = st.radio("Do you use LPG for cooking?", options=["yes", "no"])

# -----------------------
# 🔹 Emission Factors (kg CO₂)
# -----------------------
factors = {
    "electricity": 0.233,   # per kWh
    "travel": 0.21,         # per km
    "air_travel": 0.15,     # per km (assumed 1000 km per flight)
    "lpg": 2.98             # per kg of LPG
}

# -----------------------
# 🔘 Button to Show Results
# -----------------------
if st.button("🔍 Show Results"):
    # -----------------------
    # 🔹 Calculations
    # -----------------------
    annual_electricity = electricity * 12
    annual_travel = travel * 52
    air_distance = air_travel_count * 1000
    lpg_emissions = factors["lpg"] * 14.2 * 6 if lpg_used == "yes" else 0

    emissions = {
        "Electricity": annual_electricity * factors["electricity"],
        "Travel": annual_travel * factors["travel"],
        "Air Travel": air_distance * factors["air_travel"],
        "LPG": lpg_emissions
    }

    total = sum(emissions.values())

    st.header("📉 Results")
    st.subheader(f"🧮 Estimated Annual Carbon Footprint: `{total:.2f} kg CO₂`")

    # Tips
    st.subheader("💡 Tips to Reduce Emissions:")
    tips = [
        "1. Turn off unused lights and appliances.",
        "2. Prefer walking, cycling, or public transport.",
        "3. Use efficient cooking practices to save LPG."
    ]
    if air_travel_count > 0:
        tips.insert(2, "3. Reduce air travel when possible.")
    for tip in tips[:4 if air_travel_count > 0 else 3]:
        st.markdown(f"- {tip}")

    # Chart
    st.subheader("📊 Emissions Breakdown")
    categories = list(emissions.keys())
    values = list(emissions.values())

    fig, ax = plt.subplots(figsize=(7, 3))
    ax.plot(categories, values, marker='o', linestyle='-', color='green')
    ax.set_ylabel("kg CO₂/year")
    ax.set_title("Emissions by Source")
    ax.grid(True)
    st.pyplot(fig)
else:
    st.info("Fill in the values above and click **Show Results** to view your carbon footprint.")
