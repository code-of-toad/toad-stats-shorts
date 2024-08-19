from manim import *

"""
Uncomment the next 4 lines for vertical resolution.
"""
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9.0
config.frame_height = 16.0

class idk(Scene):
    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        self._config()
        # ---------------------------------------------------------------------
        # 1. Create axes w/ labels.
        axes = Axes(
            # tips=False,  # Show arrow tips on the axes
            x_range=[-3, 3, 1],  # x-axis range w/ tick spacing
            y_range=[-2, 2, 1],  # y-axis range w/ tick spacing
            x_length=6,
            y_length=4,
            axis_config={
                'color': BLUE,  # axis color
                'include_numbers': True
            },
        )
        # 2. Add labels to the axes.
        # 3. Define the function to plot (e.g., a quadratic function).
        # 4. Create a label for the graph.
        # 5. Add everything to the scene.
        self.play(Create(axes), run_time=0.2)
        self.wait()


    def _config(self, bg_color='#131313', grid=True):
        self.camera.background_color = bg_color
        if grid:
            self.add(NumberPlane(
                x_length=config.frame_width,
                x_length=config.frame_height,
                background_line_style={
                    "stroke_color": WHITE, "stroke_width": 1, "stroke_opacity": 0.1
                },
                axis_config={
                    "stroke_color": WHITE, "stroke_width": 1, "stroke_opacity": 0.1
                }
            ))

