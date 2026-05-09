import pandas as pd
import plotly.express as px

# =========================
# CARREGAR DADES
# =========================
df = pd.read_csv("hotel_bookings.csv")

# =========================
# NETEJA
# =========================
df = df[df["adr"] >= 0]
df = df[df["adr"] < 1000]

df["children"] = df["children"].fillna(0)

df = df[(df["adults"] + df["children"] + df["babies"]) > 0]
df = df[(df["stays_in_week_nights"] + df["stays_in_weekend_nights"]) > 0]

# =========================
# GRÀFIC 1
# =========================
fig1 = px.histogram(
    df,
    x="is_canceled",
    color="is_canceled",
    title="Cancel·lacions globals",
    color_discrete_sequence=["#00b894", "#d63031"]
)

fig1.write_html("chart1.html", include_plotlyjs='cdn')

# =========================
# GRÀFIC 2
# =========================
fig2 = px.histogram(
    df,
    x="hotel",
    color="is_canceled",
    barmode="group",
    title="Cancel·lacions per tipus d'hotel",
    color_discrete_sequence=["#00b894", "#d63031"]
)

fig2.write_html("chart2.html", include_plotlyjs='cdn')

# =========================
# GRÀFIC 3
# =========================
top = df["country"].value_counts().nlargest(10).index

df_top = df[df["country"].isin(top)]

fig3 = px.histogram(
    df_top,
    x="country",
    color="is_canceled",
    barmode="group",
    title="Cancel·lacions per país",
    color_discrete_sequence=["#00b894", "#d63031"]
)

fig3.write_html("chart3.html", include_plotlyjs='cdn')

# =========================
# GRÀFIC 4
# =========================
fig4 = px.box(
    df,
    x="is_canceled",
    y="lead_time",
    title="Lead time vs cancel·lació",
    color="is_canceled",
    color_discrete_sequence=["#00b894", "#d63031"]
)

fig4.write_html("chart4.html", include_plotlyjs='cdn')

print("✅ gràfics exportats")