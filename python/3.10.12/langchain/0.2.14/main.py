import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar o modelo de linguagem
chat = ChatOpenAI(
    temperature=0.7,  # Controle de criatividade (0 = mais objetivo, 1 = mais criativo)
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo"
)

# Mensagens do contexto do chatbot
def main():
    print("Chatbot: Olá! Eu sou seu assistente. Pergunte-me qualquer coisa. Digite 'sair' para encerrar.\n")

    # Lista para armazenar o histórico de mensagens
    messages = [SystemMessage(content="Você é um assistente útil e amigável.")]

    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Chatbot: Até logo!")
            break

        # Adiciona a mensagem do usuário ao histórico
        messages.append(HumanMessage(content=user_input))

        # Gera a resposta do chatbot
        try:
            response = chat.invoke(messages)
            chatbot_reply = response.content
            print(f"Chatbot: {chatbot_reply}")

            # Adiciona a resposta do AI ao histórico
            messages.append(AIMessage(content=chatbot_reply))
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()