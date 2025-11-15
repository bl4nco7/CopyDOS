from manim import *
from manim_slides import Slide

class Portada(Slide):
    def construct(self):
        # --- Color De Fondo (Colocar en Todas las esccenas)---
        self.camera.background_color = WHITE

        # --- Creación de Textos (Agrupados y Simplificados) ---

        # 1. Título (Usando VGroup para centrar y alinear)
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

        # --- Elemento Gráfico ---

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

        # Animación de Salida: usando Unwrite (desescritura) y FadeOut
        self.play(
            FadeOut(creditos, shift=DOWN), # Sale hacia abajo
            Unwrite(titulo),
            Uncreate(rect1),
            run_time=2.5 # Animación de salida ligeramente más rápida
        )

######################## Lamina 1 #############################

class lamina_1(Slide):
    def construct(self):
        # Define a cor de fundo
        self.camera.background_color = WHITE 
        # Plantilla LaTeX para justificación (si se necesita)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        # Linea
        linea = Line(np.array([-6.5, 3, 0]), np.array([6.5, 3, 0]), color=BLUE_D, stroke_width=0.7)


        text = Text("Álgebra exterior de Grassmann", color=BLUE_D, font_size=30)
        text.move_to([text.width/2 - 6.5, 3.5, 0])
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(text[0]) # Position the cursor

        # Adicion titulo del Slide
        self.add(linea)
  

        # Primeiro Paragrafo
        paragrafo_1 = "A álgebra exterior de Grassmann com base em um espaço vetorial $\\textmd{V}$ sobre $\\mathbb{R}$, é o espaço $\\displaystyle \\bigwedge \\textmd{V}$ que se descompõe como:"
        text1 = Tex(paragrafo_1, tex_template=myTemplate, tex_environment="justify",color=BLACK)
        text1.font_size = 35
        text1.move_to([text1.width/2 - 6.5, 2.3, 0])

        # Algebra Graduada
        equa = MathTex(
            "\\bigwedge \\textmd{V} = \\bigoplus_{p=0}^n \\bigwedge^p \\textmd{V}",
            "=\\mathbb{R} \\oplus \\textmd{V} \\oplus \\bigwedge^2 \\textmd{V} \\oplus \\cdots \\oplus \\bigwedge^p \\textmd{V}",
            color=BLACK
        ).scale(0.8)
        equa.next_to(text1, DOWN) 
        equa[0].shift(2*RIGHT)

        self.play(FadeIn(equa[0],text1),TypeWithCursor(text, cursor),Blink(cursor, blinks=2)) 

        self.next_slide()  # PASO DE LAMINA
        self.play(equa[0].animate.shift(2*LEFT),run_time = 2)
        self.play(Write(equa[1]))
        self.next_slide() # PASO DE LAMINA

        # Texto 2
        texto2 = "com um produto exterior bilinear e associativo"
        text2 = Tex(texto2, tex_template=myTemplate, tex_environment="justify",color=BLACK, font_size=35)
        text2.next_to(equa, DOWN,aligned_edge=LEFT) # .align_to(equa, LEFT)
        # .next_to(text1, DOWN, aligned_edge=LEFT) # Alinea con text1

 

        # Ecua 2
        equa2 = MathTex(
             "\\wedge:\\bigwedge^p \\mathbb{R}^n\\times\\bigwedge^q \\mathbb{R}^n \\rightarrow\\bigwedge^{p+q} \\mathbb{R}^n",
            color=BLACK
        ).scale(0.8)
        equa2.next_to(text2, DOWN) 

        self.play(FadeIn(text2), Write(equa2)) 
        self.next_slide() # PASO DE LAMINA
        # Texto 3
        texto3 = "este produto é alternante,"
        text3 = Tex(texto3, tex_template=myTemplate, tex_environment="justify",color=BLACK)
        text3.font_size = 35
        text3.next_to(equa2, DOWN) 
      

        equa3 = MathTex(
            "\\textmd{A} \\wedge \\textmd{B} = ", 
            "\\textmd{A} \\wedge \\textmd{B}", # Este es el segundo argumento (índice 1)
            ", \\quad \\text{se} \\quad \\textmd{A} \\in \\bigwedge^{p}\\: \\mathbb{R}^{n} \\: \\text{e} \\: \\textmd{B} \in \\bigwedge^{q}\\: \\mathbb{R}^{n}",
            color=BLACK
        ).scale(0.8)
        equa3.next_to(text3, DOWN)

        self.play(FadeIn(text3),Write(equa3[0]),Write(equa3[1]))   

        parte_seleccionada = equa3[1]

        # 2. Definir el objeto final (la expresión a la que se transforma)
        equa4 = MathTex("(-1)^{pq} \\left( \\textmd{B} \\wedge \\textmd{A} \\right)",color=BLACK).scale(0.8)
        
        # 3. Posicionar equa4 SOBRE la parte seleccionada ANTES de la transformación.
        # Esto asegura que el centro de equa4 coincida con el centro de parte_seleccionada.
        equa4.move_to(parte_seleccionada.get_center()).shift(RIGHT)
        t = equa3[2].shift(2*RIGHT)
        self.next_slide() # PASO DE LAMINA
        self.play(Transform(parte_seleccionada, equa4))
        self.play(FadeIn(t))
        self.wait() 
        self.next_slide() # PASO DE LAMINA
        self.play(FadeOut(text2,equa2,text3,equa3,t,text1,equa))
        # self.play(UntypeWithCursor(text, cursor),run_time = 2) # Se va a borrar en la lamina dos

######################## Lamina 2 #############################

class lamina_2(Slide):
    def construct(self):
        # Define a cor de fundo
        self.camera.background_color = WHITE 
        # Plantilla LaTeX para justificación (si se necesita)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        # Linea
        linea = Line(np.array([-6.5, 3, 0]), np.array([6.5, 3, 0]), color=BLUE_D, stroke_width=0.7) 


        text = Text("Álgebra exterior de Grassmann", color=BLUE_D, font_size=30)
        text.move_to([text.width/2 - 6.5, 3.5, 0])
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(text[0]) # Position the cursor
        self.add(linea,text)
        self.next_slide()
        # Primeiro Paragrafo
        paragrafo_1 = "Seus elementos são multivetores, ou também chamados blade de grau $p$, ou $p$-blade, é"
        text1 = Tex(paragrafo_1, tex_template=myTemplate, tex_environment="justify",color=BLACK)
        text1.font_size = 35
        text1.move_to([text1.width/2 - 6.5, 2.3, 0])

        # Algebra Graduada
        equa = MathTex(
              "\\textmd{A} = v_1\\wedge\\cdots\\wedge v_p \\quad \\text{com} \\quad  v_1,\\ldots,v_p\in \\mathbb{R}^n ",
            color=BLACK
        ).scale(0.8)
        equa.next_to(text1, DOWN)

        self.play(FadeIn(text1),Write(equa),run_time=2)
        self.next_slide() # PASO DE LAMINA
        # Texto 2
        texto2 = "que representa um paralelepípedo gerado por $\\{v_1,\\ldots,v_p\\}$ e determina um subespaço $[\\textmd{A}] = \\text{span}\\{v_1,\\ldots,v_p\\}.$ O produto interno de $\\textmd{A} = v_1\\wedge\\cdots\\wedge v_p$ e $\\textmd{B}=w_1\\wedge\\cdots\\wedge w_p$, é "
        text2 = Tex(texto2, tex_template=myTemplate, tex_environment="justify",color=BLACK)
        text2.font_size = 35
        text2.next_to(equa, DOWN)


        # Ecua 2
        equa2 = MathTex(
             "<\\textmd{A} , \\textmd{B}> = \\det \\big(<v_i , w_j> \\big)",
            color=BLACK
        ).scale(0.8)
        equa2.next_to(text2, 2*DOWN)
        self.play(FadeIn(text2),Write(equa2),run_time=2)

        # Texto 3
        texto3 = "a norma $\\| \\textmd{A} \\| = \sqrt{<\\textmd{A} , \\textmd{A}>}$ da o $p-$dimensional do paralelepípedo"
        text3 = Tex(texto3, tex_template=myTemplate, tex_environment="justify",color=BLACK)
        text3.font_size = 35
        text3.next_to(equa2, 2*DOWN) 
        self.next_slide() # PASO DE LAMINA
        self.play(FadeIn(text3),run_time=2)  

        self.play(FadeOut(text1,equa,text2,equa2,text3),run_time = 2)

        self.play(UntypeWithCursor(text, cursor))

########################################################## Ultima Lamina  ########################################

class GraciasFinal(Slide):
  def construct(self): 
      self.camera.background_color = WHITE
      self.next_slide(loop=True)
      src = Text(
            "¡Muchas Gracias!",
            font_size=86,
            color=BLUE_D
        )
      tar = Text(
            "Muito Obrigado!",
            font_size=86,
            color=BLUE_D
        )
        
        # 1. Animación Inicial (Escribir "Muchas Gracias!")
      self.play(Write(src), run_time = 3) 
      self.play(Transform(src, tar),run_time = 2)
