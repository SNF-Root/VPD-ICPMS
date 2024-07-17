import argparse
from scanner import VPDScanner

def custom_scan(filename, droplet_volume, wipe_speed, wipe_height, wafer_size):
    """
    ### PROGRAM SKELETON DEFINED HERE ###
    
   Construct your custom script in CUSTOM SCRIPT area below. See README.md for a
   list of all availible methods. Below is a skeloton of a simple wafer scan script. 

    """
    
    my_custom_scan = VPDScanner(droplet_volume, wipe_speed, wipe_height, wafer_size) # create an instance of the VPDScanner class
    my_custom_scan.header() # insert necessary header GCODE at the beginning of the file

    ###########################
    ### BEGIN CUSTOM SCRIPT ###
    ###########################

    my_custom_scan.aspirate_from_cuvette()
    my_custom_scan.center()
    my_custom_scan.put_down_droplet()
    my_custom_scan.scan_wafer()
    my_custom_scan.pick_up_droplet()
    my_custom_scan.dispense_into_cuvette()
    my_custom_scan.send_to_back_corner()

    ###########################
    #### END CUSTOM SCRIPT ####
    ###########################

    my_custom_scan.write_to_file(filename) # write GCODE to file

if __name__ == "__main__":
    """
    Eexecuted when the python script is run from the command line. 
    Generates the GCODE file based on the content of main and the flags provided by the user
    when calling the python script.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--filename", required=True, help="Name of gcode file to be saved (can or cannot include .gcode)")
    parser.add_argument("--droplet_volume", required=True, help="Volume in mL of droplet to dispense")
    parser.add_argument("--wipe_speed", required=True, help="Speed in mm/min to wipe the syringe tip")
    parser.add_argument("--wipe_height", required=True, help="Height in mm above the wafer to wipe the syringe tip")
    parser.add_argument("--wafer_size", required=True, help="Diameter in mm of wafer to be tested")

    args = parser.parse_args()

    custom_scan(args.filename, float(args.droplet_volume), float(args.wipe_speed), float(args.wipe_height), float(args.wafer_size))