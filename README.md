# Illumination Invariance via Edge-Based Representations

This project studies how different visual representations respond to changes in illumination.
While raw pixel representations are highly sensitive to global lighting variations, certain
structural representations can remain stable under such transformations.

We construct a minimal synthetic experiment where an image is subjected to illumination changes
(e.g., brightness scaling). We then compare two representations:
(1) raw pixel intensities and (2) edge-based representations.

Our results show that raw representations change significantly under illumination,
whereas edge-based representations remain nearly invariant, with embedding distances
close to zero. This demonstrates that invariance can emerge from representation choice,
without requiring explicit data augmentation or architectural constraints.

The project highlights the importance of inductive bias in vision models and provides
a minimal, quantitative demonstration of illumination invariance.

