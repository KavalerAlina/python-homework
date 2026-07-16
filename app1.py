import streamlit as st

# Вправа 12. Поле для пароля

password = st.text_input("Введіть пароль")
st.write("Довжина пароля: ", len(password))


# Вправа 13. Функція `has_digit`

def has_digit(text):
    for number in text:
        if number.isdigit():
             return True

    return False

result = has_digit(password)
st.write("Є цифра: ", result)


# Вправа 14. Проста web-перевірка пароля

def check_password(password):
    password_len = len(password)
    if password_len >= 8:
        for number in password:
            if number.isdigit():
                return True

    return False

clicked = st.button("Перевірити пароль")

is_valid = check_password(password)
if clicked:
    if is_valid:
        st.write("Пароль підходить")
    else:
        st.write("Пароль не підходить")


# Вправа 15. Детальна web-перевірка пароля

def get_password_problem(password):
    password_len = len(password)
    if password_len < 8:
        return "Пароль закороткий"

    for number in password:
        if not number.isdigit():
            return "Додайте цифру"

    return "Пароль підходить"

result = get_password_problem(password)
st.write(result)


# Вправа 16. Поле для повідомлення

message = st.text_input("Введіть повідомлення")

if message:
    st.write("Повідомлення: ", message)

    message_len = len(message)
    st.write("Кількість символів: ", message_len)

    message_lower = message.lower()
    st.write("Повідомлення у нижньому регістрі: ", message_lower)


    

