import enum
class VerbForm:
    def __init__(self, description, godan_ending, ichidan_ending):
        self.description = description
        self.godan_ending = godan_ending
        self.ichidan_ending = ichidan_ending

class JapaneseVerbForms(enum.Enum):
    # Basic Verb Forms
    DICTIONARY_FORM = VerbForm(
        "Dictionary Form (辞書形, jisho-kei): The basic form found in dictionaries.",
        "u",
        "ru"
    )
    MASU_FORM = VerbForm(
        "Masu Form (ます形, masu-kei): Polite present/future form.",
        "imasu",
        "masu"
    )
    # TE_FORM = VerbForm(
    #     "Te Form (て形, te-kei): Used for connecting verbs, making requests, and forming continuous tenses.",
    #     "tte",
    #     "te"
    # )
    # TA_FORM = VerbForm(
    #     "Ta Form (た形, ta-kei): Past tense.",
    #     "utta",
    #     "uta"
    # )
    NAI_FORM = VerbForm(
        "Nai Form (ない形, nai-kei): Negative form.",
        "anai",
        "nai"
    )
    NAIDE_FORM = VerbForm(
        "Naide Form (ないで形, naide-kei): Negative request form.",
        "anaide",
        "naide"
    )

    # TARA_FORM = VerbForm(
    #     "Tara Form (たら形, tara-kei): Do when V",
    #     "ttara",
    #     "tara"
    # )

    # Volitional and Desire Forms
    VOLITIONAL_FORM = VerbForm(
        "Volitional Form (意向形, ikou-kei): Let's V",
        "ou",
        "you"
    )
    TAI_FORM = VerbForm(
        "Tai Form (たい形, tai-kei): Want to V",
        "itai",
        "tai"
    )

    # Imperative Forms
    IMPERATIVE_FORM = VerbForm(
        "Imperative Form (命令形, meirei-kei): Command ",
        "e",
        "ro"
    )
    NEGATIVE_IMPERATIVE_FORM = VerbForm(
        "Negative Imperative Form (禁止形, kinshi-kei): Don't Command V.",
        "una",
        "ru na"
    )

    # Passive and Causative Forms
    PASSIVE_FORM = VerbForm(
        "Passive Form (受身形, ukemi-kei): be V passive.",
        "areru",
        "rareru"
    )
    CAUSATIVE_FORM = VerbForm(
        "Causative Form (使役形, shieki-kei): Make somebody V",
        "aseru",
        "saseru"
    )
    CAUSATIVE_PASSIVE_FORM = VerbForm(
        "Causative Passive Form (使役受身形, shieki ukemi-kei): Being made to V",
        "aserareru",
        "saserareru"
    )

    # Potential Forms
    POTENTIAL_FORM = VerbForm(
        "Potential Form (可能形, kanou-kei): Can V",
        "eru",
        "rareru"
    )

    # Polite Forms
    POLITE_PRESENT_FORM = VerbForm(
        "Polite Present/Future Form (ます形, masu-kei): Polite V",
        "imasu",
        "masu"
    )
    POLITE_PAST_FORM = VerbForm(
        "Polite Past Form (ました形, mashita-kei): Polite V in the past",
        "imashita",
        "mashita"
    )
    POLITE_NEGATIVE_FORM = VerbForm(
        "Polite Negative Form (ません形, masen-kei): Polite not V",
        "imasen",
        "masen"
    )
    POLITE_NEGATIVE_PAST_FORM = VerbForm(
        "Polite Negative Past Form (ませんでした形, masen deshita-kei): Polite not V in the past",
        "imasen deshita",
        "masen deshita"
    )

    # Others
    PROVISIONAL_FORM = VerbForm(
        "Provisional Form (仮定形, katei-kei): Hypothetical form often used for 'if' statements.",
        "eba",
        "reba"
    )
    CONDITIONAL_FORM = VerbForm(
        "Conditional Form (条件形, jouken-kei): Another form for expressing conditions.",
        "eba",
        "reba"
    )
    EBA_FORM = VerbForm(
        "Eba Form (えば形, eba-kei): If (similar to ba-form).",
        "eba",
        "reba"
    )