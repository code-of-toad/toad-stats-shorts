from manim import *
from math import cos, sin
"""
Uncomment the next 4 lines for vertical resolution.
"""
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9.0
config.frame_height = 16.0


class ToadScene(Scene):
    def play(self, *args, **kwargs):
        defaults = {
            'run_time': 0.5,
        }
        for k, v in defaults.items():
            kwargs.setdefault(k, v)
        super().play(*args, **kwargs)


class LineBasics(ToadScene):
    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        self._config(grid=True, screen_border=False)#, bg_color=BLACK)
        # ---------------------------------------------------------------------
        # s1 = Square(color=RED, fill_opacity=0.3)
        # s2 = Square(color=GREEN, fill_opacity=0.3)
        # s3 = Square(color=BLUE, fill_opacity=0.3)
        # s4 = Square(color=ORANGE, fill_opacity=0.3)
        x_axis = NumberLine(
            x_range=(-6, 6, 1),
            # unit_size=0.75,
            length=9,
            # rotation=PI/16,  # This parameter will RARELY (if ever) be used.

            # include_ticks=False,
            # tick_size=0.5,

            include_numbers=True,
            numbers_to_exclude=[0],
            # numbers_with_elongated_ticks=[n for n in range(-6, 7, 2)],
            label_direction=DOWN,
            font_size=22,
            # decimal_number_config={'num_decimal_places': 1},
            # line_to_number_buff=0.35,

            include_tip=True,
            tip_width=0.2,
            tip_height=0.2,
        )
        self.play(Create(x_axis))
        """
        Now, suppose that you want to place a dot on the number line at x = -3.
        How can you (or, rather, SHOULD you) do that?
        -----------------------------------------------------------------------
        let dot_green = CORRECTLY placed dot
        let dot_red = INCORRECTLY placed dot

        `NumberLine.n2p()` will return the `Scene` coordinates of the tick of interest.
        """
        dot_green = Dot(color=GREEN, point=x_axis.n2p(-3), stroke_width=8)
        dot_red =   Dot(color=RED,   point=[-3, 0, 0],     stroke_width=8)
        # dot_blue =  Dot(color=BLUE,  point=x_axis.p2n([-3, 0, 0]), stroke_width=8)  # ???
        self.play(Create(dot_green), Create(dot_red))

        self.wait(2)


    def _config(self, bg_color='#131313', grid=True, screen_border=False):
        self.camera.background_color = bg_color
        if grid:
            self.add(NumberPlane(
                x_range=[-config.frame_width/2,  config.frame_width/2,  1],
                y_range=[-config.frame_height/2, config.frame_height/2, 1],
                background_line_style={
                    "stroke_color": WHITE, "stroke_width": 1, "stroke_opacity": 0.2
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

