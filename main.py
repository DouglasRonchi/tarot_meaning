import streamlit as st
from deck import Deck  # Supondo que o código da classe Deck esteja em 'your_code.py'

def main():
    # Título e descrição
    st.title("Significado das Cartas de Tarô")
    st.write("""
        Bem-vindo à leitura de cartas! Escolha o tipo de baralho e o número de cartas para a tiragem.
        Em seguida, selecione as cartas e descubra seus significados.
    """)

    # Escolher o tipo de baralho
    deck_type = st.selectbox("Escolha o tipo de baralho:", ["comum", "cigano", "marselha"])

    # Inicializar o baralho com o tipo selecionado
    deck = Deck(deck_type)

    # Exibir o baralho
    st.write(f"Baralho selecionado: {deck_type.capitalize()}")

    # Seleção do número de cartas
    num_cards = st.slider("Quantas cartas você quer tirar?", 1, 20, 1)

    # Escolher as cartas
    selected_cards = deck.choose_cards(num_cards=num_cards)

    if selected_cards:
        # Exibir os significados das cartas selecionadas
        st.write("Significados das cartas:")
        for card in selected_cards:
            meaning = deck.cards_meaning(card)
            st.write(f"{card}: {meaning}")

if __name__ == "__main__":
    main()
