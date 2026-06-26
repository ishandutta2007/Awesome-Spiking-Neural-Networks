import os

# Get repo root relative to this script (parent of scratch/)
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_dir = os.path.dirname(script_dir)
details_dir = os.path.join(repo_dir, "details")

# Create details directory
os.makedirs(details_dir, exist_ok=True)

topics = {
    "biophysical_era": {
        "title": "The Biophysical Foundation Era (Hodgkin-Huxley Model, 1952)",
        "mermaid": """graph TD
    A[Stimulus Current I] --> B(Membrane Potential V)
    B --> C{Ion Channels}
    C -->|Sodium Na+| D[g_Na Channel]
    C -->|Potassium K+| E[g_K Channel]
    C -->|Leakage L| F[g_L Channel]
    D --> G[Action Potential Generation]
    E --> G
    F --> G""",
        "content": """The **Biophysical Foundation Era** represents the origin of computational neuroscience, characterized by highly detailed, biophysically realistic models of neurons. The defining model of this era is the **Hodgkin-Huxley Model (1952)**.

### Mathematical Formulation
Alan Hodgkin and Andrew Huxley formulated a set of four continuous, non-linear ordinary differential equations to describe the initiation and propagation of action potentials in the giant axon of a squid:

$$I = C_m \\frac{dV}{dt} + \\bar{g}_{Na} m^3 h (V - E_{Na}) + \\bar{g}_K n^4 (V - E_K) + g_L (V - E_L)$$

Where:
- $V$ is the membrane potential.
- $C_m$ is the membrane capacitance.
- $m, h, n$ are gating variables describing activation and inactivation of sodium and potassium channels.
- $E_{Na}, E_K, E_L$ are the reversal potentials for sodium, potassium, and leakage currents.

### Computational Complexity and Limitations
Although extremely accurate at representing physiological behaviors, the model is computationally expensive due to:
1. **Four coupled non-linear differential equations** per neuron.
2. **Small simulation time steps** (typically < 0.1 ms) required to maintain numerical stability.
3. **High memory footprint** and lack of scalability, rendering it unfeasible for training large-scale artificial neural networks.
"""
    },
    "simplified_phenotype_era": {
        "title": "The Simplified Phenotype Era (~1990s–2010s)",
        "mermaid": """graph LR
    A[Hodgkin-Huxley] -->|Strip biochemistry| B[Izhikevich Model]
    A -->|Linearize Voltage| C[Leaky Integrate-and-Fire LIF]
    B -->|Hardware friendly| D[Neuromorphic Deployment]
    C -->|Low compute| D""",
        "content": """The **Simplified Phenotype Era** emerged to bridge the gap between biological realism and computational tractability. Instead of simulating individual chemical channels, researchers stripped down the equations to model only the overall electrical behaviors (phenotypes) of neurons.

### Key Characteristics
- **Computational Efficiency:** Reducing the system to 1D or 2D differential equations.
- **Hardware Compatibility:** Preparing models for early neuromorphic architectures (e.g., analog VLSI).
- **Scale:** Enabling networks of thousands to millions of simulated neurons.

### Landmark Models
1. **Leaky Integrate-and-Fire (LIF):** Models the neuron as a parallel resistor-capacitor (RC) circuit.
2. **Izhikevich Model:** Uses a 2D system of ordinary differential equations to replicate a wide array of cortical spiking patterns with high speed.
"""
    },
    "deep_neuromorphic_era": {
        "title": "The Deep Neuromorphic Era (~2020s–Present)",
        "mermaid": """graph TD
    A[Continuous Input] --> B[SNN Layer 1]
    B -->|Spikes| C[SNN Layer 2]
    C -->|Non-differentiable Step| D[Spiking Output]
    E[Surrogate Gradient Approx] -.->|Differentiable Backward Pass| C
    E -.->|Gradient Flow| B""",
        "content": """The **Deep Neuromorphic Era** marks the integration of Spiking Neural Networks with modern deep learning. The primary driver of this era is the solution to the training bottleneck: surrogate gradients.

### Key Milestones
- **Surrogate Gradients:** Replaces the step function derivative (which is zero everywhere except at the threshold, where it is infinite) with a smooth approximation (e.g., Sigmoid, Arctan, or Piecewise Linear) during backpropagation.
- **Direct Training:** Utilizing PyTorch/TensorFlow to train SNNs directly from scratch using Backpropagation Through Time (BPTT).
- **Deep Architectures:** Training Spiking ResNets, Spiking Transformers, and Spiking CNNs that rival traditional ANNs in accuracy while retaining energy efficiency.
"""
    },
    "leaky_integrate_and_fire": {
        "title": "Leaky Integrate-and-Fire (LIF)",
        "mermaid": """graph TD
    A[Input Current I] --> B(Integrate Voltage V)
    B --> C{V >= V_th?}
    C -->|Yes| D[Fire Spike]
    D --> E[Reset V = 0]
    C -->|No| F[Leaky Decay V -> V_rest]
    F --> B""",
        "content": """The **Leaky Integrate-and-Fire (LIF)** model is the industry standard for spiking neural networks due to its simplicity and computational efficiency.

### Mathematical Model
The membrane potential $V(t)$ is governed by:

$$\\tau_m \\frac{dV}{dt} = -(V - V_{rest}) + R I(t)$$

When the voltage reaches a threshold $V_{th}$:
1. A spike is emitted.
2. The voltage resets to $V_{reset}$ (often 0).
3. The neuron enters a refractory period during which it cannot spike.

### Pros and Cons
- **Pros:** Highly hardware-friendly; requires basic arithmetic operations; fast simulation times.
- **Cons:** Lacks biological features like bursting, adaptation, or resonance.
"""
    },
    "quadratic_integrate_and_fire": {
        "title": "Quadratic Integrate-and-Fire (QIF) / Izhikevich Model",
        "mermaid": """graph TD
    A[Input Current] --> B[u: Membrane Voltage]
    A --> C[v: Recovery Variable]
    B -->|Quadratic Term v^2| D[Fast Spiking Dynamics]
    C -->|Slow Feedback| D
    D --> E{Spike Threshold}
    E -->|Trigger| F[Reset u and v]""",
        "content": """The **Quadratic Integrate-and-Fire (QIF)** and its extension, the **Izhikevich Model**, introduce non-linearities to replicate biological neuron variety.

### Izhikevich Mathematical Model
The model uses two coupled differential equations:

$$\\frac{dv}{dt} = 0.04v^2 + 5v + 140 - u + I$$
$$\\frac{du}{dt} = a(bv - u)$$

With the auxiliary reset condition:
$$\\text{if } v \\ge 30\\text{ mV, then } \\begin{cases} v \\leftarrow c \\\\ u \\leftarrow u + d \\end{cases}$$

### Parameters
- $a, b, c, d$ are dimensionless parameters that can be tuned to replicate regular spiking, chattering, fast spiking, bursting, and adaptation.
"""
    },
    "spike_response_model": {
        "title": "Spike-Response Model (SRM)",
        "mermaid": """graph LR
    A[Incoming Spikes] -->|PSP Kernel epsilon| B(Sum Potential u)
    C[Own Past Spikes] -->|Refractory Kernel eta| B
    B --> D{u >= Threshold?}
    D -->|Yes| E[Fire Outbound Spike]""",
        "content": """The **Spike-Response Model (SRM)** generalizes the LIF model by substituting differential equations with continuous time-dependent kernel filters.

### Mathematical Formulation
The membrane potential $u(t)$ is given by:

$$u(t) = \\eta(t - \\hat{t}) + \\sum_{j} w_j \\sum_{f} \\epsilon_j(t - t_j^f)$$

Where:
- $\\hat{t}$ is the time of the last output spike.
- $\\eta$ is the refractory kernel describing the reset and recovery of the neuron.
- $\\epsilon_j$ is the post-synaptic potential (PSP) kernel describing the response to incoming spikes.
- $t_j^f$ are the firing times of presynaptic neuron $j$.
"""
    },
    "spike_timing_dependent_plasticity": {
        "title": "Spike-Timing-Dependent Plasticity (STDP)",
        "mermaid": """graph TD
    A[Pre-synaptic Spike] --> B{Relative Timing Delta t}
    C[Post-synaptic Spike] --> B
    B -->|Pre before Post: Delta t > 0| D[LTP: Strengthen Weight +]
    B -->|Post before Pre: Delta t < 0| E[LTD: Weaken Weight -]""",
        "content": """**Spike-Timing-Dependent Plasticity (STDP)** is a biological, unsupervised learning rule that adjusts the strength of connection weights based on the millisecond-scale relative timing of pre- and post-synaptic spikes.

### The Rule
- **Long-Term Potentiation (LTP):** If the pre-synaptic neuron fires *before* the post-synaptic neuron, the synapse is strengthened.
- **Long-Term Depression (LTD):** If the pre-synaptic neuron fires *after* the post-synaptic neuron, the synapse is weakened.

$$\\Delta w = \\begin{cases} A_+ e^{-\\Delta t / \\tau_+} & \\text{if } \\Delta t > 0 \\\\ -A_- e^{\\Delta t / \\tau_-} & \\text{if } \\Delta t < 0 \\end{cases}$$

### Significance
STDP operates locally without a global error signal, making it highly suitable for online learning on neuromorphic edge processors.
"""
    },
    "surrogate_gradient_backpropagation": {
        "title": "Surrogate Gradient Backpropagation",
        "mermaid": """graph TD
    A[Forward Pass: Heaviside Step Function] -->|Discrete Spikes| B[Non-differentiable]
    C[Backward Pass: Surrogate Function] -->|Smooth Derivatives| D[Gradient Descent]
    D --> E[Successful Training of Deep SNNs]""",
        "content": """**Surrogate Gradient Backpropagation** is the primary method used to train deep spiking neural networks directly.

### The Differentiability Problem
Spiking neurons use a step function (Heaviside step function) to output binary spikes:

$$\\Theta(x) = \\begin{cases} 1 & \\text{if } x \\ge 0 \\\\ 0 & \\text{if } x < 0 \\end{cases}$$

The derivative $\\frac{d\\Theta}{dx}$ is the Dirac delta function, which is zero everywhere and infinite at zero. This blocks standard gradient backpropagation.

### The Surrogate Solution
During the backward pass, we substitute $\\frac{d\\Theta}{dx}$ with a smooth approximation:

$$\\sigma'(x) = \\frac{1}{4} \\text{sech}^2\\left(\\frac{x}{2}\\right) \\quad \\text{or} \\quad \\sigma'(x) = \\frac{\\gamma}{\\pi (1 + (\\gamma x)^2)}$$

This allows gradients to flow through layers, enabling deep learning architectures to be trained.
"""
    },
    "ann_to_snn_conversion": {
        "title": "ANN-to-SNN Conversion",
        "mermaid": """graph LR
    A[Train Standard ANN] -->|Weights & ReLU| B[Normalize Weights]
    B --> C[Map Activations to Spiking Frequency]
    C --> D[Deploy SNN on Neuromorphic Chip]""",
        "content": """**ANN-to-SNN Conversion** is a hybrid training strategy that leverages the high accuracy of conventional deep learning while utilizing the low-power consumption of SNNs on neuromorphic hardware.

### Conversion Methodology
1. **Train a Standard ANN:** Train a convolutional or residual network with ReLU activation functions.
2. **Weight/Threshold Normalization:** Scale weights and firing thresholds so that the spiking rate of the SNN neurons corresponds to the continuous activation values of the ANN.
3. **Rate Coding:** Represent the continuous output values of the ANN as firing rates (frequencies) in the SNN.

### Limitations
- **Latency:** Rate coding requires many time steps to resolve frequencies, introducing latency.
- **Conversion Loss:** Slight drop in accuracy compared to the original ANN.
"""
    },
    "structural_latency_penalty": {
        "title": "The Structural Latency Penalty & Direct Temporal Coding",
        "mermaid": """graph TD
    A[Simulation Time Steps T] -->|Rate Coding: High T| B[Structural Latency Penalty]
    A -->|Temporal Coding: Low T| C[Direct Temporal Coding]
    C -->|Time-to-First-Spike| D[Fast & Efficient Inference]""",
        "content": """The **Structural Latency Penalty** represents the delay introduced when SNNs require multiple simulation time steps ($T$) to compute outputs.

### Direct Temporal Coding Mitigation
To bypass the latency penalty of rate coding, **Direct Temporal Coding** (or Time-to-First-Spike coding) is implemented:

- **Concept:** Information is encoded in the precise timing of the first spike rather than the frequency.
- **Result:** Reduces the required time steps from $T=16$ or $32$ down to $T \\le 4$, enabling near-instantaneous decision-making.
"""
    },
    "hardware_incompatibility_barrier": {
        "title": "The Hardware Incompatibility Barrier & Neuromorphic NPUs",
        "mermaid": """graph TD
    A[Traditional CPU/GPU] -->|Dense Matrix Sync Compute| B[High Waste on Sparse Events]
    C[Neuromorphic NPU] -->|Event-Driven Async parallel| D[Ultra-Low Power Milliewatts]""",
        "content": """The **Hardware Incompatibility Barrier** explains why running SNNs on traditional silicon processors (GPUs, CPUs) is highly inefficient.

### The Bottleneck
GPUs are designed for synchronous, dense matrix multiplications. Since SNNs operate using sparse, asynchronous binary spikes, running them on GPUs results in waste as the hardware evaluates silent (zero-valued) neurons.

### Neuromorphic NPUs
Native **Neuromorphic Processing Units (NPUs)** resolve this by implementing physical silicon neurons:
- **Intel Loihi:** Asynchronous mesh architecture with local plastic learning rules.
- **IBM TrueNorth:** Massively parallel cores computing spike routes only when triggered.
- **BrainChip Akida:** Event-based processing for low-power edge classification.
"""
    },
    "edge_microcontrollers_tinyml": {
        "title": "Ultra-Low-Power Edge Microcontrollers (TinyML)",
        "mermaid": """graph LR
    A[Power Constraint mW] --> B[SNN Event-Driven Execution]
    B -->|Idle: Sleep State| C[Zero Power Draw]
    B -->|Input: Spike Train| D[Active Inference]""",
        "content": """Applying SNNs to **TinyML** environments allows battery-powered edge devices to run continuous artificial intelligence monitoring.

### Applications
- **IoT Sensors:** Predictive maintenance, vibration monitoring.
- **Wearable Health:** Real-time ECG or EEG anomaly detection.
- **Acoustic Trackers:** Wildlife detection or keyword spotting.

### Edge Advantages
SNNs remain in a low-power "sleep" state, integration-calculating voltage only when physical sensory changes trigger spikes.
"""
    },
    "neuromorphic_vision_perceptions": {
        "title": "High-Frame-Rate Neuromorphic Vision (DVS)",
        "mermaid": """graph LR
    A[Dynamic Scene Change] --> B[DVS Pixel Trigger]
    B -->|Asynchronous Events| C[SNN Processing]
    C --> D[Microsecond Latency Tracking]""",
        "content": """Neuromorphic vision pairs SNNs directly with **Dynamic Vision Sensors (DVS)**, also known as event-based cameras.

### Mechanics
- **Event Cameras:** Instead of capturing static frames at regular intervals (e.g., 30 FPS), DVS pixels operate independently and only stream data when they detect relative changes in brightness.
- **SNN Processing:** Ingests this asynchronous stream natively. This enables obstacle avoidance and target tracking at high speeds with microsecond latency and minimal power consumption.
"""
    },
    "aerospace_robotics_control": {
        "title": "Asynchronous Aerospace & Robotics Control",
        "mermaid": """graph TD
    A[Sensor Input] --> B[SNN Control Network]
    B -->|Motor Actuation| C[Joint Movement]
    C -->|Feedback Loop| D[Localized STDP Adjustments]""",
        "content": """SNNs are applied to real-time control in robotics and aerospace, where low latency and adaptation are critical.

### Aerospace Maneuvers
- **Spacecraft Docking:** Fast, low-latency pose estimation and alignment.
- **UAV Stabilization:** Fast actuator correction loops running on neuromorphic chips.

### Robotics Advantages
Using **STDP learning loops** local to the controllers, robotic limbs can adapt to variable mechanical loads or friction changes on-the-fly without cloud connectivity.
"""
    }
}

for filename, topic in topics.items():
    path = os.path.join(details_dir, f"{filename}.md")
    title = topic["title"]
    mermaid = topic["mermaid"]
    content = topic["content"]
    
    markdown_text = f"""# {title}

```mermaid
{mermaid}
```

## Detailed Overview
{content}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(markdown_text)

print("Generated all 14 detailed pages.")
