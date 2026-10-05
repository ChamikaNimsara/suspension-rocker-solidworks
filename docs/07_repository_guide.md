# Repository layout and native-file handoff

## Use the current repository

1. Use `D:\Suspension_Rocker_Solidworks\suspension-rocker-solidworks` as the main local repository.
2. Review `README.md` and preserve the folder layout and relative links.
3. Before publishing, review `git status` and the ignored-file policy. Locally present files are not necessarily committed or available in a remote clone.
4. Keep `README.md` at the repository root when publishing to GitHub.
5. Review the rendered README to check that its images and PDF links work.

Suggested repository description: **Conceptual suspension rocker design in SolidWorks: kinematics, assembly verification, static FEA, mesh convergence and mass reduction.**

Suggested topics: `solidworks`, `fea`, `suspension`, `motorsport`, `mechanical-design`, `cad`, `engineering-portfolio`.

## Native files now present

Copies of the native files from the source SolidWorks project are now organized in the local repository. The source project was left unchanged. The existing CSV records remain transcribed summaries. Reference and result-path resolution in SolidWorks was not checked as part of this documentation review.

- `CAD/` contains 22 `.SLDPRT` models and both `.SLDASM` assemblies. Verify that both assemblies open from this location without missing-reference prompts and use the repository copies of their components. Use Pack and Go if further reference gathering is needed; preserve filenames.
- `Drawings/` contains both native `.SLDDRW` sources and both PDFs. Verify that the native drawings resolve their model references to `CAD/`.
- `Simulation/` contains copied solver results and supporting artifacts. `.CWR` and `.LOG` files are excluded by `.gitignore`; archive them separately if they are needed for a published handoff. Verify the studies' result paths against this folder before using the copied results.
- `Animations/` contains `Rocker_Travel_Baseline.avi`. No optimized travel video is included.
- `Results/` contains the existing CSV summaries, evidence manifest and two copied interference-calculation `.xlsx` spreadsheets.
- For large CAD/video binaries, consider Git LFS. The provided `.gitattributes` marks binaries but does not configure LFS or silently change your repository storage policy.

## Publication checks

Before uploading native files, inspect Pack and Go content for unrelated projects, private paths or identifying metadata. Select a license intentionally; the package does not grant an open-source license by default. Keep the stated concept scope and known limitations visible in the README.

The repository can present the completed engineering work now. Native SolidWorks reproducibility still depends on verifying the copied model references and study result paths, and making any required Git-ignored results available with the handoff. A reader can already regenerate all included summary charts from the CSV files.
