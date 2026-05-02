import streamlit as st

st.set_page_config(page_title="Free AI Chatbot", page_icon="🤖")

st.title("🤖 Free AI Chatbot")
st.write("Ask me anything!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

# Simple AI logic
def get_reply(user_input):
    text = user_input.lower()

    if any(w in text for w in ["hi", "hello", "hey"]):
        return "Hello Kumar! 😊 How can I help you?"

    elif "how are you" in text:
        return "I'm doing great 😎 How about you?"

    elif "ai" in text:
        return "AI (Artificial Intelligence) allows machines to think and learn like humans 🤖"

    elif "python" in text:
        return "Python is one of the best programming languages for AI and Data Science 🐍🔥"

    elif "data science" in text:
        return "Data Science involves analyzing data to make predictions and insights 📊"

    elif "money" in text or "earn" in text:
        return "You can earn money through freelancing, building apps, or creating AI tools 💰"

    elif "project" in text:
        return "You can build projects like chatbots, recommendation systems, and more 🚀"

    elif "movie" in text:
        return "Your movie recommender is a great project — keep improving it 🔥"

    elif "bye" in text:
        return "Goodbye Kumar! 👋 Keep learning and building!"

    else:
        return "That's interesting 🤔 Can you tell me more?"

# When user sends message
if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    reply = get_reply(user_input)

    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})