# Mechanism physics and kinematics

## Displacement and force transformation

For a small rotation dθ, the velocity of a rocker pickup is perpendicular to the arm from O. Its projection along the connected link axis determines the axial motion transferred through that link. The rigid pushrod retains its length, so the velocities of A and C have equal projections along AC; damper compression depends on the relative axial velocity of B and D. The effective arm is therefore

$$e=|\mathbf r\times\hat{\mathbf u}|.$$

The arm's physical radius alone is not the motion ratio: pushrod angle and damper line of action also matter. At ride, A has a 96 mm horizontal arm, while a horizontal damper force at B has a 76.8 mm moment arm. Their ratio is 0.80 for the guided-input layout near ride.

Define positive q as upward guided input C and positive s as damper compression:

$$MR=\frac{ds}{dq}.$$

Under lossless, quasi-static virtual work,

$$F_q\,dq=F_d\,ds,\qquad F_d=F_q/MR.$$

A damper that moves less than the input must carry more force. At ride MR ≈0.80, a 6 kN input corresponds to approximately 7.5 kN at the damper. A bearing pressure is applied at the rocker pickup to represent this force transfer in the structural model.

## Spring-rate relationship

For an approximately constant local MR, the equivalent input stiffness is

$$k_q\approx k_sMR^2.$$

One factor of MR comes from displacement transformation and the other from force transformation. A 67.5 N/mm input stiffness at MR=0.80 requires approximately 105.47 N/mm spring stiffness. This is a local calculation, not a specification of a catalogue spring.

When MR varies and the spring carries force, the tangent stiffness includes a geometric term:

$$\frac{dF_q}{dq}=k_sMR^2+F_s\frac{dMR}{dq}.$$

Preload and ride force matter to that term. It is not valid to claim a constant wheel rate across travel solely from the ride ratio.

## Recorded sweep

| Input q (mm) | Mate distance (mm) | Damper length BD (mm) | Compression s (mm) |
|---:|---:|---:|---:|
| -30 | 405.88 | 327.34 | -27.33 |
| -20 | 395.88 | 317.40 | -17.39 |
| -10 | 385.88 | 308.34 | -8.33 |
| -5 | 380.88 | 304.09 | -4.08 |
| 0 | 375.88 | 300.01 | 0.00 |
| +5 | 370.88 | 296.09 | 3.92 |
| +10 | 365.88 | 292.32 | 7.69 |
| +20 | 355.88 | 285.26 | 14.75 |
| +30 | 345.88 | 278.82 | 21.19 |

The independently displayed lengths and compression records are rounded to 0.01 mm; small differences in their subtraction should not be treated as new measurements.

![Travel curve](../Plots/damper_travel.png)

The central ±5 mm estimate is (3.92 - (-4.08))/10 = **0.800**. Finite-interval ratios decrease toward bump: 0 to +10 mm gives 0.769, +10 to +20 gives 0.706, and +20 to +30 gives 0.644. Toward droop, interval values are 0.833, 0.906 and 0.994. The smaller ±5 mm intervals are retained in the CSV and plot.

![Interval-average motion ratio](../Plots/motion_ratio.png)

The plot uses Δs/Δq at interval midpoints; it is not an exact analytic derivative. Measured travel is **21.19 mm compression**, **27.33 mm extension** and **48.52 mm total excursion**. The envelope model does not establish a real damper's available stroke or bump-stop margin.

## Important boundary of the result

C is constrained to a vertical guide. There is no upright, wishbone geometry, steering sweep or tyre contact point in this assembly. Call this ratio damper-to-guided-input MR; mapping it to actual wheel motion requires a full suspension model. The decreasing ratio also departs from the initial constant-ratio ±5% ambition and is retained as a measured result, not hidden as an acceptance pass.
