import enum
from japverbconj.constants.enumerated_types import VerbClass
from japverbconj.verb_form_gen import generate_japanese_verb_by_str
# Define enums for BaseForm, Formality, Tense, and Polarity
class BaseForm(enum.Enum):
    PLAIN = "pla"
    POLITE = "pol"
    TE = "te"
    TA = "ta"
    TARI = "tari"
    CONDITIONAL = "cond"
    VOLITIONAL = "vol"
    POTENTIAL = "pot"
    IMPERATIVE = "imp"
    PROVISIONAL = "prov"
    CAUSATIVE = "caus"
    PASSIVE = "pass"
    def lower(self):
        return self.value.lower()

class Formality(enum.Enum):
    PLAIN = "pla"
    POLITE = "pol"

class Tense(enum.Enum):
    NONPAST = "nonpast"
    PAST = "past"

class Polarity(enum.Enum):
    POSITIVE = "pos"
    NEGATIVE = "neg"