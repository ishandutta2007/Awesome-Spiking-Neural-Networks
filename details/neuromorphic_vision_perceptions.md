# High-Frame-Rate Neuromorphic Vision (DVS)

```mermaid
graph LR
    A[Dynamic Scene Change] --> B[DVS Pixel Trigger]
    B -->|Asynchronous Events| C[SNN Processing]
    C --> D[Microsecond Latency Tracking]
```

## Detailed Overview
Neuromorphic vision pairs SNNs directly with **Dynamic Vision Sensors (DVS)**, also known as event-based cameras.

### Mechanics
- **Event Cameras:** Instead of capturing static frames at regular intervals (e.g., 30 FPS), DVS pixels operate independently and only stream data when they detect relative changes in brightness.
- **SNN Processing:** Ingests this asynchronous stream natively. This enables obstacle avoidance and target tracking at high speeds with microsecond latency and minimal power consumption.

