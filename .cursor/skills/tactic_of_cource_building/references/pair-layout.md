# Структурна схема пари

Це **схема типів**. На нову тему перейменуй `title` під syllabus цієї пари; `type` і порядок зон не міняй. Не копіюй заголовки з живої пари й не звіряйся з HTML-прототипом.

## chrome

```text
chrome  До плану
chrome  Пара {N}/{total}
chrome  ☰
chrome  {назва пари}
chrome  Студенти · {student_active}
chrome  Версія · {material_version}
chrome  Для викладача
chrome  Редактор
chrome  Зошит
chrome  ← {N-1}
chrome  {N+1} →
chrome  Окремо
chrome  Завантажити
```

## rail

```text
toc  Зміст
```

Пункти TOC не пиши вручну — збери з `stage[].title` + `id`.

## notebook

Одна комірка на кожен runnable `code` / `task` зі `stage`. Поки комірок не відомо — шість слотів:

```text
notebook  Комірка · {приклад 1}
notebook  Комірка · {приклад 2}
notebook  Комірка · {приклад 3}
notebook  Комірка · {метрики}
notebook  Комірка · завдання 1
notebook  Комірка · завдання 2
```

Якщо комірок ще не відомо — лиши 6 слотів з `Потребує допрацювання`.

## stage (порядок типів)

Кластери не розривай. Teacher-близнюк стоїть **одразу після** студентського кластера, який він веде.

```text
banner      План і цілі
teacher     Бриф пари
teacher     Вау-приклад на старті
teacher     Що робимо сьогодні

theory      Карта пари · 10 кроків
diagram     Карта · схема 10 кроків
extra       Пояснення кроків
extra       Коротко / детально

theory      {факт 1}
diagram     {схема факту 1}
callout     Коротко · {термін}
teacher     Кроки · {факт 1}

example     {приклад до факту}
code        {демо}
diagram     {схема демо}
callout     Зверніть увагу
trap        Часта пастка
extra       Розбір {прикладу}
teacher     Кроки · {приклад}

theory      {уточнення / місток}
theory      {підготовка даних / split}
code        {код підготовки}
trap        Часта пастка · {leakage}
checkpoint  Мікроперевірка · 15 хв
teacher     Кроки · {підготовка}

example     {наступний приклад}
diagram     {схема}
code        {код}
extra       Розбір
trap        {синонім / API-пастка}
teacher     Кроки · {приклад}

theory      {метрики / критерій якості}
callout     Зверніть увагу
example     {наскрізний кейс}
code        {архітектура / рахунок параметрів}
extra       Розбір кейсу
checkpoint  Мікроперевірка · 30 хв
teacher     Кроки · {кейс}

theory      {механізм теми}
diagram     {де стоїть у пайплайні}
extra       Розбір механізму
teacher     Кроки · {механізм}

example     {порівняння параметрів}
code        {цикл / таблиця}
trap        Часта пастка · {означення параметра}
theory      {сигнал overfitting / gap}
diagram     {криві train vs test}
checkpoint  Мікроперевірка · 45 хв
example     {чесне вимірювання}
code        {eval / no_grad або еквівалент}
callout     Орієнтир · обидва важелі
extra       {глибше про параметр}
extra       {overfit / underfit}
teacher     Кроки · {gap}

task        {офіційний практикум · рамка}
task        Завдання 1 · {тема}
callout     Звідки дані і навіщо · 1
teacher     Walkthrough · завдання 1
checkpoint  Мікроперевірка · 60 хв
task        Завдання 2 · {тема}
callout     Звідки дані і навіщо · 2
teacher     Walkthrough · завдання 2
checkpoint  Checkpoint

extra       {опційний акцент A}
extra       {демо A}
extra       {практика A}
extra       {опційний акцент B}
extra       {практика B}
extra       Паспорт даних
teacher     Нотатки опційного шару

homework    Домашнє
teacher     Еталон ДЗ
exit        Exit ticket
extra       Deep-study
teacher     Кроки · deep-study
```

## Таймінг 80 хв

У пігулки банера входять лише блоки з хвилинами **required**. Типовий розподіл (сума 80):

| Слот | хв |
|------|----|
| теорія/приклад × 9 по 5 | 45 |
| один теорійний слот 4 | 4 |
| практикум (рамка + завдання 1–2) | 24 |
| Checkpoint | 3 |
| Exit ticket | 4 |

`extra`, `teacher`, мікроперевірки 15/30/45/60, homework, deep-study — **опційно**, поза 80, якщо немає власного `data-timing="required"`.
