import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation", layout="centered")

st.title("Hyperbolic Tangent (Tanh)")
st.write("Tanh is similar to the sigmoid function but, maps the input to values between -1 and 1.")

# Render the mathematical formula
st.latex(r"f(x) = \tanh(x)")

# 1. Range slider for the graph axis
x_range = st.slider("Graph x-axis range", min_value=-10.0, max_value=10.0, value=(-6.0, 6.0), step=0.1)

# 2. Standard slider for the specific input value
selected_x = st.slider("Choose an input x", min_value=x_range[0], max_value=x_range[1], value=0.0, step=0.1)

# Data arrays and computation
x = np.linspace(x_range[0], x_range[1], 400)
y = np.tanh(x)
calculated_y = np.tanh(selected_x)

# Create the plot
fig, ax = plt.subplots(figsize=(7, 4))

# Plot the main curve
ax.plot(x, y, label="Tanh", color="red", linewidth=2)

# Plot the interactive dot based on the user's slider input
ax.plot(selected_x, calculated_y, 'o', color="darkorange", markersize=8, label="Selected input")

# Chart formatting
ax.set_title("Tanh Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output (y)")
ax.grid(color='lightgray', linestyle='-', linewidth=0.5)
ax.axhline(0, color='gray', linewidth=0.8) 
ax.legend()

# Display the plot
st.pyplot(fig)

# Display the calculated metrics
st.write("Calculated output")
st.markdown(f"## {calculated_y:.4f}")
st.write(f"For x = {selected_x}, Tanh(x) = {calculated_y:.4f}.")
