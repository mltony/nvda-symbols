@echo off
setlocal EnableDelayedExpansion
set n=0

erase final.dic
echo symbols: > final.dic
for %%s in (
    "Arrows" 
    "Block Elements"
    "Box Drawing"
    "Braille Patterns"
    "Dingbats"
    "Enclosed Alphanumerics"
    "Geometric Shapes Extended"
    "Geometric Shapes"
    "Halfwidth and Fullwidth Forms"
    "Ideographic Description Characters"
    "Letterlike Symbols"
    "Mathematical Alphanumeric Symbols"
    "Mathematical Operators"
    "Miscellaneous Mathematical Symbols-A"
    "Miscellaneous Mathematical Symbols-B"
    "Miscellaneous Symbols and Arrows"
    "Miscellaneous Symbols and Pictographs"
    "Miscellaneous Symbols"
    "Miscellaneous Technical"
    "Musical Symbols"
    "Playing Cards"
    "Supplemental Mathematical Operators"
    "Supplemental Punctuation"
) do  (
    type allBlocks\%%s.dic >> final.dic
)

type PresortedGeneralPunctuation.dic >> final.dic
type Greek\ProcessedGreek5.dic >> final.dic
