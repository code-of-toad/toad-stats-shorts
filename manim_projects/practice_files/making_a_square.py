from manim import *
"""
Uncomment the next 4 lines for vertical resolution.
"""
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9.0
config.frame_height = 16.0


class MakingASquare(Scene):
    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        self._config(grid=True, screen_border=False)
        # ---------------------------------------------------------------------
        pts = [
            [2, 2, 0],
            [-2, 2, 0],
            [-2, -2, 0],
            [2, -2, 0],
            [2, 2, 0],
        ]
        dots = VGroup(*[Dot(p, color=RED_A, stroke_width=9) for p in pts[:-1]])
        sq = VMobject(color=RED, stroke_width=6)
        sq.set_points_as_corners(pts)
        self.play(Create(dots.set_z_index(1)))  # Make the dots appear IN FRONT of the square
        self.play(Create(sq))
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

