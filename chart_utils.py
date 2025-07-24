import altair as alt
import pandas as pd

def bookings_chart(df: pd.DataFrame):
    chart = alt.Chart(df).mark_line(point=True).encode(
        x="date:T",
        y="bookings:Q",
        tooltip=["date", "bookings"]
    ).properties(
        width=700,
        height=400,
        title="📈 Booking Demand Trend"
    ).interactive()

    return chart
