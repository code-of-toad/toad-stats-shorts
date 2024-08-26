from manim import *
from manim.utils.simple_functions import lru_cache
"""
Uncomment the next 4 lines for vertical resolution.
"""
# config.pixel_width  = 1080
# config.pixel_height = 1920
# config.frame_width  = 9.0
# config.frame_height = 16.0


class ToadScene(Scene):
    def play(self, *args, **kwargs):
        """
        CUSTOM OVERRIDE:
        ----------------
        Applies default values for animation parameters if they are not explicitly provided.
        
        `self.play()` Parameter Defaults:
        ---------------------------------
        run_time:  1.0     ->  [0.0, inf)
        lag_ratio: 0.0     ->  [0.0, 1.0]
        rate_func: smooth  ->  {smooth, linear, rush_into, rush_from, there_and_back_with_pause}
        """
        defaults = { 
            'run_time':  0.6,
            'lag_ratio': 0.0,
            'rate_func': smooth,
        }
        for parameter, new_default in defaults.items():
            kwargs.setdefault(parameter, new_default)
        super().play(*args, **kwargs)


class UpdaterAnimations(ToadScene):
    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        self._config(grid=True, screen_border=False)
        # ---------------------------------------------------------------------
        r = ValueTracker(0.5)  # tracks the radius value

        txt = always_redraw(
            lambda: Tex(rf'radius={round(r.get_value(), 2)}').to_corner(UL)
        )
        c = always_redraw(
            lambda: Circle(color=YELLOW, radius=r.get_value())
        )
        line_radius = always_redraw(
            lambda: Line(color=RED, stroke_width=10, start=c.get_center(), end=c.get_bottom())
        )
        line_circumference = always_redraw(
            lambda: Line(color=YELLOW, stroke_width=5).set_length(2*PI*r.get_value()).next_to(c, DOWN, buff=0.2)
        )
        t = always_redraw(
            lambda: Polygon(c.get_top(), c.get_left(), c.get_right())
        )

        self.add(txt)
        self.play(Create(c))
        self.play(DrawBorderThenFill(line_radius))
        self.play(DrawBorderThenFill(t))
        self.play(ReplacementTransform(c.copy(), line_circumference), run_time=1)
        self.play(r.animate.set_value(2), run_time=2)

        self.wait()
        

    def _config(self, bg_color='#131313', grid=True, screen_border=False):
        self.camera.background_color = bg_color
        if grid:
            self.add(NumberPlane(
                x_range=[-config.frame_width/2,  config.frame_width/2,  1],
                y_range=[-config.frame_height/2, config.frame_height/2, 1],
                background_line_style={
                    "stroke_color": WHITE, "stroke_width": 1, "stroke_opacity": 0.1
                },
                axis_config={
                    "stroke_color": WHITE, "stroke_width": 1, "stroke_opacity": 0.1
                }
            ))
        if screen_border:
            self.add(Rectangle(
                width =config.frame_width,
                height=config.frame_height,
                stroke_color=GREEN,
                stroke_width=20
            ))

