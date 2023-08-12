# dublU's Symbol+Modifier Dictionary

# Based off of Emily's Symbol Dictionary and Emily's Modifier Dictionary
# https://github.com/EPLHREU/emily-symbols
# https://github.com/EPLHREU/emily-modifiers

import re
from plover.key_combo import CHAR_TO_KEYNAME
#             standard command num/fn
uniqueEnders = ["LTZ", "GTZ", "LGTZ"]

# define if attachment keys define where "space"s or "attachment"s lie
attachmentMethod = "space"

LONGEST_KEY = 1

# variant format = ['', 'E', 'U', 'EU']
symbols = {
    # more computer function-y symbols
    "TR"    : ["{#Tab}", "{#Backspace}", "{#Delete}", "{#Escape}"],
    "KPWR"  : ["{#Up}", "{#Left}", "{#Right}", "{#Down}"],
    "TKPWR" : ["{#Page_Up}", "{#Home}", "{#End}", "{#Page_Down}"],
    "TKWR"  : ["{#AudioPlay}", "{#AudioPrev}", "{#AudioNext}", "{#AudioStop}"],
    "TKW"   : ["{#AudioMute}", "{#AudioLowerVolume}", "{#AudioRaiseVolume}", "{#Eject}"],
    ""      : ["⁥", "{*!}", "{*?}", "{#Space}"],
    "TH"    : ["{*-|}", "{*<}", "{<}", "{*>}"],

    # typable symbols
    "TK"     : ["!", "¬", "↦", "¡"],
    "TP"     : ["\"", "“", "”", "„"],
    "TKHR"   : ["#", "©", "®", "™"],
    "KPWH"   : ["$", "¥", "€", "£"],
    "TKPW"   : ["%", "‰", "‱", "φ"],
    "SKP"    : ["&", "∩", "∧", "∈"],
    "T"      : ["'", "‘", "’", "‚"],
    "TPH"    : ["(", "[", "<", "\{"],
    "KWR"    : [")", "]", ">", "\}"],
    "H"      : ["*", "∏", "§", "×"],
    "R"      : ["+", "∑", "¶", "±"],
    "W"      : [",", "∪", "∨", "∉"],
    "PH"     : ["-", "−", "–", "—"],
    "K"      : [".", "•", "·", "…"],
    "KP"     : ["/", "⇒", "⇔", "÷"],
    "HR"     : [":", "∋", "∵", "∴"],
    "KW"     : [";", "∀", "∃", "∄"],
    "PWHR"   : ["=", "≡", "≈", "≠"],
    "TPW"    : ["?", "¿", "∝", "‽"],
    "TKPWHR" : ["@", "⊕", "⊗", "∅"],
    "TW"     : ["\\", "Δ", "√", "∞"],
    "KPR"    : ["^", "«", "»", "°"],
    "WR"     : ["_", "≤", "≥", "µ"],
    "P"      : ["`", "⊂", "⊃", "π"],
    "PW"     : ["|", "⊤", "⊥", "¦"],
    "TPWR"   : ["~", "⊆", "⊇", "˜"],
    "TPWH"   : ["↑", "←", "→", "↓"]
}

# fingerspelling dictionary entries for relevant theories 
spelling = {
    "A"     : "a",
    "PW"    : "b",
    "KR"    : "c",
    "TK"    : "d",
    "E"     : "e",
    "TP"    : "f",
    "TKPW"  : "g",
    "H"     : "h",
    "EU"    : "i",
    "AOEU"    : "i", # magnum
    "SKWR"  : "j",
    "SKWRAEU" : "j", # magnum
    "K"     : "k",
    "HR"    : "l",
    "PH"    : "m",
    "TPH"   : "n",
    "O"     : "o",
    "P"     : "p",
    "KW"    : "q",
    "R"     : "r",
    "S"     : "s",
    "T"     : "t",
    "U"     : "u",
    "SR"    : "v",
    "W"     : "w",
    "KP"    : "x",
    "KWR"   : "y",
    "STKPW" : "z",
    "STKPWHR" : "z", # magnum 
}

def lookup(chord):

    # normalise stroke from embedded number, to preceding hash format
    stroke = chord[0]
    if any(k in stroke for k in "1234506789"):  # if chord contains a number
        stroke = list(stroke)
        numbers = ["O", "S", "T", "P", "H", "A", "F", "P", "L", "T"]
        for key in range(len(stroke)):
            if stroke[key].isnumeric():
                stroke[key] = numbers[int(stroke[key])]  # set number key to letter
                numberFlag = True
        stroke = ["#"] + stroke
        stroke = "".join(stroke)

    # the regex decomposes a stroke into the following groups/variables:
    # capitalization        #
    # pattern                    STKPWHR
    # variants                               AO
    # attachment                                    */-
    # repetition                                           EU
    # modifier                                                    FRPB
    # ender                                                                LGTSDZ
    match = re.fullmatch(r'(#?)([STKPWHR]*)([AO]*)([*-]?)([EU]*)([FRPB]*)([LGTSDZ]*)', stroke)

    if match is None:
        raise KeyError
    (capitalization, pattern, variants, attachment, repetitions, modifier, ender) = match.groups()

    if ender not in uniqueEnders:
        raise KeyError
    if len(chord) != 1:
        raise KeyError
    assert len(chord) <= LONGEST_KEY


    # get the attachment method
    attachment = attachment == "*"
    attach = [(attachmentMethod == "space") ^ ('F' in modifier),
                (attachmentMethod == "space") ^ ('R' in modifier)]

    # get if command or not
    command = True if modifier and not attachment else False

    # get variant number
    variant = 0
    if 'A' in variants:
        variant = variant + 1
    if 'O' in variants:
        variant = variant + 2

    # get number of repetitions
    repeat = 1
    if 'E' in repetitions:
        repeat = repeat + 1
    if 'U' in repetitions:
        repeat = repeat + 2


    function = False
    # get pressed character
    character = None
    if ender == uniqueEnders[0]: # symbols -LTZ
        character = symbols[pattern]
    elif ender == uniqueEnders[1]: # letters -GTZ
        character = spelling[pattern]
    elif ender == uniqueEnders[2]: # numbers / fn keys -LGTZ
        # get binary number from pattern
        count = 0
        if "R" in pattern:
            count = count + 1
        if "W" in pattern:
            count = count + 2
        if "K" in pattern:
            count = count + 4
        if "S" in pattern:
            count = count + 8

        # if TP is being held as well, then user is inputting a Fx key - like alt+F4
        if "T" in pattern and "P" in pattern:
            function = True

        # add the 'F' if fn key
        if function:
            character = "F" + str(count)
            if count > 12:
                raise KeyError
        else:
            if count > 9:
                raise KeyError
            character = str(count)

    # get variant
    if type(character) == list:
        character = character[variant]
    output = character


    if command or function:

        if not function: # don't do this to function keys
            if output not in CHAR_TO_KEYNAME:
                raise KeyError
            output = CHAR_TO_KEYNAME[output] # ";" -> "semicolon"

        output = ' '.join([output * repeat])

        mods = []
        if "R" in modifier:
            mods.append("shift")
        if "F" in modifier:
            mods.append("control")
        if "B" in modifier:
            mods.append("alt")
        if "P" in modifier:
            mods.append("super")

        # add modifiers
        for mod in mods:
            output = mod + "(" + output + ")"

        # plover command syntax
        output = "{#" + output + "}"

    else:
        # repeat the symbol the specified number of times
        output = output * repeat

        if character not in ["{*!}", "{*?}"]:

            # attachment space to either end of the symbol string to avoid escapement,
            # but prevent doing this for retrospective add/delete spaces, since it'll
            # mess with these macros
            output = " " + output + " "

            # add appropriate attachment as specified (again, prevent doing this 
            # for retrospective add/delete spaces)
            if attach[0]:
                output = "{^}" + output
            if attach[1]:
                output = output + "{^}"

        # cancel out some formatting when using space attachment
        if attachmentMethod == "space":
            if not attach[0]:
                output = "{}" + output
            if not attach[1]:
                output = output + "{}"

    # apply capitalisation
    if capitalization == "#":
        output = output + "{-|}"

    # all done :D
    return output
