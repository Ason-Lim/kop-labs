# Research Releases

**Version:** Official v1.0  
**Owner:** Institution Design Studio  
**Repository:** KOP Labs

## Purpose

This directory records official research baselines for Institution Engineering.

A Research Release does not replace Git history. It provides an institutional
record that identifies the purpose, included artifacts, governing milestone,
source commit, and next research stage of each baseline.

## Release Model

```text
Research Activity
        ↓
Sprint Completion
        ↓
Baseline Commit
        ↓
Research Release Record
        ↓
Annotated Git Tag
        ↓
Next Sprint
```

## Current Releases

| Release | Sprint | Title | Source Commit | Status |
|---|---|---|---|---|
| RELEASE-2026-001 | SPRINT-2026-001 | Research Governance Foundation | `7285c71` | Official Baseline |
| RELEASE-2026-002 | SPRINT-2026-002 | Research Program Baseline | `47bdab8` | Official Baseline |

## Rules

1. Each official research baseline shall have one release record.
2. A release record shall identify its exact source commit.
3. Release records added later do not rewrite the historical source commit.
4. Annotated tags shall point to the original source commits.
5. Later corrections shall be recorded through a new version or superseding record.
