from manim import *
from manim_slides import Slide

class Portada(Slide):
    def construct(self):         
        # Define a cor de fundo
        self.camera.background_color = WHITE 
        # 1. Título
        titulo_texto = [
            "Métrica Assimétrica de Fubini-Study",
            "na Grassmanniana total"
        ]

        # Crear textos y agruparlos
        titulo = VGroup(
            *[
                Text(t, font_size=40, color=BLUE_D, font='sans-serif')
                for t in titulo_texto
            ]
        ).arrange(DOWN, buff=0.5).shift(UP * 2.5) # Alinea verticalmente y sube el grupo

        # 2. Autor, Orientador y Universidad (Usando VGroup para alineación simple)
        autor_texto = Text(
            "Drahcir Alexander Blanco Garcia",
            font_size=30,
            color=BLACK
        )
        orientador = Text(
            "Orientador: Dr. André Luís Godinho Mandolesi",
            font_size=30,
            color=BLACK
        )
        univ_texto = Text(
            "Universidade Federal da Bahia",
            font_size=20,
            color=BLACK
        )

        creditos = VGroup(autor_texto,orientador, univ_texto).arrange(DOWN, buff=1)
       

        # --- Rectangulo ---  
        rect1 = RoundedRectangle(
            width=13,
            height=2.0,
            color=BLACK,
            fill_opacity=0.1
        ).shift(UP * 2.5)  
        # --- Ubicación del Rectangulo ---  
        creditos.next_to(rect1,3*DOWN)
         
        # --- Animación --- 
        self.play(
            FadeIn(titulo), # Animación con escalado ligero
            FadeIn(creditos),
            DrawBorderThenFill(rect1),
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
        self.add(linea)
        ######################################## USAR CN TODAS LAS LAMINAS ####################################### 
        
        # Parte 1
        text = Text("Álgebra exterior de Grassmann", color=BLUE_D, font_size=30,font='sans-serif')
        text.move_to([text.width/2 - 6.5, 3.5, 0])
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(text[0]) # Position the curso 
        # Adicion titulo del Slide
        self.play(TypeWithCursor(text, cursor))
        self.play(Blink(cursor, blinks=2))
        # Primeiro Paragrafo
        paragrafo_1 = "A álgebra exterior de Grassmann com base em um espaço vetorial $\\textmd{V}$ sobre $\\mathbb{R}$, é o espaço $\\displaystyle \\bigwedge \\textmd{V}$ que se descompõe como:"
        text1 = Tex(paragrafo_1, tex_template=myTemplate, tex_environment="justify",color=BLACK,font_size = 35)
        text1.move_to([text1.width/2 - 6.5, 2.3, 0])
        # Algebra Graduada
        equa = MathTex(
            "\\bigwedge \\textmd{V} = \\bigoplus_{p=0}^n \\bigwedge^p \\textmd{V}",
            "=\\mathbb{R} \\oplus \\textmd{V} \\oplus \\bigwedge^2 \\textmd{V} \\oplus \\cdots \\oplus \\bigwedge^p \\textmd{V}",
            color=BLACK
        ).scale(0.8)
        equa.next_to(text1, DOWN)
        equa[0].shift(2*RIGHT)
        # Animacion 
        self.play(FadeIn(equa[0],text1))
        self.next_slide() # Paso de Lamina 
        self.play(equa[0].animate.shift(2*LEFT),run_time = 2)
        self.play(Write(equa[1]))
        # Texto 2
        self.next_slide() # Paso de Lamina
        texto2 = "com um produto exterior bilinear e associativo"
        text2 = Tex(texto2, tex_template=myTemplate, tex_environment="justify",color=BLACK, font_size=35)
        text2.move_to([text2.width/2 - 6.5,0, 0]) 
        # Ecua 2
        equa2 = MathTex(
             "\\wedge:\\bigwedge^p \\mathbb{R}^n\\times\\bigwedge^q \\mathbb{R}^n \\rightarrow\\bigwedge^{p+q} \\mathbb{R}^n",
            color=BLACK
        ).scale(0.8)
        equa2.next_to(equa, 2.5 * DOWN)
        self.play(FadeIn(text2), Write(equa2))
        # Texto 3
        texto3 = "este produto é alternante,"
        text3 = Tex(texto3, tex_template=myTemplate, tex_environment="justify",color=BLACK)
        text3.font_size = 35
        text3.move_to([text3.width/2 - 6.5,-1.5, 0])  
        self.next_slide() # Paso de Lamina 

        equa3 = MathTex(
            "\\textmd{A} \\wedge \\textmd{B} = ",
            "\\textmd{A} \\wedge \\textmd{B}", # Este es el segundo argumento (índice 1)
            ", \\quad \\text{se} \\quad \\textmd{A} \\in \\bigwedge^{p}\\: \\mathbb{R}^{n} \\: \\text{e} \\: \\textmd{B} \in \\bigwedge^{q}\\: \\mathbb{R}^{n}",
            color=BLACK
        ).scale(0.8)
        equa3.next_to(equa2, 2.5*DOWN) 

        self.play(FadeIn(text3),Write(equa3[0]),Write(equa3[1]))

        parte_seleccionada = equa3[1]

        # 2. Definir el objeto final (la expresión a la que se transforma)
        equa4 = MathTex("(-1)^{pq} \\left( \\textmd{B} \\wedge \\textmd{A} \\right)",color=BLACK).scale(0.8)

        # 3. Posicionar equa4 SOBRE la parte seleccionada ANTES de la transformación.
        # Esto asegura que el centro de equa4 coincida con el centro de parte_seleccionada.
        equa4.move_to(parte_seleccionada.get_center()).shift(RIGHT)
        t = equa3[2].shift(2*RIGHT)
        self.next_slide() # Paso de Lamina

        self.play(Transform(parte_seleccionada, equa4))
        self.play(FadeIn(t))
        self.wait()
        self.next_slide() # Paso de Lamina

        self.play(FadeOut(text2,equa2,text3,equa3,t,text1,equa)) 

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
        self.add(linea)
        ######################################## USAR CN TODAS LAS LAMINAS ####################################### 


        text = Text("Álgebra exterior de Grassmann", color=BLUE_D, font_size=30,font='sans-serif')
        text.move_to([text.width/2 - 6.5, 3.5, 0])
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(text[0]) # Position the cursor
        self.add(text)

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

        self.play(FadeIn(text1))
        self.play(Write(equa),run_time=2)
        self.next_slide() # Paso de Lamina

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
        self.next_slide() # Paso de Lamina

        # Texto 3
        texto3 = "a norma $\\| \\textmd{A} \\| = \sqrt{<\\textmd{A} , \\textmd{A}>}$ dá o vlume $p-$dimensional do paralelepípedo"
        text3 = Tex(texto3, tex_template=myTemplate, tex_environment="justify",color=BLACK)
        text3.font_size = 35
        text3.next_to(equa2, 2*DOWN)

        self.play(FadeIn(text3),run_time=2)
        self.next_slide() # Paso de Lamina 

        self.play(FadeOut(text1,equa,text2,equa2,text3),run_time = 2)

        self.play(UntypeWithCursor(text, cursor)) 

         # Lamina 3

         ######################## Lamina 4 #############################
class lamina_4(Slide):
    def construct(self):
        # Define a cor de fundo
        self.camera.background_color = WHITE
        # Plantilla LaTeX para justificación (si se necesita)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        # Linea
        linea = Line(np.array([-6.5, 3, 0]), np.array([6.5, 3, 0]), color=BLUE_D, stroke_width=0.7)
        self.add(linea)
        ######################################## USAR CN TODAS LAS LAMINAS ####################################### 
        # === 1. Título ===
        text = Text("Ângulos entre subespaços", color=BLUE_D, font_size=30, font='sans-serif')
        text.move_to([text.width/2 - 6.5, 3.5, 0])
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(text[0]) # Position the cursor
        self.play(TypeWithCursor(text, cursor))
        self.play(Blink(cursor, blinks=2))
        ## RECATNGULOS 
        block_box = RoundedRectangle(
            color = BLACK,         # Cor da borda (Azul Escuro)
            fill_color = BLACK,
            fill_opacity = 0.1,
            height = 1,
            width = 14,
             )
        block_box.move_to([0,2.3,0])
        block_box1 = RoundedRectangle(
            color = BLACK,         # Cor da borda (Azul Escuro)
            fill_color = BLUE_A,
            fill_opacity = 0.5,
            height = 4.5,
            width = 14,
           )
        block_box1.next_to(block_box, DOWN, buff=0.1) 
      
         # === 2. "Definição" ===
        definicao = Tex("Definição", color=BLACK)
        definicao.move_to([definicao.width/2-6.5,2.3,0])
        self.play(Create(block_box), 
                  Write(definicao), 
                  FadeIn(block_box1, shift=LEFT)
                  )
        

        # === 3. Texto inicial sobre as bases ===
        paragrafo = "Bases ortonormais $\\textmd{B}_{\\textmd{V}}=\\{e_1,\ldots,e_p\\}$ e $\\textmd{B}_{\\textmd{W}}=\\{f_1,\\ldots,f_q\\}$ de $\\textmd{V},\\textmd{W}\\subset\\mathbb{R}^n$ são principais se:"
        texto_bases = Tex(paragrafo,tex_template=myTemplate, tex_environment="justify",color=BLACK,font_size = 35) #, t2c={"Bases ortonormais": ORANGE, "weight": RED}  )
        #texto_bases.scale(0.8)
        texto_bases.next_to(definicao, 2 * DOWN, aligned_edge=LEFT)  
        #texto_bases.move_to([texto_bases.width/2 -6.5, 1.3, 0])
        self.play(FadeIn(texto_bases, shift=DOWN))
        self.next_slide() # Paso de Lamina 

        # === 4. Equação do produto interno com os casos ===
        eq_produto = MathTex(
        r"\langle e_i , f_j\rangle = "
        r"\begin{cases}"
        r"0 & \text{se } i \neq j,\\[4pt]"
        r"\cos(\theta_i)"
        r"& \text{se } i = j."
        r"\end{cases}",
        color=BLACK
        )
        eq_produto.scale(0.9)
        eq_produto.move_to([eq_produto.width/2 -6.5, 0, 0])
        self.play(Write(eq_produto))
        self.wait(0.7)

        # === 5. Ordenação dos ângulos ===
        eq_ordenacao = MathTex(
            r"0 \leq \theta_1 \leq \cdots \leq \theta_m \leq \frac{\pi}{2},",
            color=BLACK
        )
        eq_ordenacao.scale(0.9)
        eq_ordenacao.move_to([5-eq_ordenacao.width/2, 0, 0])
        self.play(Write(eq_ordenacao))
        self.next_slide() # Paso de Lamina 

        # === 6. Fórmula final dos ângulos principais ===
        eq_theta = MathTex(
            r"\theta_i = \cos^{-1}(e_i \cdot f_i).",
            color=BLACK
        )
        eq_theta.scale(0.9)
        eq_theta.move_to([0,-2,0])
        self.play(Write(eq_theta))
        self.next_slide() # Paso de Lamina  
        # === Encerramento ===
        self.play(FadeOut(block_box,shift=RIGHT),
                  FadeOut(block_box1,shift=DOWN),
                  FadeOut(definicao, shift=UP),
                  FadeOut(texto_bases,shift=DOWN),
                  FadeOut(eq_produto, shift=UP),
                  FadeOut(eq_ordenacao, shift=UP),
                  FadeOut(eq_theta, shift=UP),
                  )

        self.play(UntypeWithCursor(text, cursor))
        ## Lamina 5 ## 
class lamina_5(Scene):
    def construct(self):
        # Define a cor de fundo
        self.camera.background_color = WHITE
        # Plantilla LaTeX para justificación (si se necesita)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        # Linea
        linea = Line(np.array([-6.5, 3, 0]), np.array([6.5, 3, 0]), color=BLUE_D, stroke_width=0.7)
        self.add(linea)
        ######################################## USAR CN TODAS LAS LAMINAS #######################################

        # === 1. Título ===
        text = Text("Grassmanniana total de      .", color=BLUE_D, font_size=30, font='sans-serif')
        text.move_to([text.width/2 - 6.5, 3.5, 0])
        rn = Tex(r"$\mathbb{R}^n$",color=BLUE_D).scale(1.1)
        rn.move_to([-(7-text.width), 3.5, 0])
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
          ).move_to(text[0]) # Position the cursor
        self.play(TypeWithCursor(text, cursor))
        self.play(FadeIn(rn))
        self.play(Blink(cursor, blinks=2))

        # Bloque tipo beamer (rectángulo)
        block_box = RoundedRectangle(
            color = BLACK,         # Cor da borda (Azul Escuro)
            fill_color = BLACK,
            fill_opacity = 0.1,
            height = 1,
            width = 14,
             )
        block_box.move_to([0,2.3,0])
        block_box1 = RoundedRectangle(
            color = BLACK,         # Cor da borda (Azul Escuro)
            fill_color = BLUE_A,
            fill_opacity = 0.5,
            height = 4.5,
            width = 14,
           )
        block_box1.next_to(block_box, DOWN, buff=0.1)

         # === 2. "Definição" ===
        definicao = Tex("Definição (Grassmannianas)", color=BLACK)
        definicao.move_to([definicao.width/2-6.5,2.3,0])
        self.play(Create(block_box),
                  Write(definicao),
                  FadeIn(block_box1, shift=LEFT)
                  )
        self.wait(0.5)


        # Contenido del bloque
        texto = Tex(
            r"""
            Seja $\textmd{V}$ um espaço vetorial sobre $\mathbb{R}$ de dimensão $n$.
            \begin{itemize}
                \item A $p$-Grassmanniana $\textmd{Gr}_{p}(\mathbb{R}^n)$ se define como o conjunto \\
                de sub-espaços vetoriais de dimensão $p$ do espaço vetorial $\textmd{V}$.
                \item Grassmanniana total
                 \[
                    \textmd{Gr}(\mathbb{R}^n)=\bigcup_{p=0}^n \textmd{Gr}_{p}(\mathbb{R}^n).
                 \]
            \end{itemize}
            """,
            color=BLACK,
            font_size = 35,
            tex_environment="justify",
            tex_template=myTemplate
        ).next_to(definicao, 2 * DOWN, aligned_edge=LEFT)
        self.play(FadeIn(texto, shift=DOWN))
        self.next_slide() # Paso de Lamina   

        self.play(FadeOut(block_box,shift=RIGHT),
                  FadeOut(block_box1,shift=DOWN),
                  FadeOut(definicao, shift=UP),
                  FadeOut(texto, shift=LEFT)
                  )
        self.play(Unwrite(rn))
        self.play(UntypeWithCursor(text, cursor))
 

        
        ############################################  Penultima Lamina (Referencias)  ########################################


class Referencias(Slide):
    def construct(self):
        # Define a cor de fundo
        self.camera.background_color = WHITE
        # Plantilla LaTeX para justificación (si se necesita)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        # Linea
        linea = Line(np.array([-6.5, 3, 0]), np.array([6.5, 3, 0]), color=BLUE_D, stroke_width=0.7)
        self.add(linea)
        ######################################## USAR CN TODAS LAS LAMINAS #######################################

        # Título
        text = Text("Referências", color=BLUE_D, font_size=30, font='sans-serif')
        text.move_to([text.width/2 - 6.5, 3.5, 0])
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(text[0])
 
        self.play(TypeWithCursor(text, cursor))
        self.play(Blink(cursor, blinks=2))
        self.next_slide() # Paso de Lamina

        # --- Lista de referências ---
        refs = [
            r"A.~L.~G. Mandolesi, \emph{Grassmann angles between real or complex subspaces}, arXiv:1910.00147 (2019).",
            r"A.~L.~G. Mandolesi, \emph{Blade products and angles between subspaces}, \textit{Adv. Appl. Clifford Algebras} \textbf{31} (2021), no.~69.",
            r"A.~C.~G. Mennucci, \emph{Geodesics in asymmetric metric spaces}, \textit{Anal. Geom. Metr. Spaces} \textbf{2} (2014), no.~1, 115--153.",
            r"S.~E. Kozlov, \emph{Geometry of real Grassmann manifolds. Parts I, II, III}, \textit{J. Math. Sci.} \textbf{100} (2000), no.~3, 2239--2268.",
            r"K.~Ye, L.~H. Lim, \emph{Schubert varieties and distances between subspaces of different dimensions}, \textit{SIAM J. Matrix Anal. Appl.} \textbf{37} (2016), no.~3, 1176--1197.",
            r"K.~Ye, L.~H. Lim, \emph{Schubert varieties and distances between subspaces of different dimensions}, SIAM J. Matrix Anal. Appl. \textbf{37} (2016), no.~3, 1176--1197."
        ]

        # --- Crear referencias con numeración y colorear títulos ---
        referencias = VGroup()

        for i, t in enumerate(refs, start=1):
            # Añadimos la enumeración [1], [2], ...
            enumerated = rf"[{i}]~" + t

            tex_ref = Tex(
                enumerated,
                tex_template=myTemplate,
                tex_environment="justify",
                font_size=28,
                color=BLACK
            )

            referencias.add(tex_ref)

        referencias.arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # Posición agradable en la diapositiva
        referencias.move_to([referencias.width/2 - 5.5, -0.25, 0])

        self.play(FadeIn(referencias))

        self.next_slide() # Paso de Lamina 
 

        self.play(FadeOut(referencias))
        self.play(UntypeWithCursor(text, cursor))


############################################ Ultima Lamina (Agradecimientos)  ########################################

class GraciasFinal(Slide):
    def construct(self): 
        self.camera.background_color = WHITE
        self.next_slide(loop=True)
        src = Text(
             "¡Muchas Gracias!",
             font_size=86,
             color=BLUE_D,
             font='sans-serif'
                  ) 
        tar = Text(
            "Muito Obrigado!",
            font_size=86,
            color=BLUE_D,
            font='sans-serif'
            )
        
        # 1. Animación Inicial (Escribir "Muchas Gracias!")
        self.play(Write(src), run_time = 3) 
        self.play(Transform(src, tar),run_time = 2)
