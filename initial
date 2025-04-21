import streamlit as st

st.set_page_config(page_title="Dream Day Generator", page_icon="✨")

st.title("🌙 Dream Day Generator")
st.subheader("Let's create your perfect day...")

# 1. Mood Input
mood = st.text_input("💭 How are you feeling right now?", 
                     placeholder="Type words or emojis (e.g., peaceful, 🥺, overwhelmed but hopeful)")

# 2. Aesthetic Selection
st.markdown("### 🎨 Choose your aesthetic vibe")

aesthetic_mode = st.radio("How would you like to set your aesthetic?",
                          ["Pick from a list", "Surprise me", "Describe my vibe"])

if aesthetic_mode == "Pick from a list":
    aesthetic = st.selectbox("Choose an aesthetic:", [
        "Cottagecore", "Cozy Academia", "Minimal / Zen", 
        "Dreamy / Ethereal", "Retro 90s", "Soft Cyberpunk"
    ])
elif aesthetic_mode == "Describe my vibe":
    vibe_description = st.text_input("Describe your vibe (e.g., 'Rainy bookshop with candlelight')")
    aesthetic = f"Custom: {vibe_description}" if vibe_description else "Custom"
else:
    aesthetic = "Surprise Me"

# 3. Goal of the Day
st.markdown("### ✨ What do you want your day to help you feel?")

goal_mode = st.radio("Choose how you'd like to set your day's focus:",
                     ["Pick from a list", "Surprise me", "Describe it"])

if goal_mode == "Pick from a list":
    goal = st.selectbox("Choose a goal:", [
        "Feel peace", "Spark creativity", "Romanticize life", 
        "Reconnect with self", "Be inspired", "Rest and heal"
    ])
elif goal_mode == "Describe it":
    custom_goal = st.text_input("Describe your intention for today (e.g., 'feel like the main character')")
    goal = f"Custom: {custom_goal}" if custom_goal else "Custom"
else:
    goal = "Surprise Me"

# Display Summary
if st.button("💫 Generate My Dream Day"):
    st.markdown("## 🌟 Your Selections")
    st.write(f"**Mood:** {mood if mood else 'Not specified'}")
    st.write(f"**Aesthetic:** {aesthetic}")
    st.write(f"**Goal of the Day:** {goal}")
    st.success("All set! Ready to dream ✨ (Next step: Itinerary Generation)")

