# Тултіпи для explaine_simple

Глосарій пари: `term-glossary.js`. Підказка на вебі — `#term-tip` з `data-tip`.

## Текст

- Новий шар: терміни в `<code class="mv">` (opt-in крізь SKIP `CODE`) або як ключ ENTRIES.
- Не лишай голими: `Dropout`, `eval()`, `train()`, `autograd`, `nn.Module`, `state_dict`, `BatchNorm`, `zero_grad`, тензор, градієнт, регуляризація.
- `<code>eval()</code>` без `class="mv"` тултіпа не має: `CODE` у SKIP. Став `class="mv"` або ключ `eval` / `eval()` у ENTRIES.
- У шарі **Детально (v11)** не покладайся на автообгортання: `PRE` / `language-python` глосарій пропускає. Став `<span class="term" data-tip>` на кожен термін у прозі, на ASCII-схемі і рядком «Наведіть на слова» одразу під фрагментом коду.
- Не лишай голими: `Dropout`, `eval()`, `train()`, `autograd`, `nn.Module`, `state_dict`, `BatchNorm`, `zero_grad`, тензор, градієнт, регуляризація.
- На схемі підпис може бути `eval()`, не `model.eval()` — обидва варіанти мають `data-tip`.
- Не вертай порожні «очевидні» ключі (`дані`, `модель`, `навчання`) — вони били тултіпи по всьому реченню.

## Схеми (SVG)

`shouldSkip` не загортає SVG. Тому підпис блоку сам несе підказку:

```html
<text class="term" data-tip="zero_grad&#10;Обнуляє .grad перед новим кроком." ...>zero_grad</text>
```

Обов’язково:

```css
.diagram svg text { pointer-events: none; }
.diagram svg text.term,
.diagram svg [data-tip] { pointer-events: auto; cursor: help; }
```

Без другого правила наведення на блок картинки не працює.

У `bindTips` слухай `.term, svg [data-tip]`, не лише `span.term`.
