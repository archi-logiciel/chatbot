# Configuration Llama3 avec Ollama

## Installation d'Ollama

1. **Télécharger Ollama** :
   - Allez sur https://ollama.ai/download
   - Téléchargez la version Windows
   - Installez le programme

2. **Télécharger le modèle Llama3** :
   ```bash
   ollama pull llama3
   ```

3. **Démarrer Ollama** :
   ```bash
   ollama serve
   ```
   
   Ou simplement lancer l'application Ollama depuis le menu Démarrer.

## Utilisation

1. **Assurez-vous qu'Ollama est démarré** (vous devriez voir l'icône dans la barre des tâches)

2. **Lancez le chatbot** :
   ```bash
   python chat.py
   ```

## Modèles disponibles

Vous pouvez changer le modèle en modifiant la variable `MODEL_NAME` dans `chat.py` :

- `llama3` - Llama 3 8B (recommandé)
- `llama3:70b` - Llama 3 70B (plus puissant mais plus lent)
- `codellama` - Code Llama pour la programmation
- `mistral` - Mistral 7B
- `gemma` - Google Gemma

## Dépannage

- **Erreur de connexion** : Vérifiez qu'Ollama est bien démarré
- **Modèle non trouvé** : Téléchargez le modèle avec `ollama pull llama3`
- **Réponses lentes** : Normal, Llama3 s'exécute localement sur votre machine

## Avantages de Llama3 avec Ollama

- ✅ Gratuit et sans limite d'usage
- ✅ Données privées (tout reste sur votre machine)
- ✅ Pas besoin de clé API
- ✅ Fonctionne hors ligne
- ❌ Plus lent que les APIs cloud
- ❌ Nécessite une bonne configuration matérielle
