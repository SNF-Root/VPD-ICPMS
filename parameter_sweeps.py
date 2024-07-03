import argparse
from scanner import VPDScanner

def p_sweep_1():
    """
    Varying droplet volumes. Water on silicon wafer
    """

    wipe_height = 1 # mm
    wipe_speed = 50 # mm/min
    droplet_volumes = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.045] # mL

    my_scan = VPDScanner(droplet_volumes[0], wipe_speed, wipe_height, 150)
    
    my_scan.header()
    for column in range(1):
        for row in range(len(droplet_volumes)):
            my_scan.droplet_volume = droplet_volumes[row]
            my_scan.aspirate()
            my_scan.move_to(70.2 + column*30, 179.3 - row*12.5, wipe_height)
            my_scan.linear_wipe(80)
            my_scan.collect_droplet()
                    
    my_scan.send_to_back_corner()

    filename = "p_sweep_1_2"
    my_scan.write_to_file(filename)

def p_sweep_2():
    "Testing the limits of the length of droplet sizes in circles"
    wipe_height = 1 # mm
    wipe_speed = 50 # mm/min

    droplet_volumes = [0.1, 0.2, 0.3, 0.4, 0.5] # mL
    
    my_scan = VPDScanner(droplet_volumes[0], wipe_speed, wipe_height, 150)

    my_scan.header()
    for ring in range(5):
        my_scan.droplet_volume = droplet_volumes[ring]
        my_scan.aspirate()
        my_scan.move_to(my_scan.WAFER_CENTER_X, my_scan.WAFER_CENTER_Y, wipe_height)
        my_scan.circle(5 + ring*7.5)
        my_scan.collect_droplet()
    
    my_scan.send_to_back_corner()

    filename = "p_sweep_2_2"
    my_scan.write_to_file(filename)

def p_sweep_3():
    "Testing the limits of the length of droplet sizes in circles"
    wipe_height = 1 # mm
    wipe_speed = 600

    droplet_volume = 0.075
    
    my_scan = VPDScanner(droplet_volume, wipe_speed, wipe_height, 150)

    my_scan.header()
    for ring in range(5):
        my_scan.aspirate()
        my_scan.move_to(my_scan.WAFER_CENTER_X, my_scan.WAFER_CENTER_Y, wipe_height)
        my_scan.circle(15 + ring*7.5)
        my_scan.collect_droplet()
    
    my_scan.send_to_back_corner()

    filename = "p_sweep_3_4"
    my_scan.write_to_file(filename)


if __name__ == "__main__":
    """
    Eexecuted when the python script is run from the command line.
    """

    #p_sweep_1()
    #p_sweep_2()
    p_sweep_3()