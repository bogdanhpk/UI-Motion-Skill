# Product motion

Use this for functional web interactions. For SwiftUI use [its matching guide](swiftui/guide.md); for exact-design showcase pacing use [design to motion](design-to-motion.md).

For interaction quality, use the relevant [motion principles](motion-principles.md). The timing and Bezier recipes below are fallbacks for projects without their own motion system, not a replacement for platform springs or component motion tokens.

## Decide what motion explains

Name the purpose: feedback, spatial continuity, state indication, bridging an abrupt change, or explanation. Reserve theatrical delight for rare moments. Frequency limits intensity: keyboard-driven and high-frequency flows usually need instant feedback or a short opacity/color change; do not make them wait for an entrance or stagger.

If motion has no useful purpose, keep the state change immediate and implement the requested usable result. If the user explicitly requests expressive motion, fit it to the interaction and explain any material tradeoff instead of imposing a blanket refusal.

## Choose the implementation

Inspect the installed component and animation libraries first. Keep native/library animation when it meets the need. Do not build a new dropdown, toast, modal, or other control just to animate it. Motion must fit the supported control API.

| Need | Prefer |
|---|---|
| Hover, press, color, toggled state | CSS transition on explicit properties |
| Entry on mount without JS state | `@starting-style` when target browsers support it |
| Predetermined decorative sequence | CSS animation, with reduced-motion handling |
| Programmatic playback without a dependency | WAAPI |
| Springs, layout, exit, interruptible gestures | The existing Motion/Framer Motion integration |

Transform/opacity animations can be composited when eligible; CSS, WAAPI, or a full transform string alone does not guarantee this. Inspect the actual animation when frame drops matter. Avoid a dependency for a fade. Match `motion/react` versus `framer-motion` to the package and neighboring imports already present.

## Geometry and timing

- Prefer `transform` and `opacity`; limit animated blur and clipping to cases where the result warrants their cost. Measured height animation is sometimes appropriate for a collapse; keep it short and test layout.
- Start ordinary surface entrances close to full size (`0.95` is a starting point), with opacity fading in. Do not grow a whole surface from `scale(0)`.
- Anchor a popover's transform origin to its trigger through the component's supported API. Centered modals stay centered. A sheet can translate by its own height.
- Set transforms on the moving element rather than propagating frame-by-frame CSS variables through a large subtree.
- Keep data people read or act on stable; pointer tracking is for a purposeful gesture or illustration.

Use the project's tokens. Only when the project has no equivalent, the following inherited recipes provide a starting vocabulary:

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
```

| Interaction | Starting duration |
|---|---|
| Press feedback | 100–160ms |
| Tooltip / small popover | 125–200ms |
| Dropdown / select | 150–250ms |
| Modal | About 200–300ms |
| Spatial sheet / drawer | About 200–500ms, proportionate to distance |

For generic feedback, ease-out is a useful entrance/exit fallback, ease-in-out can connect positions, and linear suits constant-rate progress. Preserve the host system's semantic curves: Carbon, for example, distinguishes a departing object's accelerating exit from a nearby panel that slows to rest offscreen. Do not force all exits to share a curve. Avoid delaying the visible response to input. The roughly 300ms feedback budget is a heuristic, not a platform limit; distance, scale, gesture physics, and the component contract can justify longer motion. See [Carbon's easing guidance](https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview).

For gestures, preserve velocity through interruption with a spring. Match the app's existing spring vocabulary first; for custom exploratory tuning a possible starting point is `{ type: "spring", duration: 0.5, bounce: 0.2 }`, not an Apple specification. Ordinary state swaps generally need no bounce. Do not copy spring numbers between frameworks without checking their parameter definitions; damping ratios, damping coefficients, perceptual durations, and settling times are different quantities.

## Interruption, exits, and accessibility

- Transitions retarget toward the latest state. Keep repeated toggles and reversals smooth instead of restarting a fixed sequence from zero.
- Keep exit content mounted until its transition completes using the framework/library's supported presence API. Exit toward the entry edge where that explains the object's location, with a shorter or softer path when appropriate.
- For deliberate hold-to-confirm interactions, the hold can be slow and linear while release/cancel is immediate or snappy. Do not replace the product's confirmation model without a reason in the brief.
- Preserve pointer capture, grab offset, multitouch protection, overdrag resistance, and velocity-aware release for gestures. Use real async completion for success states.
- Gate hover motion with `(hover: hover) and (pointer: fine)`. A press state can work on touch without hover.
- Reduced motion uses an instant or gentle opacity change without spatial travel or animated blur. Keep persistent state cues and library accessibility behavior.

## Recipes and checks

Read the relevant section of [product-recipes.md](product-recipes.md). Recipes illustrate animation mechanics; they are not permission to replace a component, duplicate semantic controls, or override a design system. Press feedback uses the shared polish baseline `0.96` when custom press styling is appropriate. Native/library press behavior comes first.

Check quick retriggers, reversal, exit/unmount, keyboard/focus, touch, reduced motion, and first load. Avoid `transition: all`, hidden interactive content during a stagger, decorative movement on frequently used paths, and large surfaces growing from zero. Inspect the animation in the current browser; if unavailable, identify the unverified behavior rather than claiming the motion was observed.
