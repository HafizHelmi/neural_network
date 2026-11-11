import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReLU Activation", layout="centered")
st.title("Rectified Linear Unit (ReLU)")
st.write("ReLU allows only positive values to pass through it. The negative values are mapped to zero.")

x = np.linspace(-6, 6, 400)
y = np.maximum(0, x)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, label="ReLU", color="blue", linewidth=2)
ax.set_title("ReLU Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output (y)")
ax.grid(True)
ax.legend()
st.pyplot(fig)