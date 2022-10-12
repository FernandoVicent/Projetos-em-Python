from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('pandora')

trainer = ListTrainer(chatbot)

trainer.train([
    "Não estou conseguindo imprimir, can I help you?",
    "Você poderia tentar verificar se você esta com acesso a rede,ou se sua impressora é conectada pelo usb verifique o cabo.",
    "Your flight has been booked."
])
nome_user = input('Digite seu nome: ')
while True:
    request = input(f'{nome_user}: ')
    response = chatbot.get_response(request)
    print('BOT: ',response)

print(response)