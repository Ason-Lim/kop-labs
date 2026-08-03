# Reference Model

**Document ID:** RM-2026-003  
**Title:** Operational Research Framework  
**Version:** Official v1.1  
**Status:** Active Reference Model  
**Supersedes:** RM-2026-003 Official v1.0  
**Research Program:** RP-2026-001  
**Owner:** Institution Design Studio

## 1. Revision Basis

Version 1.1 incorporates evidence from EXP-2026-001, OE-2026-002, and
VAL-2026-002.

## 2. Revised Core Model

```text
Research Question
        ↓
Hypothesis
        ↓
Architecture Review
        ↓
Experiment Protocol
        ↓
Environment Verification
        ↓
Execution
        ↓
Operational Evidence
        ↓
Product Validation
        ↓
Methodology Validation
        ↓
Reference Model Revision
        ↓
Operational Improvement
        ↓
New Research Question
```

## 3. Research Objects

| Object | Purpose |
|---|---|
| RQ | Defines the research question |
| H | States a testable expectation |
| AR | Establishes architectural baseline |
| EXP | Defines a reproducible experiment protocol |
| OE | Records operational facts |
| VAL | Evaluates evidence |
| RM | Generalizes validated knowledge |
| FTR | Registers mature theory candidates |
| FP | Requests institutional adoption |

## 4. Environment Explicitness

> Every operational experiment shall explicitly identify and verify its
> execution environment before product results are interpreted.

## 5. Evidence Classification

Operational evidence shall distinguish product failure, environment failure,
test-harness failure, configuration failure, incomplete execution, and
successful execution.

## 6. Historical and Novel Evidence

> Reproducing prior engineering verification creates valid traceable evidence,
> but it shall not be misrepresented as newly discovered product evidence.

## 7. Experiment Lifecycle

```text
planned
    ↓
prepared
    ↓
environment_verified
    ↓
active
    ↓
completed
    ↓
validated
    ↓
archived
```

## 8. Evidence Maturity

```text
Static Repository Evidence
        ↓
Controlled Test Evidence
        ↓
Runtime Integration Evidence
        ↓
New Development Evidence
        ↓
Repeated Cross-Domain Evidence
        ↓
Cross-Platform Evidence
```

EXP-2026-001 reached Controlled Test Evidence.

## 9. Product and Methodology Validation

Product Validation asks whether product behavior satisfied experiment criteria.

Methodology Validation asks whether the framework produced useful, traceable,
and reproducible knowledge.

## 10. Foundation Relationship

A successful experiment does not directly produce Foundation Theory.

```text
Multiple Experiments
        ↓
Repeated Evidence
        ↓
Reference Model Stability
        ↓
Independent Review
        ↓
FTR Candidate
        ↓
FP
        ↓
Institutional Adoption
```

## 11. Recommended Next Cases

1. Goat
2. Cheese
3. Coffee
4. Wine

## 12. Conclusion

RM-2026-003 v1.1 adds Experiment, Environment Verification, Evidence
Classification, and the distinction between historical reproduction and new
product evidence.
