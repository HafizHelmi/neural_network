import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReLU Activation", layout="centered")

st.title("Rectified Linear Unit (ReLU)")
st.write("ReLU allows only positive values to pass through it. The negative values are mapped to zero.")

# Render the mathematical formula
st.latex(r"f(x) = \max(0, x)")

# 1. Range slider for the graph axis
x_range = st.slider("Graph x-axis range", min_value=-10.0, max_value=10.0, value=(-6.0, 6.0), step=0.1)

# 2. Standard slider for the specific input value
selected_x = st.slider("Choose an input x", min_value=x_range[0], max_value=x_range[1], value=0.0, step=0.1)

# Data arrays and computation
x = np.linspace(x_range[0], x_range[1], 400)
y = np.maximum(0, x)
calculated_y = np.maximum(0, selected_x)

# Create the plot
fig, ax = plt.subplots(figsize=(7, 4))

# Plot the main curve
ax.plot(x, y, label="ReLU", color="blue", linewidth=2)[cite: 56]

# Plot the interactive dot based on the user's slider input
ax.plot(selected_x, calculated_y, 'o', color="darkorange", markersize=8, label="Selected input")

# Chart formatting
ax.set_title("ReLU Activation Function")[cite: 56]
ax.set_xlabel("Input (x)")[cite: 56]
ax.set_ylabel("Output (y)")[cite: 56]
ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
ax.axhline(0, color='gray', linewidth=0.8) 
ax.legend()

# Display the plot
st.pyplot(fig)

# Display the calculated metrics
st.write("Calculated output")
st.markdown(f"## {calculated_y:.4f}")
st.write(f"For x = {selected_x}, ReLU(x) = {calculated_y:.4f}.")
