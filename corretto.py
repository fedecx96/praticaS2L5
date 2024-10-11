import datetime
def assistente_virtuale(comando):
    if comando == "Qual è la data di oggi?": #non gestito lettera minuscola
        oggi = datetime.date.today() #bug2
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."
    return risposta
while True: #bug1
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente.lower() == "esci": #non comunica come uscire dal programma
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))
