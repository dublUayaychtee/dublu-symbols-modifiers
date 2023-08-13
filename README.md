# dublU's Symbol Dictionary

This is dictionary that combines Emily's Modifier Dictionary and Emily
s Symbol Dictionary so that they work the same way. Check those dictionaries out here:

-   [Emily's Symbol Dictionary](https://github.com/EPLHREU/emily-symbols)
-   [Emily's Modifier Dictionary](https://github.com/EPLHREU/emily-modifiers)

## Design

This dictionary was created with the following goals in mind:

-   Have a consistent method to type (pretty much) every symbol
-   Specify spacing and capitalisation of that symbol in 1 stroke
-   Hackable and understandable to anyone who finds it useful :)

## Sections

To support the design goals, for each symbol there are 6 different options specifiable in sections of each stroke:

1. Capitalisation (Teal)
2. Symbol (Purple)
3. Variant (Magenta)
4. Repetition (Blue)
5. Spacing (Yellow)
6. Modifier (Green)
7. Ending (Orange/Red)

These options are mapped to different sections of the steno board:

![Coloured Layout Diagram](img/layout.svg)

### Enders

The enders are used to tell what patterns should be used.

| Keys                                            | Description             |
| ----------------------------------------------- | ----------------------- |
| ![Ender Diagram Letters](img/ender-letters.svg) | Use `-LGSZ` for letters |
| ![Ender Diagram Symbols](img/ender-symbols.svg) | Use `-LTDZ` for symbols |
| ![Ender Diagram Numbers](img/ender-numbers.svg) | Use `-GSDZ` for numbers |

### Modifier keys

To do a key combo, press one or more of the modifier keys.

| Keys                                         | Description |
| -------------------------------------------- | ----------- |
| ![Modifier Diagram Control](img/control.svg) | Control     |
| ![Modifier Diagram Shift](img/shift.svg)     | Shift       |
| ![Modifier Diagram Super](img/super.svg)     | Super       |
| ![Modifier Diagram Meta](img/meta.svg)       | Meta / Alt  |

### Spacing / Attachment

To specify spacing, use the `E` and `U` keys.
In `space` mode, use the `E` key for a space to the left of the symbol, and use the `U` key for a space to the right of the symbol.
In `attachment` mode, there are spaces on both sides by default and pressing the key removes the space on that side.

| Keys                                          | Space mode | Attach mode |
| --------------------------------------------- | ---------- | ----------- |
| ![Spacing Diagram None](img/space-none.svg)   | `x.x`      | `x . x`     |
| ![Spacing Diagram Left](img/space-left.svg)   | `x .x`     | `x. x`      |
| ![Spacing Diagram Right](img/space-right.svg) | `x. x`     | `x .x`      |
| ![Spacing Diagram Both](img/space-both.svg)   | `x . x`    | `x.x`       |

### Capitalisation

The `#` can be used to specify capitalisation of the text following the symbol.

By default no capitalisation is applied.
| Key | Output |
|-----------------------------------------|------------------|
| ![Lowercase Diagram](img/lowercase.svg) | `x . x`, `(cons` |

With the `#` key used, the next input is capitalised.
| Key | Output |
|-----------------------------------------|---------------------|
| ![Uppercase Diagram](img/uppercase.svg) | `x . X`, `said "To` |

### Variant

There are a lot of similar symbols, to manage this, each symbol has a base symbol and a list of variant symbols.
The specific variant required is chosen with a combination of the `E` and `U` keys, this allows for 4 total variants of a symbol.

| Key                                     | Variant | Output |
| --------------------------------------- | ------- | ------ |
| ![Variant 0 Diagram](img/variant-0.svg) | `0`     | `(`    |
| ![Variant 1 Diagram](img/variant-1.svg) | `1`     | `[`    |
| ![Variant 2 Diagram](img/variant-2.svg) | `2`     | `<`    |
| ![Variant 3 Diagram](img/variant-3.svg) | `3`     | `{`    |

### Symbol

The main section is the symbol section, used to specify the specific symbol to type.
Only a 2x3 grid is needed to address all the symbols, using variants. Exception: & Ampersand.
All of the patterns for symbols are done according to shape, rather than phonetics or briefs, and so should be remember visually with the images as an aid.
For each symbol shape the pattern only addresses the base symbol, it doesn't apply as well to the variant symbols. As such, the variants should be anchored in memory to the base symbol itself rather than the pattern.

All of these are the same as Emily's Symbol Dictionary, except that they are located on the left side (`TKPWHR`), and the & Ampersand is `SKP`, and not mirrored.

| Pattern                                           | Symbols                                                         | Description                                                                 |
| ------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Whitespace                                        |                                                                 |                                                                             |
| ![Whitespace Diagram](img/whitespace.svg)         | `{#Tab} {#Backspace} {#Delete} {#Escape}`                       | The pattern aligns with the tips of the arrows on a tab key legend: ↹       |
| Arrows                                            |                                                                 |                                                                             |
| ![Arrow Diagram](img/arrow.svg)                   | `{#Up} {#Left} {#Right} {#Down}`                                | Looks like an arrow key cluster                                             |
| ↑                                                 |                                                                 |                                                                             |
| ![Arrow Symbols Diagram](img/arrow-symbols.svg)   | `↑ ← → ↓`                                                       | Looks like an upside-down arrow key cluster                                 |
| Navigation                                        |                                                                 |                                                                             |
| ![Navigation Diagram](img/nav.svg)                | `{#Page_Up} {#Home} {#End} {#Page_Down}`                        | Arrow key cluster but with an addition key held down                        |
| Music                                             |                                                                 |                                                                             |
| ![Music Diagram](img/music.svg)                   | `{#AudioPlay} {#AudioPrev} {#AudioNext} {#AudioMute}`           | Like a strangely rotated L for err... \_L_ovely music?                      |
| Audio                                             |                                                                 |                                                                             |
| ![Audio Diagram](img/audio.svg)                   | `{#AudioMute} {#AudioLowerVolume} {#AudioRaiseVolume} {#Eject}` | Like a smaller strangely rotated L for err... \_l_ovely music control?      |
| Blank                                             |                                                                 |                                                                             |
| ![Blank Diagram](img/blank.svg)                   | `'' {*!} {*?} {#Space}`                                         | It's blank! Self descriptive                                                |
| Capitalization                                    |                                                                 |                                                                             |
| ![Capitalization Diagram](img/capitalization.svg) | `{*-\|} {*<} {<} {*>}`                                          | Up at the top, separate, it's pointy like capital letters                   |
| !                                                 |                                                                 |                                                                             |
| ![Exclamation Diagram](img/exclamation.svg)       | `! ¬ ↦ ¡`                                                       | Vertical shape that's off to the left, like `!` on a regular keyboard       |
| "                                                 |                                                                 |                                                                             |
| ![Double Quote Diagram](img/double-quote.svg)     | `" “ ” „`                                                       | Two dots up high like its shape, and off to the left like on ISO keyboards  |
| \#                                                |                                                                 |                                                                             |
| ![Hash Diagram](img/hash.svg)                     | `# © ® ™`                                                       | Two vertical bars like in the shape                                         |
| $                                                 |                                                                 |                                                                             |
| ![Dollar Diagram](img/dollar.svg)                 | `$ ¥ € £`                                                       | Makes an `S` shape like a `$`                                               |
| %                                                 |                                                                 |                                                                             |
| ![Percent Diagram](img/percent.svg)               | `% ‰ ‱ φ`                                                       | Same as a `/` but with the two extra keys representing the dots             |
| &                                                 |                                                                 |                                                                             |
| ![Ampersand Diagram](img/ampersand.svg)           | `& ∩ ∧ ∈`                                                       | Same as the standard 'and' brief                                            |
| '                                                 |                                                                 |                                                                             |
| ![quote Diagram](img/quote.svg)                   | `' ‘ ’ ‚`                                                       | One dot up high, similar to `"`, on the index for importance                |
| (                                                 |                                                                 |                                                                             |
| ![Open Diagram](img/open.svg)                     | `( [ < {`                                                       | Similar to the standard steno brief                                         |
| )                                                 |                                                                 |                                                                             |
| ![Close Diagram](img/close.svg)                   | `) ] > }`                                                       | Similar to the standard steno brief                                         |
| \*                                                |                                                                 |                                                                             |
| ![Star Diagram](img/star.svg)                     | `* ∏ § ×`                                                       | single dot shape, off to the right like JIS, up high in the sky             |
| +                                                 |                                                                 |                                                                             |
| ![Plus Diagram](img/plus.svg)                     | `+ ∑ ¶ ±`                                                       | single dot shape, off to the right like JIS, under the star                 |
| ,                                                 |                                                                 |                                                                             |
| ![Comma Diagram](img/comma.svg)                   | `, ∪ ∨ ∉`                                                       | Single dot shape, below like on a keyboard, middle finger as less important |
| -                                                 |                                                                 |                                                                             |
| ![Dash Diagram](img/dash.svg)                     | `- − – —`                                                       | Line in shape, up in the top right like a normal keyboard                   |
| .                                                 |                                                                 |                                                                             |
| ![Dot Diagram](img/dot.svg)                       | `. • · …`                                                       | Single dot in shape, below like on a keyboard, index finger as important    |
| /                                                 |                                                                 |                                                                             |
| ![Slash Diagram](img/slash.svg)                   | `/ ⇒ ⇔ ÷`                                                       | Shape of a `/`                                                              |
| :                                                 |                                                                 |                                                                             |
| ![Colon Diagram](img/colon.svg)                   | `: ∋ ∵ ∴`                                                       | Vertical shape, off to the right like a normal keyboard                     |
| ;                                                 |                                                                 |                                                                             |
| ![Semicolon Diagram](img/semicolon.svg)           | `; ∀ ∃ ∄`                                                       | Literally a `,` and `.` at the same time                                    |
| =                                                 |                                                                 |                                                                             |
| ![Equals Diagram](img/equals.svg)                 | `= ≡ ≈ ≠`                                                       | Literally a `-` and a `_` at the same time                                  |
| ?                                                 |                                                                 |                                                                             |
| ![Question Diagram](img/question.svg)             | `? ¿ ∝ ‽`                                                       | Looks like the top of a `?`                                                 |
| @                                                 |                                                                 |                                                                             |
| ![At Diagram](img/at.svg)                         | `@ ⊕ ⊗ ∅`                                                       | Large complicated shape, only way to make a big spiral                      |
| \\                                                |                                                                 |                                                                             |
| ![Backslash Diagram](img/backslash.svg)           | `\ Δ √ ∞`                                                       | Shape of a `\`                                                              |
| ^                                                 |                                                                 |                                                                             |
| ![Caret Diagram](img/caret.svg)                   | `^ « » °`                                                       | Shape of a `^` and other pointy/raised symbols                              |
| \_                                                |                                                                 |                                                                             |
| ![Underscore Diagram](img/underscore.svg)         | `_ ≤ ≥ µ`                                                       | A line down low opposing `-`, and other lowered symbols                     |
| \`                                                |                                                                 |                                                                             |
| ![Backtick Diagram](img/backtick.svg)             | `` ` ⊂ ⊃ π``                                                    | Single dot up high, next to `'`                                             |
| \|                                                |                                                                 |                                                                             |
| ![Pipe Diagram](img/pipe.svg)                     | `\| ⊤ ⊥ ¦`                                                      | Nice symetrical vertical shape goes in the middle                           |
| \~                                                |                                                                 |                                                                             |
| ![Tilde Diagram](img/tilde.svg)                   | `~ ⊆ ⊇ ˜`                                                       | Makes the shape of a `~`                                                    |

### Repetition

You may want to duplicate certain symbols, such as logical OR `||` or org-mode headings `### Title`.
Repetition is done in binary with the `E` and `U` keys.
By default any symbol is typed out once.

| Key                             | Output |
| ------------------------------- | ------ |
| ![One Diagram](img/one.svg)     | `:`    |
| ![Two Diagram](img/two.svg)     | `::`   |
| ![Three Diagram](img/three.svg) | `:::`  |
| ![Four Diagram](img/four.svg)   | `::::` |

## Poster

Poster does not match this version of the dictionary.

See the poster here:
[emily-symbols-poster](emily-symbols-poster.pdf)
