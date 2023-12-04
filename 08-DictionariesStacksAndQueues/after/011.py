import stack as st

while True:
    operators = ["*", "-", "/", "+", "="]
    user_input = input("Enter: ")

    if user_input not in operators:
        user_input = int(user_input)
        st.push(user_input)
    else:
        operators.pop()
        if user_input in operators:
            x = st.pop()
            y = st.pop()
            st.push(eval(f"{x}{user_input}{y}"))
        else:
            st.display()
            quit()