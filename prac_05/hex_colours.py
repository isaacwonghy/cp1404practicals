
COLOUR_NAME_TO_CODE = {"Absolute zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
               "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
               "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1","Aqua": "00ffff"}

print(colours)

hex_colours = input("Enter colour: ").upper()
 while hex_colours != "":
    if hex_colours in COLOUR_NAME_TO_CODE:
        print(hex_colours, "is", COLOUR_NAME_TO_CODE[hex_colours])
    else:
        print("Invalid hex colour")
    hex_colours = input("Enter colour: ").upper()

