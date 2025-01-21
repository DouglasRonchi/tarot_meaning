import streamlit as st

class Deck:
    def __init__(self, deck_type="comum"):
        """Inicializa o baralho com o tipo desejado (comum, cigano, marselha)."""
        self.deck_type = deck_type
        self.cards = self.create_deck()

    def create_deck(self):
        """Cria o baralho de acordo com o tipo escolhido."""
        if self.deck_type == "comum":
            return self.create_common_deck()
        elif self.deck_type == "cigano":
            return self.create_cigano_deck()
        elif self.deck_type == "marselha":
            return self.create_marselha_deck()
        else:
            raise ValueError("Tipo de baralho desconhecido.")

    def create_common_deck(self):
        """Cria o baralho com base no tipo escolhido."""
        if self.deck_type == "comum":
            suits = ['Copas', 'Ouro', 'Paus', 'Espadas']
            ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
            suit_emojis = {
                "Copas": "♥️",  # Emoji de Copas
                "Ouro": "♦️",    # Emoji de Ouro
                "Paus": "♣️",    # Emoji de Paus
                "Espadas": "♠️"  # Emoji de Espadas
            }
            return [f"{rank} de {suit_emojis[suit]}" for suit in suits for rank in ranks]

    def create_marselha_deck(self):
            arcana_maior = [
                "O Louco", "O Mago", "A Sacerdotisa", "A Imperatriz", "O Imperador", 
                "O Hierofante", "Os Enamorados", "O Carro", "A Justiça", "O Eremita", 
                "A Roda da Fortuna", "A Força", "O Enforcado", "A Morte", "A Temperança", 
                "O Diabo", "A Torre", "A Estrela", "A Lua", "O Sol", 
                "O Julgamento", "O Mundo"
            ]
            suit_emojis = {
                "Copas": "♥️",  # Emoji de Copas
                "Ouro": "♦️",    # Emoji de Ouro
                "Paus": "♣️",    # Emoji de Paus
                "Espadas": "♠️"  # Emoji de Espadas
            }
            ranks = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei']
            arcana_menor = [f"{rank} de {suit_emojis[suit]}" for suit in ['Copas', 'Ouro', 'Paus', 'Espadas'] 
                            for rank in ranks]
            return arcana_maior + arcana_menor
    
    def create_cigano_deck(self):
            cards = [
                "Cavaleiro", "Trevo", "Navio", "Casa", "Árvore", "Nuvens",
                "Cobra", "Caixão", "Buquê", "Foice", "Chicote", "Pássaros",
                "Criança", "Raposa", "Urso", "Estrela", "Cegonha", "Cão",
                "Torre", "Jardim", "Montanha", "Caminhos", "Ratos", "Coração",
                "Anel", "Livro", "Carta", "Homem", "Mulher", "Flor", "Sol",
                "Lua", "Chave", "Peixes", "Âncora", "Cruz"
            ]
            return cards


    def choose_cards(self, num_cards=1):
        """Permite ao usuário escolher cartas do baralho usando um multiselect do Streamlit."""
        selected_cards = st.multiselect(
            'Escolha as cartas', 
            options=self.cards, 
            default=[],  # Inicialmente sem nenhuma carta escolhida
            max_selections=num_cards  # Limita a seleção de cartas ao número desejado
        )

        # Verifica se o número de cartas selecionadas corresponde ao solicitado
        if len(selected_cards) != num_cards:
            st.error(f"Você deve selecionar exatamente {num_cards} cartas.")
            return []
        return selected_cards

    def cards_meaning(self, card):
        """Return the meaning of a card."""
        meaning = {}

        suits_emojis = {
            'Copas': '♥️',
            'Espadas': '♠️',
            'Ouro': '♦️',
            'Paus': '♣️'
        }

        if self.deck_type == "comum":
            meaning = {
                "A de ♦️": "Casa",
                "2 de ♦️": "Viagem de Dia",
                "3 de ♦️": "Recado Muito Bom",
                "4 de ♦️": "Palavras de Amor Íntimo",
                "5 de ♦️": "Dinheiro",
                "6 de ♦️": "Dinheiro",
                "7 de ♦️": "Certeza Muito Boa",
                "8 de ♦️": "Mudança Boa",
                "9 de ♦️": "Filho",
                "J de ♦️": "(Pensamentos) Alemão",
                "Q de ♦️": "Loira",
                "K de ♦️": "Loiro",
                "A de ♥️": "Casa",
                "2 de ♥️": "Viagem de Dia",
                "3 de ♥️": "Recado Muito Bom",
                "4 de ♥️": "Palavras de Amor Fraterno",
                "5 de ♥️": "Felicidade",
                "6 de ♥️": "Falsidade / Engano",
                "7 de ♥️": "Certeza",
                "8 de ♥️": "Mudança",
                "9 de ♥️": "Filho",
                "J de ♥️": "(Pensamentos) Branco / Italiano",
                "Q de ♥️": "Branca",
                "K de ♥️": "Branco",
                "A de ♣️": "Fofoca",
                "2 de ♣️": "Viagem de Noite",
                "3 de ♣️": "Recado Ruim",
                "4 de ♣️": "Doença Passageira",
                "5 de ♣️": "Perca",
                "6 de ♣️": "Susto",
                "7 de ♣️": "Certeza",
                "8 de ♣️": "Choro",
                "9 de ♣️": "Fofoca",
                "J de ♣️": "(Pensamentos) Moreno Claro",
                "Q de ♣️": "Morena",
                "K de ♣️": "Moreno",
                "A de ♠️": "Raiva",
                "2 de ♠️": "Viagem de Noite",
                "3 de ♠️": "Recado Ruim",
                "4 de ♠️": "Doença Grave",
                "5 de ♠️": "Feitiço",
                "6 de ♠️": "Caixão",
                "7 de ♠️": "Certeza Ruim",
                "8 de ♠️": "Bebedeira / Festa",
                "9 de ♠️": "Justiça",
                "J de ♠️": "(Pensamentos) Preto",
                "Q de ♠️": "Preta",
                "K de ♠️": "Preto",
            }

        elif self.deck_type == "marselha":
            meaning = {
                # Arcanos Maiores
                "O Louco": "Liberdade, novos começos, imprevisibilidade.",
                "O Mago": "Habilidade, iniciativa, ação, potencial.",
                "A Sacerdotisa": "Sabedoria, intuição, mistério, espiritualidade.",
                "A Imperatriz": "Abundância, criatividade, maternidade, beleza.",
                "O Imperador": "Autoridade, estrutura, estabilidade, liderança.",
                "O Hierofante": "Tradição, ensinamentos, espiritualidade, ética.",
                "Os Enamorados": "Escolhas, relacionamentos, harmonia, amor.",
                "O Carro": "Determinação, vitória, controle, progresso.",
                "A Justiça": "Verdade, justiça, equilíbrio, responsabilidade.",
                "O Eremita": "Introspecção, busca interior, sabedoria, solidão.",
                "A Roda da Fortuna": "Mudança, ciclos, sorte, destino.",
                "A Força": "Coragem, paciência, autocontrole, compaixão.",
                "O Enforcado": "Sacrifício, perspectiva, ♣️a, rendição.",
                "A Morte": "Transformação, finais, novos começos, renascimento.",
                "A Temperança": "Equilíbrio, moderação, harmonia, paciência.",
                "O Diabo": "Apego, materialismo, tentação, repressão.",
                "A Torre": "Mudança súbita, crise, libertação, revelação.",
                "A Estrela": "Esperança, inspiração, renovação, serenidade.",
                "A Lua": "Ilusões, intuição, incerteza, mistério.",
                "O Sol": "Sucesso, alegria, clareza, vitalidade.",
                "O Julgamento": "Renascimento, absolvição, decisão, despertar.",
                "O Mundo": "Conclusão, realização, integridade, plenitude.",
                
                # Naipes - ♥️, ♠️, ♣️ e ♦️
                # Naipe de ♥️
                "Ás de ♥️": "Novo amor, emoção, fertilidade.",
                "2 de ♥️": "Parceria, conexão, equilíbrio emocional.",
                "3 de ♥️": "Celebração, amizade, abundância.",
                "4 de ♥️": "Estagnação emocional, introspecção.",
                "5 de ♥️": "Decepção, perda emocional, arrependimento.",
                "6 de ♥️": "Nostalgia, memórias, bondade.",
                "7 de ♥️": "Ilusões, escolhas, fantasias.",
                "8 de ♥️": "Deixar ir, busca de propósito.",
                "9 de ♥️": "Satisfação emocional, realização de desejos.",
                "10 de ♥️": "Felicidade, harmonia familiar, plenitude.",
                "Valete de ♥️": "Mensagem emocional, novidade criativa.",
                "Rainha de ♥️": "Empatia, intuição, compaixão.",
                "Rei de ♥️": "Controle emocional, sabedoria emocional.",
                
                # Naipe de ♠️
                "Ás de ♠️": "Verdades reveladas, clareza, decisão.",
                "2 de ♠️": "Conflito, indecisão, equilíbrio entre opostos.",
                "3 de ♠️": "Coração partido, dor emocional, traição.",
                "4 de ♠️": "Descanso, recuperação, introspecção.",
                "5 de ♠️": "Perda, conflito, vitória a qualquer custo.",
                "6 de ♠️": "Viagem, transição, alívio, mudança.",
                "7 de ♠️": "Engano, furtividade, dissimulação.",
                "8 de ♠️": "Limitações, aprisionamento, falta de liberdade.",
                "9 de ♠️": "Ansiedade, pesadelos, medo, preocupação.",
                "10 de ♠️": "Fim de um ciclo doloroso, traição, colapso.",
                "Valete de ♠️": "Curiosidade, mensagens, vigilância.",
                "Rainha de ♠️": "Lógica, independência, sabedoria.",
                "Rei de ♠️": "Autoridade intelectual, clareza mental, julgamento imparcial.",
                
                # Naipe de ♣️
                "Ás de ♣️": "Novos começos, inspiração, criatividade.",
                "2 de ♣️": "Planejamento, tomada de decisão, visão futura.",
                "3 de ♣️": "Expansão, visão de longo prazo, trabalho em equipe.",
                "4 de ♣️": "Estabilidade, celebração, harmonia.",
                "5 de ♣️": "Conflito, competição, desafios.",
                "6 de ♣️": "Vitória, reconhecimento, sucesso público.",
                "7 de ♣️": "Defesa, resistência, desafios a superar.",
                "8 de ♣️": "Velocidade, movimento rápido, progresso.",
                "9 de ♣️": "Perseverança, resistência, cuidado com os obstáculos.",
                "10 de ♣️": "Sobrecarregado, responsabilidade excessiva, fardo.",
                "Valete de ♣️": "Mensagem, novos começos, entusiasmo.",
                "Rainha de ♣️": "Confiança, carisma, criatividade.",
                "Rei de ♣️": "Liderança, inspiração, ação decisiva.",
                
                # Naipe de ♦️
                "Ás de ♦️": "Novas oportunidades financeiras, abundância, prosperidade.",
                "2 de ♦️": "Equilíbrio financeiro, adaptabilidade, mudanças.",
                "3 de ♦️": "Trabalho em equipe, aprendizado, reconhecimento.",
                "4 de ♦️": "Conservadorismo, segurança financeira, avareza.",
                "5 de ♦️": "Perda, dificuldades financeiras, exclusão.",
                "6 de ♦️": "Generosidade, ajuda mútua, caridade.",
                "7 de ♦️": "Paciência, avaliação, retorno sobre investimento.",
                "8 de ♦️": "Trabalho árduo, dedicação, aperfeiçoamento.",
                "9 de ♦️": "Conquista material, segurança financeira.",
                "10 de ♦️": "Herança, riqueza duradoura, estabilidade familiar.",
                "Valete de ♦️": "Mensagem de prosperidade, novos negócios.",
                "Rainha de ♦️": "Segurança material, nutrição, riqueza.",
                "Rei de ♦️": "Sucesso financeiro, autoridade, estabilidade.",
            }

        elif self.deck_type == "cigano":
            meaning = {
                "Cavaleiro": "Movimento, progresso, mudanças positivas.",
                "Trevo": "Sorte, pequenas oportunidades, simplicidade.",
                "Navio": "Viagem, jornada, transformação.",
                "Casa": "Estabilidade, segurança, conforto.",
                "Árvore": "Saúde, crescimento, conexão espiritual.",
                "Nuvens": "Dúvida, confusão, incerteza temporária.",
                "Cobra": "Traição, sedução, alerta.",
                "Caixão": "Finais, encerramentos, renascimento.",
                "Buquê": "Felicidade, presentes, gratidão.",
                "Foice": "Corte, separação, decisões rápidas.",
                "Chicote": "Conflito, discussão, repetição.",
                "Pássaros": "Comunicação, ansiedade, fofoca.",
                "Criança": "Início, ingenuidade, pureza.",
                "Raposa": "Astúcia, engano, inteligência.",
                "Urso": "Proteção, força, autoridade.",
                "Estrela": "Esperança, inspiração, sorte.",
                "Cegonha": "Mudanças, renovação, novos começos.",
                "Cão": "Amizade, lealdade, confiança.",
                "Torre": "Isolamento, autoridade, visão ampla.",
                "Jardim": "Socialização, comunidade, eventos públicos.",
                "Montanha": "Obstáculos, desafios, superação.",
                "Caminhos": "Escolhas, decisões, possibilidades.",
                "Ratos": "Perdas, preocupações, desgaste.",
                "Coração": "Amor, emoções, paixão.",
                "Anel": "Compromisso, acordo, união.",
                "Livro": "Conhecimento, segredo, mistério.",
                "Carta": "Mensagem, comunicação, novidade.",
                "Homem": "Homem significativo, força masculina.",
                "Mulher": "Mulher significativa, força feminina.",
                "Flor": "Gratidão, beleza, admiração.",
                "Sol": "Sucesso, clareza, vitalidade.",
                "Lua": "Intuição, reconhecimento, sonhos.",
                "Chave": "Solução, resposta, revelação.",
                "Peixes": "Abundância, finanças, fluxo.",
                "Âncora": "Estabilidade, perseverança, segurança.",
                "Cruz": "Desafios, destino, aprendizado espiritual.",
            }
        for suit, emoji in suits_emojis.items():
            for key in meaning.keys():
                if suit in key:
                    meaning[key] = meaning[key].replace(suit, emoji)
        
        return meaning.get(card, "Significado não encontrado.")


    def play_manually_input(self):
        num_cards = int(input("Digite o número de cartas para a tiragem personalizada: ").strip())
        return {f"Carta {i + 1}": card for i, card in enumerate(self.draw_cards(num_cards))}

    def __str__(self):
        """Representação textual do baralho."""
        return f"Baralho de tipo {self.deck_type} com {len(self.cards)} cartas."
