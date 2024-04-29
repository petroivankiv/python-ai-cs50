from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Puzzle 0
# A says "I am both a knight and a knave."
# Expected: A is a Knave
knowledge0 = And(
    # Правила гри
    Biconditional(AKnight, Not(AKnave)),

    # A says "I am both a knight and a knave."
    # Implication(AKnight, And(AKnight, AKnave)),
    Or(Not(AKnight), And(AKnight, AKnave)),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
# Expected: A is a Knave, B is a Knight
knowledge1 = And(
    # Правила гри
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),

    # A says "We are both knaves."
    Biconditional(AKnight, And(AKnave, BKnave)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# Expected: A is a Knave, B is a Knight
knowledge2 = And(
    # Правила гри
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),

    # A says "We are the same kind."
    # Or(Not(AKnight), BKnight),
    # Or(Not(AKnave), Not(BKnave)),
    Biconditional(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),

    # B says "We are of different kinds."
    # Or(Not(BKnight), Not(AKnight)),
    # Or(Not(BKnave), AKnave),
    Biconditional(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# Expected: A is a Knight, B is a Knave, C is a Knight
knowledge3 = And(
    # Правила гри
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
    
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Biconditional(AKnight, Or(AKnave, AKnight)),
    
    # B says "A said 'I am a knave'."
    Implication(BKnight, Implication(AKnight, AKnave)),
    
    # B says "C is a knave."
    Implication(BKnight, CKnave),
    
    # C says "A is a knight."
    Biconditional(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
