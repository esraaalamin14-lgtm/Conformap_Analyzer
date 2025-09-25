import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

st.set_page_config(page_title="ConforMap Analyzer", layout="wide")

st.title("🔷 ConforMap Analyzer")
st.subheader("Visualize conformal mappings in the complex plane")

st.markdown("Enter a Möbius transformation of the form: `f(z) = (az + b)/(cz + d)`")

# Input fields
a = st.number_input("Coefficient a", value=1.0)
b = st.number_input("Coefficient b", value=2.0)
c = st.number_input("Coefficient c", value=1.0)
d = st.number_input("Coefficient d", value=1.0)

# Generate grid
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Möbius transformation
def mobius_transform(z, a, b, c, d):
    return (a*z + b) / (c*z + d)

Z_transformed = mobius_transform(Z, a, b, c, d)

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].scatter(Z.real, Z.imag, s=1)
ax[0].set_title("Original Domain")
ax[0].set_xlabel("Re(z)")
ax[0].set_ylabel("Im(z)")
ax[0].grid(True)

ax[1].scatter(Z_transformed.real, Z_transformed.imag, s=1, color='red')
ax[1].set_title("Transformed Domain")
ax[1].set_xlabel("Re(f(z))")
ax[1].set_ylabel("Im(f(z))")
ax[1].grid(True)

st.pyplot(fig)

st.markdown("✅ Transformation complete. You can adjust coefficients and re-run.")
