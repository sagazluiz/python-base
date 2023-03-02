names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barabara", 
    "Brian",
     ]


# Todo: Usar lambdas

def starts_with_b(text):
    return text[0].lower() == "b"

print(*list(filter(starts_with_b, names)))
