from manim import *
from numpy import sin
"""
Uncomment the next 4 lines for vertical resolution.
"""
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9.0
config.frame_height = 16.0


class ParametricSinCurve(Scene):
    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        self._config(grid=True, screen_border=False)
        # ---------------------------------------------------------------------
        sin_curve = ParametricFunction(
            function=lambda t: [t, sin(t), 0],
            t_range=[-PI, PI, 0.1],
        )
        sin_curve.set_color(YELLOW)
        self.play(Create(sin_curve))

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

