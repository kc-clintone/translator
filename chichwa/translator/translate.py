eng_swa = {
    "buy maize": "nunua mahindi",
    "hello": "habari",
    "good morning": "habari za asubuhi",
    "thank you": "asante",
    "water": "maji",
    "food": "chakula",
    "how are you": "habari yako",
    "yes": "ndio",
    "no": "hapana",
    "come here": "kuja hapa",
    "put stone": "weka mawe",
    "it is bad": "ni mbaya",
}

swa_eng = {v: k for k, v in eng_swa.items()}


def translate(text, target):
    text = text.lower().strip()

    if target == "sw":
        return eng_swa.get(text, text)

    if target == "en":
        return swa_eng.get(text, text)

    return text