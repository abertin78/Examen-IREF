import streamlit as st
import random
from functions import *

# initialisation
st.title("Quiz d'entraînement examen IREF")
st.sidebar.markdown("## Comment ça marche ?")
st.sidebar.markdown("10 questions sont sélectionnées aléatoirement parmi un pool de ~50 questions.")
st.sidebar.markdown("Une seule bonne réponse est possible par question.")
space_side(2)

st.sidebar.markdown("## Comment utiliser ce quiz ?")
st.sidebar.markdown("1. Lisez les questions et choisissez la bonne réponse")
st.sidebar.markdown("2. Cliquez sur le bouton **Soumettre toutes les réponses** pour afficher votre score final")
st.sidebar.markdown("3. Re-clicker sur le bouton **Soumettre toutes les réponses** pour afficher les bonnes réponses sous chaque question")
st.sidebar.markdown("4. Cliquez sur le bouton **Recommencer** (2 fois) pour recommencer le quiz")
space_side(2)

st.sidebar.markdown("## À propos")
st.sidebar.markdown("Si vous voyez des **erreurs** dans les réponses ou si vous avez des **suggestions** de questions à ajouter, envoyez moi les cours ou des questions en format **csv** avec 4 colonnes:")
st.sidebar.markdown("- *Question*: la question")
st.sidebar.markdown("- *Réponse*: la réponse correcte")
st.sidebar.markdown("- *Option A*: une réponse possible")
st.sidebar.markdown("- *Option B*: une réponse possible")
st.sidebar.markdown("- *Option C*: une réponse possible")
space(2)

data = load_data("qa.csv")
total_questions = 10

# initialisation session
if 'question_indices' not in st.session_state:
    st.session_state.question_indices = random.sample(range(len(data)), total_questions)
    st.session_state.answers = [None] * total_questions
    st.session_state.submitted = False

# Affichage de toutes les questions
for i in range(total_questions):
    question_data = data.iloc[st.session_state.question_indices[i]]
    question, correct_answer = question_data['Question'], question_data['Réponse']
    options = [question_data['Option A'], question_data['Option B'], question_data['Option C']]

    st.markdown(f"### Question {i + 1} sur {total_questions}")
    st.markdown(f"**{question}**")
    chosen_answer = st.radio(f"Choisissez la bonne réponse pour la question {i + 1}", 
                             options, 
                             key=f"Question{i}")

    # Afficher le message de succès ou d'erreur si les réponses ont été soumises
    if st.session_state.submitted:
        if chosen_answer == correct_answer:
            st.success(f"Correct! La bonne réponse est: **{correct_answer}**")
        else:
            st.error(f"Incorrect. La bonne réponse est: {correct_answer}")

# Bouton de soumission des réponses
if st.button("Soumettre toutes les réponses"):
    st.session_state.submitted = True
    score = 0
    for i in range(total_questions):
        question_data = data.iloc[st.session_state.question_indices[i]]
        correct_answer = question_data['Réponse']
        if st.session_state[f"Question{i}"] == correct_answer:
            score += 1
    st.write("Quiz terminé!")
    st.markdown(f"Votre score: **{score} sur {total_questions}**")

# restart
if st.button("Recommencer"):
    st.session_state.question_indices = random.sample(range(len(data)), total_questions)
    st.session_state.answers = [None] * total_questions
    st.session_state.submitted = False

space(5)

