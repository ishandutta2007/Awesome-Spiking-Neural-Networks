# The Structural Latency Penalty & Direct Temporal Coding

```mermaid
graph TD
    A[Simulation Time Steps T] -->|Rate Coding: High T| B[Structural Latency Penalty]
    A -->|Temporal Coding: Low T| C[Direct Temporal Coding]
    C -->|Time-to-First-Spike| D[Fast & Efficient Inference]
```

## Detailed Overview
The **Structural Latency Penalty** represents the delay introduced when SNNs require multiple simulation time steps ($T$) to compute outputs.

### Direct Temporal Coding Mitigation
To bypass the latency penalty of rate coding, **Direct Temporal Coding** (or Time-to-First-Spike coding) is implemented:

- **Concept:** Information is encoded in the precise timing of the first spike rather than the frequency.
- **Result:** Reduces the required time steps from $T=16$ or $32$ down to $T \le 4$, enabling near-instantaneous decision-making.

