from manim import *

class Main(MovingCameraScene):
    def fade_all_scene(self):
        self.rec_wrapper = Rectangle(height=self.camera.frame_height, width=self.camera.frame_width, color=BLACK)
        self.rec_wrapper.fill_color = BLACK
        self.rec_wrapper.set_opacity(1)
        self.play(FadeIn(self.rec_wrapper))

    def show_all_scene(self):
        self.play(FadeOut(self.rec_wrapper))

    def greeting(self):
        main_msg = Text("Essência da trigonometria").scale_to_fit_height(
            self.camera.frame_height
        ).scale_to_fit_width(
            self.camera.frame_width
        )
        main_msg.scale(0.7)

        self.play(Write(main_msg))
        self.play(main_msg.animate.scale(0.7))
        self.wait()
        self.play(main_msg.animate.move_to(UP * self.camera.frame_height / 3))
        self.wait()
        self.play(FadeOut(main_msg))

    def plot_function_formula(self):
        formula_rec_wrapper = Rectangle(height=1, width=3, color=BLACK).to_edge(UL)
        formula_rec_wrapper.fill_color = BLACK
        formula_rec_wrapper.set_opacity(1)
        function_formula = Tex("$f(x)=x$")

        function_formula.move_to(formula_rec_wrapper.get_center())

        self.add(VGroup(formula_rec_wrapper, function_formula))

        self.play(Create(formula_rec_wrapper), Write(function_formula))

    def plot_main_scene(self):
        default_scene_width = self.camera.frame_width
        default_scene_height = self.camera.frame_height

        main_plane = NumberPlane(faded_line_ratio=2,background_line_style={"stroke_opacity": 1, "stroke_width": 2.5})
        background_plane = NumberPlane(faded_line_ratio=2, background_line_style={"stroke_color": GREY, "stroke_width": 2}, faded_line_style={"stroke_width": 2})
        background_plane.set_opacity(0.3)

        main_line = main_plane.plot(lambda x: x, color=YELLOW)

        function_x_comp = Line(start= main_plane.c2p(0, 0, 0), end=main_plane.c2p(3, 0, 0), color=RED)
        function_y_comp = Line(start=main_plane.c2p(3, 0, 0), end=main_plane.c2p(3, 3, 0), color=GREEN)

        x_comp_brace = Brace(function_x_comp, DOWN, buff=0.01).scale(1)
        x_comp_brace_label = x_comp_brace.get_tex("3").scale(1).next_to(x_comp_brace, DOWN, buff=0.05)

        y_comp_brace = Brace(function_y_comp, RIGHT, buff=0.03).scale(1)
        y_comp_brace_label = y_comp_brace.get_tex("3").scale(1).next_to(y_comp_brace, RIGHT, buff=0.05)

        main_scene_frame = VGroup(main_plane ,background_plane, main_line)
        self.camera.frame.save_state()
        self.play(Create(main_scene_frame))
        self.plot_function_formula()

        self.wait()

        self.play(Create(function_x_comp), Create(function_y_comp))
        self.play(Write(x_comp_brace), Write(x_comp_brace_label))
        self.play(Write(y_comp_brace), Write(y_comp_brace_label))

        #self.play(self.camera.frame.animate.restore())



    def construct(self):
        self.greeting()
        #self.plot_main_scene()
        #self.fade_all_scene()
        self.wait(2)
        #self.show_all_scene()