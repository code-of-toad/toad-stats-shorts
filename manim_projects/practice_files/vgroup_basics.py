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
        self._k      = k
        step_s = 0.05
        theta_domain = np.arange(0, TAU + step_s, step_s)
        pts = [
            [radius * cos(k * theta) * cos(theta),  # x-coord
             radius * cos(k * theta) * sin(theta),  # y-coord
             0  # z-coord
            ] for theta in theta_domain
        ]
        self.set_points_smoothly(pts)


class RosePatternWithParamFunc(ParametricFunction):
    _radius: float
    _k:      float
    def __init__(self, radius=2, k=10, **kwargs):
        self._radius = radius
        self._k      = k
        step_s = 0.05
        super().__init__(
            function=lambda theta: [
                radius * cos(k * theta) * cos(theta),
                radius * cos(k * theta) * sin(theta),
                0
            ],
            t_range=(0, TAU + step_s, step_s),
            **kwargs
        )


class ToadScene(Scene):
    def play(self, *args, **kwargs):
        kwargs = self._override_defaults(**kwargs)
        super().play(*args, **kwargs)
    def _override_defaults(self, **kwargs):
        defaults = {
            'run_time': 0.5,
        }
        for k, v in defaults.items():
            kwargs.setdefault(k, v)
        return kwargs


class Idk(ToadScene):
    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        self._config(grid=True, screen_border=False)#, bg_color=BLACK)
        # ---------------------------------------------------------------------
        s1 = Square(color=RED, fill_opacity=0.3)
        s2 = Square(color=GREEN, fill_opacity=0.3)
        s3 = Square(color=BLUE, fill_opacity=0.3)
        s4 = Square(color=ORANGE, fill_opacity=0.3)
        # hex = RegularPolygon(6, color=WHITE)

        shapes = VGroup()
        shapes.add(s1, s2, s3, s4)
        shapes.scale(0.75)
        self.add(shapes)
        self.wait(0.25)
        shapes.set_stroke(GRAY)
        self.play(shapes.animate.arrange(buff=0))
        self.play(shapes.animate.arrange(LEFT, buff=0))
        self.play(shapes.animate.arrange(UP, buff=0))
        self.play(shapes.animate.arrange(DOWN, buff=0))
        self.play(shapes.animate.arrange(UL, buff=0))
        self.play(shapes.animate.arrange_in_grid(2, 2, buff=0))

        self.wait(2)


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
                    "stroke_color": WHITE, "stroke_width": 1, "stroke_opacity": 0.3
                }
            ))
        if screen_border:
            self.add(Rectangle(
                width =config.frame_width,
                height=config.frame_height,
                stroke_color=GREEN,
                stroke_width=20
            ))

