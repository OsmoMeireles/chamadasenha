import streamlit as st

st.image('Meli.jpg')
st.title("Chamada de Senhas")

# Campo para digitar a senha
with st.form("form_senha"):
    nova_senha = st.text_input("Digite a senha a ser chamada:", max_chars=10)
    enviar = st.form_submit_button("Chamar Senha")

    if enviar:
        nova_senha = nova_senha.strip().upper()
        if nova_senha:
            # Salva a senha no arquivo
            with open("senhas.txt", "a") as f:
                f.write(nova_senha + "\n")
            st.success(f"Senha {nova_senha} chamada com sucesso!")
        else:
            st.warning("⚠️ Digite uma senha válida.")



