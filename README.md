#  Distributed Deadlock Detection using Wait-For Graph
Name: Madhumitha S
Register Number:22MID0154

##  Objective
The objective of this project is to simulate a **Distributed Deadlock Detection System** using the **Wait-For Graph (WFG) model** and implement a **probe-based Edge-Chasing algorithm**. The system is developed using **SimPy** for discrete-event simulation and **Streamlit** for interactive visualization.

###  Distributed Deadlock
A deadlock occurs when a set of processes are waiting for each other indefinitely, causing the system to halt. In distributed systems, deadlocks are more complex because processes are spread across multiple sites.

###  Wait-For Graph (WFG)
A Wait-For Graph is a directed graph where:

* Nodes represent processes (P1, P2, ...)
* Edges represent waiting relationships
  (Pi → Pj means Pi is waiting for Pj)

 A **cycle in the graph indicates a deadlock**

###  Edge-Chasing Algorithm
The Edge-Chasing algorithm detects deadlocks using **probe messages**:
* A probe is represented as:
  ```
  Probe (initiator, sender, receiver)
  ```
* The probe is passed along the wait-for graph
* If the probe returns to the initiator → **Deadlock Detected**

##  System Architecture
The system is divided into multiple components:
* **Processes:** Compete for shared resources
* **Sites:** Each site maintains a local Wait-For Graph
* **Simulation Engine:** SimPy handles process execution
* **Deadlock Detector:** Edge-Chasing algorithm
* **User Interface:** Streamlit dashboard

##  Technologies Used
* Python
* SimPy (Discrete Event Simulation)
* Streamlit (Web UI)
* NetworkX (Graph Visualization)
* Matplotlib

##  Implementation Details
### 🔹 Modules
* `models/`
  * `probe.py` → Defines probe messages
  * `site.py` → Maintains local wait-for graph
* `algorithms/`
  * `edge_chasing.py` → Implements probe-based deadlock detection
* `simulation.py`
  * Simulates distributed processes and resource waiting
* `utils/`
  * `graph_visualization.py` → Draws wait-for graph
* `app.py`
  * Streamlit UI for interaction

### 🔹 Working
1. Processes randomly request resources
2. Wait-for edges are created
3. Probe messages are initiated
4. Probes propagate through processes
5. If a cycle is found → Deadlock detected

## Sample Output
###  Probe Logs
```
 P2 waits for P4
 P1 waits for P3
 Probe(1 → 1 → 3)
 Probe(1 → 3 → 4)
 Probe(1 → 4 → 1)
```
###  Graph Output
* Nodes represent processes
* Directed edges represent waiting relationships

##  How to Run
### Step 1: Install dependencies
```
pip install -r requirements.txt
```
### Step 2: Run the application
```
python -m streamlit run app.py
```
### Step 3: Open in browser
`

###  Features
Distributed system simulation
Multiple sites with local WFG
Edge-Chasing deadlock detection
Real-time probe logging
Interactive UI using Streamlit
Graph visualization using NetworkX

###  Advantages
* Demonstrates real-world distributed deadlock detection
* Easy visualization of complex dependencies
* Modular and scalable architecture

###  Limitations
* Random simulation (not deterministic)
* Does not include resource allocation graphs
* Limited to small-scale systems

###  Future Enhancements
* Highlight deadlock cycle in graph
* Add resource-level modeling
* Implement other detection algorithms
* Improve UI with animations

###  Conclusion
This project successfully demonstrates distributed deadlock detection using the Wait-For Graph model and Edge-Chasing algorithm. The integration of SimPy and Streamlit enables both simulation and visualization of complex distributed interactions. The system effectively detects deadlocks through probe propagation and provides a clear graphical representation, making it useful for understanding distributed system behavior.

###  GitHub Repository
https://github.com/Madhumitha154-create/distributed-deadlock-detection

### Video link
https://drive.google.com/file/d/1YIv9a_LDaDL5mb5jP_s4gSnxoKAdbrTd/view?usp=drive_link
