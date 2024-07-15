# Low-Cost, DIY Vapor Phase Decomposition (VPD) Scanner for Trace Metal Detection on Surface of Wafers

*Insert GIF of the scanner operating*

## Introduction
Vapor phase decomposition (VPD) is a process used in the semiconductor industry to quantify trace metal contaminants on the surface of wafers. While VPD is most commonly used by commerical fabs to verify the purity of wafers shipped from suppliers, the goal of this project was to measure cross-contamination between different atomic layer deposition (ALD) jobs at an academic instution. This GitHub repo provides the end-to-end instructions to manufacture, program, and install an DIY VPD capable of XXX atoms/CM^2 measurements for academic cleanrooms. 

This project was created by Alex Denton, Trevor, and Thomas Rimer at the [Stanford Nanofabrication Facility](https://snf.stanford.edu/). All ICP-MS analysis was performed by Karrie Weaver and Kathleen Akbar at the [SIGMA lab](https://sigmalab.stanford.edu/).

*Add small SNF and SIGMA logo*

## Overview

*Insert image of the scanner sitting inside its box in a fume hood*

VPD (vapor phase decomposition) is a technique to collect metal and chemical contamininats on the surface of a wafer into a single, liquid droplet. The details of this collection process are explained in the "Operating Principles Section" right below. Crucially, VPD *does not* involve the measurement or quantification of chemicals; it's simply a technique (among many) to collect them. That's where ICP-MS comes in...

ICP-MS stands for "Inductively Coupled Plasma Mass Spectroscopy." It's one of the most sensitive techniques for measuring the conentration of metals (among other chemicals) in liquid solutions. Check out [this video](https://www.youtube.com/watch?v=tP5ZKUTWiuQ) from Agilent (an ICP-MS tool manufacturer) to learn about the basic operating principles of an ICP-MS. In summary, the liquid sample is aerosolized before getting ionized inside a plasma. Metals in the solution are then accelerated down a sampling coloumn where they're seperated out by their charge/mass ratio and then measured. 

When VPD and ICP-MS are combined, it's called VPD-ICP-MS. Note that VPD doesn't necessarily need to use ICP-MS for analysis; alternatives like Atomic Absorption Spectroscopy (AAS) are also common. Similarly, VPD is not the only way to collect samples for ICP-MS; anything from blood to seawater to colloidal space dust can be measured in an ICP-MS.

To summarize, VPD collects contaminants on the surface of a wafer into a small liquid droplet. That droplet is then transferred into an off-the-shelf ICP-MS which measures and quantifies the concentrations of contaminants.

Using the provided instructions outlined below, the entire scanner and its enclosure can be built and installed in <XXX hours for $XX,000. 

Detailed performance information is availible in the [Performance](#performance) section.

## Operating Principles

The VPD scanner is based on a modified 3D printer; instead of a hot-end to extrude plastic, it has a motor-controlled syringe. To scan a wafer, the syringe first aspirates ~200 uL of an HF/H2O2/Water solution. Then it lowers to the surface of the wafer and dispenses the solution, forming a droplet on the surface of the wafer. Crucially, the droplet remains connected to the tip of the syringe. Over the course of 5-15 minutes (depending on wafer size), the scanner slowly moves the syringe head in a series of expanding concentric rings, dragging the droplet across the entire surface of the wafer. The HF in the scan solution attacks the ~2nm native oxide on the wafer's surface, dissolving any contaminants on the surface and within the first few layers of SiO2. Finally, the scanner sucks up the droplet from the surface and dispenses it in a collection cuvette, for analysis by an ICP-MS.

This droplet-dragging technique is similar to what's found in commercial VPD machines. However, there are a few differences worth noting:

**Vapor Etching:** As the name "Vapor Phase Decomposition" might suggest, commerical VPDs use an HF vapor to etch the entire surface of the wafer at once, before the droplet scan commences. This VPD scanner relies on aqueous HF within the scan solution to etch and collect the contaminants at the same time, avoiding the vapor etching step.

**Full Automation:** A human user is needed for setup and sample transfer for this DIY VPD. Most commercial VPDs have fully automated setups which allow for seamless integration into production lines.

**Speed:** While our machine takes ~20+ minutes to process a wafer, a commercial machine can often complete a scan in <60 seconds.

## Imporant Notes

**Analysis**: As hinted at above, this project assumes you have access to an ICP-MS or similarly sensitive tool to analyze the samples. The VPD scanner itself has no capacity to analyze the droplets it collects. More information about the ICP-MS analysis—along with alternatives—are detailed in the XXX section below. 

**Safety**: This project relies on hydrofluoric acid (HF) for the collection solution. HF is an extremely toxic chemical; if you need to google why, this project is *not* for you.

**Setup**: This machine produces small amounts of HF vapor and should therefore be operated inside a fume hood. The minimum fume hood space required is 20" wide, 25" deep, and 42" tall.

## DIY VPD Instructions

The rest of this document is dedicated to the detailed instructions for fabricating, testing, and using your own DIY VPD. 

0. [Fabrication Overview](#step-0-fabrication-overview)
1. [Procurement](#procurement)
2. [Manufacturing and Assembly](#manufacturing-and-assembly)
3. [Scripting](#scripting)
4. [Characterization](#characterization)
5. [Standard Operation](#tunning-your-first-test)
6. [Misc](#mis)

## Step 0: Fabrication Overview

The fabrication, setup, and programming of the machine are as follows:
1) First, all supplies need to be purchased. This is thoroughly explained in [Procurement](#procurement)
2) Next, both parts of the VPD need to be built: the scanner (which scans the droplet) and the enclosure (which forms a clean environment around the scanner). Instructions are layed out in [Manufacturing and Assembly](#manufacturing-and-assembly)
3) After building the VPD, it needs to be programmed. [Scripting](#scripting) explains the tradeoffs between pre-generated scripts and writing custom programs.
4) With the VPD fully operational, it needs to be characterized. This involves "recovery tests" which directly measure how precise the VPD is and help diagnose hidden performance issues like contamination. The steps are outlined in [Characterization](#characterization).
5) After characterization, the VPD is ready for users! [Standard Operation](#tunning-your-first-test) offers advice on installement, intermittent calibration, and other practical guidelines for transporting samples for analysis. 
6) [Misc](#misc) contains credit and license information.

All aspects of the manufacturing process are designed to be as accessible as possible. However, it's assumed that some basic tools are availible for fabrication. Below is a list of the required materials:

- 3D printer (minimum bed size: 7.5" x 7.5" x 2")
- Laser cutter (minimum bed size: 24" x 20")
- Phillips screwdriver
- Metric allen keys
- Soldering iron
- Scissors
- Tape

### Contact Us

If you've read this far, you're probably pretty interested in VPD. Please reach out if you're thinking about building a scanner, have questions about the build process, or have issues with your own DIY-VPD! We're excited to get these into as many labs as possible! We ask you use the "Issues" tab to ask questions (even if it's not strictly an "issue"). This will allow other people thinking of building a VPD to see who else is interested, what they're thinking, and issues they're having.

## Step 1: Procurement

*Every good project starts with a McMasterr Carr order; the VPD scanner is no different.*

Below are three tables, each with a set of components. The "Scanner Components" are used to build the scanner itself. The "Enclosure Components" are used to build the enclosure around the scanner. The "Experimentation Supplies" are the consumables needed to actually run experiments. All prices are approximate, as of July 2024.

All components in the first two tables can be purchased from  McMaster Carr or Amazon. However, the strict purity requirements for the sample collection means many of the experimentation suppliers must be ordered directly from suppliers.

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

  **Ordering notes**: Feel free to purchase the Ender 3 from any website. Note that there are different versions of the Ender 3 (Ender 3s, Ender 3 pro, etc...) Make sure you purchase the Ender 3 to ensure the syringe head 3D prints fit the gantry. If you do order from a different supplier, make sure it comes with a MicroSD card (or you order a micro SD card seperately).
  
  **Alternatives**: Using any other 3D printer will almost certainly mean a complete redesign of all mechanical components, including the clean enclosure (unless the alternative printer is smaller than the Ender 3). Additionally, the scan programs would no longer work, meaning you'd need to generate your own (which should be easy using the program builder script included in this repo, but is still an additional step). If there were one component in this build we'd suggest not replacing, it's the Ender 3 printer. 

  ### Filament
  **Ordering notes**: Any brand of 3D printer filament will work just fine. Because the 3D prints will never come in contact with the scan solution, it does not matter what plastic you use. We recommend PLA for its ease of printing. However, PolyMax filament from PolyMaker has repeatedly proven itself as the most durable filament based on our testing, so we think it's worth purchasing. 
  
  **Alternatives**: If yo're feeling ambitious, some/all 3D printed components can be machined out of teflon. This will provide excellent chemical resistance and durability. Stanford actually has a version of the scanner with custom machined teflon components. Finding a teflon machine shop, creating engineering drawings, and managing the manufacturing process is not discussied in this guide.
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

  **Ordering notes**: Minimize sheet size is 23.5" x 19.5." We recommend NOT purchasing the plastic through McMaster. Instead, find a local plastic shop or hardware store that sells acrylic sheets. We purchased all our acrylic from TAP plastics; if you're in the San Francisco Bay Area, this is by far the best place to pick up material. Local shops will also cut stocks down to a size convenient for you; for example, we had TAP cut all our acrylic down to 32"x20" sheets to fit our laser cutter. 
  
  **Alternatives**: As the most expensive building material, it's tempting to find alternatives. Theoretically, any plastic enclosure that can fit the 3D printer inside and can have holes cut in it for ventilation would work. However, the clear material makes viewing the operation of the machine much easier. 

  ### Blower Fan

  **Alternatives**: If you plan on using a different blower fan, know that there are a few important considerations. First, make sure it runs on the same voltage as the power supply (and thus by extension LED lights) to avoid needing a second PSU. Second, a multi-speed blower fan is ideal to allow standby and operating blowing speeds. Lastly, a different blower fan will need a redesigned fan shroud to couple the fan output to the ULPA filter.

  ### ULPA Filter
  
  A ULPA filter was selected over a HEPA filter for its increased filtering power. We recommend using ULPA filters to lower the chance of airborne contaimination. 

  The ULPA filter linked in the table is very large and should last for years. Based your spare ordering on that length scale (Stanford did not purchase any spare filters).

  **Alternatives**: If you have spare, clean ULPA filters availible from another source, feel free to use them. Just note that you will need to change both the hole size in the top of the container and fan shround to couple the blower air into the filter. Also make sure the filter is not too restrictive to air flow.

  ### Acrylic Cement

  Acrylic cement produces bad fumes and can be difficult to use. However, when done properly, it forms an invisible and airtight bond. 

  **Ordering Notes**: We suggest purchasing your acrylic cement from a local supplier; acrylic cement is fairly toxic, so shipping can sometimes be an issue. If you do buy in person, make sure you also purchase an applicator bottle and needle (the Amazon listing has both included).

  **Alternatives**: You can use epoxy instead of acrylic cement if fumes or manufacturing difficulty are a concern. However, epoxy will likely get all over the enclosure and may not look good. 

  ### Epoxy Resin

  **Ordering Notes**: Brand or size of epoxy resin does not matter; it will work so long as it's a general purpose epoxy designed to bond metal and plastic.

  **Alternatives**: Super glue is the best alternative, though it will form a less durable bond than epoxy. Avoid hot glue.

  ### Magnets

  **Ordering notes**: The magnets are so inexpensive we recommend ordering and using the suggested ones. However, if you have spare disc magnets laying around, you can use them. Make sure they are magnetized through their thickness and are not too strong or weak to support the acrylic front panels. Different magnets will required a magnet holder redesign.

  ### Silicone Caulk

  **Ordering Notes**: Brand or size of the silicone caulk does not matter; feel free to purchase from a local hardware store or use a tube laying around the lab (as long as it hasn't gone bad).

  ### Power Supply

  **Ordering Notes**: Any 12v power supply will do as long as its current rating matches or exceeds the sum of the blower fan and LED light requirements.

  ### LED Lights

  While the LED lights are not necessary, they improve visibility of the VPD scanner.

  **Ordering Notes**: Any LED light strip with the same voltage as the power supply will work fine.

  **Alternatives**: Any lighting (bulb, lamp, etc...) that operates on either 120v or the power supply voltage will work.

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

## Step 2: Manufacturing and Assembly
The VPD scanner has two sub assmblies; the scanner and the enclosure. Each can be built independently of the other, making it convienent to split up amongst multiple people.

There are XX 3D prints requried for this project. To minimize the amount of time spent waiting for 3D prints to finish, we recommend printing parts as soon you begin on the project.

Tehcnically, you can 3D print all components on the Ender 3 printer purchased for the scanner. This is recommended only if you have limited access to other printers. If you decide to 3D print the components on the Ender 3, you should first fully assemble the 3D printer following the video in [Step 2.1](#step-2-1) (not skipping any steps). Then, print all components (as outlined below) before continuing on the project. Know that once you've modified the printer into the scanner, it will take around an hour to uninstall the VPD parts and restore the Ender to a print-worthy state. 

<details>
  <summary> Click here for a complete list of required 3D printed parts, their associated quantities, and recommended print settings/orientations</summary>
   
  TODO: Add the complete list of STL files and how many need to be made.

</details>

### 2.1 Scanner Manufacturing

*Insert image of finished scanenr*

#### Step 2.1.1: Assembling the Ender 3s

The Ender 3s comes partially assembled from the factory. There are several high-quality YouTube tutorials already made outlining exactly how to assemble an Ender 3. Here's a well-made one from [3D Printing Canada](https://www.youtube.com/watch?v=dQ0q9zLygTY) (https://www.youtube.com/watch?v=dQ0q9zLygTY).

While most of the build proceeds as normal, there are a few steps you should <ins>not</ins> do:

- Do not mount the extruder stepper motor on the bracket designed for it. However, you should still wire the stepper. The extruder stepper motor will be used later on to control the syringe.
- Similarly, do not install the spring-loaded extruder gear assembly. This is not needed for the VPD.
- Do not mount or screw in the bed leveling adjustment dials. These will be installed later.
- Do not binder-clip the Ender-branded build surface onto the print bed. Parts will mount directly onto the print bed later, so this build surface is not needed.

Save all components (and spare parts) that you do not install. You will need some of these materials later.

#### Step 2.1.2: Print and Install Parts For Wafer Holder

There are four 3D printed components required for the wafer holder:

- 001_Wafer_Holder_Base
- 002_Wafer_Holder_2_inch_Chuck
- 003_Wafer_Holder_4_inch_Chuck
- 004_Wafer_Holder_6_inch_Chuck

<details>
  <summary> Click here for a details about 3D printing orientation and settings
  <br></br>
  </summary>
   
  TODO: Include pictures of recommended print orientation and print settings for the  components. This should be a copy from the complete 3D print list above.

</details>

Place 001_Wafer_Holder_Base on the print bed, alligning the the holes in each corner with the screws holes in the aluminum bed. The two cylindrical cavities should face the front of the printer. Slide the included bed-leveling screws through the four screw holes in each corner of the Wafer Holder Body, making sure it also goes through the metal print bed. Underneath each corner, slide a bed leveling spring onto the screw stick out. Then twist on a large bed leveling dial (included with the Ender). Tighten until there are a few phillips threads visible sticking out past the dial. Precise adjustmenet of the bed leveling dial will occur later.

*Include image of the 3D printed base on the print bed with screws through them. Include side image of the dial on the phillips screw with spring in proper compression*

Each chuck is designed to fit into the center cavity. For testing and calibration, install the 6 inch chuck.

*Include image of installed 6" chuck*

#### Step Step 2.1.3: Print and Install Parts For Syringe Head

There are three 3D printed components required for the syringe head:

- 005_Syringe_Holder_Body
- 006_Syringe_Holder_Rack
- 007_Syringe_Holder_Pinion 

<details>
  <summary> Click here for a details about 3D printing orientation and settings
  <br></br>
  </summary>
   
  TODO: Include pictures of recommended print orientation and print settings for the  components. This should be a copy from the complete 3D print list above.

</details>

First, use three XX mm long MX screws included with the hot end to mount the Syringe Holder Body onto the gantry, as pictured below.

*Include image of the syringe holder body mounted on the gantry*

Next, use XXX M3 screws included with the extruder stepper motor to mount the extruder stepper motor onto the backside of the syringe holder body, as pictured below. Make sure the stepper motor cable points in the direction away from the LCD panel. 

*Include image of the syringe holder body and stepper motor*

Press fit the 3D printed pinion on to the stepper motor shaft. It should fit snuggly. If the pinion is too loose, wrap a layer of tape evenly around the shaft and try press fitting again. If the pinion does not fit on the shaft (hole is too small), file/sand down the hole until it fits.

*Show image of the pinion press fit onto the stepper shaft*

Lastly, slide the rack into the syringe holder body. Insert the two dovetails on the back of the Syringe Holder Rack into the dovetail slots on the top of the Syringe Holder Body. Press the rack down until its teeth make contact with the pinion. Continue pushing the rack down, causing the pinion to interface with the rack and begin spinning. Push the rack all the way down until the small arm collides with the Sryinge Holder Body's ledge and prevents it from going further. There should be some friction/resistance to pressing the dovetails together, especially the first time they're connected. 

*Show two images of the rack, one of it getting inserted into the top, and the other of it bottomed out.

### 2.2 Enclosure Manufacturing

*Insert CAD rendering of finished enclosure*

The enclosure is built from laser-cut acrylic panels. A fan mounted on top of a ULPA filter blows clean air into the top of the enclosure. Slots cut into the bottom of the enclosure allow the clean air to escape out the bottom, ensuring laminar, downward flow throughout the entire box. A power supply mounted on the back of the ULPA filter powers the fan and LED lights. The box and scanner is enabled/disabled by a single power switch mounted on the side. The front panel is split in three parts, all mounted on the front of the box by magnets. This allows easy access during routine operation, and the ability to completely remove the scanner during installation and cleaning. The bottom of the enclosure has a teflon film to protect the acrylic from HF splashes.

The complete CAD assembly is availible in the CAD/enclsoure folder. All individual parts are also availible as STEPS and F3Ds.

**Step 2.2.1: Cutting Acrylic Panels**

There are 8 pieces that must be cut from the acrylic side panels:
- Left panel
- Right panel
- Back panel
- Bottom panel
- Top panel
- Front top panel
- Front middle panel
- Front bottom panel

All DXFs for the panels are in the [XXX/XXX folder]().

We  strongly suggest using a laser cutter to cut the acrylic side panels given acrylic cement needs flush edges to form a proper bond. The layout of the DXFs depends on the bed size of your laser cutter. The Stanford Nanofab has a 32"x20" laser cutter which allowed us to cut the panels in the following layout:

*Insert screenshot of the lasercutting layout*

As mentioned in the drop down section under Enclosure Components, the largest panels are 23.5" x 19.5". Make sure your laser cutter bed is large enough to accomodate those panels.

Do not cut panels out of the corner of your plastic; i.e. don't bump your cuts right up against the edge of your plastic sheet. The laser used to cut the plastic has a certain kerf which affects the final dimensions of the part by a few tenths of a mm. The enclsoure was designed to cancel out these errors, so long as all edges are affected the same amount. If some of the panel edges are laser cut and others are saw cut (from the factory/store), you may end up with gaps that the acrylic cement cannot bond.

*Include image showing proper and improper arrangement of panels relative to plastic sheet*

**Step 2.2.2: Acrylic Enclosure Welding**

Acrylic weld is a super runny solvent that dissolves the two edges it comes into contact with, chemically bonding them together. When done properly, acrylic weld leaves strong and aesthetic bonds. When done improperly, acrylic weld fails to join the two edges and the joint breaks easily. 

The most important step to take to get good acrylic weld joints is *making sure the two edges are flush.* Acrylic weld works through capillary action, when you apply a drop to the corner, it should spread across the seam thanks to capillary forces. This is only possible if the two edges are perfectly flat against each other. If there is a small gap (<0.5mm) the acrylic weld will not properly dissolve the two edges together and no bond will form. 

Note that acrylic weld produces bad fumes that cause a bad headache; use it outdoors or in a well ventilated room. 

**Step 2.3: Mounting Magnets**

**Step 2.4: ULPA Filter Installation**

**Step 2.5: Blower Fan Installation**

**Step 2.6: LED Light Installation**

**Step 2.7: Power Switch Installation**

**Step 2.8: Power Supply Mounting and Wiring**

**Step 2.9: Teflon Base Installation**

## Step 3: Scripting

### Scription Overview

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
4) Remove the sd card from your computer and plug it into the micro sd port on the front, bottom, left black controller box (underneath the scan bed).

The GCODE routines are now loaded on the printer and ready to run. To execute one, turn the scanner on. After the initialization screen, use the scroll wheel to navigate to "Print from SD." Click the scroll wheel to select it, then select the desired routine.

## Calibration

*TODO: Explain how to perform a leach test. Explain our results*

*TODO: Explain how to perform a recovery test*

*TODO: Explain our recovery results*

## Standard Operation

*Information about installment in a fumehood*

*How we process, store, and run tests with the SIGMA lab*

*Connecting to NEMO*

## Misc

### License

This project is licensed under the MIT License. See the LICENSE file for more details.