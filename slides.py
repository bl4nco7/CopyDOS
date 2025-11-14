from manim import *
from manim_slides import Slide


class Introduction(Slide):
    def construct(self):
        welcome = Text("Estos es una prueba para mi presentación em Python")
        square = Square(color=BLUE)
        dot = Dot(color=RED).shift(RIGHT + UP)

        self.play(FadeIn(welcome))
        self.next_slide()

        self.wipe(welcome, square)
        self.play(FadeIn(dot))

        self.next_slide(loop=True)
        self.play(
            MoveAlongPath(dot, square, rate_func=linear), run_time=2
        )

class WithTeX(Slide):
    def construct(self):
        tex, text = VGroup(
            Tex(r"También es posible utilizar \TeX, ejemplo:, $\cos\theta=1$"),
            Text("que no se muestra como texto sin formato"),
        ).arrange(DOWN)

        self.play(FadeIn(tex))
        self.next_slide()

        self.play(FadeIn(text, shift=DOWN))


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Más información sobre mi presentación:"),
            Text("https://bl4nco7.github.io/CV/"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
