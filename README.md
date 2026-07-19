# TGS-2025053922 - Certified Lean Six Sigma Yellow Belt (CLSSYB) Training

> **Course:** WSQ - Certified Lean Six Sigma Yellow Belt (CLSSYB) Training  
> **Course Code:** TGS-2025053922  
> **Register here:** https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-yellow-belt-clssyb-training.html

These are the hands-on lab exercises for the WSQ Certified Lean Six Sigma Yellow Belt (CLSSYB) Training course delivered by [Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/).

This repository contains **14 guided Lean Six Sigma Yellow Belt labs** (9 core and 5 elective), structured around the **DMAIC roadmap** and grounded in the Council for Six Sigma Certification (CSSC) Yellow Belt body of knowledge.

---

## Courseware

| Artifact | File |
|----------|------|
| **Slide deck** | `courseware/Certified Lean Six Sigma Yellow Belt (CLSSYB) Training-v7.pptx` (and `.pdf`) |
| **Learner Guide (Markdown)** | [LG-Certified Lean Six Sigma Yellow Belt (CLSSYB) Training.md](LG-Certified%20Lean%20Six%20Sigma%20Yellow%20Belt%20%28CLSSYB%29%20Training.md) |
| **Learner Guide (DOCX/PDF)** | `courseware/LG-Certified Lean Six Sigma Yellow Belt (CLSSYB) Training.docx` (and `.pdf`) |
| **Lesson Plan (DOCX/PDF)** | `courseware/LP-Certified Lean Six Sigma Yellow Belt (CLSSYB) Training.docx` (and `.pdf`) |
| **Lab Index** | [labs/README.md](labs/README.md) |
| **Tools and Templates** | [labs/tools.md](labs/tools.md) |

> **Note:** assessment papers, answer keys and trainer-only materials are intentionally not published in this repository.

---

## How to use

1. Read the Learner Guide first — it follows the same DMAIC order as the course.
2. Complete the core labs in order using the Contoso Service Desk scenario.
3. Complete the elective labs if time allows, or as post-course practice.
4. Keep every worksheet — the final lab combines them into one improvement package.
5. Review the 'Check your work' step at the end of each lab before moving on.

---

## Lab catalogue

### Foundations — Six Sigma Foundations

- [Lab 1 - Yellow Belt Role, Certification Paths, and Improvement Scenario](labs/lab-01-yellow-belt-role-certification-paths-and-improvement-scenari.md)

### Define — Scope the Problem

- [Lab 2 - Lean, Six Sigma, Waste, Voice of Customer, and Value](labs/lab-02-lean-six-sigma-waste-voice-of-customer-and-value.md)
- [Lab 3 - SIPOC, Process Mapping, Handoffs, and SME Support](labs/lab-03-sipoc-process-mapping-handoffs-and-sme-support.md)
- [Lab 4 - PDCA Small Improvement Project Charter](labs/lab-04-pdca-small-improvement-project-charter.md) *(elective)*
- [Lab 5 - DMAIC Overview, Problem Statement, Scope, and Stakeholders](labs/lab-05-dmaic-overview-problem-statement-scope-and-stakeholders.md)
- [Lab 11 - Affinity Diagram and Kano Analysis](labs/lab-11-affinity-diagram-and-kano-analysis.md) *(elective)*

### Measure — Quantify Performance

- [Lab 6 - Data Collection, KPIs, Check Sheets, and Basic Metrics](labs/lab-06-data-collection-kpis-check-sheets-and-basic-metrics.md)
- [Lab 12 - Value Stream Map and Takt Time](labs/lab-12-value-stream-map-and-takt-time.md) *(elective)*

### Analyze — Find the Root Cause

- [Lab 7 - Pareto, Run Charts, Variation, Yield, DPU, and DPMO](labs/lab-07-pareto-run-charts-variation-yield-dpu-and-dpmo.md)
- [Lab 8 - Root Cause Analysis with 5 Whys, Fishbone, and Evidence](labs/lab-08-root-cause-analysis-with-5-whys-fishbone-and-evidence.md)

### Improve — Fix the Cause

- [Lab 9 - Countermeasures, 5S, Mistake Proofing, Standard Work, and Kaizen](labs/lab-09-countermeasures-5s-mistake-proofing-standard-work-and-kaizen.md)
- [Lab 13 - Solution Selection Matrix, Benchmarking, and FMEA](labs/lab-13-solution-selection-matrix-benchmarking-and-fmea.md) *(elective)*

### Control — Hold the Gain

- [Lab 10 - Control Plan, A3 Summary, Handover, and Certification Readiness](labs/lab-10-control-plan-a3-summary-handover-and-certification-readiness.md)
- [Lab 14 - Descriptive Statistics and Implementation Planning](labs/lab-14-descriptive-statistics-and-implementation-planning.md) *(elective)*

---

## Repository structure

```
courseware/          slide deck (PPTX + PDF), Learner Guide, Lesson Plan
  archive/           superseded deck versions
  assets/            diagrams and images used by the deck
labs/                the 14 lab worksheets + index + toolkit
LG-Certified Lean Six Sigma Yellow Belt (CLSSYB) Training.md
                     Learner Guide (Markdown mirror of the DOCX)
.claude/skills/courseware-build/build/
                     single-source generators: one content module
                     drives the deck, LP, LG and labs
```

All artifacts are generated from `course_data.py` + `data_domainN.py`, so the deck, Lesson Plan, Learner Guide and labs stay 100% aligned.

## Interactive tools

- [SIPOC & Process Map](https://alfredang.github.io/sipoc/) — guided SIPOC, swimlane and handoff table
- [5 Whys](https://alfredang.github.io/5whys/) — root-cause chain builder
- [Fishbone Diagram](https://alfredang.github.io/fishbone/) — Ishikawa cause-and-effect builder
- [Pareto Chart](https://alfredang.github.io/paretochart/) — collaborative team brainstorm, vote and live chart
- [NovaSPC](https://alfredang.github.io/novaspc/) — run charts, SPC charts and process capability

## Reference

- [Council for Six Sigma Certification - Lean Six Sigma Yellow Belt Certification](https://www.sixsigmacouncil.org/lean-six-sigma-yellow-belt-certification/)
- [Course registration page](https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-yellow-belt-clssyb-training.html)
- [labs/tools.md](labs/tools.md) - templates, formulas and free tools used in the labs

## Free tools used

- Microsoft Excel, LibreOffice Calc, or Google Sheets
- Draw.io / diagrams.net for SIPOC, process maps and fishbone diagrams
- The interactive tools listed above
- Whiteboard or sticky notes for facilitation activities

---

*Version v7 · 20 July 2026 · © 2026 Tertiary Infotech Academy Pte Ltd*
