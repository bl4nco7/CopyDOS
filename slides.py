from manim import *
from manim_slides import Slide


class Introduction(Slide):
    def construct(self):
        # Color Del Fondo
        self.camera.background_color = WHITE
        # Titulo
        titulo_texto = [
            "Métrica Assimétrica de Fubini-Study",
            "na Grassmanniana total"
        ]
        
        # Crear textos y agruparlos
        titulo = VGroup(
            *[
                Text(t, font_size=40, color=BLUE_D)
                for t in titulo_texto
            ]
        ).arrange(DOWN, buff=0.5).shift(UP * 1.5) # Alinea verticalmente y sube el grupo
        # 2. Autor y Universidad (Usando VGroup para alineación simple)
        autor_texto = Text(
            "Drahcir Alexander Blanco Garcia", 
            font_size=30, 
            color=BLACK
        )
        univ_texto = Text(
            "Universidade Federal da Bahia", 
            font_size=20, 
            color=BLACK
        )
        
        creditos = VGroup(autor_texto, univ_texto).arrange(DOWN, buff=1.0).shift(DOWN * 2)

        # Rectángulo (usando .to_edge(UP) para fijarlo al borde superior)
        # Se fija el centro del rectangulo en y=3.7 para que el borde superior quede cerca del limite.
        rect1 = RoundedRectangle(
            width=13, 
            height=2.0, 
            color=BLACK, 
            fill_opacity=0.1
        ).shift(UP * 1.5) # Sube el centro para que quede en la parte superior

        # --- Animación ---
        
        # Animación de Entrada: usando FadeIn con el VGroup y Create para el rectángulo
        self.play(
            FadeIn(titulo, scale=1.2), # Animación con escalado ligero
            FadeIn(creditos),
            Create(rect1),
            run_time=3
        ) 
        self.next_slide()

        # BETA DOS
        
        self.wipe(welcome, square)
        self.play(FadeIn(dot))

        self.next_slide(loop=True)
        self.play(
            MoveAlongPath(dot, square, rate_func=linear), run_time=2
        )

class WithTeX(Slide):
    def construct(self):
        tex, text = VGroup(
            Tex(r"You can also use \TeX, e.g., $\cos\theta=1$"),
            Text("which does not render like plain text"),
        ).arrange(DOWN)

        self.play(FadeIn(tex))
        self.next_slide()

        self.play(FadeIn(text, shift=DOWN))


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
