import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Groq API configuration
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama3-8b-8192"  # Llama3 8B model on Groq

def call_llama3(messages):
    """Call Groq API to get response from Llama3"""
    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": MODEL_NAME,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1000
        }
        
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]
        
    except requests.exceptions.ConnectionError:
        raise Exception("Impossible de se connecter à Groq API. Vérifiez votre connexion internet.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            raise Exception("Clé API Groq invalide. Vérifiez votre variable d'environnement GROQ_API_KEY.")
        elif response.status_code == 429:
            raise Exception("Limite de taux atteinte. Attendez un moment avant de réessayer.")
        else:
            raise Exception(f"Erreur HTTP {response.status_code}: {e}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erreur lors de l'appel à Groq API: {e}")
    except KeyError:
        raise Exception("Réponse inattendue de l'API Groq.")
    except Exception as e:
        raise Exception(f"Erreur inattendue: {e}")

def chatbot():
    # Create a list to store all the messages for context
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    # Keep repeating the following
    while True:
        # Prompt user for input
        message = input("User: ")

        # Exit program if user inputs "quit"
        if message.lower() == "quit":
            break        # Add each new message to the list
        messages.append({"role": "user", "content": message})

        try:
            # Request Llama3 for chat completion
            chat_message = call_llama3(messages)
            print(f"Bot: {chat_message}")
            messages.append({"role": "assistant", "content": chat_message})
            
        except Exception as e:
            print(f"Erreur lors de l'appel à Groq API: {e}")
            print("Vérifiez votre clé API Groq dans le fichier .env")

if __name__ == "__main__":
    # Check if API key is set
    if not GROQ_API_KEY:
        print("Erreur: La variable d'environnement GROQ_API_KEY n'est pas définie.")
        print("Veuillez ajouter votre clé API Groq dans le fichier .env:")
        print("GROQ_API_KEY=votre_cle_api_ici")
        exit(1)
    
    print("Démarrage du chatbot avec Llama3 via Groq...")
    print("Start chatting with the bot (type 'quit' to stop)!")
    chatbot()