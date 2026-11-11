import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation", layout="centered")
st.title("Hyperbolic Tangent (Tanh)")
st.write("Tanh is similar to the sigmoid function but, maps the input to values between -1 and 1.")

x = np.linspace(-6, 6, 400)
y = np.tanh(x)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, label="Tanh", color="red", linewidth=2)
ax.set_title("Tanh Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output (y)")
ax.grid(True)
ax.legend()
st.pyplot(fig)