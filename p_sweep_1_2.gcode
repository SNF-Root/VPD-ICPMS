; BEGIN HEADER
G21 ; set units to mm
G90 ; absolute coordinates for X,Y,Z, and E
M302 S0; always allow extrusion (disable temp/length checking)
M92 E3938.0 ; set extruder steps per mL
G28 ; home all axes
G92 X0 Y0 Z0 E0 ; zero all axes
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.05 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.05 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X70.2 Y179.3 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN LINEAR WIPE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G1 E0 F5 ; extrude droplet
G1 X80 F50 ; wipe in a straight line
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.1 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.1 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.1 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X70.2 Y166.8 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN LINEAR WIPE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G1 E0 F5 ; extrude droplet
G1 X80 F50 ; wipe in a straight line
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.2 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.15 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.15 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X70.2 Y154.3 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN LINEAR WIPE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G1 E0 F5 ; extrude droplet
G1 X80 F50 ; wipe in a straight line
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.3 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.2 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.2 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X70.2 Y141.8 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN LINEAR WIPE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G1 E0 F5 ; extrude droplet
G1 X80 F50 ; wipe in a straight line
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.4 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.25 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.25 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X70.2 Y129.3 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN LINEAR WIPE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G1 E0 F5 ; extrude droplet
G1 X80 F50 ; wipe in a straight line
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.5 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.3 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.3 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X70.2 Y116.80000000000001 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN LINEAR WIPE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G1 E0 F5 ; extrude droplet
G1 X80 F50 ; wipe in a straight line
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.6 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.35 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.35 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X70.2 Y104.30000000000001 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN LINEAR WIPE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G1 E0 F5 ; extrude droplet
G1 X80 F50 ; wipe in a straight line
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.7 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.4 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.4 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X70.2 Y91.80000000000001 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN LINEAR WIPE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G1 E0 F5 ; extrude droplet
G1 X80 F50 ; wipe in a straight line
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.8 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.045 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.045 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X70.2 Y79.30000000000001 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN LINEAR WIPE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G1 E0 F5 ; extrude droplet
G1 X80 F50 ; wipe in a straight line
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.09 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN SEND TO BACK CORNER
G0 Z35 F500 ; move to safe travel height
G0 X0 Y185 F15000 ; move to back corner
M400 ; wait for commands to finish
M300 P1000 ; beep
