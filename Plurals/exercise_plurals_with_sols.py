import random 
irregular_plural_dict = {
    "addendum": "addenda or addendums",
    "aircraft": "aircraft",
    "alumna": "alumnae",
    "alumnus": "alumni",
    "analysis": "analyses",
    "antenna": "antennae or antennas",
    "antithesis": "antitheses",
    "apex": "apices or apexes",
    "appendix": "appendices or appendixes",
    "axis": "axes",
    "bacillus": "bacilli",
    "bacterium": "bacteria",
    "basis": "bases",
    "beau": "beaux or beaus",
    "bison": "bison",
    "bureau": "bureaux or bureaus",
    "cactus": "cacti or cactus or cactuses",
    "château": "châteaux or châteaus",
    "child": "children",
    "codex": "codices",
    "concerto": "concerti or concertos",
    "corpus": "corpora",
    "crisis": "crises",
    "criterion": "criteria or criterions",
    "curriculum": "curricula or curriculums",
    "datum": "data",
    "deer": "deer or deers",
    "diagnosis": "diagnoses",
    "die": "dice or dies",
    "dwarf": "dwarves or dwarfs",
    "ellipsis": "ellipses",
    "erratum": "errata",
    "faux pas": "faux pas",
    "fez": "fezzes or fezes",
    "fish": "fish or fishes",
    "focus": "foci or focuses",
    "foot": "feet or foot",
    "formula": "formulae or formulas",
    "fungus": "fungi or funguses",
    "genus": "genera or genuses",
    "goose": "geese",
    "graffiti": "graffiti",
    "grouse": "grouse or grouses",
    "half": "halves",
    "hoof": "hooves or hoofs",
    "hypothesis": "hypotheses",
    "index": "indices or indexes",
    "larva": "larvae or larvas",
    "libretto": "libretti or libretto",
    "loaf": "loaves",
    "man": "men",
    "medium": "media",
    "memorandum": "memoranda or memorandums",
    "mouse": "mice",
    "nucleus": "nuclei",
    "oasis": "oases",
    "octopus": "octopi or octopuses",
    "ovum": "ova",
    "phenomenon": "phenomena",
    "radius": "radii",
    "stimulus": "stimuli",
    "syllabus": "syllabi or syllabuses",
    "thesis": "theses",
    "tooth": "teeth",
    "woman": "women"
}

keys = list(irregular_plural_dict.keys())
values = list(irregular_plural_dict.values())

i = 0
action = "Go on!"

while action != "q":
    i = random.randint(0, len(keys) - 1)
    action = input(f"Index: {keys[i]}\nPress Enter to reveal the plural, or 'q' to quit: ")

    if action.lower() == 'q':
        print("Quitting...")
        break

    print(f"The plural is {values[i]}\n")
