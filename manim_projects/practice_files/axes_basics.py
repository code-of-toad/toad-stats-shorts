from manim import *
from numpy import sin, cos
"""
Uncomment the next 4 lines for vertical resolution.
"""
# config.pixel_width  = 1080
# config.pixel_height = 1920
# config.frame_width  = 9.0
# config.frame_height = 16.0


class ToadScene(Scene):
    def play(self, *args, **kwargs):
        defaults = { 
            'run_time':  0.75,
            # 'lag_ratio': 0.0,
            'rate_func': smooth,
        }
        for parameter, new_default in defaults.items():
            kwargs.setdefault(parameter, new_default)
        super().play(*args, **kwargs)


class AxesBasics(ToadScene):
    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        self._config(grid=1, screen_border=0)
        # ---------------------------------------------------------------------
        ax = Axes(
            x_range=[-2*PI, 2*PI, PI/4],
            y_range=[-2, 2, 1],
            x_length=4*PI,
            y_length=4,
            axis_config={
                'unit_size': PI/14,

                'include_numbers': False,
                'font_size': 32,

                'include_tip': True,
                'tip_width':  0.2,
                'tip_height': 0.2,
            },
            x_axis_config={
            },
            y_axis_config={
                'numbers_to_include': [-1, 1],
            }
        )
        ax.get_x_axis().add_labels(
            {-2*PI:   r'$-2\pi$',
             -7*PI/4: r'$-\frac{7\pi}{4}$',
             -3*PI/2: r'$-\frac{3\pi}{2}$',
             -5*PI/4: r'$-\frac{5\pi}{4}$',
               -PI:   r'$-\pi$',
             -3*PI/4: r'$-\frac{3\pi}{4}$',
               -PI/2: r'$-\frac{\pi}{2}$',
               -PI/4: r'$-\frac{\pi}{4}$',
             # 0: r'$0$',
               PI/4: r'$\frac{\pi}{4}$',
               PI/2: r'$\frac{\pi}{2}$',
             3*PI/4: r'$\frac{3\pi}{4}$',
               PI:   r'$\pi$',
             5*PI/4: r'$\frac{5\pi}{4}$',
             3*PI/2: r'$\frac{3\pi}{2}$',
             7*PI/4: r'$\frac{7\pi}{4}$',
             2*PI:   r'$2\pi$'}
        )
        ax_labels = ax.get_axis_labels('x', 'f(x)')
        self.play(Create(ax), Write(ax_labels))

        sin_foo = ax.plot(lambda t: sin(t)).set_stroke(color=BLUE)
        cos_foo = ax.plot(lambda t: cos(t)).set_stroke(color=BLUE_B)
        asymp_h = ax.plot(lambda _: 1)     .set_stroke(color=RED, width=2)
        pt = Dot(point=ax.c2p(-PI, 1.5), stroke_width=8, color=RED_C)
        pt_line_h = DashedLine(start=ax.c2p(0, 1.5), end=ax.c2p(-PI, 1.5), dash_length=0.15, color=RED_C)
        pt_line_v = DashedLine(start=ax.c2p(-PI, 0), end=ax.c2p(-PI, 1.5), dash_length=0.15, color=RED_C)

        self.play(Create(pt), Create(pt_line_h), Create(pt_line_v))
        self.play(Create(asymp_h))
        self.play(Create(sin_foo))
        self.play(Create(cos_foo))

        graph = VGroup(ax, ax_labels, sin_foo, cos_foo, asymp_h, pt, pt_line_h, pt_line_v)
        self.play(graph.animate.scale(0.75))
        self.play(graph.animate.rotate(0.75))

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

