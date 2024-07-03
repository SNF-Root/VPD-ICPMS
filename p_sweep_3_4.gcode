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
G1 E0.075 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.075 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X110.2 Y129.3 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN CIRCLE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G0 X15.0 F15000 ; move to circle circumference
G1 E0 F5 ; extrude droplet
G2 I-15.0 F600 ; wipe a clockwise circle
G1 X-15.0 F600 ; return to center of circle
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.15 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.075 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.075 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X110.2 Y129.3 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN CIRCLE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G0 X22.5 F15000 ; move to circle circumference
G1 E0 F5 ; extrude droplet
G2 I-22.5 F600 ; wipe a clockwise circle
G1 X-22.5 F600 ; return to center of circle
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.15 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.075 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.075 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X110.2 Y129.3 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN CIRCLE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G0 X30.0 F15000 ; move to circle circumference
G1 E0 F5 ; extrude droplet
G2 I-30.0 F600 ; wipe a clockwise circle
G1 X-30.0 F600 ; return to center of circle
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.15 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.075 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.075 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X110.2 Y129.3 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN CIRCLE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G0 X37.5 F15000 ; move to circle circumference
G1 E0 F5 ; extrude droplet
G2 I-37.5 F600 ; wipe a clockwise circle
G1 X-37.5 F600 ; return to center of circle
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.15 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN ASPIRATE
G0 Z35 F500 ; move to safe travel height
G0 X29 Y50 F15000 ; move high above aspirate cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0.2 F5 ; withdraw 0.2 mL of air
G1 E0 F5 ; return to 0 mL
G0 Z4 F300 ; plunge into aspirate cuvette
G1 E0.075 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.075 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN MOVE TO
G0 Z35 F500 ; move to safe travel height
G0 X110.2 Y129.3 F15000 ; move above position
G0 Z1 F500 ; lower to position
; 
; BEGIN CIRCLE
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G0 X45.0 F15000 ; move to circle circumference
G1 E0 F5 ; extrude droplet
G2 I-45.0 F600 ; wipe a clockwise circle
G1 X-45.0 F600 ; return to center of circle
G90 ; set absolute coordinates
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.15 F2.5 ; slowly suck up droplet
G0 Z1 F300 ; raise to wipe height
; 
; BEGIN SEND TO BACK CORNER
G0 Z35 F500 ; move to safe travel height
G0 X0 Y185 F15000 ; move to back corner
M400 ; wait for commands to finish
M300 P1000 ; beep
