import streamlit as st
from streamlit import text_input

import functions
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("WELCOME!")
st.subheader("Hi! I am Siddharth, and this is my To-Do app.")
st.write("Your Checklist:")

for index, todo in  enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo,key="new_todo")
