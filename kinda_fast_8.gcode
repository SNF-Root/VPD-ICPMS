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
G1 E0.03 F5 ; aspirate solution
G1 E0 F5 ; dispense solution
G1 E0.03 F5 ; aspirate solution
G0 Z30 F300 ; raise to cuvette holder height
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN CENTER
G0 Z35 F500 ; move to safe travel height
G0 X110.2 Y129.3 F15000 ; move high above wafer center
G0 Z0.5 F500 ; lower to wipe height
; 
; BEGIN SCAN WAFER
G91 ; set relative coordinates
M82 ; set extruder to absolute coordinates
G0 X2.5 F15000 ; move to beginning of first circle
G1 E0 F5 ; extrude droplet
G2 I-2.5 F1250.0 ; wipe a clockwise circle
G1 X5 F1250.0 ; move to next circle circumnference
G2 I-7.5 F1250.0 ; wipe a clockwise circle
G1 X5 F1250.0 ; move to next circle circumnference
G2 I-12.5 F1250.0 ; wipe a clockwise circle
G1 X5 F1250.0 ; move to next circle circumnference
G2 I-17.5 F1250.0 ; wipe a clockwise circle
G1 X5 F1250.0 ; move to next circle circumnference
G2 I-22.5 F1250.0 ; wipe a clockwise circle
G90 ; set absolute coordinates
G1 X110.2 Y129.3 F1250.0 ; move to wafer center
; 
; BEGIN COLLECT DROPLET
G1 Z1 F300 ; lower closer to wafer
G1 E0.06 F2.5 ; slowly suck up droplet
G0 Z0.5 F300 ; raise to wipe height
; 
; BEGIN DISPENSE
G0 Z35 F500 ; move to safe travel height
G0 X190 Y50 F15000 ; move high above dispense cuvette
G0 Z30 F500 ; lower to cuvette holder height
G1 E0 F5 ; dispense all solution in syringe
G0 Z35 F500 ; move to safe travel height
; 
; BEGIN SEND TO BACK CORNER
G0 Z35 F500 ; move to safe travel height
G0 X0 Y185 F15000 ; move to back corner
M400 ; wait for commands to finish
M300 P1000 ; beep
