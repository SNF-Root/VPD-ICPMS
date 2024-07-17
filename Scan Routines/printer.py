class MarlinPrinter:
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