from manim import *
"""
Uncomment the next 4 lines for vertical resolution.
"""
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9.0
config.frame_height = 16.0


class BasicCollision(Scene):
    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        # self._config(grid=True, screen_border=False)
        # ---------------------------------------------------------------------
        width, height = 6, 9
        box = Rectangle(width=width, height=height, stroke_width=6)
        ball = Dot(color=GREEN, radius=0.2, stroke_width=7)
        ball.dx, ball.dy = 0.15, 0.15

        def collision_update(ball):
            pt_right  = ball.get_right()[0]
            pt_left   = ball.get_left()[0]
            pt_top    = ball.get_top()[1]
            pt_bottom = ball.get_bottom()[1]
            if pt_right >= width/2 or pt_left <= -width/2:
                ball.dx *= -1
                self.add_sound('./assets/audio/bop.wav')
            if pt_top >= height/2 or pt_bottom <= -height/2:
                ball.dy *= -1
                self.add_sound('./assets/audio/bop.wav')
            ball.shift(ball.dx*RIGHT, ball.dy*UP)

        self.play(Create(box))
        self.play(Create(ball))
        ball.add_updater(collision_update)
        self.play(UpdateFromFunc(ball, lambda _: None), run_time=10)
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

