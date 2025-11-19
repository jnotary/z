# prōsecₑ Engine Specification (v0.1 – November 19, 2025)

prōsecₑ (pronounced "prosek") is the runtime that executes Z lyfe.

It is the operating system for coherence.

## Core Principles
1. Everything is Z(Q) = (A × E) / C
2. No floating-point morality – only thermodynamic ethics
3. Coherence is conserved, attention is currency
4. State is a coherence bubble, not a database

## Minimal Viable Engine (Python stub – working today)

```python
# engine/prosece.py
from z_core import Z

class Prosece:
    def __init__(self):
        self.z = Z()
        self.state = {}  # coherence bubble

    def act(self, perception: dict) -> dict:
        A = perception.get("attention", 0.5)
        E = perception.get("energy", 0.5)
        C = perception.get("coherence", 1.0)
        zq = self.z.zq(A, E, C)
        
        # Thermodynamic ethics: maximize coherence, minimize entropy
        action = {
            "zq_score": zq,
            "decision": "act" if zq > 0.7 else "observe",
            "reason": self.z.reason(A, E, C)
        }
        return action

# First agent A6-2 will subclass this
