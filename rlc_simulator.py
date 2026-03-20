import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Page setup
st.set_page_config(page_title="RLC Simulator", layout="wide")

st.title("🔌 RLC Frequency Response Simulator")

# Sidebar
st.sidebar.header("⚙️ Input Parameters")

R = st.sidebar.number_input("Resistance (Ohms)", value=100.0)
L = st.sidebar.number_input("Inductance (H)", value=0.01)

# ✅ Flexible input for Capacitance
C_input = st.sidebar.text_input("Capacitance (F)", "1e-6")

try:
    C = float(C_input)
except:
    st.sidebar.error("Enter valid value (e.g., 1e-6 or 0.000001)")
    C = 1e-6

# Circuit type
circuit_type = st.sidebar.selectbox("Circuit Type", ["Series", "Parallel"])

# Frequency range
f = np.logspace(1, 6, 500)
w = 2 * np.pi * f

# Impedance calculation
if circuit_type == "Series":
    Z = R + 1j * (w * L - 1 / (w * C))
else:
    Z = 1 / (1 / R + 1 / (1j * w * L) + 1j * w * C)

magnitude = np.abs(Z)
phase = np.angle(Z)

# Resonance frequency
f0 = 1 / (2 * np.pi * np.sqrt(L * C))

# Q factor
if circuit_type == "Series":
    Q = (1 / R) * np.sqrt(L / C)
else:
    Q = R * np.sqrt(C / L)

# Bandwidth
BW = f0 / Q

# Display metrics
col1, col2, col3 = st.columns(3)
col1.metric("Resonance Frequency (Hz)", f"{f0:.2f}")
col2.metric("Q Factor", f"{Q:.2f}")
col3.metric("Bandwidth (Hz)", f"{BW:.2f}")

# Graphs
col4, col5 = st.columns(2)

# Magnitude plot
with col4:
    fig, ax = plt.subplots()
    ax.semilogx(f, magnitude)
    ax.axvline(f0, linestyle='--')
    ax.set_title("Magnitude Response")
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude")
    st.pyplot(fig)

# Phase plot
with col5:
    fig2, ax2 = plt.subplots()
    ax2.semilogx(f, phase)
    ax2.axvline(f0, linestyle='--')
    ax2.set_title("Phase Response")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Phase (radians)")
    st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("💡 Interactive visualization of RLC circuits for educational and engineering applications.")