from preswald import text, plotly, connect, get_df, table, query, slider, alert, button, selectbox
import pandas as pd
import plotly.express as px

# Load the CSV
connect()
df = get_df("imdb_top_5000_tv_shows_csv")

# SQL query
sql = 'SELECT * FROM imdb_top_5000_tv_shows WHERE "AVERAGERATING" > 8 AND "AVERAGERATING" < 9'
filtered_df = query(sql, "imdb_top_5000_tv_shows")
text("# My Data")
table(filtered_df, title="Filtered Data")

# Slider and dynamic filtering
threshold = slider("Threshold", min_val=0, max_val=10, default=8)
button(label="Click Me!")
alert(message="This is an alert!", level="critical")
choice = selectbox(
    label="Choose Dataset",
    options=["Dataset A", "Dataset B", "Dataset C"]
)
table(df[df["AVERAGERATING"] > threshold], title="Dynamic Data View")

# Create a scatter plot
fig = px.scatter(df, x="PRIMARYTITLE", y="DIRECTORS", color="GENRES")
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig.update_layout(template='plotly_white')
plotly(fig)

# Final table view
print(f"User selected: {choice}")
table(df)
