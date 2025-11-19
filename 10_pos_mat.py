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
        self.add(titulo,creditos,rect1)
        
        self.next_slide() # Proxima Slide 

        # Animación de Salida: usando Unwrite (desescritura) y FadeOut
        self.play(
           FadeOut(creditos,shift=DOWN),
           Unwrite(titulo,shift=DOWN),
           Uncreate(rect1,shift=DOWN), 
        )

##################################################### Lamina 1 #####################################################

class lamina_1(Scene):
    def construct(self):
        # Define a cor de fundo 
        self.camera.background_color = WHITE
        # Plantilla LaTeX para justificación (si se necesita)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        # Adicionar Linea de la cabecera 
        linea = Line(np.array([-6.5, 3, 0]), np.array([6.5, 3, 0]), color=BLUE_D, stroke_width=0.7)
        self.add(linea)
        ############################## Titulo de la Lamina #######################
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
        self.play(Blink(cursor, blinks=1))
        ############################ Cuerpo de la Presentación #######################################


        texto = Tex(r"""A álgebra exterior de Grassmann com base em um espaço vetorial $\textmd{V}$ sobre $\mathbb{R}$, é o espaço $\bigwedge \textmd{V}$ que se descompõe como
        \[
        \bigwedge \textmd{V}=\bigoplus_{p=0}^n \bigwedge^p \textmd{V} = \mathbb{R} \oplus \textmd{V} \oplus \bigwedge^2 \textmd{V}\oplus \cdots \oplus \bigwedge^p \textmd{V}
        \]
        com um produto exterior bilinear e associativo
        \[
        \wedge: \bigwedge^p \mathbb{R}^n\times\bigwedge^q \mathbb{R}^n \rightarrow\bigwedge^{p+q} \mathbb{R}^n
        \]  
        este produto é alternante,
        \[
        \textmd{A} \wedge \textmd{B} =(-1)^{pq}\left(\textmd{B}\wedge \textmd{A}\right) \quad \text{se} \quad \textmd{A} \in \bigwedge^{p}\: \mathbb{R}^{n} \: \text{e} \: \textmd{B} \in \bigwedge^{q}\: \mathbb{R}^{n}
        \]""",
                tex_template=myTemplate,
             tex_environment="justify",
                       color=BLACK,
                   font_size=35).next_to(linea,DOWN)
        self.play(FadeIn(texto))

        self.next_slide() # Proxima Slide  
        
        ################### Ultima Parte #####################

        self.play(FadeOut(texto))
        # self.play(UntypeWithCursor(text, cursor)) # Se va a quitar en la siguiente pagina 

##################################################### Lamina 2 #####################################################







