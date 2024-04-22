def expectedPrioriProb():

    """
        Primero obtenemos nuestro winrate general, 
        despues al ser eventos independientes A=abordajesAnteriores, B=AbordajeFuturo
        vamos a usar la regla de la multiplicacion P(A)*P(B)
        vamos a partir de la regla de pareto para este ejemplo (no tengo data especifica sobre esto lol)
        Queremos "jugar" con edge o en un estado de balance al menos, entonces tendemos a preguntar a mutuals
        o a sus amig@s que onda (pienso), entonces la taza de exito particular debería ser la siguiente segun
        tengamos edge, no sepamos o no tengamos:
        
        1. sabemos que le gustamos-->80% de las veces vamos a tener exito mientras no digamos nada TAAAN estupido o en contra de sus ideales
        
        2. No sabemos --> Let's gamble my boy

        3. sabemos que no le gustamos --> The best of men are but men at best, nadie te dice que no pero no deberías lol...
    """
    totalApproaches = int(input("Ingrese el número total de abordajes (ultimo año): "))
    totalSuccess = int(input("Ingrese el número total de éxitos (ultimo año): "))
    insiderInfoInput = input("¿Sabes si le gustas? (Si/No/No se): ").lower()
    
    if insiderInfoInput == "si":
        insiderInfoEdge = 0.8
    elif insiderInfoInput == "no":
        insiderInfoEdge = 0.2
    elif insiderInfoInput=="no se":
        insiderInfoEdge = 0.5
    
    globalWinRate = totalSuccess / totalApproaches
    expectedOutcome = globalWinRate * insiderInfoEdge
    
    return expectedOutcome

# Una vez tenemos una prob a priori ligeramente más realista (creo) que un simple 50/50, ahora si vamos a bayes

def isSheIntoYou(priori_prob: float, evidences: list=[]):
    """
        Ahora aqui calculamos si le gustas o no LOL,
        usando Bayes, vamos a usar una lista de evidencias

        evidences:
            es una lista de tuplas estructuradas de la siguiente forma:
            (Evento, probabilidad que ocurra si le gustas, evidencia especifica, probabilidad de que ocurra independientemente si le gusta o no)

        return:
            Retornamos el valor float resultante de la formula
    """

    print("Le pareces atractivo?")

    for evidence in evidences:
        event=evidence[0]
        evidenceGivenSheIntoYou=evidence[1]
        evidence= evidence[3]
        print("Situacion: "+ event + " --- Probabilidad si le pareces atractivo: " + str(evidenceGivenSheIntoYou))
        posteriori_prob = (priori_prob * evidenceGivenSheIntoYou) / evidence
        priori_prob = posteriori_prob / (posteriori_prob + (1 - priori_prob))
    
    return priori_prob

if __name__ == "__main__":
    # Calcula la probabilidad a priori
    priori_prob = expectedPrioriProb()

    # Define las evidencias
    evidences = [
        #Evento, probabilidad que ocurra si le gustas, evidencia especifica, probabilidad de que ocurra independientemente si le gusta o no
        ("Conversación fluida", 0.7, "Se rie mucho", 0.8),
        ("Amigos en común", 0.5, "Te sigue en redes sociales", 0.9),
        ("Likear stories", 0.8, "Te likea seguido", 0.8),
        ("responder stories", 0.7, "te responde seguido",0.8),
        ("Sube indirectas", 0.9, "Son especificas a tu perfil", 0.5),
        ("Esta disponible en tiempo", 0.85, "Sale contigo", 0.5),
        ("Ghosting", 0.5, "te deja hablando solo lol", 0.5),
        ("sugerir salir", 0.7, "salen", 0.6),
        ("Etiquetarse en publicaciones", 0.65, "Te etiqueta en publicaciones", 0.9),
        ("Enviar memes", 0.5, "Te envía memes", 0.5),
        ("Chats nocturnos", 0.8, "Chatea contigo hasta tarde", 0.7),
        ("Compartir música", 0.8, "Te comparte canciones o listas de reproducción", 0.8),

    ]

    # Calcula la probabilidad posterior utilizando Bayes
    res = isSheIntoYou(priori_prob, evidences)

    print("La probabilidad de que le atraigas es:", res)

    if res>0.51:
        print("Prolly le gusta tu atención y tu")
    elif res<0.51 and res>0.4:
        print("Prolly le gusta tu atención, no tu")
    elif res<0.4:
        print("mi hermano en cristo, para pq te van a demandar lol")