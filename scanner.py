class VPDScanner():
    # Define printer's bed volume limits
    X_MIN = 0
    Y_MIN = 0
    Z_MIN = 0
    
    X_MAX = 235
    Y_MAX = 235
    Z_MAX = 250

    # Define printer's rapid velocities (mm/min)
    XY_RAPID_VELOCITY = 15000
    Z_RAPID_VELOCITY = 500

    # Define printer's safe travel heights (mm)
    TRAVEL_HEIGHT = 35
    CUVETTE_HOLDER_HEIGHT = 30

    # Define printer's cuvette coordinates (mm)
    ASPIRATE_CUVETTE_X = 29
    ASPIRATE_CUVETTE_Y = 50
    ASPIRATE_CUVETTE_Z = 4

    DISPENSE_CUVETTE_X = 190
    DISPENSE_CUVETTE_Y = 50

    # Define wafer center coordinates (mm)
    WAFER_CENTER_X = 110.20
    WAFER_CENTER_Y = 129.30

    # Define printer's extruder parameters
    SYRINGE_CAPACITY = 1.0
    SYRINGE_LENGTH = 58.0
    RACK_TEETH_PER_MM = 0.636619
    GEAR_TEETH = 30
    EXTRUSION_MOTOR_FEEDRATE = 5 # mL/min. Used for extruder feedrate
    EXTRUSION_MOTOR_STEPS_PER_REV = 3200
    EXTRUSION_MOTOR_STEPS_PER_MM = EXTRUSION_MOTOR_STEPS_PER_REV * (1/GEAR_TEETH) * RACK_TEETH_PER_MM # mm
    EXTRUSION_MOTOR_STEPS_PER_ML = EXTRUSION_MOTOR_STEPS_PER_MM * (SYRINGE_LENGTH/SYRINGE_CAPACITY) # mL

    def __init__(self, droplet_volume, wipe_speed, wipe_height, wafer_size):
        self.master_command_list = [] # list that holds all GCODE commands

        self.droplet_volume = droplet_volume # define droplet volume
        self.wipe_speed = wipe_speed # define speed which droplet will be wiped across wafer surface
        self.wipe_height = wipe_height # define height above wafer surface syringe will wipe
        self.wafer_size = wafer_size # diameter of wafer to be tested

        self.DROPLET_DIAMETER = 3 # width (mm) of droplet dispensed

    def header(self):
        """
        Standard header to initialize the printer. Appends appropriate G-CODE commands to 
        the master_command_list. Include this at the beginning of every G-CODE file.
        """

        self.master_command_list.append("; BEGIN HEADER")
        self.master_command_list.append("G21 ; set units to mm")
        self.master_command_list.append("G90 ; absolute coordinates for X,Y,Z, and E")
        self.master_command_list.append("M302 S0; always allow extrusion (disable temp/length checking)")
        self.master_command_list.append(f"M92 E{self.EXTRUSION_MOTOR_STEPS_PER_ML//1} ; set extruder steps per mL")
        self.master_command_list.append("G28 ; home all axes")
        self.master_command_list.append("G92 X0 Y0 Z0 E0 ; zero all axes")
    
    def aspirate_from_cuvette(self):
        """
        Aspirates given volume of solution from left cuvette.

        Initialization:
            Tip can start anywhere. No solution within the syringe.
        
        Termination:
            Tip finishes above aspirate cuvette, at a safe travel height. Solution of volume droplet_volume is within the syringe.
        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN ASPIRATE")

        # Move just above aspirate cuvette
        self.master_command_list.append(f"G0 Z{self.TRAVEL_HEIGHT} F{self.Z_RAPID_VELOCITY} ; move to safe travel height")
        self.master_command_list.append(f"G0 X{self.ASPIRATE_CUVETTE_X} Y{self.ASPIRATE_CUVETTE_Y} F{self.XY_RAPID_VELOCITY} ; move high above aspirate cuvette")
        self.master_command_list.append(f"G0 Z{self.CUVETTE_HOLDER_HEIGHT} F{self.Z_RAPID_VELOCITY} ; lower to cuvette holder height")

        # Cycle the syringe in air to remove bubbles
        self.master_command_list.append(f"G1 E0.2 F{self.EXTRUSION_MOTOR_FEEDRATE} ; withdraw 0.2 mL of air")
        self.master_command_list.append(f"G1 E0 F{self.EXTRUSION_MOTOR_FEEDRATE} ; return to 0 mL")

        # Withdraw solution
        self.master_command_list.append(f"G0 Z{self.ASPIRATE_CUVETTE_Z} F{self.Z_RAPID_VELOCITY} ; plunge into aspirate cuvette")
        self.master_command_list.append(f"G1 E{self.droplet_volume} F{self.EXTRUSION_MOTOR_FEEDRATE} ; aspirate solution")
        self.master_command_list.append(f"G1 E0 F{self.EXTRUSION_MOTOR_FEEDRATE} ; dispense solution")
        self.master_command_list.append(f"G1 E{self.droplet_volume} F{self.EXTRUSION_MOTOR_FEEDRATE} ; aspirate solution")
        self.master_command_list.append(f"G0 Z{self.CUVETTE_HOLDER_HEIGHT} F{self.Z_RAPID_VELOCITY} ; raise to cuvette holder height")
        self.master_command_list.append(f"G0 Z{self.TRAVEL_HEIGHT} F{self.Z_RAPID_VELOCITY} ; move to safe travel height")

    def center(self):
        """
        Center the syringe above the wafer at wipe_height.

        Initialization:
            Tip can start anywhere.
        
        Termination:
            Tip finishes above wafer center, at wipe_height.

        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN CENTER")

        self.master_command_list.append(f"G0 Z{self.TRAVEL_HEIGHT} F{self.Z_RAPID_VELOCITY} ; move to safe travel height")
        self.master_command_list.append(f"G0 X{self.WAFER_CENTER_X} Y{self.WAFER_CENTER_Y} F{self.XY_RAPID_VELOCITY} ; move high above wafer center")
        self.master_command_list.append(f"G0 Z{self.wipe_height} F{self.Z_RAPID_VELOCITY} ; lower to wipe height")

    def circle(self, radius):
        """
        Wipes a circle of given radius on the wafer.

        Initialization:
            Tip begins above center of circle, at wipe_height. All solution is within the syringe.
        
        Termination:
            Tip finishes above center of circle, at wipe_height. Droplet is still on the wafer.
        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN CIRCLE")
        
        self.master_command_list.append("G91 ; set relative coordinates")
        self.master_command_list.append("M82 ; set extruder to absolute coordinates")
        self.master_command_list.append(f"G0 X{radius} F{self.XY_RAPID_VELOCITY} ; move to circle circumference")
        self.master_command_list.append(f"G1 E0 F{self.EXTRUSION_MOTOR_FEEDRATE} ; extrude droplet")
        self.master_command_list.append(f"G2 I-{radius} F{self.wipe_speed} ; wipe a clockwise circle")
        self.master_command_list.append(f"G1 X-{radius} F{self.wipe_speed} ; return to center of circle")
        self.master_command_list.append("G90 ; set absolute coordinates")
    
    def scan_wafer(self):
        """
        Scans the wafer with a series of concentric circles. 
        
        Initialization:
            Assumes tip begins above center of the wafer, at wipe_height. All solution is within the syringe.
        
        Termination:
            Tip finishes above center of the wafer, at wipe_height. Droplet is still on the wafer.
        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN SCAN WAFER")

        wipe_radius = self.DROPLET_DIAMETER/2 # radius of first circle 
        max_wipe_radius = self.wafer_size/2 - (self.DROPLET_DIAMETER/2 + 5) # radius of largest circle. include 5mm buffer from edge

        # Move to and complete first circle
        self.master_command_list.append("G91 ; set relative coordinates")
        self.master_command_list.append("M82 ; set extruder to absolute coordinates")
        self.master_command_list.append(f"G0 X{wipe_radius} F{self.XY_RAPID_VELOCITY} ; move to beginning of first circle")
        self.master_command_list.append(f"G1 E0 F{self.EXTRUSION_MOTOR_FEEDRATE} ; extrude droplet")
        self.master_command_list.append(f"G2 I-{wipe_radius} F{self.wipe_speed} ; wipe a clockwise circle")

        # Wipe concentric circles
        while wipe_radius + self.DROPLET_DIAMETER < max_wipe_radius:
            self.master_command_list.append(f"G1 X{self.DROPLET_DIAMETER} F{self.wipe_speed} ; move to next circle circumnference")
            wipe_radius += self.DROPLET_DIAMETER
            self.master_command_list.append(f"G2 I-{wipe_radius} F{self.wipe_speed} ; wipe a clockwise circle")
        
        # Return to wafer center
        self.master_command_list.append("G90 ; set absolute coordinates")
        self.master_command_list.append(f"G1 X{self.WAFER_CENTER_X} Y{self.WAFER_CENTER_Y} F{self.wipe_speed} ; move to wafer center")
    
    def put_down_droplet(self):
        """
        Dispenses the droplet from the syringe onto the surface of the wafer.

        Initialization:
            Tip is anywhere above wafer. All solution is within the syringe. 
        
        Termination:
            Tip remains in the same XY coordinate, moves to wipe_height. Droplet is entirely dispensed onto the wafer surface.
        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN COLLECT DROPLET")

        # Lower closer to wafer surface
        self.master_command_list.append(f"G1 Z{self.wipe_height} F{self.Z_RAPID_VELOCITY} ; lower to wipe height")
        
        # Dispense droplet
        self.master_command_list.append(f"G1 E{0} F{self.EXTRUSION_MOTOR_FEEDRATE} ; dispense droplet")

        
    def pick_up_droplet(self):
        """
        Collects the droplet from the wafer.

        Initialization:
            Tip is anywhere above wafer, at wipe_height. Droplet is on the wafer.
        
        Termination:
            Tip finishes at same location above wafer, at wipe_height. All solution is within the syringe.
        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN COLLECT DROPLET")

        withdraw_volume = self.SYRINGE_CAPACITY
        if 2*self.droplet_volume < withdraw_volume:
            withdraw_volume = 2*self.droplet_volume

        # Lower closer to wafer surface
        self.master_command_list.append(f"G1 Z0.3 F{self.Z_RAPID_VELOCITY} ; lower closer to wafer")

        # Withdraw droplet
        self.master_command_list.append(f"G1 E{withdraw_volume} F{self.EXTRUSION_MOTOR_FEEDRATE/2} ; slowly suck up droplet")
        self.master_command_list.append(f"G0 Z{self.wipe_height} F{self.Z_RAPID_VELOCITY} ; raise to wipe height")    

    def dispense_into_cuvette(self):
        """
        Dispenses the droplet into the dispense cuvette.

        Initialization:
            Tip can start anywhere. All solution is within the syringe.

        Termination:
            Tip finishes above dispense cuvette, at a safe travel height. No solution within the syringe.
        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN DISPENSE")

        # Move just above dispense cuvette
        self.master_command_list.append(f"G0 Z{self.TRAVEL_HEIGHT} F{self.Z_RAPID_VELOCITY} ; move to safe travel height")
        self.master_command_list.append(f"G0 X{self.DISPENSE_CUVETTE_X} Y{self.DISPENSE_CUVETTE_Y} F{self.XY_RAPID_VELOCITY} ; move high above dispense cuvette")
        self.master_command_list.append(f"G0 Z{self.CUVETTE_HOLDER_HEIGHT} F{self.Z_RAPID_VELOCITY} ; lower to cuvette holder height")

        # Dispense solution
        self.master_command_list.append(f"G1 E0 F{self.EXTRUSION_MOTOR_FEEDRATE} ; dispense all solution in syringe")

        # Return to safe travel height
        self.master_command_list.append(f"G0 Z{self.TRAVEL_HEIGHT} F{self.Z_RAPID_VELOCITY} ; move to safe travel height")
    
    def send_to_back_corner(self):
        """
        Sends the syringe to the back corner of the printer bed. Beeps when complete.

        Initialization:
            Tip can start anywhere.

        Termination:
            Tip finishes at back left corner of printer bed, at a safe travel height.
        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN SEND TO BACK CORNER")

        self.master_command_list.append(f"G0 Z{self.TRAVEL_HEIGHT} F{self.Z_RAPID_VELOCITY} ; move to safe travel height")
        self.master_command_list.append(f"G0 X0 Y{self.Y_MAX-50} F{self.XY_RAPID_VELOCITY} ; move to back corner")
        self.master_command_list.append("M400 ; wait for commands to finish")
        self.master_command_list.append("M300 P1000 ; beep")
    
    def write_to_file(self, filename):        
        """
        Save G-CODE commands to file.
        """

        if ".gcode" not in filename:
                filename += ".gcode"

        with open(filename, "w") as file:
            for command in self.master_command_list:
                file.write(f"{command}\n")
    
    def move_to(self, x, y, z):
        """
        Move the syringe to a given position.

        Initialization:
            Tip can start anywhere.
        
        Termination:
            Tip finishes at the coordinates provided.
        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN MOVE TO")

        if x or y:
            self.master_command_list.append(f"G0 Z{self.TRAVEL_HEIGHT} F{self.Z_RAPID_VELOCITY} ; move to safe travel height")
            self.master_command_list.append(f"G0 X{x} Y{y} F{self.XY_RAPID_VELOCITY} ; move above position")
            self.master_command_list.append(f"G0 Z{z} F{self.Z_RAPID_VELOCITY} ; lower to position")
        else:
            self.master_command_list.append(f"G0 Z{z} F{self.Z_RAPID_VELOCITY} ; move up/down to position")
                

    def move(self, **kwargs):
        """
        Move the syringe relative to a given position. If any of the x, y, or z coordinates are not provided, the syringe will not move in that direction.

        Initialization:
            Tip can start anywhere.
        
        Termination:
            Tip finishes at the coordinate(s) provided.
        """
        
        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN MOVE")

        self.master_command_list.append(f"G91 ; set relative coordinates")
        self.master_command_list.append(f"G0 X{kwargs.get('x', 0)} Y{kwargs.get('y', 0)} Z{kwargs.get('z', 0)} F{self.XY_RAPID_VELOCITY}")
        self.master_command_list.append(f"G90 ; set absolute coordinates")
    
    def linear_wipe(self, length):
        """
        Wipes the syringe tip in a straight line of given length mm to the right of the starting position.

        Initialization:
            Tip begins above wafer, at wipe_height. All solution is within the syringe.
        
        Termination:
            Tip finishes length mm to the right of the starting position, at wipe_height. Droplet is still on the wafer.
        """

        self.master_command_list.append("; ")
        self.master_command_list.append("; BEGIN LINEAR WIPE")

        self.master_command_list.append(f"G91 ; set relative coordinates")
        self.master_command_list.append("M82 ; set extruder to absolute coordinates")
        self.master_command_list.append(f"G1 E0 F{self.EXTRUSION_MOTOR_FEEDRATE} ; extrude droplet")
        self.master_command_list.append(f"G1 X{length} F{self.wipe_speed} ; wipe in a straight line")
        self.master_command_list.append("G90 ; set absolute coordinates")

    def insert_gcode(self, gcode_command):
        """
        Insert a custom G-CODE command into the master_command_list.

        Initialization:
            Tip can start anywhere.
        
        Termination:
            Tip finishes wherever you specify, depending on the G-CODE command.
        """

        self.master_command_list.append(gcode_command)