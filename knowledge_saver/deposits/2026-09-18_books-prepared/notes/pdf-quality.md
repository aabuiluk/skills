# PDF quality and TOC map

Four files in `books/`:

| File | Book | Pages | Text layer |
|------|------|------:|------------|
| Bhargava_Grokaem-algoritmy.581423.pdf | Grokking Algorithms (Piter) | 290 | glyphs OK in Chrome; PDF ToUnicode is PUA. **Solved:** render + Windows.Media.Ocr (`ru`), 290/290 pages. |
| Trask_Grokaem-glubokoe-obuchenie.581982.pdf | Grokking Deep Learning | 354 | OK, offset PDF = book+1 |
| Van_Grokaem-striming.738373.pdf | Grokking Streaming Systems (Fischer, Wang) | 288 | OK, offset 0 |
| Vogan_-…607848.pdf | Impractical Python Projects | 466 | OK, offset PDF = book+1 |

No PDF outlines. TOC recovered from printed contents pages.

Working corpus: `books_prepared/` (INDEX.md → slug/chapters).
Do not duplicate PDFs here; originals stay in `books/`.
