import argparse
from scanner import VPDScanner

def default_scan(filename, droplet_volume, wipe_speed, wipe_height, wafer_size):
    """
    ### DEFAULT SCAN DEFINED BELOW ###

    This basic scan scans a droplet across the surface of a wafer in concentric rings. 
    If you want to create your own scan routine, edit the custom.py script. Below are
    detailed instruction
    
    
    1) Aspirates a droplet from the sample (left) cuvette.
    2) Moves to the center of the wafer.
    3) Dispenses the droplet onto the surface.
    4) Drags the droplet across the entire surface of the wafer in concentric circles.
    5) Sucks up the droplet back into the syringe.
    6) Dispenses the droplet into a the right cuvette
    """
    
    my_scan = VPDScanner(droplet_volume, wipe_speed, wipe_height, wafer_size) # create an instance of the VPDScanner class
    
    my_scan.header() # insert necessary header GCODE at the beginning of the file
    my_scan.aspirate_from_cuvette() # suck up droplet from aspirate cuvette
    my_scan.center() # center the syringe over the wafer
    my_scan.put_down_droplet() # dispense droplet onto the surface of the wafer
    my_scan.scan_wafer() # scan the droplet across the surface of the wafer in concentric circles
    my_scan.pick_up_droplet() # pick up droplet from surface of the wafer
    my_scan.dispense_into_cuvette() # dispense droplet into rear cuvette
    my_scan.send_to_back_corner() # move syringe out of the way of the wafer
    my_scan.write_to_file(filename) # save the gcode to file

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

    default_scan(args.filename, float(args.droplet_volume), float(args.wipe_speed), float(args.wipe_height), float(args.wafer_size))