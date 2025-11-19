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

      ######################## Lamina 3 #############################
class lamina_3(Slide):
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
        # === === === === === === === === === === 1. Título === === === === === === === === === ===
        text = Text("Representação Geométrica en      .", color=BLUE_D, font_size=30, font='sans-serif')
        text.move_to([text.width/2 - 6.5, 3.5, 0])
        r3 = Tex(r"$\mathbb{R}^3$",color=BLUE_D).scale(1.1)
        r3.move_to([-(7-text.width), 3.6, 0])
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
          ).move_to(text[0]) # Position the cursor
        # Aparece el texto del título más el cursor
        self.play(TypeWithCursor(text, cursor))
        self.play(FadeIn(r3))
        self.play(Blink(cursor, blinks=1))
        # Crea la division del plano

        # Linha com Traços Mais Longos (dash_length maior)
        dashed_line_1 = DashedLine(
            start=np.array([-6.5,0,0]),
            end=np.array([6.5,0,0]),
            dash_length=0.2, # Traços mais longos
            color=BLUE
        )
        # Linha com Traços Mais Longos (dash_length maior)
        dashed_line_2 = DashedLine(
            start=linea.get_center(),
            end=-linea.get_center()+np.array([0,-1,0]),
            dash_length=0.2, # Traços mais longos
            color=BLUE
        )

        # === === === === === === === === === === 0 - blade (Inicial) === === === === === === === === === ===

        ponto = Dot(radius=0.16, color=BLUE_D).move_to([-2.5,0,0])
        ponto.pf = ponto.copy().move_to([-linea.width/4, dashed_line_2.height/4 ,0]) # Copia del Punto

        # Texto del punto
        texto_ponto = MathTex(
            r"v = \{0\}", r",\: \text{é um }", r"0\text{-blade}",
            color=BLACK
          ).next_to(ponto, RIGHT)
        texto_ponto.pf = texto_ponto[2].copy().next_to(ponto.pf, DOWN)
        # Aparece
        self.play(Write(ponto),FadeIn(texto_ponto))
        self.next_slide() # Paso de Lamina
        # Desaparece
        self.play(FadeOut(ponto),Unwrite(texto_ponto))
        self.next_slide() # Paso de Lamina
        # === === === === === === === === === === 1 - blade (Inicial) === === === === === === === === === ===

        # Donde esta la posicion inicial del vector
        posicao_vetor = np.array([-3.5, 0, 0])

        vetor = Arrow(
            start=ORIGIN,
            end=np.array([2, 1, 0]),
            buff=0,
            color=BLUE_D
        ).shift(posicao_vetor) # <--- CORREÇÃO 1: Usar .shift() ou .move_to()
        vetor.pf = vetor.copy().move_to([linea.width/4, dashed_line_2.height/4 ,0]) # Copia del vector

        # Texto del vector
        texto_vetor = MathTex(
            r"\vec{v}", # <-- MathTex separa por chunks. \vec{v} é o chunk [0]
            r"\:\text{é um }",r"1\text{-blade}",
            color=BLACK
        ).next_to(vetor, RIGHT)
        texto_vetor.pf = texto_vetor[2].copy().next_to(vetor.pf,DOWN)

        # 3. Definição do Vetor Negativo (Mobject de DESTINO)
        # O destino da transformação deve ter a mesma estrutura (chunk) ou ser um objeto Tex/MathTex válido.
        # Para Transformar texto em texto, o ideal é que seja apenas MathTex.
        menos_vetor_mobj = MathTex(r"-\vec{v}", color=BLACK)
        menos_vetor_mobj.next_to(texto_vetor[1],LEFT)
        # Posicionamos o destino fora da tela ou no lugar do alvo (a transformação cuidará do posicionamento)

        # Aparece
        self.play(GrowArrow(vetor), Write(texto_vetor))
        self.next_slide() # Paso de Lamina

        # Siguiente Slide

        # Se transforma
        self.play(
            # A rotação de PI (180 graus) deve ser feita usando .rotate().
            vetor.animate.rotate(PI), # <--- CORREÇÃO 2: Rotação em torno do ponto de origem do vetor

            # Transformar o primeiro chunk do texto (vetor v) para o novo Mobject (-\vec{v})
            Transform(texto_vetor[0], menos_vetor_mobj) # <--- CORREÇÃO 3: Renomeada para evitar confusão.
        )
        # Desaparece el vector
        self.next_slide() # Paso de Lamina
        self.play(Uncreate(menos_vetor_mobj),Uncreate(texto_vetor),FadeOut(vetor))

        # === === === === === === === === === === 2 - blade (Inicial) === === === === === === === === === ===
        # Animacion del 2-blade

        v1 = np.array([2, 1, 0])
        v2 = np.array([1, 2, 0])

        v_1 = Arrow(ORIGIN, v1, color=BLUE_D, buff=0)
        v_2 = Arrow(ORIGIN, v2, color=BLUE_D, buff=0)


        # Calcular los puntos del paralelogramo
        p0 = ORIGIN
        p1 = v1
        p2 = v1 + v2
        p3 = v2

        area = Polygon(p0, p1, p2, p3, color=BLUE, fill_opacity=0.15)

        grupo_area = VGroup(area,v_1,v_2).scale(1.3).move_to(LEFT*2)
        grupo_area.pf = grupo_area.copy().move_to([-linea.width/4, -dashed_line_2.height/4 ,0]).scale(0.5)

        texto_area = MathTex(
            r"v_1 \wedge v_2",r"\:\text{é um }", r"2\text{-blade}",
            color=BLACK
        )
        texto_area.next_to(v_1, 3*RIGHT + UP)
        texto_area.pf = texto_area[2].copy().next_to(grupo_area.pf,DOWN)

        # Vetores al contrario

        menos_bi_vetor = MathTex(r"-(v_2\wedge v_1) ",color=BLACK)
        menos_bi_vetor.move_to(texto_area.get_center()+np.array([-1,0,0]))

        self.play(GrowArrow(v_1),GrowArrow(v_2),Write(texto_area),run_time =3 )
        self.play(FadeIn(area))
        self.next_slide() # Paso de Lamina

        # Alcontrario

        self.play(grupo_area.animate.rotate(PI),
                  texto_area[1].animate.shift(RIGHT),
                  texto_area[2].animate.shift(RIGHT),
                  Transform(texto_area[0],menos_bi_vetor)
                  )
        self.next_slide() # Paso de Lamina
        # Borrar Cosas  del bi-vector

        self.play(FadeOut(grupo_area), FadeOut(texto_area))


        # === === === === === === === === === === 3 - blade (Inicial) === === === === === === === === === ===
        # vetores del paralelepipedo

        flecha1 = Arrow(np.array([-1, 0, 0]), np.array([3,0,0]), buff=0, color=BLUE_D)
        flecha2 = Arrow(np.array([-1, 0, 0]), np.array([-2, -1, 0]), buff=0, color=BLUE_D)
        flecha3 = Arrow(np.array([-1, 0, 0]), np.array([0, 2, 0]), buff=0, color=BLUE_D)

        paralelepipedo = VGroup(flecha1,flecha2,flecha3)

        # Caras del paralelepipedo

        # Cara de Abajo

        cara_aba = Polygon([-1,0,0], [-2, -1, 0], [2,-1, 0], [3,0, 0],
                       fill_opacity=0.15, color=BLUE_D)

        # Cara Izquierde

        cara_izq = Polygon([-1,0,0], [-2, -1, 0], [-1, 1, 0], [0, 2, 0],
                       fill_opacity=0.15, color=BLUE_D)

        # Cara derecha

        cara_dere = cara_izq.copy().set_color(BLUE_D)
        cara_dere.shift(4*RIGHT)

        # Cara de Arriba

        cara_arri = cara_aba.copy().set_color(BLUE_D)
        cara_arri.shift(2*UP+RIGHT)

        # Cara Frontal

        cara_fron = Polygon([-2,-1,0], [-1, 1, 0], [3,1, 0], [2,-1, 0],
                       fill_opacity=0.15, color=BLUE_D)

        # Cara trasera

        cara_tras = cara_fron.copy().set_color(BLUE_D)
        cara_tras.shift(UP+RIGHT)

        # Todas las caras

        caras_todas = VGroup(cara_izq,cara_dere,cara_aba,cara_arri,cara_tras,cara_fron)
        casi_todas_caras = VGroup(cara_izq,cara_dere,cara_arri,cara_tras,cara_fron)

        # Todo el beta

        blade3_todo = VGroup(caras_todas,paralelepipedo).shift(4*LEFT)
        blade3_todo.pf = blade3_todo.copy().move_to([linea.width/4, - dashed_line_2.height/4 ,0]).scale(0.5)

        texto_volume = MathTex(
            r"v_1 \wedge v_2 \wedge v_3", r"\:\text{é um }", r"3\text{-blade}",
            color=BLACK
            )
        texto_volume.next_to(blade3_todo, RIGHT)
        texto_volume.pf = texto_volume[2].copy().next_to(blade3_todo.pf,DOWN)

        menos_tri_vetor = MathTex(r"-(v_2 \wedge v_1 \wedge v_3) ",color=BLACK)
        menos_tri_vetor.move_to(texto_volume.get_center()+np.array([-1,0,0]))

        self.play(GrowArrow(flecha1),GrowArrow(flecha2))#,GrowArrow(flecha3))
        self.play(Create(cara_aba))
        self.next_slide() # Paso de Lamina
 
        self.play(GrowArrow(flecha3)) 
        self.next_slide() # Paso de Lamina

        self.play(FadeIn(casi_todas_caras))
        self.play(Write(texto_volume))
        self.next_slide() # Paso de Lamina

        self.play(blade3_todo.animate.rotate(PI), texto_volume[1].animate.shift(RIGHT),texto_volume[2].animate.shift(RIGHT),Transform(texto_volume[0],menos_tri_vetor))

        self.next_slide() # Paso de Lamina
        self.play(FadeOut(blade3_todo),FadeOut(texto_volume))
        self.next_slide() # Paso de Lamina 
        # Aparecen las lineas que dividen el plano
        self.play(Write(dashed_line_1),Write(dashed_line_2))
        self.next_slide() # Paso de Lamina


        # === === === === === === === === === === Blades (Final) === === === === === === === === === ===
        self.play(Write(ponto.pf),Write(texto_ponto.pf))
        self.play(Write(vetor.pf),Write(texto_vetor.pf))
        self.play(Write(texto_area.pf) ,Write(grupo_area.pf))
        self.play(Write(blade3_todo.pf),FadeIn(texto_volume.pf))
        self.next_slide() # Paso de Lamina

        # Desaparecen los elementos
        self.play(FadeOut(dashed_line_1),FadeOut(dashed_line_2),
                  Unwrite(ponto.pf),Unwrite(texto_ponto.pf),
                  Unwrite(vetor.pf),Unwrite(texto_vetor.pf),
                  Unwrite(texto_area.pf),Unwrite(grupo_area.pf),
                  Unwrite(blade3_todo.pf),Unwrite(texto_volume.pf)
                  )

        # Desaparece el texto del título más el cursor
        self.play(Unwrite(r3))
        self.play(UntypeWithCursor(text, cursor))

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
class lamina_5(Slide):
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
