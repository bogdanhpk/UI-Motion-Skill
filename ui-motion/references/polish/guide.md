# UI polish

Refine the requested interface while keeping its component library, tokens, density, and motion vocabulary. This combines the former `better-ui` principles with the shared motion workflow. Load detail files only for the change at hand.

## Surfaces and alignment

Read [surfaces.md](surfaces.md) for nested radii, optical alignment, elevation, and image outlines.

- Close, evenly nested surfaces generally look concentric when the outer radius equals the inner radius plus padding. Independent surfaces and asymmetric insets need judgment. Use the design system's approved tokens and components rather than forcing exact pixel arithmetic onto them.
- Judge icon/text alignment optically. Use the component's intended icon slot and sizing before considering a custom adjustment. Do not alter library internals or shared SVG assets to nudge one control.
- Shadows communicate elevation; borders communicate structure, selection, focus, and separation. Preserve those roles. Choose existing surface variants and tokens before adding styling.
- A subtle image outline can clarify the edge without affecting layout. The inherited neutral black/white examples apply to surfaces the project permits you to style; a design-system border token takes precedence.

## Icons

Read [icons.md](icons.md) for optical weight, currentColor, size, and RTL; read [icon-transitions.md](icon-transitions.md) for a changing icon.

- Use one coherent icon system per surface. Match visual weight to neighboring text with the library's supported sizes/variants. Directional icons may mirror in RTL; logos and non-directional glyphs usually do not.
- Prefer one icon asset using `currentColor` over separate recolored assets. Preserve accessible labels and persistent selected/loading/success cues.
- For an occasional contextual swap, the inherited recipe uses opacity `0↔1`, scale `0.25↔1`, blur `4px↔0`, and a `0.3s` no-bounce spring; the CSS alternative uses `cubic-bezier(0.2, 0, 0, 1)`. This is an optional small-glyph recipe, not a surface entrance or an instruction to animate every icon. Keep reduced motion gentle and use the installed motion package only.

## Interaction polish

Read [animations.md](animations.md), [enter-exit.md](enter-exit.md), and [performance.md](performance.md) as needed; use [product motion](../product-motion.md) for the overall decision sequence.

- Interactive state changes should retarget from their current visual state. Reserve a staged timeline for a sequence that benefits from one.
- If the component permits custom press feedback and it fits the app, use scale `0.96` as the shared starting recipe. Do not add a new `static` prop to a library component or override its own press treatment.
- Stagger only infrequent entrances where order conveys hierarchy, generally by semantic groups. Do not stagger repeated navigation, typing, or row hovers. Keep content usable during the sequence.
- Keep exits softer and shorter when possible. Preserve spatial direction for sheets and other edge-anchored surfaces.
- `initial={false}` can prevent unwanted first-render entrances where a presence integration supports it; keep intentional page/illustration intros.
- Avoid a whole-page color smear on theme changes. Prefer the existing theme manager's transition suppression. If a local suppression is needed, scope it to the swap and always remove it; do not override meaningful transform/opacity transitions elsewhere.
- Specify transition properties. Add `will-change` only for measured first-frame stutter and remove persistent hints when unnecessary.

The detailed files retain implementation examples from `better-ui`. Their literal values, custom markup, and imperative wording apply only where this guide and the project's APIs allow customization. Do not treat them as higher-priority design-system requirements.

## Review and deliver

When implementation is requested, make the changes and report them briefly. When review is requested, group findings by root cause and order by user impact:

| Severity | Location | Before | Suggested change | User impact |
|---|---|---|---|---|

High severity breaks interaction, makes motion unusable, or communicates state only while moving. Medium severity is a visible inconsistency; low severity is isolated polish. Cover the actual states relevant to the change, including focus, hover, active, loading, empty, and reduced motion when present. In the browser replay transitions slowly when necessary to locate a pop or misalignment. State what was not verified; an approval verdict is appropriate only if the user requested it and coverage supports it.
