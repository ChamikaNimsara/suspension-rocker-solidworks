# Mass reduction and interpretation

The optimization was a single geometric iteration: a Ø36 mm through-window was added at x=-40 mm, y=+30 mm relative to O. Pickup locations, hub and plate thickness were retained so the assemblies use the same mechanism geometry.

Removing material reduces mass, but also reduces the area and bending stiffness through which loads flow. The correct comparison therefore includes mass, stress and displacement under matching boundary conditions.

## Quantified trade-off

| Metric | Baseline | Optimized | Change |
|---|---:|---:|---:|
| Mass | 613.86 g | 572.63 g | -41.23 g / -6.72% |
| Volume | 227,354.57 mm³ | 212,086.43 mm³ | -15,268.14 mm³ |
| Bump stress, 1.5/0.3 mm mesh | 82.43 MPa | 83.80 MPa | +1.66% |
| Bump URES, 1.5/0.3 mm mesh | 0.04651 mm | 0.06127 mm | +31.74% |
| Reverse stress, 1.5/0.3 mm mesh | 31.60 MPa | 31.30 MPa | -0.95% |
| Reverse URES, 1.5/0.3 mm mesh | 0.01734 mm | 0.02256 mm | +30.10% |

![Mass](../Plots/mass_comparison.png)
![Matched mesh comparison](../Plots/matched_mesh_comparison.png)

At the fine meshes, bump stress is 85.14 MPa baseline and 83.87 MPa optimized, while URES is 0.04655 versus 0.06128 mm. The slight stress decrease in that comparison should not be presented as a robust improvement in strength: coarse-to-fine baseline variation is larger than the between-design difference, and peak nodal stress depends on discretization and local load distribution.

The most defensible conclusion is **6.72% lower rocker body mass, similar computed bump stress, and roughly 32% greater maximum bump displacement** under these idealized cases. Whether that extra compliance is acceptable needs a relative pickup-deflection requirement and a full suspension compliance budget.

## Engineering judgment

The iteration demonstrates the workflow from baseline geometry to a tested mass change. It is not topology optimization or proof that this is the best possible geometry. A second iteration could investigate window shape, blended transitions, fillets and hub proportions, but would need to preserve machinability and reconsider fatigue/contact behaviour. Such changes were not performed in this project.
