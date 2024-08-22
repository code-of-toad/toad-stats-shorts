from manim import *
from numpy import random
"""
Uncomment the next 4 lines for vertical resolution.
"""
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9.0
config.frame_height = 16.0


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
            'run_time':  0.3,
            'lag_ratio': 0.0,
            'rate_func': smooth,
        }
        for parameter, new_default in defaults.items():
            kwargs.setdefault(parameter, new_default)
        super().play(*args, **kwargs)


class MmmDonut(ThreeDScene):
    def construct(self):
        self.camera.background_color = '#131313'
        # Set up the camera orientation with a slightly higher angle
        self.set_camera_orientation(phi=50 * DEGREES, theta=-45 * DEGREES)

        # Create a larger torus (the donut)
        torus = Torus(major_radius=2.25, minor_radius=1.35, resolution=(24, 32))
        
        # Apply a gradient by interpolating colors from blue to dark blue
        torus.set_fill(YELLOW_B, opacity=1)
        for submobject in torus.family_members_with_points():
            submobject.set_fill(interpolate_color(YELLOW_B, YELLOW_E, submobject.get_center()[2] / 2))

        torus.set_stroke(WHITE, width=0.5)

        # Add the torus to the scene
        self.add(torus)

        # Function to create a sprinkle
        def create_sprinkle():
            length = 0.1
            radius = 0.05
            sprinkle = Cylinder(radius=radius, height=length, resolution=12)
            sprinkle.set_fill(random.choice([RED, GREEN, YELLOW, PINK, ORANGE]), opacity=1)
            sprinkle.rotate(random.uniform(0, TAU), axis=OUT)
            sprinkle.rotate(random.uniform(0, TAU), axis=RIGHT)
            sprinkle.rotate(random.uniform(0, TAU), axis=UP)
            return sprinkle

        # Add sprinkles on the surface of the torus
        num_sprinkles = 250
        for _ in range(num_sprinkles):
            sprinkle = create_sprinkle()

            # Position the sprinkle randomly on the upper half of the torus surface
            while True:
                u = random.uniform(0, 1)
                v = random.uniform(0, 1)
                theta = u * TAU
                phi = v * TAU
                x = (2.25 + 1.35 * np.cos(phi)) * np.cos(theta)
                y = (2.25 + 1.35 * np.cos(phi)) * np.sin(theta)
                z = 1.35 * np.sin(phi)

                # Place sprinkles only on the upper side (z >= 0)
                if z >= 0:
                    sprinkle.move_to(np.array([x, y, z]))
                    self.add(sprinkle)
                    break

        # Rotate the camera around the torus
        self.begin_ambient_camera_rotation(rate=PI/10)  # Rotates the camera continuously
        self.wait(10)  # Duration of the rotation

        # Stop the camera rotation
        self.stop_ambient_camera_rotation()

        # Hold the final frame for a bit
        self.wait(2)


    # def construct2(self):
    #     self.camera.background_color = '#131313'
    #     # Set up the camera orientation
    #     self.set_camera_orientation(phi=125 * DEGREES, theta=-45 * DEGREES)
    #
    #     # Create a torus
    #     torus = Torus(major_radius=2.75, minor_radius=1.25, resolution=(24, 32))
    #     torus.set_fill(YELLOW_B, opacity=0.5)
    #     torus.set_stroke(WHITE, width=0.5)
    #
    #     # Add the torus to the scene
    #     self.add(torus)
    #
    #     # Rotate the camera around the torus
    #     self.begin_ambient_camera_rotation(rate=PI/10)  # Rotates the camera continuously
    #     self.wait(10)  # Duration of the rotation
    #
    #     # Stop the camera rotation
    #     self.stop_ambient_camera_rotation()
    #
    #     # Hold the final frame for a bit
    #     self.wait(2)
    #

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

