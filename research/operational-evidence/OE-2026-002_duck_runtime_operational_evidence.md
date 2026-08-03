# Operational Evidence

**Document ID:** OE-2026-002  
**Title:** Duck Runtime Operational Evidence  
**Version:** Official v1.0  
**Status:** Completed  
**Experiment:** EXP-2026-001  
**Platform:** Commerce AI Platform  
**Owner:** Institution Design Studio

## 1. Purpose

This document records verified operational facts produced by EXP-2026-001.

## 2. Evidence Source

Evidence was generated from actual command execution in:

```text
/Users/mom/commerce_ai_generator
```

| Item | Value |
|---|---|
| Python executable | `.venv/bin/python` |
| pytest executable | `.venv/bin/pytest` |
| Python version | 3.14.6 |
| pytest version | 9.1.1 |
| Plugin | anyio 4.13.0 |
| Repository root | `/Users/mom/commerce_ai_generator` |
| Baseline commit | `39ce15d` |

## 3. Initial Environment Evidence

The first direct test execution failed during collection with:

```text
ModuleNotFoundError: No module named 'app'
```

The failure occurred before Duck tests executed and was classified as an
environment configuration issue.

## 4. Environment Correction

Verified approaches:

- `python -m pytest`
- `PYTHONPATH=. python -m pytest`
- `pytest.ini` with `pythonpath = .`

Final configuration:

```ini
[pytest]
pythonpath = .
testpaths = tests
```

## 5. Import Evidence

```text
app import: PASS
DuckKnowledgeProvider import: PASS
```

## 6. Duck Domain Test Evidence

Command:

```bash
python -m pytest tests/services/food/knowledge/meat/duck -v
```

Result:

```text
90 passed
```

## 7. Registry Integration Evidence

Command:

```bash
python -m pytest   tests/services/food/knowledge/test_duck_registry_integration.py   -v
```

Result:

```text
6 passed
```

Verified cases:

- Duck provider is registered;
- default provider order includes Duck;
- resolution by category ID;
- resolution by product name;
- registry data loads;
- registered provider analyzes product.

## 8. Reproduction Evidence

The Duck suite was repeated with explicit `PYTHONPATH=.` and then again through
the repository `pytest.ini` configuration.

Both repeated executions returned:

```text
90 passed
```

## 9. Evidence Summary

| Evidence Item | Result |
|---|---|
| Virtual environment active | Verified |
| pytest available | Verified |
| App import | PASS |
| Duck provider import | PASS |
| Duck domain tests | 90/90 PASS |
| Duck registry integration | 6/6 PASS |
| Total verified tests | 96/96 PASS |
| Reproducible rerun | PASS |
| Environment deviation recorded | Yes |
| Unresolved Duck failure | None observed |

## 10. Limitations

This evidence does not independently verify production traffic, external APIs,
UI behavior, complete recommendation-ranking integration, other domains, or
longitudinal stability.

## 11. Research Observation

Environment configuration is part of operational evidence. The same code can
appear to fail or pass depending on whether the execution environment is
explicitly defined and reproducible.

## 12. Closing Statement

OE-2026-002 records 96 successful Duck-related tests and the environment
correction required to make the execution reproducible.
