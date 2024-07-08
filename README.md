# Low-Cost Vapor Phase Decomposition (VPD) Scanner for Trace Metal Detection on Surface of Wafers

*Insert GIF of the scanner operating*

## Introduction
Vapor phase decomposition (VPD) is a common technique used in the semiconductor industry to collect trace contaiminates on the surface of wafers into a droplet. When paired with an ICP-MS (a common instrument for measuring low concentrations of chemicals in liquid solutions), a 'VPD-ICP-MS' enables users to quantify the chemical impurities on the surface of their wafers.

However, no low-cost VPD systems exist for academic institutions interested in characterizing their own wafers' contaiminatints. This project provides the end-to-end manufcturing, programming, installation, and standard operating procedure for anyone to create their own VPD scanner.

This project was created and now maintained at the Stanford Nanofabrication Facility (SNF) by Alex Denton, Trevor, and Thomas Rimer. All ICP-MS analysis was performed by Karrie Weaver and Kathleen Kathleen Akbar at the SIGMA lab.

*Add small SNF and SIGMA logo*

## Overview

*Insert image of the scanner sitting inside its box in a fume hood*

The VPD scanner is based on a modified Ender 3 3D printer. Using the provided STLs, Python scripts, and ordering sheet outlined below, the entire VPD scanner can be built and installed in just ~6 hours of work for $4,000. In addition to the written instructions on this doc, there are also accompanying video tutorials going in depth on certain parts of the project. 

**Analysis Note**: This project assumes you have access to an ICP-MS or similarly sensitive tool to analyze the samples. The VPD scanner itself has no capacity to analyze the droplets it collects. Some work arounds are noted below if an ICP-MS is not availible. 

**Safety Note**: This project relies on hydrofluoric acid (HF) for the collection solution. HF is an extremely toxic chemical; if you need to google why, this project is *not* for you.

All aspects of the manufacturing process are designed to be as accessble as possible. Below are a list of tools you're assumed to already have. There are workarounds to every tool:

- 3D printer
- Laser cutter 
- Phillips screw driver
- Metric allen keys
- Soldering iron
- Scissors
- Tape

## Operating Principle

The scanner is based on a 3D printer with its hot-end replaced with a motor-controlled syringe. To scan a wafer, the syringe first aspirates ~200 uL of an HF/H2O2/Water solution. Then it lowers to just 200 um above the center of the wafer and dispenses the solution, forming a droplet on the surface of the wafer that still remains attached to the tip of the syringe. Over the course of 5-15 minutes (depending on wafer size), the scanner slowly moves the syringe head in a series of expanding concentric rings, dragging the droplet across the entire surface of the wafer. The HF in the scan solution attacks the ~2nm native oxide on the wafer's surface, dissolving any contaminants on the surface or within the first few layers of SiO2. Finally, the scanner sucks up the droplet from the surface and dispenses it in a collection cuvette, for analysis by an ICP-MS.

This droplet-dragging technique is similar to what's found in commercial VPD machines. However, there are a few differences worth noting:

**Full Automation:** A human user is needed for setup and sample transfer for the VPD outlined in this repo. Most commercial VPDs have fully automated, load-lock-compatible setups which allow seamless integration into their production lines.

**Vapor Etching:** As the name "Vapor Phase Decomposition" might suggest, commerical VPDs use an HF vapor to etch the entire surface of the wafer at once, before the droplet scan commences. This VPD scanner relies on HF within the scan solution to etch and collect the contaminants at the same time, avoiding the vapor etching step.

**Speed:** While our machine takes ~20+ minutes to process a wafer, a commercial machine can often complete a scan in <60 seconds.

## How to Make Your Own

1. [Procurement](#procurement)
2. [Manufacturing and Assembly](#manufacturing-and-assembly)
3. [Scripting](#scripting)
4. [Calibration](#contact)
5. [Standard Operation](#tunning-your-first-test)
6. [Misc](#mis)

## Procurement

*Every good project starts with a McMasterr Carr order; the VPD scanner is no different.*

Below are three tables, each with a set of components. The "Scanner Components" are used to build the scanner itself. The "Enclosure Components" are used to build the enclosure around the scanner. The "Experimentation Supplies" are the consumables needed to actually run experiments. All prices are approximate, as of July 2024.

All components in the first two table can be purchased from  McMaster Carr or Amazon. However, the strict purity requirements for the sample collection means many of the experimentation suppliers must be ordered directly from suppliers.

Note that each section has dropdowns that go into further detail on different items, including alternative recommendations.


### Scanner Components
| Item | Price per Unit | Units | Subcost | Link | Use
|----------|----------|----------|----------|----------|----------|
| Ender 3 3D Printer    | $249     | 1     | $168 | [Amazon](https://www.amazon.com/Comgrow-Creality-Ender-Aluminum-220x220x250mm/dp/B07BR3F9N6/) | Sacrifical 3D printer converted into the scanner
| Filament    | $25     | 1     | $25 | [Amazon](https://www.amazon.com/HATCHBOX-Printer-Filament-Dimensional-Accuracy/dp/B09G85F1CC/?th=1) | Material used to print the necessary Ender modifications

Scanner Components Subtotal: **~$200**

<details>
  <summary> Click here for details about Scanner Components, alternatives to certain items, and other comments</summary>
   
  ### Ender 3 S1 3D Printer
  The Ender 3 is a super popular, low cost, easily modifiable 3D printer chosen for its large support community and easily accessible components.

  **Ordering notes**: Feel free to purchase the Ender 3 from any website you see fit. Note that there are different versions of the Ender 3 (Ender 3s, Ender 3 pro, etc...) Make sure you purchase the Ender 3s to ensure the syringe head 3D prints fit the gantry. If you do order from a different supplier, make sure it comes with a MicroSD card or you order one seperately.
  
  **Alternatives**: Using any other 3D printer will almost certainly mean a complete redesign of all mechanical components, including the clean enclosure (unless the alternative printer is smaller). Additionally, the scan programs would no longer work, meaning you'd need to generate your own (which should be easy using the program builder script included in this repo, but is still worth noting). If there were one component in this build we'd suggest not replacing, it's the Ender 3s printer. 

  ### Filament
  **Ordering notes**: Any brand of 3D printer filament will work just fine. Because the 3D prints will never come in contact with the scan solution, it does not matter what plastic you use. We recommend PLA for its ease of printing. 
  
  **Alternatives**: If yo're feeling ambitious, some/all 3D printed components can be machined out of teflon. This will provide excellent chemical resistance and durability. Stanford actually has a version of the scanner with custom machined teflon components.

</details>


### Enclosure Components
| Item | Price per Unit | Units | Subcost | Link | Use
|----------|----------|----------|----------|----------|----------|
| Acrylic Plastic Sheet    | $57     | 7     | $400 | [McMaster](https://www.mcmaster.com/8560K357/) | Clear panels cut to form enclosure walls. 24"x24", 1/4" thick
| Blower fan    | $92     | 1     | $92 | [McMaster](https://www.mcmaster.com/2059K36/) | Forces air through the filter, positively pressurizing the enclosure
| ULPA Filter    | $285     | 1     | $285 | [McMaster](https://www.mcmaster.com/5543N11/) | Removes 99.999% of particulate <0.3um in the air entering the box
| Teflon Film    | $21     | 3ft     | $63 | [McMaster](https://www.mcmaster.com/8569K63/) | Protects enclosure against HF splashes
| Acrylic Cement    | $29     | 1     | $29 | [Amazon](https://www.amazon.com/Weld-Acrylic-Plastic-Cement-Applicator/dp/B0149IG548/) | Joins the acrylic side panels together
| Magnets    | $0.90     | 16     | $14 | [McMaster](https://www.mcmaster.com/5862K103/) | Magnetically joins the front panels to the enclosure box
| Epoxy Resin    | $5     | 1     | $5 | [Amazon](https://www.amazon.com/Gorilla-Epoxy-Minute-ounce-Syringe/dp/B001Z3C3AG/?th=1) | Bonds 3D prints to the acrylic enclosure sidewalls
| Silicone Caulk    | $7     | 1     | $7 | [Amazon](https://www.amazon.com/GE-Advanced-Silicone-Kitchen-Bathroom/dp/B0C9VYYCPB/?th=1) | Non-permanent bond for filter components
| 12v Power Supply    | $26     | 1     | $26 | [Amazon](https://www.amazon.com/LRS-200-12-Switching-Supply-Single-Output/dp/B0131UU9E2/?th=1) | Powers the blower fan and LED strips
| LED Light Strip    | $21     | 1     | $21 | [Amazon](https://www.amazon.com/TOPAI-Waterproof-Brightness-2400LEDs-Cuttable/dp/B0BVR996T2/) | Illuminates inside of the box
| Power Switch    | $8     | 1     | $8 | [Amazon](https://www.amazon.com/mxuteuk-Illuminated-Household-Appliances-MXU3-101NR/dp/B07QQ21CZD/) | Toggles power to enclosure and scanner
| Power Cable    | $6     | 1     | $6 | [Amazon](https://www.amazon.com/Amazon-Basics-Computer-Monitor-Replacement/dp/B072BYGKZZ/?th=1) | Cannabilized into master power cable for scanner and enclsoure

Enclosure Components Subtotal: **~$950**

<details>
  <summary> Click here for details about Scanner Components, alternatives to certain items, and other comments</summary>
   
  ### Acrylic Plastic Sheets

  **Ordering notes**: We recommend NOT purchasing the plastic through McMaster if possible. Instead, find a local plastic shop or hardware store that sells acrylic sheets. We purchased all our acrylic from TAP plastics; if you're in the San Francisco Bay Area, this is by far the best place to pick up material. Local shops will also cut stocks down to a size convenient for you; for example, we had TAP cut all our acrylic down to 32"x20" sheets to fit our laser cutter. 
  
  **Alternatives**: As the most expensive building material, it's tempting to find alternatives. Theoretically, any plastic enclosure that can fit the 3D printer inside and can have holes cut in it for ventilation would work. However, the clear material makes viewing the operation of the machine much easier. 

  ### Blower Fan

  **Alternatives**: If you plan on using a different blower fan, know that there are a few important considerations. First, make sure it runs on the same voltage as the power supply (and thus by extension LED lights) to avoid needing a second PSU. Second, a multi-speed blower fan is ideal to allow standby and operating blowing speeds. Lastly, a different blower fan will need a redesigned fan shroud to couple the fan output to the ULPA filter.

  ### ULPA Filter
  
  A ULPA filter was selected over a HEPA filter for its increased filtering power. We recommend using ULPA filters to lower the chance of airborne contaimination. 

  **Alternatives**: If you have spare, clean ULPA filters availible from another source, feel free to use them. Just note that you will need to change both the hole size in the top of the container and fan shround to couple the blower air into the filter. Also make sure the filter is not too restrictive to air flow.

  ### Acrylic Cement

  Acrylic cement produces bad fumes and can be difficult to use. However, when done properly, it forms an invisible and airtight bond. 

  **Ordering Notes**: We suggest purchasing your acrylic cement from a local supplier if you can (acrylic cement is fairly toxic, so shipping can sometimes be an issue). If you do buy in person, make sure you also purchase an applicator bottle and needle (the Amazon listing has it included).

  **Alternatives**: You can use epoxy instead of acrylic cement if fumes or manufacturing difficulty are a concern. However, epoxy will likely get all over the enclosure and will probably not look very good. 

  ### Epoxy Resin

  **Ordering Notes**: Brand or size of epoxy resin does not matter; so long as it's a general purpose epoxy designed to bond metal and plastic 
  it will work fine. 

  **Alternatives**: Super glue is the best alternative, though it will form a less durable bond than epoxy. Avoid hot glue.

  ### Magnets

  **Ordering notes**: The magnets are so inexpensive we recommend ordering and using the suggested ones. However, if you have spare disc magnets laying around, you can use them. Make sure they are magnetized through their thickness and are not too strong or weak to support the acrylic front panels. Different magnets will required a magnet holder redesign.

  ### Silicone Caulk

  **Ordering Notes**: Brand or size of the silicone caulk does not matter; feel free to purchase from a local hardware store or use a tube laying around the lab (as long as it hasn't gone bad).

  ### Power Supply

  **Ordering Notes**: Any 12v power supply will do as long as its current rating matches or exceeds the sum of the blower fan and LED light requirements.

  ### LED Lights

  While the LED lights are not necessary, they improve visibility of the VPD scanner while working with it, and can also act as a clear indicator whether the tool is on or off. 


  **Ordering Notes**: Any LED light strip with the same voltage as the power supply will work fine.

  **Alternatives**: Any lighting (bulb, lamp, etc...) that operates on either 120v or the power supply voltage will work. When ins

</details>

### Experimentation Supplies
| Item | Price per Unit | Units | Subcost | Link | Use
|----------|----------|----------|----------|----------|----------|
| 1mL Syringes    | $29     | 1     | $29 | [Amazon](https://www.amazon.com/Syringe-Luer-Slip-Plastic-PK100/dp/B0763KTQV5/) | Pack of 100 polyethlyne syringes. Mounts inside the scanner to aspirate, move, and dispense droplet.
| Teflon Cuvette    | $--     | -     | $-- | [Amazon]() | Sterile container for both the scan soltion and scanned droplets
| Teflon Jar    | $--     | -     | $-- | [Amazon]() | Sterile container to prepare HF and H2O2 scan solution 
| Ultrapure HF    | $---     | -     | $--- | [Amazon]() | Ultrapure 2% HF to prepare scan solution
| Ultrapure H2O2    | $---     | -     | $--- | [Amazon]() | Ultrapure H2O2 to prepare scan solution
| MS Standard Solution    | $---     | -     | $-- | [Amazon]() | Pre-made solution containing ~24 heavy metals for characterizing VPD

Experimentation Supplies Subtotal: **~$1,500**

<details>
  <summary> Click here for details about Experimentation Supplies, alternatives to certain items, and other comments</summary>
   
  TODO: Complete ordering details once testing is finished and part suppliers are finalized.

</details>

## Manufacturing and Assembly

The VPD scanner has two parts; assembling the scanner and building its enclosure. Each can be made independently of the other, making it convienent to split up amongst multiple people or parallelize.

There are XX 3D prints requried for this project. To minimize the amount of time spent waiting for 3D prints to finish, we recommend printing parts (regardless of what printer you use) as soon you begin on the project.


Tehcnically, you can 3D print all components on the Ender 3S printer purchased for the scanner. This is recommended only if you have limited access to other printers. If you decide to 3D print the components on the Ender 3S, you should first fully assemble the 3D printer following the video in Step 1.1 (not skipping any steps). Then, print all components (as outlined below) before continuing on the project. Know that once modifications begin, it will take at least an hour to uninstall the syringe head and reinstall the print head for additional prints.
<details>
  <summary> Click here for a complete list of required 3D printed parts, their associated quantities, and recommended print settings</summary>
   
  TODO: Add the complete list of STL files and how many need to be made.

</details>

### 1 Scanner Manufacturing

*Insert image of finished scanenr*

#### Step 1.1: Assembling the Ender 3s

The Ender 3s comes partially assembled from the factory. There are several high-quality YouTube tutorials already made outlining exactly how to assemble an Ender 3. Here's a well-made one from [3D Printing Canada](https://www.youtube.com/watch?v=dQ0q9zLygTY) (https://www.youtube.com/watch?v=dQ0q9zLygTY).

While most of the build proceeds as normal, there are a few steps you should <ins>not</ins> do:

- Do not mount the extruder stepper motor on the bracket designed for it. However, you should still wire it as if you were going to mount it. The extruder stepper motor will be used later on to control the syringe.
- Similarly, do not install the spring-loaded extruder gear assembly. This is not needed for the VPD.
- Do not mount or screw in the bed leveling adjustment dials. These will be installed later.
- Do not binder-clip the Ender-branded build surface onto the print bed. Parts will mount directly onto the print bed later, so this build surface is not needed.

Save all components (and spare parts) that you do not install. You will need some of these materials later.

#### Step 1.2: Print and Install Parts For Wafer Holder

There are seven 3D printed compoentns required for the wafer holder:

- 001_Wafer_Holder_Body_A
- 002_Wafer_Holder_Body_B
- 003_Wafer_Holder_Body_C
- 004_Wafer_Holder_Body_D
- 005_Wafer_Holder_2_in_Chuck
- 006_Wafer_Holder_4_in_Chuck
- 007_Wafer_Holder_6_in_Chuck

<details>
  <summary> Click here for a details about 3D printing orientation and settings
  <br></br>
  </summary>
   
  TODO: Include pictures of recommended print orientation and print settings for the seven components

</details>

Wafer Holder Body A-D are four pieces that form the Wafer Holder Body. Puzzle-piece the components together together and place them on the print bed. Slide the included bed-leveling screws through the four screw holes in each corner of the Wafer Holder Body, making sure it also goes through the metal print bed. At each corner, add a bed leveling spring onto the screw before twisting on a large bed leveling dial (included with the Ender). Twist on the bed leveling dial until there are a few phillips threads visible sticking out past the dial. 

*Include image of the four 3D printed pieces on the print bed with screws through them. Include side image of the dial on the phillips screw with spring in proper compression*

Each chuck is designed to fit into the center cavity. For testing and calibration, install the 6 inch chuck.

*Include image of installed 6" chuck*

#### Step Step 1.3: Print and Install Parts For Syringe Head

There are three 3D printed components required for the syringe head:

- 00X_Syringe_Holder_Body
- 00X_Syringe_Holder_Rack
- 00X_Syringe_Holder_Pinion 

<details>
  <summary> Click here for a details about 3D printing orientation and settings
  <br></br>
  </summary>
   
  TODO: Include pictures of recommended print orientation and print settings for the three components

</details>

First, use three M3 screws included with the hot end to mount the Syringe Holder Body onto the gantry, as pictured below.

*Include image of the syringe holder body mounted on the gantry*

Next, use four M3 screws included with the extruder stepper motor to mount the extruder stepper motor onto the backside of the syringe holder body, as pictured below. Make sure the stepper motor cable leaves in the direction away from the LCD panel. 

*Include image of the syringe holder body and stepper motor*

Press fit the 3D printed pinion on to the stepper motor shaft. It should fit snuggly. If the pinion is too loose, wrap a layer of tape evenly around the shaft and try press fitting again. If the pinion does not fit on the shaft (hole is too small), file/sand down the hole until it fits.

*Show image of the pinion press fit onto the stepper shaft*

Lastly, insert the two dovetails on the back of the Syringe Holder Rack into the dovetail slots on the top of the Syringe Holder Body. Slide the rack down until its teeth make contact with the pinion. Continue pushing the rack down, causing the pinion to interface with the rack and begin spinning. Push the rack all the way down until the small arm collides with the Sryinge Holder Body's ledge and prevents it from going further.

*Show two images of the rack, one of it getting inserted into the top, and the other of it bottomed out.

### Enclosure Manufacturing

*Insert CAD rendering of finished enclosure*

The enclosure is built from laser-cut acrylic panels. A fan mounted on top of a ULPA filter blows clean air into the top of the enclosure. Slots cut into the bottom of the enclosure allow the clean air to escape out the bottom, ensuring laminar, downward flow throughout the entire box. A power supply mounted on the back of the ULPA filter powers the fan and LED lights. The box and scanner is enabled/disabled by a single power switch mounted on the side. The front panel is split in three parts, all mounted on the front of the box by magnets. This allows easy access during routine operation, and the ability to completely remove the scanner during installation and cleaning. The bottom of the enclosure has a teflon film to protect the acrylic from HF splashes.

The complete CAD assembly is availible in the CAD/enclsoure folder. All individual parts are also availible as STEPS and F3Ds.

**Step 1: Cutting Acrylic Panels**

There are 8 pieces that must be cut from the acrylic side panels:
- Left panel
- Right panel
- Back panel
- Bottom panel
- Top panel
- Front top panel
- Front middle panel
- Front bottom panel

All DXFs for the panels are availible from 

We would strongly suggest using a laser cutter to cut the acrylic side panels given it 

**Step 2: Acrylic Enclosure Welding**

**Step 3: Mounting Magnets**

**Step 4: ULPA Filter Installation**

**Step 5: Blower Fan Installation**

**Step 6: LED Light Installation**

**Step 7: Power Switch Installation**

**Step 8: Power Supply Mounting and Wiring**

**Step 9: Teflon Base Installation**

## Scripting

### Introduction

*Download the GitHub repo to your computer to access and run the scripts*

After fabricating the VPD scanner, you need to control it. The printer runs on GCODE, a human-readable, tool-control language where each line corrosponds to a movement (or modificatoin to a movement). There are three options for generating GCODE files, each with greater flexibility at the cost of greater complexity:

- **Pregenerated Routine (easiest) (recommended)**: In the 'pre-generated routines' folder are several GCODE files that can be directly uploaded and run on the scanner. They are specifically generated for the scanner described in this document. If you built your scanner following the instructions provided here, you can run the scanner entirely off of these commands. The pre-generate routines require no programming or terminal commands. 
- **Regenerated Default Routine (more difficult)**: In the 'generate_default_routine' folder is a python script that will automatically generate a scan routine based a select number of parameters you input (like droplet volume, scan speed, syringe, etc...). A regenerated defualt routine involves a single terminal command.  
- **Custom Routine (most difficult)**: If you would like to write your own custom scan routine, you can with the 'generate_custom_routine' script in the same folder. This will allow you to create a routine with any sort of movement, aspiration, or dispensing. A custom routine requires several (10+) lines of python and a terminal command.

The GCODE routine needs to be uploaded to the printer after its generated. This is simply done through a micro SD card file transfer.

The three generation options as well as SD card file transfer are all explained in detail below.

### Pregenerated Routines

Within the 'pregenerated_routines' folder are six scan routines for different sized wafers. The size in the name of routine is the size of the wafer being scanned:

- 1_inch_wafer_scan_pre_generated.gcode
- 2_inch_wafer_scan_pre_generated.gcode
- 3_inch_wafer_scan_pre_generated.gcode
- 4_inch_wafer_scan_pre_generated.gcode
- 5_inch_wafer_scan_pre_generated.gcode
- 6_inch_wafer_scan_pre_generated.gcode

The pre-generated routines have the following parameters:
- Scan pattern: concentric starting in middle
- Droplet volume: 300 uL
- Scan speed: 175 mm/min
- Scan height: 200 um
- Droplet width: 5 mm

Follow the the instructions in 'Uploading Routines to the Scanner' to send the pregenerated routines to the scanner. 

### Regenerated Routine

Within the 'regenerated_routines' folder is the python script 'regenerate_default_scan.py' which takes several input flags and generates a concentric scan based on their parameters.

To regenerate a routine based on your desired parameters, first navigate to the 'regenerated_routines' directory in terminal. For example...

```console
foo@bar: cd /Users/thomas-rimer/Desktop/DIY-VPD/regenerated_routines
```

Next call the 'regenerate_default_scan.py' along with the six required flags, explained below:

| Flag Name                | Details                   |
|-------------------------|-----------------------------------------|
| filename | **Description**: name of the GCODE file saved to disk <br> **Units**: string <br> **Range**: <256 characters, just letters, numbers, and underscores |
| droplet_volume | **Description**: volume of the droplet used to scan the wafer <br> **Units**: mL <br> **Range**: anywhere between 0.001 and 1 |
| wipe_speed | **Description**: scan speed of the syringe over the wafer <br> **Units**: mm/min <br> **Range**: anywhere between 0.001 and 10000 |
| wipe_height | **Description**: height of the syringe above the wafer while scanning <br> **Units**: mm <br> **Range**: any value above 0 |
| droplet_width | **Description**:  width of the droplet formed on the surface of the wafer <br> **Units**: mm <br> **Range**: any value above 0 <br> **NOTE**: you must physically measure this value with calipers. guess 5mm the first time you generate the script, then revise based on measurement. |
| wafer_size | **Description**:  diameter of the wafer to be scanned <br> **Units**: mm <br> **Range**: anywhere between 1 and 150 |

An example call might look like

```console
foo@bar: python3 regenerate_default_scan.py --filename=myCustomScan --droplet_volume=0.1 --wipe_speed=150 --wipe_height=0.3 --droplet_width=4.7 --wafer_size=150
```

After calling this in terminal, a GCODE file with the entered filename (i.e. 'myCustomScan.gcode') will be created in the 'regenerated_routines' directory. If there is already a GCODE file with the same name, it will be overwritten.

Follow the the instructions in 'Uploading Routines to the Scanner' to send the regenerated routine to the scanner. 

### Custom Routine

Creating a custom routine requires knowledge about the machine and how GCODE works. For that reason, there is a seperate document outlining how to make a custom routine called 'CUSTOM_ROUTINE.MD' in the 'custom_routine' folder. 

### Uploading Routines to the Scanner

The scanner uses the original 3D printer interface to run gcode files. To upload a routine to the scanner
1) Plug the micro sd card into your computer using the provided micro sd to usb adapter.
2) If it's your first time uploading a routine, delete all existing files on the sd card.
3) Transfer desired gcode files from the pregenerated, regenerated, or custom folder onto the sd card.
4) Remove the sd card from your computer and plug it into the micro sd port on the front, bottom, left black controller box (underneath the bed).

## Calibration

## Standard Operation

## Misc

### Contact

Please reach out if you're thinking about building a scanner, we're excited to see these get into as many labs as possible! We ask you use the "Issues" tab to ask questions, this will allow other people thinking of building a VPD to see what is and isn't going well. 

### License

This project is licensed under the MIT License. See the LICENSE file for more details.