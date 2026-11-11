import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sigmoid Activation", layout="centered")
st.title("Sigmoid Function")
st.write("The sigmoid function maps the input (x axis) to values between 0 and 1.")

x = np.linspace(-6, 6, 400)
y = 1 / (1 + np.exp(-x))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, label="Sigmoid", color="green", linewidth=2)
ax.set_title("Sigmoid Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output (y)")
ax.grid(True)
ax.legend()
st.pyplot(fig)