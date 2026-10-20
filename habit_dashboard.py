import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Habit Tracker", page_icon="🎯", layout="centered")
st.title("🎯 AI Quick Habit Tracker & Daily Motivator")
st.write("Build unbreakable daily habits and stay motivated on your growth journey!")

if "habits" not in st.session_state:
    st.session_state.habits = []

new_habit = st.text_input("Enter a new daily habit (e.g., Code for 1 hour, Drink 3L water):")
if st.button("Add Habit"):
    if new_habit and new_habit not in st.session_state.habits:
        st.session_state.habits.append({"Habit": new_habit, "Status": False})
        st.success(f"Habit '{new_habit}' added successfully!")

if st.session_state.habits:
    st.subheader("Your Daily Checklist")
    for i, habit in enumerate(st.session_state.habits):
        st.session_state.habits[i]["Status"] = st.checkbox(habit["Habit"], value=habit["Status"], key=f"habit_{i}")

    completed = sum(1 for h in st.session_state.habits if h["Status"])
    total = len(st.session_state.habits)
    st.progress(completed / total if total > 0 else 0)
    st.info(f"Completed {completed} out of {total} habits today. Keep pushing forward!")
else:
    st.info("No habits added yet. Start by adding your first daily habit above!")
