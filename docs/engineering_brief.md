# Suspension Rocker Engineering Brief

**Author:** Chamika Nimsara  
**Software:** SolidWorks 2023  
**Completed:** 5 October 2026

> **6.72% lower rocker mass**, with similar computed bump stress and approximately **32% higher maximum displacement**. The iteration demonstrates a measured mass/stiffness trade-off.

## Objective and design

Develop a conceptual front-corner pushrod suspension rocker that redirects input movement into damper compression, then evaluate its kinematics, assembly packaging and structural response. The 6061-T6 body uses 96 mm and 82 mm pickup radii, a 15 mm plate and a 30 mm pivot hub. A Ø36 mm through-window provides the mass-reduction iteration while preserving the pickup geometry.

## Engineering method

Parametric modelling and assembly mates established the mechanism, pivot stack and linkage joints. A vertical guided input was swept through ±30 mm to measure damper travel. Linear elastic rocker-only FEA used distributed bearing loads, a hinged pivot constraint and a small angular-reference fixture.

Baseline studies covered ride, bump, droop and reverse loading; optimized studies covered bump and reverse. Bump meshes were refined from **1.5/0.3 mm** to **1.2/0.24 mm** maximum/minimum sizes.

## Key results

| Metric | Baseline | Optimized |
|---|---:|---:|
| Rocker mass | 613.86 g | 572.63 g |
| Bump stress, matched mesh | 82.43 MPa | 83.80 MPa |
| Bump displacement, matched mesh | 0.04651 mm | 0.06127 mm |
| Bump stress, fine mesh | 85.14 MPa | 83.87 MPa |
| Reverse stress, matched mesh | 31.60 MPa | 31.30 MPa |

**Load cases:** bump at +30 mm with an assumed 6 kN vertical input; reverse at ride with a 2 kN reversed input. Stress is maximum nodal von Mises; displacement is maximum resultant URES. Matched mesh is 1.5/0.3 mm; fine mesh is 1.2/0.24 mm.

At ride, the measured local motion ratio is approximately **0.80**. The full sweep requires **21.19 mm damper compression** and **27.33 mm extension**, with the ratio decreasing toward bump. Final bump refinement changed stress by **3.29%** for the baseline and **0.084%** for the optimized body; displacement changed by less than **0.1%** in both.

The author confirmed smooth assembly movement and no remaining interferences at ride, bump and droop after eight known thread-envelope overlaps were ignored. These were discrete-position checks, not continuous collision verification.

## Interpretation and scope

The **41.23 g mass saving** increases compliance: matched-mesh bump displacement rises **31.74%**, while stress rises **1.66%**. The small fine-mesh stress difference is insufficient to claim improved strength.

Guided input travel is a wheel-motion surrogate, not a complete suspension model, and the ratio departs from the initial constant-ratio target. The work includes nominal part/assembly drawings and a BOM. Fatigue, hardware and chassis strength, manufacturing fits/tolerances and physical testing remain outside this concept study.

## Supporting project material

- [Optimized assembly image](../Images/evidence/optimized_assembly.png)
- [Mass comparison](../Plots/mass_comparison.png)
- [Matched-mesh stress and displacement comparison](../Plots/matched_mesh_comparison.png)
- [Motion-ratio curve](../Plots/motion_ratio.png)
- [Mesh-refinement comparison](../Plots/mesh_convergence.png)
- [Rocker drawing](../Drawings/Rocker_Optimized.pdf) and [assembly drawing](../Drawings/Rocker_Assembly_Optimized.pdf)
- [Full engineering documentation](../README.md#read-the-engineering-work)

*Portfolio concept based on CAD measurements and idealized static analysis. Not a manufacturing release.*
