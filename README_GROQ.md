# Configuration Llama3 avec GroqCloud

## Qu'est-ce que GroqCloud ?

GroqCloud est une plateforme cloud qui offre un accès ultra-rapide aux modèles de langage comme Llama3. Elle utilise des puces spécialisées (LPU - Language Processing Units) pour des inférences très rapides.

## Configuration

1. **Créer un compte GroqCloud** :
   - Allez sur https://console.groq.com/
   - Créez un compte gratuit
   - Obtenez votre clé API

2. **Configurer la clé API** :
   - Ouvrez le fichier `.env` dans le dossier chatbot
   - Remplacez `your_groq_api_key_here` par votre vraie clé API :
   ```
   GROQ_API_KEY=gsk_votre_cle_api_ici
   ```

3. **Lancer le chatbot** :
   ```bash
   python chat.py
   ```

## Modèles disponibles sur Groq

Vous pouvez changer le modèle en modifiant la variable `MODEL_NAME` dans `chat.py` :

- `llama3-8b-8192` - Llama 3 8B (rapide, recommandé)
- `llama3-70b-8192` - Llama 3 70B (plus puissant)
- `mixtral-8x7b-32768` - Mixtral 8x7B
- `gemma-7b-it` - Google Gemma 7B

## Avantages de GroqCloud

- ✅ **Ultra-rapide** : 500+ tokens/seconde
- ✅ **Gratuit** : Tier gratuit généreux
- ✅ **Compatible OpenAI** : API similaire à OpenAI
- ✅ **Pas d'installation** : Fonctionne directement
- ✅ **Modèles récents** : Llama3, Mixtral, Gemma

## Limites du tier gratuit

- 6 000 tokens par minute
- 30 requêtes par minute
- Largement suffisant pour un usage personnel

## Dépannage

- **Erreur 401** : Vérifiez votre clé API dans le fichier `.env`
- **Erreur 429** : Limite de taux atteinte, attendez un moment
- **Pas de réponse** : Vérifiez votre connexion internet

## Comparaison avec d'autres solutions

| Solution | Vitesse | Coût | Installation | Confidentialité |
|----------|---------|------|--------------|-----------------|
| GroqCloud | ⭐⭐⭐⭐⭐ | Gratuit/Payant | Aucune | API Cloud |
| OpenAI | ⭐⭐⭐⭐ | Payant | Aucune | API Cloud |
| Ollama | ⭐⭐ | Gratuit | Complexe | Local |

GroqCloud est idéal pour le développement rapide avec Llama3 !
