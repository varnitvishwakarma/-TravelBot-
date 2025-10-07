🌍 TravelBot - Personalized AI Travel Planner
TravelBot is an intelligent AI-powered chatbot designed to help users plan personalized travel experiences. Using Gemini 2.5 Pro, LangChain, and Streamlit, TravelBot understands user intent, tracks preferences, and recommends the best travel destinations with detailed insights.
🚀 Features
Intelligent User Intent Understanding

Classifies trips: solo, family, or with friends

Identifies trip types: adventure, beach, honeymoon, nature, spiritual, etc.

Extracts key details: destination, budget, trip duration, preferred month/season, and interests

Stateful Conversation Management

Persists user preferences across multiple interactions

Retrieves context for returning users

Ensures recommendations are always context-aware and personalized

Destination Recommendations

Suggests 4–5 destinations tailored to user preferences

Ranks destinations based on popularity, safety, and seasonal suitability

Filters out destinations that are closed or inaccessible during the user’s travel time

Engaging Travel Content

Provides short, concise, and visually appealing descriptions

Includes travel tips, pros & cons, attractions, and safety guidance

Uses bullet points and emojis for readability and engagement

💡 Key Advantages

Personalized travel recommendations based on budget, duration, and interests

Ensures destination availability and seasonal appropriateness

Friendly, easy-to-use chat interface with memory for continuous interaction

Ideal for planning trips with friends, family, or solo adventures

🛠 Tech Stack

AI Model: Gemini 2.5 Pro (Google Generative AI)

Framework: LangChain for conversation memory and prompt management

Frontend: Streamlit for chat interface

Environment Variables: python-dotenv for API keys

⚡ Installation & Setup
1. Clone the repository
git clone <your-repo-url>
cd TravelBot

2. Create a virtual environment
python -m venv travelenv

3. Activate the environment

Windows (PowerShell):

Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\travelenv\Scripts\Activate.ps1


Linux/Mac:

source travelenv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Create a .env file in the project root
GOOGLE_API_KEY=your_google_api_key_here

6. Run the TravelBot app
streamlit run app.py

📌 Usage

Enter your travel preferences in the chat (budget, trip type, month, duration, destination interests).

TravelBot will classify your trip, store your preferences, and recommend destinations with helpful tips.

Keep chatting to refine your recommendations!

🌟 Example Queries

“I want a 4-day beach trip with friends in December, budget $500–$700.”

“Plan a solo adventure trip in Himachal Pradesh for January.”

“Suggest romantic honeymoon destinations in March.”

🛡 Privacy & Data Handling

TravelBot stores session memory only temporarily for context-aware recommendations.

No personal data is stored permanently or shared externally.

💬 Future Enhancements

Integrate live destination status from official sources (temple closures, park availability)

Add image previews and clickable links for destinations

Multi-language support for international users

📄 License

MIT License — freely use, modify, and distribute.