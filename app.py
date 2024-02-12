import streamlit as st
import random
random.seed(42)
from functions import *


# function to calculate and display score
def display_score():
    if st.session_state.submitted:
        score = sum(st.session_state[f"Question{i}"] == data.iloc[st.session_state.question_indices[i]]['Réponse']
                    for i in range(total_questions))
        
        # display score
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"Votre score: **{score} sur {total_questions}**")
        with col2:
            width = 100
            if score < 4:
                st.image('img/bad.png', caption='NOT GOOD', width=width)
            elif score < 7:
                st.image('img/mid.png', caption='NOT BAD', width=width)
            elif score < 10:
                st.image('img/good.png', caption='GOOD', width=width)
            else:
                st.balloons()
                st.image('img/excellent.png', caption='EXCELLENT', width=width)

# callback function for restarting the quiz
def restart_quiz():
    st.session_state.question_indices = random.sample(range(len(data)), total_questions)
    st.session_state.submitted = False

# initial setup
st.title("Quiz d'entraînement examen IREF")
st.sidebar.markdown("## Comment ça marche ?")
st.sidebar.markdown("10 questions sont sélectionnées aléatoirement parmi un pool de ~120 questions.")
st.sidebar.markdown("Une seule bonne réponse est possible par question.")
space_side(2)

st.sidebar.markdown("## Comment utiliser ce quiz ?")
st.sidebar.markdown("1. Lisez les questions et choisissez la bonne réponse")
st.sidebar.markdown("2. Cliquez sur le bouton **Soumettre toutes les réponses** 2 fois pour afficher votre score final")
st.sidebar.markdown("4. Cliquez sur le bouton **Recommencer** pour recommencer le quiz")
space_side(2)

st.sidebar.markdown("## À propos")
st.sidebar.markdown("Si vous voyez des **erreurs** dans les réponses ou si vous avez des **suggestions** de questions à ajouter, [changez les questions](https://github.com/JosephBARBIERDARNAL/Examen-IREF/blob/main/qa.csv).")
space(2)

data = load_data("qa.csv")
total_questions = 10

# initialize session state
if 'question_indices' not in st.session_state:
    st.session_state.question_indices = random.sample(range(len(data)), total_questions)
    st.session_state.submitted = False

# display all questions
for i in range(total_questions):
    question_data = data.iloc[st.session_state.question_indices[i]]
    question, correct_answer = question_data['Question'], question_data['Réponse']
    options = [question_data['Option A'], question_data['Option B'], question_data['Option C']]

    st.markdown(f"### Question {i + 1} sur {total_questions}")
    st.markdown(f"**{question}**")
    chosen_answer = st.radio(f"Choisissez la bonne réponse pour la question {i + 1}", 
                             options, 
                             key=f"Question{i}")

    # display success or error message if answers are submitted
    if st.session_state.submitted:
        if chosen_answer == correct_answer:
            st.success(f"Correct! La bonne réponse est: **{correct_answer}**")
        else:
            st.error(f"Incorrect. La bonne réponse est: **{correct_answer}**")
space(1)
display_score()

col1, col2 = st.columns(2)
with col1:
    if st.button("Soumettre toutes les réponses"):
        st.session_state.submitted = True
with col2:
    if st.button("Recommencer", on_click=restart_quiz):
        pass



space(5)