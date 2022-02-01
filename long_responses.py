import random

R_EATING = "Aku adalah bot tentu saja aku tidak makan -_-"
R_ADVICE = "Tanyakan kepada rumput yang bergoyang"


def unknown():
    response = ["Apakah kamu bisa mengulanginya? ",
                "...",
                "Aku tidak paham.",
                "Maaf aku tidak mengerti"][
        random.randrange(4)]
    return response
