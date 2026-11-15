---
name: ui-motion
description: "Create high-quality product feature previews with a visible browser header, and refine UI motion and visual polish: interactive transitions, surfaces and icons, animated designs, product demos, and SwiftUI patterns. Use when asked for a feature preview, browser-framed product shot, interface animation, UI polish, motion matching, or an animated showcase. Preserve the project's component library and design tokens."
metadata:
  version: "1.1.0"
  repository: "https://github.com/bogdanhpk/UI-Motion-Skill"
---

# UI Motion

Implement motion and UI polish that make the requested interaction or visual story clear. This skill combines product motion, UI polish, design animation, product demos, and SwiftUI matching. Load only the guidance needed for the current task.

## Choose the work

| Request | Read |
|---|---|
| Animate a working UI: press, hover, menu, modal, drawer, toast, accordion, gesture, state transition | [Product motion](references/product-motion.md); load the linked recipes for the interaction |
| Improve UI details, surfaces, nested radii, optical alignment, icons, or existing transitions | [UI polish](references/polish/guide.md); load only its relevant detail files |
| Animate a supplied Figma frame, screenshot, or static design while preserving it | [Design to motion](references/design-to-motion.md) |
| Create a product feature preview, still or animated, with a visible browser header | [Feature previews](references/feature-previews.md); use the product-demo kit only where the project's component rules allow it |
| Author a product illustration, cursor walkthrough, or demo loop without an exact source frame | [Product demos](assets/stageshow/GUIDE.md); its references, kit, examples, and recording tools are bundled alongside it |
| Choose or implement motion in SwiftUI | [SwiftUI matching](references/swiftui/guide.md), then the relevant catalog section if system motion is insufficient |

Tasks can combine modes. For example, improve a menu's alignment with UI polish and implement its transition with product motion. A supplied design remains the visual source of truth; a demo kit must not redesign it. SwiftUI uses platform APIs rather than web recipes.

## Product feature previews

When asked for a feature preview, make one feature and its benefit legible inside a believable product interface. Keep a browser header visible above the product by default, including in the poster and narrow composition. Use one existing browser frame; do not draw window controls or an address field from scratch. Keep an existing header once if the source already includes it. A specifically requested phone, native-app frame, or frameless composition overrides this default.

The [feature-preview guide](references/feature-previews.md) defines composition, framing, motion, and observable quality checks. Match the actual product's components, content, and tokens; the focal area must look like a finished product rather than a wireframe. Check the result at its real display size before calling it finished.

## Motion quality

For custom motion or a motion review, read the relevant sections of [motion principles](references/motion-principles.md), distilled from Apple HIG/WWDC, Google Material, Microsoft Fluent, and IBM Carbon. Apply this quality bar through the host design system:

- Respond as soon as input is recognized; allow redirection while a transition runs.
- Preserve the identity of moving content and communicate the actual hierarchy between views. Do not imply a spatial relationship that the navigation does not have.
- Continue from the current visual state; gesture handoffs should preserve velocity when supported. A spring need not bounce.
- Coordinate geometry and visual effects without forcing them onto an identical curve. Opacity and color must not overshoot.
- Match the motion vocabulary to the product and scale the timing to the change. The recipe milliseconds are starting values, not universal Apple or industry requirements.
- Choreograph attention across related elements; keep repeated work quiet and the final result usable with reduced motion.

## Shared constraints

- Inspect the existing implementation, component library, tokens, and installed animation packages before changing anything. Use supported component APIs, states, slots, and theme configuration. Do not recreate library controls or override their internal markup, styles, focus management, or animations to fit a recipe.
- The project's design system takes precedence over example colors, fonts, radii, shadows, spacing, icon sets, motion curves, and timings. Do not introduce a parallel token system. In Koobiq projects use `@koobiq/components`, its theme, typography, icons, and tokens; custom markup and CSS are for composition within those constraints.
- State the motion's purpose and consider how often it occurs. Frequent interactions need immediate, quiet feedback; onboarding and authored demos can have longer choreography. Do not delay the user's action for an animation.
- Keep repeated interactions interruptible. Test reversal, rapid retriggering, pending async work, and unmount/exit. Loading and completion must follow real work in functional UI; simulated work belongs to an authored demo.
- Every animated state change needs a persistent cue such as a label, icon, value, or selection state. Maintain focus, keyboard support, accessible names, and pointer/touch behavior. Gate hover motion with `(hover: hover) and (pointer: fine)`.
- Honor reduced motion. Product UI uses an instant or gentle opacity change; showcases show a meaningful still/poster. Avoid translation, scale, blur sweeps, and perpetual decorative loops in the reduced variant. Do not replace an established component's reduced-motion behavior.
- Prefer `transform` and `opacity`; use small blur and clipping only when useful and verified. Do not promise GPU acceleration for a property or library without checking actual behavior. Avoid broad `transition: all`; add `will-change` only for observed stutter.
- Keep implementation and review within the user's request. Do not add export formats, redesign other screens, add dependencies, or impose a report/audit workflow merely because a reference demonstrates them.

## Resolve recipe differences

The original guides target different media. Their numeric recipes are scoped examples, not competing global requirements.

| Context | Motion baseline |
|---|---|
| Functional product UI | Existing component behavior first; otherwise short, interruptible feedback, commonly 100–250ms. Longer sheets need a spatial reason. No decorative stagger on repeated actions. |
| UI polish | Preserve the app's motion vocabulary. The polish recipes use press scale `0.96` and no-bounce icon swaps; use them only when custom styling is permitted and they fit the interaction. |
| Exact-design showcase | Slower loading and story tracks are intentional. The design guide's roughly 2.4s intro and 12s cycle are starting values for authored showcases, not menu timings. |
| Authored demo | Choose a readable sequence with a payoff and a meaningful poster. Stageshow's story pacing applies to the illustration, not the live product it depicts. |
| SwiftUI | System animation and accessibility behavior first; adapt a catalog pattern only when it earns its place in content. |

Product-scale entrances normally start near full size. A small icon swap may use the polish guide's smaller scale; a line or bar can draw from zero. These are separate cases. Keep exit travel spatially consistent with entry, while allowing a shorter, softer exit. Existing design-system values always win.

## Work and verify

1. Identify the requested result, the source of truth, and the applicable mode. For custom motion, use the quality principles to choose the relationship, response, and motion character. Explain the key choice briefly, then implement. Infer routine choices from the project; ask only when missing source material or a material choice blocks the work.
2. Make the static state correct before adding motion: composition, readable text, tokens, surface geometry, clipping, and component states. Use supplied design references when present.
3. Implement the smallest solution that fits the stack. CSS transitions are enough for many web states; use existing Motion/Framer Motion for layout, exit, springs, or gesture values when needed. Match the installed package's import path. SwiftUI uses native APIs.
4. Verify observable behavior in the running interface: first load, normal/rapid/reversed actions, loading/error/empty states where relevant, focus, reduced motion, and narrow layouts. Watch the full transition or loop; a still alone cannot establish motion quality.
5. For authored sequences also inspect a contact sheet, the smallest output size, clipping, retained text during resizing, the loop seam, and the poster. For exact-design work verify the resting frame against the source before export.

### Browser and recorder access

Use a suitable already-open user tab first, then the Codex in-app browser or the user's current browser. Do not start a separate Chrome, browser profile, or isolated browser session unless the user explicitly requests it. If these surfaces are unavailable, continue static/build checks and identify what could not be verified.

Bundled Stageshow filming scripts currently launch a separate browser through `scripts/browser.mjs`; do not run those commands under the default browser constraint above. Adapt capture to an authorized existing browser/tab when supported. If deterministic capture is unavailable, say which checks or exports remain unverified; do not silently launch a browser to satisfy a reference's rehearsal gate.

Work on a copy of bundled demo assets in the task workspace so examples remain reusable. Run scripts from that copy's Stageshow root; their relative paths depend on keeping `kit/`, `examples/`, `playground/`, `references/`, and `scripts/` together. Keep its LICENSE, NOTICE, brand-license files, and image credits when copying assets.

## Deliver

Provide the implemented result and a brief account of what changed, the important motion choices, and what was actually checked. Name material limitations plainly. Use a findings table only when reviewing is the task; do not issue an approval verdict for unchecked coverage. Export video or GIF only for a requested showcase/export deliverable; ordinary UI polish does not require media files.

## Resource map

- [Motion principles](references/motion-principles.md): sourced Apple, Material, Fluent, and Carbon guidance, practical decisions, and observable quality checks.
- [Feature previews](references/feature-previews.md): polished product feature previews with a persistent browser header, a clear focal feature, a strong poster, and quality checks at the final size.
- [Product recipes](references/product-recipes.md): press, overlay, toast, collapse, stagger, hold, tab indicator, scroll reveal, drag, crossfade, and WAAPI examples.
- [UI polish guide](references/polish/guide.md): surfaces, icons, transitions, enter/exit, and performance references.
- [Design to motion](references/design-to-motion.md): source fidelity, layer geometry, deterministic clocks, story loops, capture, and encoding.
- [Stageshow guide](assets/stageshow/GUIDE.md): demo composition and choreography, with the complete kit, examples, and tools.
- [SwiftUI guide](references/swiftui/guide.md): system-first matching, pinned source catalogs, and adding a source.
