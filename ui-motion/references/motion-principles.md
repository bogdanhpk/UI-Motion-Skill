# Motion principles

Use this reference when designing custom interaction motion or reviewing why motion feels wrong. Read the relevant sections, then return to the implementation guide for the current medium. Primary sources checked on 2026-11-15. These are paraphrased design principles; the decision examples and checks at the end are this skill's synthesis, not claims of vendor certification.

The host component library, accessibility behavior, and tokens remain authoritative. Borrow a principle when it fits the product; do not install another design system or mix several companies' motion presets into one interface.

## Apple: purpose, control, and continuity

### Purpose and platform behavior

Prefer system components: their motion already adapts to platform conventions, accessibility settings, and input. Custom movement should explain status, feedback, or relationships. Keep frequent feedback brief and avoid making important information depend on seeing an animation. Allow cancellation instead of holding people until an animation ends. A transition's direction should fit what the gesture and interface led people to expect. See [Apple HIG: Motion](https://developer.apple.com/design/human-interface-guidelines/motion).

### Immediate response and redirection

Start feedback when the input is recognized. Watch for artificial delays introduced by timers or sequencing. Let people change their destination before a transition finishes. During a direct manipulation, content should stay connected to the gesture, including a change of intent midway through it. Judge this by interacting with the result, not just playing a timed preview. See [Apple WWDC18: Designing Fluid Interfaces](https://developer.apple.com/videos/play/wwdc2018/803/).

### Position and velocity continuity

An interrupted animation should continue from where the object is, with an appropriate continuation of its velocity. For a gesture release, a spring can carry the release velocity into settling; when a moving target changes, preserve the current velocity instead of restarting from rest. Springs can be non-bouncy. Their configured perceptual duration and actual settling time are different: do not gate the next task on waiting for tiny residual oscillations to disappear. See [Apple WWDC23: Animate with springs](https://developer.apple.com/videos/play/wwdc2023/10158/).

## Google Material: coherent physics and separate roles

The current M3 motion guidance introduces spring-based motion schemes in place of the earlier easing/duration system. It distinguishes expressive and standard schemes; standard suits utilitarian products, while expressive adds more character. Choose a coherent scheme for the product.

Within a scheme, spatial springs handle geometry; effects springs handle properties such as opacity and color without overshoot. Each role has fast, default, and slow tokens, selected with regard to the size of the change and device. These are meaningful roles rather than one timing for every property.

Reuse the implementation's motion scheme when available. Before transferring spring parameters to another platform, check its parameter definitions and supported conversion; equal numeric values do not establish equal motion. Verify implementation availability in the actual stack. See [Material 3: Motion physics system](https://m3.material.io/styles/motion/overview/how-it-works).

## Microsoft Fluent: movement explains relationships

Fluent's motion principles connect purpose, believable behavior, consistency, and appeal. Consider an element's size and travel when selecting duration; larger movement generally needs more time, while feedback should stay quick.

Choose the transition by the relationship it communicates. Elevation can explain lift and layering. For movement between top-level destinations, Fluent recommends a short fade rather than sliding large screens and implying an unintended hierarchy. Enter/exit and container transformations solve different changes; select the appropriate pattern instead of using one favorite effect everywhere. See [Fluent 2: Motion](https://fluent2.microsoft.design/motion).

## IBM Carbon: productive rhythm and choreography

### Productive versus expressive

Carbon keeps routine task work understated and reserves expressive motion for meaningful moments. Its component microinteractions are already provided; teams coordinate the larger composition. Standard, entrance, and exit easing have different roles. An object leaving permanently can accelerate out, while a panel resting just offscreen can slow down as it leaves. Size and travel affect duration. See [Carbon: Motion overview](https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview).

### Semantics, shared elements, and sequencing

Use similar motion for similar meanings, while allowing differences that explain a different action or location. Shared elements can maintain continuity between screens. Coordinate multiple moving elements into a readable sequence. Carbon's grid-aligned paths express its own design language; they are not a universal prohibition on diagonal gestures. Its stagger examples should be adapted to the number of items and the total sequence duration. See [Carbon: Motion choreography](https://www.carbondesignsystem.com/building-blocks/foundations/motion/choreography).

## Apply the principles

The following are implementation decisions synthesized for this skill. Existing component behavior takes precedence; implement custom behavior only through supported extension points.

| Situation | Decision | Observe |
|---|---|---|
| A person opens a sheet and closes it before it finishes | Retarget from the visible state; keep the actual edge relationship | No jump back to a starting pose and no ignored close action |
| A dragged card is released or grabbed again while settling | Keep gesture continuity and use the stack's velocity-aware settling | No dead stop at release and no snap when grabbed again |
| Navigation switches between peer destinations | Use the host navigation contract; a quiet fade is a candidate when no directional relationship exists | The transition does not suggest a deeper level or a return path |
| A selected row expands into its detail | Preserve identifiable shared content if the component/navigation APIs support it | The source remains understandable; text stays readable during the transformation |
| A large set of results appears | Reveal related groups together; use a short stagger only when it clarifies reading order | The last item is not held behind a long decorative queue |
| A process completes | Tie the visual response to actual completion and leave a stable completed state | Success is still clear with motion reduced or skipped |
| A geometry change also fades content | Coordinate spatial and effects tracks by role | The content does not flash or become unreadable while the surface settles |

## Check the result

Check only the cases relevant to the change, using the authorized current browser, Preview, or Simulator. Describe any coverage you could not observe.

- **Response:** does the first visible response follow recognized input without a decorative delay?
- **Control:** can a second action, reversal, or gesture change the outcome before the first motion ends?
- **Continuity:** do gesture release, retargeting, and re-grabbing avoid jumps in position or abrupt stops?
- **Meaning:** does movement explain the actual relationship, origin, destination, or change in state?
- **Composition:** can the eye follow the important change without several unrelated effects competing?
- **Readability:** are text, focus, controls, and the final state usable throughout the transition?
- **Reduced motion:** can the same task be understood and completed with spatial movement removed?
- **Performance:** does it hold up with real content and the target device/input? Short code and compositor-friendly properties alone do not prove smooth motion.

Do not give the result an “Apple-approved” label, claim a universal frame-rate/duration requirement from these sources, or use a spring's mathematical settling time as a reason to delay interaction. A convincing result demonstrates these properties in the product's own motion language.
