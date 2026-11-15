# Product feature previews

Use for requests such as “feature preview”, “product feature shot”, “превью фичи”, or an illustration that demonstrates one product capability. The result can be a still or a purposeful animation. The default frame includes a visible browser header above the product content. A specific request for another frame overrides this default.

Read the [shared UI Motion constraints](../SKILL.md) first. Use [product demos](../assets/stageshow/GUIDE.md) for authored scenes and [design to motion](design-to-motion.md) when matching a supplied frame. These preview rules specialize the generic composition rules; they do not override the host component library or authorize a product redesign.

## Define the feature and its result

Identify the product, feature, intended placement and display size, available source, and the result the viewer should understand. Use the repository, supplied screenshots, or design files before asking for information already available. If there is enough context, make routine composition choices and build.

Write one sentence: “The person does X; the product changes Y; the useful result is Z.” Show that feature rather than an unrelated dashboard decorated with a label. A still should make the result clear on its own. Animate when an action, transformation, or sequence explains the benefit better than the still.

Use the product's actual labels, icons, navigation patterns, and data structures. Illustrative data should be coherent: chart totals, table values, filters, dates, counts, and status must agree. Keep the primary feature fully rendered with meaningful content. Placeholder lines may simplify peripheral context, never the control being used or the result being demonstrated.

## Keep the browser header above the product

- Keep one browser header across the top of the visible frame. It belongs to the frame, above the product's own toolbar and content. It remains recognizable in the poster, throughout the main action, and in the compact composition.
- Include a restrained address area and standard window controls using the existing frame's API. Use a known product domain/path when available; otherwise a neutral product-name label is preferable to inventing a real hostname. Extra tabs and navigation are optional and should earn their space.
- Preserve the frame's built-in proportions, alignment, corner geometry, separators, and clipping. Do not hand-draw traffic lights, recreate a URL input, or change internal styles to make the frame fit.
- If the source already includes browser chrome, keep it once. Frame the product content without nesting two address bars. Keep supplied source content faithful; put any needed outer frame around it rather than repainting its UI.
- Crop or simplify secondary content below the header when space is tight. Do not crop the header away to enlarge the feature. A browser frame should look attached to its page, with matching width and no seam.
- Keep chrome quiet and stable while content demonstrates the feature. Do not animate the browser bar, change its address, or flash its controls unless browser navigation is the feature's action.

### Use the existing Window API

Where an illustrative frame is permitted, the bundled [Window](../assets/stageshow/kit/window.tsx) already provides browser chrome. The [kit reference](../assets/stageshow/references/kit.md#window) explains its props. In a task-local copy of the kit, the basic browser composition is:

```tsx
<Window
  chrome="native"
  url={productAddress}
  urlShape="pill"
  tabs={[featureTitle]}
  nav
>
  {featureContent}
</Window>
```

Use real content from the brief for these values. Omit optional tabs or navigation when a quieter bar serves the size better. Native chrome supports these props; other chrome variants can ignore `tabs` or `nav`. Do not combine this with `Window.sidebar`: that selects an app-style frame and takes precedence over tabs. Put the product's own sidebar inside `featureContent`, below the full browser header.

In a project that mandates Koobiq, inspect the approved components and compose the preview only through their supported APIs, primitives, and tokens. The kit example is not an exception to that requirement. Prefer an existing approved browser frame; otherwise use allowed composition of the available components. Do not add a custom visual component or counterfeit library control as a fallback.

## Compose for the actual placement

Choose the frame at the size the viewer will see. Give the feature the largest useful area and retain just enough product context to make it believable. Avoid a tiny full-screen dashboard inside a large empty canvas. A crop should feel intentional, with the action, affected content, and result all visible.

Keep one focal feature. Supporting panels, annotations, or satellites must explain that same feature and stay clear of the top browser header, important text, active controls, and results. Do not add extra windows, badges, gradients, glass, or dramatic shadows merely to make the preview look expensive.

Match the product's typography, density, surfaces, states, icons, and approved elevation. Use its tokens rather than a separate illustration palette. Keep nested radii and insets visually coherent through the permitted component APIs. Fit text before adding motion: labels should not collide, wrap unpredictably, or rely on unreadably small type.

For narrow placement, create a closer composition or an appropriate compact layout. Keep the browser header and feature result visible. Remove secondary columns or show fewer rows before shrinking the entire desktop scene. Judge it in the actual host slot, not only in a large isolated preview.

## Make the still excellent before adding motion

Build a meaningful poster showing the feature's useful state. Check it beside the supplied product reference at a comparable size. Resolve the largest discrepancy first: wrong product structure, weak focus, unreadable content, framing, spacing, then surface details. A convincing animation cannot repair an unfinished still.

Use live text and vector icons/charts where appropriate. Keep raster sources sharp at the intended display and capture scale; wait for fonts and images before capture. If the source requires pixel fidelity, follow the layer and bounds workflow in the design guide. Do not invent a polished-looking replacement for a feature whose actual behavior is unknown.

## Animate the feature's cause and effect

Use a short readable sequence when motion adds explanatory value: context, action, product response, useful result. Overlap related motion naturally and leave time to read the result. A cursor must point at the actual measured target; its press should agree with the state change.

Keep the browser frame anchored. Animate the relevant product content through approved APIs, preserving identity and text readability. Avoid scaling text with a resizing panel, unrelated pulsing, and long loading theater. In a functional preview, async states follow real work; in an authored illustration, the scene is an intentional simulation.

For a loop, return with a visible cause or an unobtrusive reset; do not visibly rewind data without explanation. Keep the final result as the poster. A static request stays static. With reduced motion, show a clear completed state without spatial movement. Pause decorative playback offscreen in a website context. Export video or GIF only when the requested deliverable requires it.

## Quality checks

Inspect the actual still or full animation at the final desktop size and the narrow slot when one is used. Use the current user browser or Codex in-app browser under the shared browser constraints. The following checks define the preview's quality; a code review alone does not establish that they pass.

| Check | Pass condition |
|---|---|
| Browser frame | One recognizable header remains visible above the product, attached to the page with consistent geometry |
| Product fidelity | Components, tokens, copy, icons, navigation, and density match the product reference |
| Feature clarity | The action and useful result are understandable without a long explanation |
| Finished focal area | The feature has real controls, meaningful content, coherent data, and no wireframe filler |
| Composition | The frame has a clear focal point; context supports it; no accidental empty bands or awkward slivers |
| Readability | Essential labels and values remain legible at display size; no collision, unintended clipping, or font substitution |
| Layering | Menus, tooltips, selection states, shadows, and result panels remain in bounds and do not cover the header or key content |
| Narrow placement | The compact composition preserves the header, action, and result without reducing everything to microtext |
| Motion, if used | Cause and effect are clear; the cursor, transitions, result hold, and loop seam have no visible jumps |
| Static fallback | The poster and reduced-motion state communicate the same feature benefit |

Fix observed failures before handoff. If runtime inspection or a capture mechanism is unavailable, identify exactly which checks remain unverified; do not substitute an invented quality score.

Deliver the preview integrated at the requested placement or a runnable preview route, with the relevant component/route location and a brief verification note. Include a still or recording when requested or useful as proof and supported by the current surface. Do not substitute a plan or a written description for a requested visual preview.
