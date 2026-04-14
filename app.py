import streamlit as st
import simpy
from simulation import DistributedSimulation
from utils.graph_visualization import draw_graph

# 🔷 TITLE
st.title(" Distributed Deadlock Detection")
st.markdown("###  Edge-Chasing Algorithm in Distributed Systems")

# 🔷 NAME
st.markdown("""
**Name:** Madhumitha S  
**Reg.No:** 22MID0154  
""")

# 🔷 LOG AREA
st.subheader(" Probe Messages")
log_area = st.empty()

# 🔷 INPUTS
num_sites = st.slider("Number of Sites", 2, 5, 3)
proc_per_site = st.slider("Processes per Site", 2, 5, 3)



# 🔷 RUN BUTTON
if st.button("▶ Run Simulation"):

    env = simpy.Environment()
    sim = DistributedSimulation(env, num_sites, proc_per_site)

    sim.set_logger(log_area)

    env.process(sim.generate_waits())
    env.run(until=5)

    

    deadlock = sim.detect_deadlock()

    st.subheader(" Wait-For Graph")
    fig = draw_graph(sim.sites)
    st.pyplot(fig)

    if deadlock:
        st.error("💥 Deadlock Detected!")
    else:
        st.success("✅ No Deadlock")