import flet as ft
from pokeapi import get_pokemon
from type_colors import TYPE_COLORS


def main(page: ft.Page):
    # Configuração da janela
    page.title = "Pokédex"
    page.window.icon = "assets/icon.png"
    page.window.width = 420
    page.window.height = 720
    page.window.resizable = False
    page.window.maximizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.SURFACE_VARIANT

    # Índice inicial para o Pokémon
    pokemon_index = 1

    # Componentes de exibição de informações do Pokémon
    pokemon_name_text = ft.Text(size=36, color="#FFFFFF", weight="bold")
    pokemon_tag_text = ft.Text(size=18, color="#FFFFFF")
    imagem = ft.Image(scale=2, width=200, height=200)
    image_container = ft.Container(content=ft.Column(
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[imagem]
            )
        ]
    ),
        bgcolor="#F79F1F", padding=10, border_radius=35, width=400, height=320
    )

    # Linha de tipos
    pokemon_type_row = ft.Row(controls=[], spacing=8,
                              alignment=ft.MainAxisAlignment.START)

    # Ícones e textos para os atributos do Pokémon
    hp_text = ft.Row([ft.Icon(ft.icons.FAVORITE, color="#FF0000"),
                     ft.Text("HP", color="#FFFFFF", size=18)])
    attack_text = ft.Row([ft.Icon(ft.icons.SPORTS_MMA_SHARP, color="#FF8C00"),
                          ft.Text("ATTACK", color="#FFFFFF", size=18)])
    defense_text = ft.Row([ft.Icon(ft.icons.SHIELD, color="#00FF00"),
                           ft.Text("DEFENSE", color="#FFFFFF", size=18)])
    special_attack_text = ft.Row([ft.Icon(ft.icons.FLASH_ON, color="#FF00FF"),
                                  ft.Text("SA", color="#FFFFFF", size=18)])
    special_defense_text = ft.Row([ft.Icon(ft.icons.SHIELD, color="#00FFFF"),
                                   ft.Text("SD", color="#FFFFFF", size=18)])
    speed_text = ft.Row([ft.Icon(ft.icons.DIRECTIONS_RUN, color="#FFFF00"),
                         ft.Text("SPEED", color="#FFFFFF", size=18)])
    weight_text = ft.Row([ft.Icon(ft.icons.FITNESS_CENTER, color="#FFFFFF"),
                          ft.Text("PESO", color="#FFFFFF", size=18)])

    # Valores dos atributos
    hp_value = ft.Text(color="#FFFFFF", size=16, weight="bold")
    attack_value = ft.Text(color="#FFFFFF", size=16, weight="bold")
    defense_value = ft.Text(color="#FFFFFF", size=16, weight="bold")
    special_attack_value = ft.Text(color="#FFFFFF", size=16, weight="bold")
    special_defense_value = ft.Text(color="#FFFFFF", size=16, weight="bold")
    speed_value = ft.Text(color="#FFFFFF", size=16, weight="bold")
    weight_value = ft.Text(color="#FFFFFF", size=16, weight="bold")

    # Atributos do Pokémon organizados em três linhas com ícones
    pokemon_stats = ft.Column(
        controls=[
            # Primeira linha de atributos: HP, ATTACK, DEFENSE
            ft.Row(
                controls=[
                    ft.Column(
                        controls=[hp_text, hp_value],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=[attack_text, attack_value],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=[defense_text, defense_value],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
            ),
            # Segunda linha de atributos: SA, SPEED, PESO
            ft.Row(
                controls=[
                    ft.Column(
                        controls=[special_attack_text, special_attack_value],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=[special_defense_text, special_defense_value],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=[speed_text, speed_value],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Column(
                        controls=[weight_text, weight_value],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
            ),
        ]
    )

    pokemon_gen_text = ft.Text(size=20, color="#FFFFFF", weight="bold")

    # Função para atualizar a exibição do Pokémon
    def update_pokemon_display(index):
        # Pegando a lista da API e dividindo em variáveis
        pokemon_data = get_pokemon(index)
        img_url = pokemon_data[0]
        pokemon_name = pokemon_data[1]
        pokemon_id = pokemon_data[2]
        pokemon_types = pokemon_data[3]
        pokemon_weight = pokemon_data[4]
        pokemon_hp = pokemon_data[5]
        pokemon_attack = pokemon_data[6]
        pokemon_defense = pokemon_data[7]
        pokemon_special_attack = pokemon_data[8]
        pokemon_special_defense = pokemon_data[9]
        pokemon_speed = pokemon_data[10]
        pokemon_gen = pokemon_data[11]

        imagem.src = img_url
        pokemon_name_text.value = pokemon_name
        pokemon_tag_text.value = f"#{pokemon_id}"

        # Define a cor de fundo com base no primeiro tipo do Pokémon
        main_color = TYPE_COLORS.get(pokemon_types[0].lower(), "#10AC84")
        image_container.bgcolor = main_color

        # Atualiza a exibição dos tipos de Pokémon
        pokemon_type_row.controls.clear()
        for pokemon_type in pokemon_types:
            type_color = TYPE_COLORS.get(pokemon_type.lower(), "#10AC84")
            pokemon_type_row.controls.append(
                ft.Container(
                    content=ft.Text(
                        pokemon_type.capitalize(),
                        size=18,
                        color="#000000",
                        weight="bold",
                    ),
                    bgcolor=type_color,
                    padding=ft.padding.all(8),
                    border_radius=12,
                    margin=ft.margin.only(right=10),
                )
            )

        # Atualiza a exibição dos valores dos atributos
        hp_value.value = str(pokemon_hp)
        attack_value.value = str(pokemon_attack)
        defense_value.value = str(pokemon_defense)
        special_attack_value.value = str(pokemon_special_attack)
        special_defense_value.value = str(pokemon_special_defense)
        speed_value.value = str(pokemon_speed)
        weight_value.value = f'{pokemon_weight} Kg'

        # Atualiza a geração de cada pokemon
        pokemon_gen_text.value = str(pokemon_gen)

        # Atualiza a página após todas as mudanças
        page.update()

    # Função de busca
    def search_pokemon(e):
        search_query = search_pokemon_bar.value.strip().lower()
        if search_query.isdigit():
            update_pokemon_display(int(search_query))
        else:
            # Procura pelo nome
            update_pokemon_display(search_query)
    # Funções para navegar entre os Pokémons

    def preview_pokemon(e):
        nonlocal pokemon_index
        if pokemon_index > 1:
            pokemon_index -= 1
            update_pokemon_display(pokemon_index)

    def next_pokemon(e):
        nonlocal pokemon_index
        pokemon_index += 1
        update_pokemon_display(pokemon_index)

    # Configuração do conteúdo principal
    main_app = ft.Container(
        bgcolor="#212121",
        width=420,
        height=720,
        border_radius=35,
        padding=ft.padding.only(left=0, right=0, top=0, bottom=0),
        content=ft.Stack(
            controls=[
                ft.Container(),
                image_container,
                ft.Column(
                    top=120,
                    left=10,
                    right=10,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.FloatingActionButton(
                                    icon=ft.icons.ARROW_BACK_ROUNDED,
                                    height=35,
                                    width=35,
                                    bgcolor="#2D3436",
                                    opacity=0.9,
                                    on_click=preview_pokemon,
                                ),
                                ft.FloatingActionButton(
                                    icon=ft.icons.ARROW_FORWARD_ROUNDED,
                                    height=35,
                                    width=35,
                                    bgcolor="#2D3436",
                                    opacity=0.9,
                                    on_click=next_pokemon,
                                ),
                            ],
                        ),
                    ],
                ),
                ft.Column(
                    top=320,
                    left=20,
                    right=20,
                    alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            width=420,
                            height=100,
                            controls=[
                                ft.Column(
                                    spacing=0,
                                    height=100,
                                    controls=[pokemon_name_text,
                                              pokemon_tag_text],
                                ),
                                ft.Column(
                                    height=100,
                                    controls=[pokemon_gen_text],
                                ),
                            ],
                        ),
                    ],
                ),
                # Linha de tipos
                ft.Container(
                    content=pokemon_type_row,
                    top=410,
                    left=10,
                ),
                ft.Container(
                    content=pokemon_stats,
                    top=460,
                    left=10,
                ),
            ],
        ),
    )

    search_pokemon_bar = ft.SearchBar(
        value="",
        bar_hint_text="Buscar Pokémon",
        height=30,
        on_submit=search_pokemon,
    )

    page.add(search_pokemon_bar,
             main_app)
    update_pokemon_display(pokemon_index)


ft.app(target=main, assets_dir="assets")
