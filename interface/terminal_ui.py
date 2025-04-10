from app.chatbot import RecyclingChatbot

def run_terminal_chatbot():
    chatbot = RecyclingChatbot()
    print("Chatbot de Reciclagem - Digite sua pergunta ou 'sair' para encerrar")
    
    while True:
        user_input = input("\nVocê: ")
        if user_input.lower() == 'sair':
            break
            
        response = chatbot.handle_query(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    run_terminal_chatbot()