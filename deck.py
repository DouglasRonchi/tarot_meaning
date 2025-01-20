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
            return [f"{rank} de {suit}" for suit in suits for rank in ranks]

    def create_marselha_deck(self):
            arcana_maior = [
                "O Louco", "O Mago", "A Sacerdotisa", "A Imperatriz", "O Imperador", 
                "O Hierofante", "Os Enamorados", "O Carro", "A Justiça", "O Eremita", 
                "A Roda da Fortuna", "A Força", "O Enforcado", "A Morte", "A Temperança", 
                "O Diabo", "A Torre", "A Estrela", "A Lua", "O Sol", 
                "O Julgamento", "O Mundo"
            ]
            arcana_menor = [f"{rank} de {suit}" for suit in ['Copas', 'Ouro', 'Paus', 'Espadas'] 
                            for rank in ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei']]
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
        if self.deck_type == "comum":
            meaning = {
                "A de Ouro": "Casa",
                "2 de Ouro": "Viagem de Dia",
                "3 de Ouro": "Recado Muito Bom",
                "4 de Ouro": "Palavras de Amor Íntimo",
                "5 de Ouro": "Dinheiro",
                "6 de Ouro": "Dinheiro",
                "7 de Ouro": "Certeza Muito Boa",
                "8 de Ouro": "Mudança Boa",
                "9 de Ouro": "Filho",
                "J de Ouro": "(Pensamentos) Alemão",
                "Q de Ouro": "Loira",
                "K de Ouro": "Loiro",
                "A de Copas": "Casa",
                "2 de Copas": "Viagem de Dia",
                "3 de Copas": "Recado Muito Bom",
                "4 de Copas": "Palavras de Amor Fraterno",
                "5 de Copas": "Felicidade",
                "6 de Copas": "Falsidade / Engano",
                "7 de Copas": "Certeza",
                "8 de Copas": "Mudança",
                "9 de Copas": "Filho",
                "J de Copas": "(Pensamentos) Branco / Italiano",
                "Q de Copas": "Branca",
                "K de Copas": "Branco",
                "A de Paus": "Fofoca",
                "2 de Paus": "Viagem de Noite",
                "3 de Paus": "Recado Ruim",
                "4 de Paus": "Doença Passageira",
                "5 de Paus": "Perca",
                "6 de Paus": "Susto",
                "7 de Paus": "Certeza",
                "8 de Paus": "Choro",
                "9 de Paus": "Fofoca",
                "J de Paus": "(Pensamentos) Moreno Claro",
                "Q de Paus": "Morena",
                "K de Paus": "Moreno",
                "A de Espadas": "Raiva",
                "2 de Espadas": "Viagem de Noite",
                "3 de Espadas": "Recado Ruim",
                "4 de Espadas": "Doença Grave",
                "5 de Espadas": "Feitiço",
                "6 de Espadas": "Caixão",
                "7 de Espadas": "Certeza Ruim",
                "8 de Espadas": "Bebedeira / Festa",
                "9 de Espadas": "Justiça",
                "J de Espadas": "(Pensamentos) Preto",
                "Q de Espadas": "Preta",
                "K de Espadas": "Preto",
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
                "O Enforcado": "Sacrifício, perspectiva, pausa, rendição.",
                "A Morte": "Transformação, finais, novos começos, renascimento.",
                "A Temperança": "Equilíbrio, moderação, harmonia, paciência.",
                "O Diabo": "Apego, materialismo, tentação, repressão.",
                "A Torre": "Mudança súbita, crise, libertação, revelação.",
                "A Estrela": "Esperança, inspiração, renovação, serenidade.",
                "A Lua": "Ilusões, intuição, incerteza, mistério.",
                "O Sol": "Sucesso, alegria, clareza, vitalidade.",
                "O Julgamento": "Renascimento, absolvição, decisão, despertar.",
                "O Mundo": "Conclusão, realização, integridade, plenitude.",
                
                # Naipes - Copas, Espadas, Paus e Ouro
                # Naipe de Copas
                "Ás de Copas": "Novo amor, emoção, fertilidade.",
                "2 de Copas": "Parceria, conexão, equilíbrio emocional.",
                "3 de Copas": "Celebração, amizade, abundância.",
                "4 de Copas": "Estagnação emocional, introspecção.",
                "5 de Copas": "Decepção, perda emocional, arrependimento.",
                "6 de Copas": "Nostalgia, memórias, bondade.",
                "7 de Copas": "Ilusões, escolhas, fantasias.",
                "8 de Copas": "Deixar ir, busca de propósito.",
                "9 de Copas": "Satisfação emocional, realização de desejos.",
                "10 de Copas": "Felicidade, harmonia familiar, plenitude.",
                "Valete de Copas": "Mensagem emocional, novidade criativa.",
                "Rainha de Copas": "Empatia, intuição, compaixão.",
                "Rei de Copas": "Controle emocional, sabedoria emocional.",
                
                # Naipe de Espadas
                "Ás de Espadas": "Verdades reveladas, clareza, decisão.",
                "2 de Espadas": "Conflito, indecisão, equilíbrio entre opostos.",
                "3 de Espadas": "Coração partido, dor emocional, traição.",
                "4 de Espadas": "Descanso, recuperação, introspecção.",
                "5 de Espadas": "Perda, conflito, vitória a qualquer custo.",
                "6 de Espadas": "Viagem, transição, alívio, mudança.",
                "7 de Espadas": "Engano, furtividade, dissimulação.",
                "8 de Espadas": "Limitações, aprisionamento, falta de liberdade.",
                "9 de Espadas": "Ansiedade, pesadelos, medo, preocupação.",
                "10 de Espadas": "Fim de um ciclo doloroso, traição, colapso.",
                "Valete de Espadas": "Curiosidade, mensagens, vigilância.",
                "Rainha de Espadas": "Lógica, independência, sabedoria.",
                "Rei de Espadas": "Autoridade intelectual, clareza mental, julgamento imparcial.",
                
                # Naipe de Paus
                "Ás de Paus": "Novos começos, inspiração, criatividade.",
                "2 de Paus": "Planejamento, tomada de decisão, visão futura.",
                "3 de Paus": "Expansão, visão de longo prazo, trabalho em equipe.",
                "4 de Paus": "Estabilidade, celebração, harmonia.",
                "5 de Paus": "Conflito, competição, desafios.",
                "6 de Paus": "Vitória, reconhecimento, sucesso público.",
                "7 de Paus": "Defesa, resistência, desafios a superar.",
                "8 de Paus": "Velocidade, movimento rápido, progresso.",
                "9 de Paus": "Perseverança, resistência, cuidado com os obstáculos.",
                "10 de Paus": "Sobrecarregado, responsabilidade excessiva, fardo.",
                "Valete de Paus": "Mensagem, novos começos, entusiasmo.",
                "Rainha de Paus": "Confiança, carisma, criatividade.",
                "Rei de Paus": "Liderança, inspiração, ação decisiva.",
                
                # Naipe de Ouro
                "Ás de Ouro": "Novas oportunidades financeiras, abundância, prosperidade.",
                "2 de Ouro": "Equilíbrio financeiro, adaptabilidade, mudanças.",
                "3 de Ouro": "Trabalho em equipe, aprendizado, reconhecimento.",
                "4 de Ouro": "Conservadorismo, segurança financeira, avareza.",
                "5 de Ouro": "Perda, dificuldades financeiras, exclusão.",
                "6 de Ouro": "Generosidade, ajuda mútua, caridade.",
                "7 de Ouro": "Paciência, avaliação, retorno sobre investimento.",
                "8 de Ouro": "Trabalho árduo, dedicação, aperfeiçoamento.",
                "9 de Ouro": "Conquista material, segurança financeira.",
                "10 de Ouro": "Herança, riqueza duradoura, estabilidade familiar.",
                "Valete de Ouro": "Mensagem de prosperidade, novos negócios.",
                "Rainha de Ouro": "Segurança material, nutrição, riqueza.",
                "Rei de Ouro": "Sucesso financeiro, autoridade, estabilidade.",
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
        return meaning.get(card, "Significado não encontrado.")


    def play_manually_input(self):
        num_cards = int(input("Digite o número de cartas para a tiragem personalizada: ").strip())
        return {f"Carta {i + 1}": card for i, card in enumerate(self.draw_cards(num_cards))}

    def __str__(self):
        """Representação textual do baralho."""
        return f"Baralho de tipo {self.deck_type} com {len(self.cards)} cartas."
