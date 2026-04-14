EN_TO_SW = {
    "buy maize": "nunua mahindi",
    "hello": "habari",
    "good morning": "habari za asubuhi",
    "thank you": "asante",
    "water": "maji",
    "food": "chakula",
    "how are you": "habari yako",
    "yes": "ndio",
    "no": "hapana",
    "come here": "kuja hapa"
}

SW_TO_EN = {v: k for k, v in EN_TO_SW.items()}


def translate(text, target):
    text = text.lower().strip()

    if target == "sw":
        return EN_TO_SW.get(text, text)

    if target == "en":
        return SW_TO_EN.get(text, text)

    return text