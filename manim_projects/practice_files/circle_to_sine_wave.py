from manim import *

"""
Uncomment the next 4 lines for vertical resolution.
"""
# config.pixel_width  = 1080
# config.pixel_height = 1920
# config.frame_width  = 4.5
# config.frame_height = 8.0

class CircleToSineWave(Scene):
    def construct(self):
        # ------------------------------ CONFIG -------------------------------
        self._config(bg_color=BLACK, grid=False)
        # ---------------------------------------------------------------------
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()
    
    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end   = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end   = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self._add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start  = np.array([-3,0,0])

    def _add_x_labels(self):
        x_labels = [
            MathTex('\pi'), MathTex('2 \pi'), 
            MathTex('3 \pi'), MathTex('4 \pi'), 
        ]
        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circ = Circle(radius=1)
        circ.move_to(self.origin_point)
        self.add(circ)
        self.circ = circ

    def move_dot_and_draw_curve(self):
        orbit = self.circ
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def __go_around_circle(mobj, dt):
            self.t_offset += (dt * rate)
            mobj.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def __get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def __get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2)

        self.curve = VGroup()
        self.curve.add(Line(self.curve_start, self.curve_start))
        def __get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(), np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)
            return self.curve

        dot.add_updater(__go_around_circle)

        origin_to_circle_line = always_redraw(__get_line_to_circle)
        dot_to_curve_line     = always_redraw(__get_line_to_curve)
        sine_curve_line       = always_redraw(__get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(__go_around_circle)


    def _config(self, bg_color='#131313', grid=True):
        self.camera.background_color = bg_color
        if grid:
            self.add(NumberPlane(
                background_line_style={
                    "stroke_color": WHITE, "stroke_width": 1, "stroke_opacity": 0.1
                },
                axis_config={
                    "stroke_color": WHITE, "stroke_width": 1, "stroke_opacity": 0.1
                }
            ))

