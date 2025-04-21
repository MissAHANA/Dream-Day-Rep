import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to generate the itinerary using the latest OpenAI API
def generate_itinerary(mood, aesthetic, goal):
    prompt = f"""
    Generate a personalized itinerary for someone who feels {mood}, loves {aesthetic}, and wants to {goal}. 
    Divide the day into four parts:
    1. Morning: Start with a calming activity or a way to ease into the day.
    2. Afternoon: Suggest an activity that matches their energy level — it could be work, creative time, or a relaxing activity.
    3. Evening: Give a peaceful, wind-down activity that matches the mood and aesthetic.
    4. Night: Suggest something for closure — either restful sleep or an inspiring thought (like stargazing or meditation).
    For each section, add a short reflection or companion message.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the latest model (e.g., GPT-3.5 or GPT-4 if available)
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.7
    )
    
    itinerary = response['choices'][0]['message']['content'].strip()
    return itinerary

# Streamlit UI for user input
st.title("🌙 Dream Day Generator")

# Get inputs from user (from earlier in Step 1)
mood = st.text_input("💭 How are you feeling right now?")
aesthetic = st.selectbox("Choose your aesthetic:", 
                         ["Cottagecore", "Cozy Academia", "Minimal / Zen", 
                          "Dreamy / Ethereal", "Retro 90s", "Soft Cyberpunk"])
goal = st.selectbox("What do you want to feel today?", 
                    ["Feel peace", "Spark creativity", "Romanticize life", 
                     "Reconnect with self", "Be inspired", "Rest and heal"])

# Button to generate the itinerary
if st.button("💫 Generate My Dream Day Itinerary"):
    if mood and aesthetic and goal:
        itinerary = generate_itinerary(mood, aesthetic, goal)
        st.markdown("## 📝 Your Dream Day Itinerary")
        st.write(itinerary)
    else:
        st.warning("Please fill in all fields before generating!")
