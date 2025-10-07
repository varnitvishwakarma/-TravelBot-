# # # import streamlit as st
# # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # from langchain.chains import ConversationChain
# # # from langchain.memory import ConversationBufferMemory
# # # from langchain.prompts import PromptTemplate
# # # from dotenv import load_dotenv

# # # # load_dotenv()


# # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # # Use gemini-1.5-flash (free tier)
# # # model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# # # print(model.invoke("suggest me a trip location with friends"))




# # # # # Streamlit page setup
# # # # st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
# # # # st.title("🤖 Gemini Chatbot with Memory")

# # # # # Create the model
# # # # llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)

# # # # # Memory to remember chat history
# # # # memory = ConversationBufferMemory(return_messages=True)

# # # # # Define a custom prompt (you can tune this later)
# # # # prompt_template = PromptTemplate(
# # # #     input_variables=["history", "input"],
# # # #     template=(
# # # #         "You are a helpful and smart AI assistant.\n"
# # # #         "Chat history:\n{history}\n"
# # # #         "User: {input}\n"
# # # #         "AI:"
# # # #     )
# # # # )

# # # # # Create conversation chain
# # # # conversation = ConversationChain(
# # # #     llm=llm,
# # # #     memory=memory,
# # # #     prompt=prompt_template,
# # # #     verbose=True
# # # # )

# # # # # Streamlit chat UI
# # # # if "messages" not in st.session_state:
# # # #     st.session_state.messages = []

# # # # # Show chat history
# # # # for msg in st.session_state.messages:
# # # #     with st.chat_message(msg["role"]):
# # # #         st.markdown(msg["content"])

# # # # # User input
# # # # user_input = st.chat_input("Type your message...")

# # # # if user_input:
# # # #     # Add user message
# # # #     st.session_state.messages.append({"role": "user", "content": user_input})
# # # #     with st.chat_message("user"):
# # # #         st.markdown(user_input)

# # # #     # Generate AI response
# # # #     response = conversation.predict(input=user_input)

# # # #     # Display and store AI message
# # # #     with st.chat_message("assistant"):
# # # #         st.markdown(response)
# # # #     st.session_state.messages.append({"role": "assistant", "content": response})



# # import streamlit as st
# # import google.generativeai as genai
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # # Configure your Gemini API key
# # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # # Initialize model (use "gemini-1.5-flash" or "gemini-1.5-pro")
# # model = genai.GenerativeModel("gemini-1.5-flash")

# # # Streamlit UI
# # st.set_page_config(page_title="Travel Chatbot 🌍")
# # st.title("🌴 Travel Chatbot (Gemini)")

# # # Chat history
# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []

# # for role, text in st.session_state.chat_history:
# #     with st.chat_message(role):
# #         st.markdown(text)

# # user_input = st.chat_input("Ask me about your next trip with friends...")

# # if user_input:
# #     st.session_state.chat_history.append(("user", user_input))
# #     with st.chat_message("user"):
# #         st.markdown(user_input)



# import streamlit as st
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
# from langchain.prompts import PromptTemplate

# # Load environment variables
# load_dotenv()

# # Streamlit setup
# st.set_page_config(page_title="🌴 TravelBot", page_icon="🌍")
# st.title("🌍 TravelBot — Plan Your Next Adventure!")

# # Initialize Gemini 2.5 Pro model
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)

# # Memory to remember chat context
# memory = ConversationBufferMemory(return_messages=True)

# # Custom prompt to make it act like a travel planner
# prompt_template = PromptTemplate(
#     input_variables=["history", "input"],
#     template=(
#         "You are TravelBot, an expert travel planner that gives personalized and fun travel ideas.\n"
#         "You help users plan trips with friends, find destinations, activities, and travel tips.\n\n"
#         "Chat History:\n{history}\n"
#         "User: {input}\n"
#         "TravelBot:"
#     )
# )

# # Create conversation chain with memory
# conversation = ConversationChain(
#     llm=llm,
#     memory=memory,
#     prompt=prompt_template,
#     verbose=False
# )

# # Session state for chat UI
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # User input box
# user_input = st.chat_input("Ask TravelBot where to go with your friends...")

# if user_input:
#     # Show user message
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Generate TravelBot's response
#     response = conversation.predict(input=user_input)

#     # Show TravelBot message
#     with st.chat_message("assistant"):
#         st.markdown(response)

#     # Store message in history
#     st.session_state.messages.append({"role": "assistant", "content": response})



import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Load API key
load_dotenv()

# Streamlit setup
st.set_page_config(page_title="🌍 TravelBot", page_icon="✈️")
st.title("✈️ TravelBot — Personalized Trip Planner")

# Initialize Gemini 2.5 Pro model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)

# Memory to persist user preferences and chat history
memory = ConversationBufferMemory(return_messages=True)

# Combined prompt template with availability check
prompt_template = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are an expert travel AI assistant. Follow these instructions carefully:

1️⃣ User Intent Understanding:
- Classify the trip (solo, family, friends)
- Identify trip type (adventure, beach, honeymoon, nature, spiritual, etc.)
- Determine geographic scope (domestic or international)
- Extract key details: destination, budget, trip duration, travel month/season, interests/purpose

2️⃣ State Tracking:
- Capture and store user preferences
- Retrieve stored preferences for returning users
- Only suggest destinations after user context is clear
- Ensure privacy and secure handling of user data

3️⃣ Destination Availability Check:
- Before recommending, check if the destination is open and accessible in the user's planned travel month/season.
- Do NOT suggest destinations that are closed, restricted, or unsafe during that time (e.g., Kedarnath in winter).

4️⃣ Destination Recommendation:
- Suggest 4-5 destinations based on user preferences and availability
- Rank by popularity, safety, and seasonal suitability
- Provide travel insights: weather, best season, key attractions, travel tips

5️⃣ Travel Content:
- Generate concise, engaging, user-friendly descriptions
- Include practical tips, pros and cons, use bullets/emojis for readability
- End each recommendation with a friendly message

Chat History:
{history}

User Query:
{input}

TravelBot:
"""
)

# Conversation chain with memory
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt_template,
    verbose=False
)

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask TravelBot for your next trip…")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    response = conversation.predict(input=user_input)

    # Display and store AI message
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
