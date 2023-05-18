def inference_rules(T, E, S, A):
    CONJUNCTION = 'and'
    DISJUNCTION = 'or'
    IMPLICATION = '<='
    NEGATION = 'not'

    def Modus_Ponens(p, q):
        if p and (p <= q):
            return q

    def Modus_Tollens(p, q):
        if (NEGATION + str(p) + IMPLICATION + str(q)) and (NEGATION + str(q)):
            return NEGATION + str(p)

    def Hypothetical_Syllogism(p, q, r):
        if (str(p) + IMPLICATION + str(q)) and (str(q) + IMPLICATION + str(r)):
            return str(p) + IMPLICATION + str(r)

    def Disjunctive_Syllogism(p, q):
        if (str(p) + DISJUNCTION + str(q)) and (NEGATION + str(p)):
            return str(q)

    def Conjunction(p, q):
        if str(p) and str(q):
            return str(p) + CONJUNCTION + str(q)

    def Disjunction(p, q):
        if str(p) or str(q):
            return str(p) + DISJUNCTION + str(q)

    def Negation(p):
        if str(p):
            return NEGATION + str(p)

    def Simplification(p, q):
        if str(p) and str(q):
            return str(p), str(q)

    def Addition(p, q):
        if str(p):
            return str(p) + DISJUNCTION + str(q)

    def Resolution(p, q, r):
        if (str(p) + IMPLICATION + str(q)) and (NEGATION + str(q) + DISJUNCTION + str(r)):
            return str(p) + IMPLICATION + eval(NEGATION + str(r))

    def Universal_Instantiation(p):
        if str(p):
            return str(p)

    def Universal_Generalization(p):
        if str(p):
            return str(p), str(p)

    def Existential_Instantiation(p):
        if str(p):
            return "p(x)"

    def Existential_Generalization(p):
        if str(p):
            return "there exists a y such that p(y)"
        if (str(p) + DISJUNCTION + str(q)) and (NEGATION + str(p)):
            return str(q)

    # Applying inference rules to the given premises
    rule1 = Hypothetical_Syllogism(T, E, S)
    rule2 = Modus_Tollens(E <= A, NEGATION + str(A))
    rule3 = Modus_Ponens(Conjunction(T, Negation(A)), rule1)
    conclusion = Disjunctive_Syllogism(rule3, rule2)

    return conclusion

paragraph = input("Enter the paragraph: ")


# Split the paragraph into sentences
sentenceslist = [sentence.strip() for sentence in paragraph.split('.') if sentence.strip()]

# Define the inference rules symbols
symbols = {
    "not": "¬",
    "and": "∧",
    "or": "∨",
    "=>": "->",
    "<=>": "<->",
    "xor": "⊕",
    "if then": "→",
    "if and only if": "↔"
}

prop = []
final = []

def translate(x):
    for s in x:
        s = s.lower()

        for key, value in symbols.items():
            s = s.replace(key, value)

        prop.append(s)

    print(prop)

    let = 97

    for p in prop:
        if symbols["not"] in p:
            f = (chr(let) + " " + symbols["not"] + " " + chr(let + 1))
            final.append(f)
            print(f)
            let += 2

        elif symbols["and"] in p:
            f = (chr(let) + " " + symbols["and"] + " " + chr(let + 1))
            final.append(f)
            print(f)
            let += 2

        elif symbols["or"] in p:
            f = (chr(let) + " " + symbols["or"] + " " + chr(let + 1))
            final.append(f)
            print(f)
            let += 2

        elif symbols["=>"] in p:
            f = (chr(let) + " " + symbols["=>"] + " " + chr(let + 1))
            final.append(f)
            print(f)
            let += 2

        elif symbols["<=>"] in p:
            f = (chr(let) + " " + symbols["<=>"] + " " + chr(let + 1))
            final.append(f)
            print(f)
            let += 2

        elif symbols["xor"] in p:
            f = (chr(let) + " " + symbols["xor"] + " " + chr(let + 1))
            final.append(f)
            print(f)
            let += 2

        elif symbols["if then"] in p:
            f = (chr(let) + " " + symbols["if then"] + " " + chr(let + 1))
            final.append(f)
            print(f)
            let += 2

        elif symbols["if and only if"] in p:
            f = (chr(let) + " " + symbols["if and only if"] + " " + chr(let + 1))
            final.append(f)
            print(f)
            let += 2

        else:
            f = p
            final.append(f)
            print(f)
            let += 1

    return final[:-1]  # Exclude the last element since it is the quotation mark



# Call the functions to perform inference and translation
conclusion = inference_rules("T", "E", "S", "A")
translated_prop = translate(sentenceslist)

# Print the conclusion of the argument
if conclusion is not None:
    print(f"Therefore, the conclusion is: {conclusion}")
    print(f"Event: {sentenceslist[-1]}")
else:
    print("Conclusion cannot be reached with the given premises.")

 
#If today is Tuesday, I have a test in English or Science. If my English Professor is absent, then I will not have a test in English. Today is Tuesday and my English Professor is absent. Therefore I have a test in Science
