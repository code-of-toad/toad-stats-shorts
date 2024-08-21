from manim import *
from math import cos, sin
"""
Uncomment the next 4 lines for vertical resolution.
"""
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9.0
config.frame_height = 16.0


class RosePattern(VMobject):
    _radius: float
    _k:      float
    def __init__(self, radius=2, k=3, **kwargs):
        super().__init__(**kwargs)
        self._radius = radius
        self._k = k
        step_size = 0.05
        theta = np.arange(0, TAU + step_size, step_size)
        pts = [
            [radius * cos(k * t) * cos(t),
             radius * cos(k * t) * sin(t),
             0] for t in theta
        ]
        self.set_points_smoothly(pts)

def get_rose_pattern(k, colors=[BLUE, WHITE]):
    return RosePattern(radius=3, k=k, stroke_width=7).set_color_by_gradient(colors)

class ShowRosePattern(Scene):

    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        self._config(grid=False, screen_border=False)#, bg_color=BLACK)
        # ---------------------------------------------------------------------
        rose = RosePattern(radius=3, k=0, stroke_width=7)
        rose.set_color_by_gradient([BLUE, WHITE])
        # ---------------------------------------------------------------------
        param_eqn_1 = MathTex(r'x = a \cos(k*\theta) \cos(\theta)',
                              substrings_to_isolate=['x', 'a', r'\cos', 'k', r'\theta'])
        param_eqn_1.set_color_by_tex_to_color_map({
            'a': RED,
            'k': BLUE,
            r'\theta': PURPLE,
        })
        param_eqn_1.shift(UP*5.2).scale(1.5)
        # ---------------------------------------------------------------------
        param_eqn_2 = MathTex(r'y = a \cos(k*\theta) \sin(\theta)',
                              substrings_to_isolate=['x', 'a', r'\cos', r'\sin', 'k', r'\theta'])
        param_eqn_2.set_color_by_tex_to_color_map({
            'a': RED,
            'k': BLUE,
            r'\theta': PURPLE,
        })
        param_eqn_2.move_to(param_eqn_1, DOWN).shift(DOWN*0.75).scale(1.5)
        # ---------------------------------------------------------------------
        polar_eqn = MathTex(r'r = a \cos(k*\theta)',
                              substrings_to_isolate=['r', 'a', r'\cos', 'k', r'\theta'])
        polar_eqn.set_color_by_tex_to_color_map({
            'a': RED,
            'k': BLUE,
            r'\theta': PURPLE,
        })
        polar_eqn.shift(DOWN*4.1).scale(1.5)
        # ---------------------------------------------------------------------
        self.play(FadeIn(rose), FadeIn(param_eqn_1), FadeIn(param_eqn_2), FadeIn(polar_eqn))

        k_value = ValueTracker(1)

        def update_eqn_1(eq):
            eq.become(MathTex(
                r'x = a \cos(' + str(round(k_value.get_value())) + r'*\theta) \cos(\theta)',
                substrings_to_isolate=['x', 'a', r'\cos', str(round(k_value.get_value())), r'\theta']
            ).set_color_by_tex_to_color_map({
                'a': RED,
                str(round(k_value.get_value())): BLUE,
                r'\theta': PURPLE,
            }).move_to(param_eqn_1).scale(1.5))

        def update_eqn_2(eq):
            eq.become(MathTex(
                r'y = a \cos(' + str(round(k_value.get_value())) + r'*\theta) \sin(\theta)',
                substrings_to_isolate=['x', 'a', r'\cos', r'\sin', str(round(k_value.get_value())), r'\theta']
            ).set_color_by_tex_to_color_map({
                'a': RED,
                str(round(k_value.get_value())): BLUE,
                r'\theta': PURPLE,
            }).move_to(param_eqn_2).scale(1.5))

        def update_polar_eqn(eq):
            eq.become(MathTex(
                r'r = a \cos(' + str(round(k_value.get_value())) + r'*\theta)',
                substrings_to_isolate=['x', 'a', r'\cos', str(round(k_value.get_value())), r'\theta']
            ).set_color_by_tex_to_color_map({
                'a': RED,
                str(round(k_value.get_value())): BLUE,
                r'\theta': PURPLE,
            }).move_to(polar_eqn).scale(1.5))

        param_eqn_1.add_updater(update_eqn_1)
        param_eqn_2.add_updater(update_eqn_2)
        polar_eqn.add_updater(update_polar_eqn)

        k_increment = 1

        for k in np.arange(1, 11, k_increment):
            self.play(
                k_value.animate.set_value(k),
                rose.animate.become(get_rose_pattern(k)),
                run_time=k_increment
            )
        rose_original = RosePattern(radius=3, k=0, stroke_width=7)
        rose_original.set_color_by_gradient([BLUE, WHITE])
        self.play(FadeOut(param_eqn_1), FadeOut(param_eqn_2), FadeOut(polar_eqn), lag_ratio=0.3)
        self.play(ReplacementTransform(rose, rose_original), run_time=2)
        self.play(FadeOut(rose_original))


    def _config(self, bg_color='#131313', grid=True, screen_border=False):
        self.camera.background_color = bg_color
        if grid:
            self.add(NumberPlane(
                x_range=[-config.frame_width/2,  config.frame_width/2,  1],
                y_range=[-config.frame_height/2, config.frame_height/2, 1],
                background_line_style={
                    "stroke_color": WHITE, "stroke_width": 1, "stroke_opacity": 0.0
                },
                axis_config={
                    "stroke_color": WHITE, "stroke_width": 2, "stroke_opacity": 0.9
                }
            ))
        if screen_border:
            self.add(Rectangle(
                width =config.frame_width,
                height=config.frame_height,
                stroke_color=GREEN,
                stroke_width=20
            ))

