# Low-Cost, DIY Vapor Phase Decomposition (VPD) Scanner for Trace Metal Detection on Surface of Wafers

*Insert GIF of the scanner operating*

## Introduction
Vapor phase decomposition (VPD) is a process used in the semiconductor industry to quantify trace metal contaminants on the surface of wafers. This GitHub repo provides the first open-source instructions to manufacture, program, and install a VPD capable of XXX atoms/CM^2 measurements for academic cleanrooms. 

This project was created by Alex Denton, Trevor, and Thomas Rimer at the [Stanford Nanofabrication Facility](https://snf.stanford.edu/). All ICP-MS analysis was performed by Karrie Weaver and Kathleen Akbar at the [SIGMA lab](https://sigmalab.stanford.edu/).

<img src="Misc/README Resources/SNF_logo.png" alt="SNF Logo" width="100" style="padding-right: 10px;"/> <img src="Misc/README Resources/sigma_logo.png" alt="SIGMA Logo" width="100" style="padding-left: 10px;"/>

## Overview

*Insert image of the scanner sitting inside its box in a fume hood*

VPD (vapor phase decomposition) is a technique to collect metal and chemical contamininats on the surface of a wafer into a liquid droplet. The details of this collection process are explained in the "Operating Principles Section" right below. Crucially, VPD *does not* involve the measurement or quantification of chemicals; it's simply a technique (among many) to collect them. That's where ICP-MS comes in...

ICP-MS stands for "Inductively Coupled Plasma Mass Spectroscopy." It's one of the most sensitive techniques for measuring the conentration of metals and other chemicals in liquid solutions. Check out [this video](https://www.youtube.com/watch?v=tP5ZKUTWiuQ) from Agilent (an ICP-MS tool manufacturer) to learn about the basic operating principles of an ICP-MS. Briefly, the liquid sample is aerosolized before getting ionized by a plasma. Metals in the solution are then sorted and counted based on their charge/mass ratio. 

When VPD and ICP-MS are combined, it's called VPD-ICP-MS. Note that VPD doesn't necessarily need to use ICP-MS for analysis; alternatives like Atomic Absorption Spectroscopy (AAS) are also common. Similarly, VPD is not the only way to collect samples for ICP-MS; anything from blood to seawater to colloidal space dust can be measured in an ICP-MS.

Using the provided instructions outlined below, the entire VPD scanner and its enclosure can be built in <XXX hours for $X,XXX. Detailed information on the VPDs performance is availible in the [Performance](#performance) section.

## Operating Principles

The VPD scanner is based on a modified 3D printer; instead of a hot-end to extrude plastic, it has a motor-controlled syringe. To scan a wafer, the syringe first aspirates ~200 uL of an HF/H2O2/Water solution. Then it lowers to the surface of the wafer and dispenses the solution, forming a droplet on the surface of the wafer. Crucially, the droplet remains connected to the tip of the syringe. Over the course of 5-15 minutes (depending on wafer size), the scanner slowly moves the syringe head in a series of expanding concentric rings, dragging the droplet across the entire surface of the wafer. The HF in the scan solution attacks the ~2nm native oxide on the wafer's surface, dissolving any contaminants on the surface (and first few layers of SiO2). Finally, the scanner sucks up the droplet from the surface and dispenses it in a collection cuvette, for later analysis by an ICP-MS.

This droplet-dragging technique is similar to what's found in commercial VPD machines. However, there are a few differences worth noting:

**Vapor Etching:** As the name "Vapor Phase Decomposition" might suggest, commerical VPDs use an HF vapor to etch the entire surface of the wafer at once, before the droplet scan commences. This VPD scanner relies on aqueous HF within the scan solution to etch and collect the contaminants at the same time, avoiding the vapor etching step.

**Full Automation:** A human user is needed for setup and sample transfer for this DIY VPD. Most commercial VPDs have fully automated setups which allow for seamless integration into production lines.

**Speed:** While our machine takes ~20+ minutes to process a wafer, a commercial machine can often complete a scan in <60 seconds.

## Imporant Notes

**Analysis**: As hinted at above, this project assumes you have access to an ICP-MS or similarly sensitive tool to analyze the samples. The VPD scanner itself has no capacity to analyze the droplets it collects. More information about the ICP-MS analysis—along with alternatives—are detailed in the XXX section below. 

**Safety**: This project relies on hydrofluoric acid (HF) for the collection solution. HF is an extremely toxic chemical; if you need to google why, this project is *not* for you.

**Setup**: This machine produces HF vapor and should therefore be operated inside a fume hood. The minimum fume hood space required is 20" wide, 25" deep, and 42" tall. Note that the enclosure built for the scanner (detailed below) is NOT a fume hood; it is a positvely pressurized chamber to keep the VPD free of contaminats. If the enclosure is placed outside of a fume hood it will pump HF fumes at the operator and surrounding environment!

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
5) After characterization, the VPD is ready for users! [Standard Operation](#tunning-your-first-test) offers advice on installement, intermittent calibration, and other practical guidelines for transporting samples to the ICP-MS for analysis. 
6) [Misc](#misc) contains credit and license information.

All aspects of the manufacturing process are designed to be as accessible as possible. However, it's assumed that some basic tools are availible for fabrication. Below is a list of the required materials:

- 3D printer (minimum bed size: 8" x 8" x 3")
- Laser cutter (minimum bed size: 24" x 20")
- Phillips screwdriver
- Metric allen keys
- Soldering iron
- Scissors
- Tape

### Contact Us

If you've read this far, you're probably pretty interested in VPD. Please reach out if you're thinking about building a scanner, have questions about the build process, or have issues with your own DIY-VPD! We're excited to get these into as many labs as possible! We ask you use the "Issues" tab on GitHub to ask questions (even if it's not strictly an "issue"). This will allow other people thinking of building a VPD to see who else is interested, what they're thinking, and problems they're encountering.

## Step 1: Procurement

*Every good project starts with a McMasterr Carr order; the VPD scanner is no different.*

Below are three tables, each with a set of components. The "Scanner Components" are used to build the scanner itself. The "Enclosure Components" are used to build the enclosure around the scanner. The "Experimentation Supplies" are the consumables needed to actually run experiments. All prices are approximate, as of July 2024.

All components in the first two tables can be purchased from  McMaster Carr or Amazon. However, the strict purity requirements for the sample collection means many of the experimentation supplies must be ordered directly from suppliers.

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

  **Ordering notes**: Feel free to purchase the Ender 3 from any website. Note that there are different versions of the Ender 3 (Ender 3s, Ender 3 pro, etc...) Make sure you purchase the Ender 3 to ensure the syringe head 3D prints fit the gantry. If you do order from a different supplier, make sure it comes with a MicroSD card. If not,  order a micro SD card seperately.
  
  **Alternatives**: Using any other 3D printer will almost certainly mean a complete redesign of all mechanical components, including the clean enclosure (unless the alternative printer is smaller than the Ender 3). Additionally, the scan programs would no longer work, meaning you'd need to generate your own using the custom routine builder included in this repo. If there were one component in this build we'd suggest not replacing, it's the Ender 3 printer. 

  ### Filament
  **Ordering notes**: Any brand of 3D printer filament will work just fine. Because the 3D prints should never come in contact with the scan solution, it does not matter what plastic you use. We recommend PLA for its ease of printing. However, PolyMax filament from PolyMaker has repeatedly proven itself as the most durable filament based on our testing, so we think it's worth purchasing. 
  
  **Alternatives**: If you're feeling ambitious, some/all 3D printed components can be machined out of teflon. This will provide excellent chemical resistance and durability. Stanford actually has a version of the scanner with custom machined teflon components. Finding a teflon machine shop, creating engineering drawings, and managing the manufacturing process is not discussed in this guide.
</details>


### Enclosure Components
| Item | Price per Unit | Units | Subcost | Link | Use
|----------|----------|----------|----------|----------|----------|
| Acrylic Plastic Sheet    | $57     | 7     | $400 | [McMaster](https://www.mcmaster.com/8560K357/) | Clear panels cut to form enclosure walls. 24"x24", 1/4" thick
| Blower fan    | $92     | 1     | $92 | [McMaster](https://www.mcmaster.com/2059K36/) | Forces air through the filter, positively pressurizing the enclosure
| ULPA Filter    | $285     | 1     | $285 | [McMaster](https://www.mcmaster.com/5543N11/) | Removes 99.999% of particulate <0.3um in the air entering the box
| Teflon Film    | $21     | 3ft     | $63 | [McMaster](https://www.mcmaster.com/8569K63/) | Protects enclosure against HF splashes
| Slow Cure Epoxy    | $14     | 1     | $14 | [Amazon](https://www.amazon.com/Bob-Smith-Industries-BSI-205-Slow-Cure/dp/B0166FFFS4/) | Joins the acrylic side panels together
| Magnets    | $0.90     | 16     | $14 | [McMaster](https://www.mcmaster.com/5862K103/) | Magnetically joins the front panels to the enclosure box
| Fast Cure Epoxy Resin    | $5     | 1     | $5 | [Amazon](https://www.amazon.com/Gorilla-Epoxy-Minute-ounce-Syringe/dp/B001Z3C3AG/?th=1) | Bonds 3D prints to the acrylic enclosure sidewalls
| Silicone Caulk    | $7     | 1     | $7 | [Amazon](https://www.amazon.com/GE-Advanced-Silicone-Kitchen-Bathroom/dp/B0C9VYYCPB/?th=1) | Non-permanent bond for filter components
| 12v Power Supply    | $26     | 1     | $26 | [Amazon](https://www.amazon.com/LRS-200-12-Switching-Supply-Single-Output/dp/B0131UU9E2/?th=1) | Powers the blower fan and LED strips
| LED Light Strip    | $21     | 1     | $21 | [Amazon](https://www.amazon.com/TOPAI-Waterproof-Brightness-2400LEDs-Cuttable/dp/B0BVR996T2/) | Illuminates inside of the box
| Power Switch    | $8     | 1     | $8 | [Amazon](https://www.amazon.com/mxuteuk-Illuminated-Household-Appliances-MXU3-101NR/dp/B07QQ21CZD/) | Toggles power to enclosure and scanner
| Power Cable    | $6     | 1     | $6 | [Amazon](https://www.amazon.com/Amazon-Basics-Computer-Monitor-Replacement/dp/B072BYGKZZ/?th=1) | Cannabilized into master power cable for scanner and enclsoure

Enclosure Components Subtotal: **~$950**

<details>
  <summary> Click here for details about Scanner Components, alternatives to certain items, and other comments</summary>
   
  ### Acrylic Plastic Sheets

  **Ordering notes**: Minimum sheet size is 23.5" x 19.5." We recommend NOT purchasing the plastic through McMaster. Instead, find a local plastic shop or hardware store that sells acrylic sheets. We purchased all our acrylic from TAP plastics; if you're in the San Francisco Bay Area, this is by far the best place to pick up material. Local shops will also cut stocks down to a size convenient for you; for example, we had TAP cut all our acrylic down to 32"x20" sheets to fit our laser cutter. 
  
  **Alternatives**: As the most expensive building material, it's tempting to find alternatives. Theoretically, any plastic enclosure that can fit the 3D printer inside and can have holes cut in it for ventilation would work. However, the clear material makes viewing the operation of the machine much easier. 

  ### Blower Fan

  **Alternatives**: If you plan on using a different blower fan, know that there are a few important considerations. First, make sure it runs on the same voltage as the power supply (and thus by extension LED lights) to avoid needing a second PSU. Second, a multi-speed blower fan is ideal to allow standby and operating blowing speeds. Lastly, a different blower fan will need a redesigned fan shroud to couple the fan output to the ULPA filter.

  ### ULPA Filter
  
  A ULPA filter was selected over a HEPA filter for its increased filtering power. We recommend using ULPA filters to lower the chance of airborne contaimination. 

  The ULPA filter linked in the table is very large and should last for years. Base your spare ordering on that working time. For what it's worth, Stanford did not purchase any spare filters.

  **Alternatives**: If you have spare, clean ULPA filters availible from another source, feel free to use them. Just note that you will need to change both the hole size in the top of the container and fan shround to couple the blower air into the filter. Also make sure the filter is not too restrictive to air flow, else you'll need to replace the blower fan.

  ### Teflon Film

  Teflon is one of a few materials resistant to HF, so this thin sheet will sit on the bottom of the acrylic enclosure to protect it from minor HF splashes.

  **Ordering Notes**: The protective sheet used on the bottom must be made from teflon. However, any brand or supplier will work fine. 

  ### Slow Cure Epoxy

  This slow cure epoxy has a long working time allowing you to fully assemble the enclosure with epoxy in the joints before it cures.

  **Alternatives**: Any long-cure (>30 min working time) will work. For aesthetic reasons we recommend a clear-drying epoxy. When building enclosures with acrylic, it's also common to see acrylic cement used; we attempted this with our enclosure and decided not to use it due to the strict edge flatness requirements. We would discourage working with acrylic cement unless you are already familiar with it. Do NOT try and use quick curing epoxy to build the enclosure, it will set before you finish assembling the enclosure.

  ### Magnets

  **Ordering notes**: The magnets are so inexpensive we recommend ordering and using the suggested ones.

  ### Fast Curing Epoxy Resin

  Rather than the slow curing epoxy, this resin is used for joining the plastic 

  **Ordering Notes**: Brand or size of epoxy resin does not matter; it will work so long as it's a general purpose epoxy designed to bond metal and plastic.

  **Alternatives**: Feel free to not order any fast curing epoxy and instead use the slow curing epoxy. Just know you'll need to wait longer for plastic parts to adhere to the acrylic, which means you'll probably need to tape them on (rather than being able to hold them against the the walls).

  ### Silicone Caulk

  **Ordering Notes**: Brand or size of the silicone caulk does not matter; feel free to purchase from a local hardware store or use a tube laying around the lab (as long as it hasn't gone bad).

  ### Power Supply

  **Ordering Notes**: Any 12v power supply will do as long as its current rating matches or exceeds the sum of the blower fan and LED light requirements.

  **Alternatives**: If you use a different LED light strip or blower fan that does not use 12v, you will need to find a new power supply accordingly. The common, rectangular, thin power supply housing type (same as the PSU linked in the table) is preferred due to its ease of mounting on the back of the ULPA filter later on.

  ### LED Lights

  While the LED lights are not necessary, they improve visibility of the VPD scanner and make it cooler.

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

*Insert labeled rendering of the final assembly*

The VPD scanner has two sub assmblies; the scanner and the enclosure. Each can be built independently of the other, making it convienent to split up amongst multiple people.

There are XX 3D prints requried for this project. To minimize the amount of time spent waiting for 3D prints to finish, we recommend printing all the parts before beginning any other manufacturing and assembly. 

Tehcnically, you can 3D print all components on the Ender 3 printer purchased for the scanner. This is recommended only if you have limited access to other printers. If you decide to 3D print the components on the Ender 3, you should first fully assemble the 3D printer following the video in [Step 2.1](#step-2-1) (not skipping any steps). Then, print all components (as outlined below) before continuing on the project. Know that once you've modified the printer into the scanner, it will take around an hour to uninstall the VPD parts and restore the Ender to a print-worthy state. 

<details>
  <summary> Click here for a complete list of required 3D printed parts, their associated quantities, and recommended print settings/orientations</summary>
   
  TODO: Add the complete list of STL files and how many need to be made.

</details>

### 2.1 Scanner Manufacturing

*Insert photograph of finished scanner*

#### Step 2.1.1: Assembling the Ender 3s

The Ender 3s comes partially assembled from the factory. There are several high-quality YouTube tutorials already made outlining exactly how to assemble an Ender 3. Here's a well-made one from [3D Printing Canada](https://www.youtube.com/watch?v=dQ0q9zLygTY) (https://www.youtube.com/watch?v=dQ0q9zLygTY).

While most of the build proceeds as normal, there are a few steps you should <ins>not</ins> do:

- Do not install the spool holder.
- Do not mount the extruder stepper motor on the bracket designed for it. However, you should still wire the stepper to the controller board. The extruder stepper motor will be used later on to control the syringe.
- Similarly, do not install the spring-loaded extruder gear assembly. This is not needed for the VPD.
- Do not mount or screw in the bed leveling adjustment dials. These will be installed later.
- Do not binder-clip the Ender-branded build surface onto the print bed. Parts will mount directly onto the print bed later, so this build surface is not needed.

Save all components (and spare parts) that you do not install. You will need some of these materials later.

#### Step 2.1.2: Print and Install Parts For Wafer Holder

There are three necessary 3D printed components for the wafer holder, and an additional five optional 3D printed components:

Required
- 001_Wafer_Holder_Base.stl
- 002_Wafer_Vial_Holder_Left.stl
- 003_Wafer_Vial_Holder_Right.stl

Optional
- 004_Wafer_Holder_2_inch_Chuck.stl
- 005_Wafer_Holder_3_inch_Chuck.stl
- 006_Wafer_Holder_4_inch_Chuck.stl
- 007_Wafer_Holder_5_inch_Chuck.stl
- 008_Wafer_Holder_6_inch_Chuck.stl

<details>
  <summary> Click here for a details about 3D printing orientation and settings
  <br></br>
  </summary>
   
  TODO: Include pictures of recommended print orientation and print settings for the  components. This should be a copy from the complete 3D print list above.

</details>

At least one optional component must be printed to use the wafer holder. 

Place 001_Wafer_Holder_Base on the print bed, alligning the the holes in each corner with the screws holes in the aluminum bed. The two cylindrical cavities should face the front of the printer. The two lock diagrams should be in the back of the printer. Slide the included bed-leveling screws through the four screw holes in each corner of the Wafer Holder Body, making sure it also goes through the metal print bed. Underneath each corner, slide a bed leveling spring onto the screw stick out. Then twist on a large bed leveling dial (included with the Ender) onto each corner. Tighten until there are a few phillips threads visible sticking out past the dial. Precise adjustmenet of the bed leveling dial will occur later.

*Include image of the 3D printed base on the print bed with screws through them. Include side image of the dial on the phillips screw with spring in proper compression*

All 5 of the optional wafer chucks are adapters designed to hold specific diameters of wafer. Print whichever sizes you anticipate needing to scan (Stanford printed all 5 of them just in case).

*Include image of installed 6" chuck*

The wafer chuck twists into place on the base. To install a chuck, place it on the base 45° off from the base such that the small bump in the middle of the base intefaces with the divot on the underside of the chuck. Rotate the chuck counter clockwise, causing the dovetails on each arm of the base to interface with the slots on the chuck. Continue twisting until the chuck flushly sits atop the base.

To uninstall a chuck, simply press the chuck in the clockwise direction. It should pop out easily. Sometimes, it can help to press on two arms at once.

#### Step Step 2.1.3: Print and Install Parts For Syringe Head

There are three 3D printed components required for the syringe head:

- 0XX_Syringe_Holder_Body.stl
- 0XX_Syringe_Holder_Rack.stl
- 0XX_Syringe_Holder_Pinion.stl

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

#### Step Step 2.1.3: Print and Install Fan Ducting

There are two 3D printed ducts required for the printer:

- 0XX_Controller_Duct.stl
- 0XX_Power_Supply_Duct.stl

<details>
  <summary> Click here for a details about 3D printing orientation and settings
  <br></br>
  </summary>
   
  TODO: Include pictures of recommended print orientation and print settings for the  components. This should be a copy from the complete 3D print list above.

</details>

These ducts prevent dust raised from the 3D printer's cooling fans from contaminating the interior of the clean enclsoure. 

To mount the controller duct, apply silicone to the hatched, flat face on the controller duct 3D print. Press the duct on to the controller housing such that to encapsulates the fan exhaust port, and the other end of the duct points to the left side of the machine. Tape the duct in place while the silicone cures to prevent the duct from falling over. 

*Include an image of the installed controller duct*

To mount the power supply duct, apply silicone to the hatched, flat face on the power supply duct 3D print. Press the duct onto the silver power supply such that the duct runs down the power supply and exhausts next to the base of the printer. Tape the duct in place while the silicone cures to prevent the duct from sliding down the power supply.

*Include an image of the installed power supply duct*

### 2.2 Enclosure Manufacturing

*Insert CAD rendering of finished enclosure*

The enclosure is built from laser-cut acrylic panels. A fan mounted on top of a ULPA filter blows clean air into the top of the enclosure. Slots cut into the bottom of the enclosure allow the clean air to escape out the bottom, ensuring laminar, downward flow throughout the entire box. A power supply mounted on the back of the ULPA filter powers the fan and LED lights. The box and scanner is enabled/disabled by a single power switch mounted on the side. The front panel is split in three parts, all mounted on the front of the box by magnets. This allows easy access during routine operation, and the ability to completely remove the scanner during installation and cleaning. The bottom of the enclosure has a teflon film to protect the acrylic from HF splashes.

The complete CAD assembly is availible in the CAD/enclsoure folder. All individual parts are also availible as STEPS files, STLs, OBJs, and F3Ds.

**Step 2.2.1: Cutting Acrylic Panels**

There are 8 acrylic side panels that must be cut from the acrylic sheets:
- Left panel
- Right panel
- Back panel
- Bottom panel
- Top panel
- Front top panel
- Front middle panel
- Front bottom panel

All patterns for the panels are in the [XXX/XXX folder](). Each panel is provided in both DXF and SVG format.

We  strongly suggest using a laser cutter to cut the acrylic side panels. Stanford used a 120 watt Trotec SP500 Laser Cutter to make all the panels, which took about 3 hours. Nearly every university has a maker space with a free-to-use laser cutter. 

The layout of the panels on the acrylic sheets depends on the size of the acrylic sheets (which in turn cannot be any larger than the bed of the laser cutter). The acrylic sheets Stanford purchased were 32"x20". Thus, the following layout was used.

*Insert screenshot of the lasercutting layout*

As mentioned in the drop down section under Enclosure Components, the largest panels for the enclosure are 23.5" x 19.5". Make sure your laser cutter bed is large enough to accomodate those panels, and the acrylic sheets you purchase are also larger.

When cutting the panels with the laser cutter, do your best not to position the cuts right along the edge of the acrylic side panel. The laser used to cut the plastic has a certain cutting width which affects the final dimensions of the part by a few tenths of a mm. The enclsoure was designed to cancel out these errors, so long as all edges are affected the same amount. If some of the panel edges are laser cut and others are saw cut (from the factory/store), you may end up with gaps that make assembly harder.

*Include image showing proper and improper arrangement of panels relative to plastic sheet*

If desired, a custom logo can be engraved in any of the side panels for decoration. Stanford etched the "SNF" logo onto the left panel. This is totally optional but can make the enclsoure look even better.

**Step 2.2.2: Acrylic Enclosure Bonding**

To bond the enclosure together, we recommend first doing a practice run with just tape. It's best to addemble the enclosure with two people (so someone can hold a side panel while the other person tapes it). Below are instructions paired with CAD renderings of the enclosure bonding process. Note that colors are for illistrative purposes.

Begin by placing the base panel on a large, flat table. 

<img src="Misc/README Resources/Acrylic Enclosure Renders/base.png" alt="Base" width="300" style="padding-right: 20px;"/>

Next, stand up the right panel on a long side of the base. The vents should be close to the base. The right panel should be flush with the side of the base, and each end of the right panel should line up with the front and back of the base. The rounded rectangular hole denotes the back of the enclosure. 

<img src="Misc/README Resources/Acrylic Enclosure Renders/base_right_1.png" alt="Base and Right Panel 1" width="300" style="padding-right: 20px;"/> <img src="Misc/README Resources/Acrylic Enclosure Renders/base_right_2.png" alt="Base and Right Panel 2" width="300" style="padding-right: 20px;"/>

Next, stand up the back panel along the back side. The back panel should be flush with the back edge of the base, and the right end of the back panel should be flush against the inside of the right panel. The vents should be at the bottom. The left end of the back panel should not be flush against the left edge of the base (there is a 1/4" gap for the left panel to mount). Use small pieces of masking tape on the outside of the enclsoure to secure the right and back panels to the base, as well as to one another. After taping, the enclsoure should be able to stand on its own. 

<img src="Misc/README Resources/Acrylic Enclosure Renders/base_right_back_1.png" alt="Base, Right, and Back Panel 1" width="300" style="padding-right: 20px;"/> <img src="Misc/README Resources/Acrylic Enclosure Renders/base_right_back_2.png" alt="Base, Right, and Back Panel 2" width="300" style="padding-right: 20px;"/>

Next, stand up the left panel along the remaining long side of the base. It should be in the same orientation as the right side panel, with the vents towards the bottom and the rounded rectangular port in the back. Tape the left side panel to the back and base.

<img src="Misc/README Resources/Acrylic Enclosure Renders/base_right_back_left_1.png" alt="Base, Right, and Back Panel 1" width="300" style="padding-right: 20px;"/> <img src="Misc/README Resources/Acrylic Enclosure Renders/base_right_back_left_2.png" alt="Base, Right, and Back Panel 2" width="300" style="padding-right: 20px;"/>

Finally, place the top panel on top of the top edges of the left, back, and right panels. If the previous steps were done correctly, all three edges should be level with one another. The small holes in the top panel should be in the back. Tape the top panel on to the left, right, and back panel.

<img src="Misc/README Resources/Acrylic Enclosure Renders/base_right_back_left_top_1.png" alt="Base, Right, and Back Panel 1" width="300" style="padding-right: 20px;"/> <img src="Misc/README Resources/Acrylic Enclosure Renders/base_right_back_left_top_2.png" alt="Base, Right, and Back Panel 2" width="300" style="padding-right: 20px;"/>

To permanently bond the pieces, repeat the same taping process, but add epoxy to the edges at each step.

Begin by dissambling the taped structure. When you are ready, mix the long-cure epoxy according to the instructions on its package. You'll have about 15 minutes after mixing to fully assemble the enclosure. Get some friends to help out. Repeat the same taping process described above, but use a popsicle stick or a finger to spread a liberal amount of epoxy along each edge before taping them up. After taping, some epoxy should leach out of the edges. Quickly wipe up the epoxy with a dry paper towel, and follow up with a cold damp paper towel at the end to get any remaining epoxy. 

Leave the box undisturbed in a corner for 24 hours before attempting to remove the tape. It will take a few days before the epoxy has reached its full mechanical strength.

**Step 2.2.3: Mounting Front Panels**

There are eight 3D printed parts required for the front panels:

- 6x 0XX_Magnet_Mount.stl
- 2x 0XX_Handle.stl

<details>
  <summary> Click here for a details about 3D printing orientation and settings
  <br></br>
  </summary>
   
  TODO: Include pictures of recommended print orientation and print settings for the  components. This should be a copy from the complete 3D print list above.

</details>

The front panel is comprised of three smaller sections

- Lower panel (4" tall)
- Middle panel (8" tall)
- Upper panel (8" tall)

Each panel is fixed to the front with a 3D printed magnet mount. This allows for it to be easily removed when accessing or installing the scanner. 

Begin by affixing magnets inside their mounts. Stack all magnets in a stick. This will allign them relative to one another. Mix a small amount of fast cure epoxy and dab it on the bottom of the hole with a toothpick or similar thin object.

**Step 2.2.4: ULPA Filter Installation**

**Step 2.2.5: Blower Fan Installation**

**Step 2.2.6: LED Light Installation**

**Step 2.2.7: Power Switch Installation**

**Step 2.2.8: Power Supply Mounting and Wiring**

**Step 2.2.9: Teflon Base Installation**

### 2.3 Install Scanner Inside Enclsoure

After both the scanner and enclosure have been built, they're ready to be put together!

**Step 2.3.1: Place Enclosure Inside Fume Hood**

The entire clean enclosure must be placed inside a fumehood with proper HF fume extraction to ensure the positively pressurized clean enclosure doesn't poison surrounding users. The minimum required fumehood space is 20" wide by 25" deep by 42" tall.

**Step 2.3.2: Clean the Enclosure**

Use Isopropyl alcohol and a Kimtech (or similar low-lint) wipe to clean all surfaces on the interior of the enclsoure. This prevents dust built up from the fabrication process from dislodging and contaminating the scanner later in its life.

**Step 2.3.3: Clean the Scanner**

For the same reasons as the enclosure, use Kimtech and IPA to wipe down all surfaces on the 3D printer. Particularly focus on the belts used to drive the two axes; these are often prone to shedding lots of particulate. Avoid using excessive IPA near electronics. 

**Step 2.3.3: Place Scanner Inside Enclosure**

Remove all magnetic front panels from the enclosure and place the scanner inside the enclsoure. The LCD panel on the scanner should face the the front opening (where all the magnetic front panels just were). Center the scanner in the middle of the enclosure (left-to-right and front-to-back). Verify the scanner is properly positioned by slowly moving the bed front to back. It should be able to travel its entire length without hitting the back of the enclsoure or passing outside the front (where the magnetic panels would be mounted).

**Step 2.3.4: Plug in the Scanner**

Pass the 3D printer's power supply through one of the rounded rectangular ports on the bottom back left and right side of the 

## Step 3: Scripting

### Scription Overview

*Download the GitHub repo to your computer to access and run the scripts*

After fabricating the VPD scanner, you need to control it. The printer runs on GCODE, a human-readable, tool-control language where each line corrosponds to motor movements (or modification to a movement). There are three options for generating GCODE files, each with greater flexibility at the cost of greater complexity:

<details>
  <summary> Click here for Pre-generated Routine instructions (easiest) (recommended): <br></br></summary>

  ### Pre-Generated Routines

  Pre-generated routines are, as the name suggests, scan programs that have already been written and tested on the scanner. All testing, characterization, and normal operation of the VPD can be run from the pre-generated routines provided in this GitHub. The pre-generated routines require no programming or terminal commands.

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

  To use the pre-generated routines, just make sure you've downloaded the GitHub repo.

  Follow the the instructions in 'Uploading Routines to the Scanner' to send the regenerated routine to the scanner. 

  **Only reason not to use pre-generated routine:** As mentioned above, we strongly recommend using the pre-generated scan routines, with the one exception of scanners built on any printer aside from the Ender 3; other 3D printers will have different physical travel limits which means using a default scan could crash the syringe into the print bed. If a different printer is being used, you'll need to create a Custom Routine.

</details>

<details>
  <summary> Click here for Re-Generated Routine instructions (more difficult): <br></br></summary>

  ### Regenerated Routines

  Regenerated routines are scan programs that are generated by the user using the regenerate_scan.py Python script provided in the GitHub repo. After executing the script with the desired custom parameters, the script will produce a program file which can be uploaded to the scanner. 

  To regenerate a routine based on your desired parameters, first ensure you've downloaded the GitHub repo. Navigate to the 'regenerated_routines' directory in terminal. For example...

  ```console
  foo@bar: cd /Users/thomas-rimer/Desktop/DIY-VPD/regenerated_routines
  ```

  To ensure you're in the right directory, type

  ```console
  foo@bar: ls
  ```

  which lists all files in your current directory. You should see 'regenerate_default_scan.py' as the only file to show up.

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

</details>

<details>
  <summary> Click here for Custom Routine instructions (most difficult): <br></br></summary>

  ### Custom Routine

  If you would like to write your own custom scan routine, you can with the 'generate_custom_routine' script in the same folder. This will allow you to create a routine with any sort of movement, aspiration, or dispensing. A custom routine requires several (10+) lines of python and a terminal command.

  *TODO: Write detailed instructions for how to generate Custom Routine*
  

</details>

### Uploading Routines to the Scanner

The scanner uses the original 3D printer interface to run routines. Routines are saved in the file format GCODE. To upload a routine (i.e. GCODE file) to the scanner

1) Plug the micro sd card into your computer using the provided micro sd to usb adapter.
2) If it's your first time uploading a routine, delete all existing files (if there are any) on the sd card.
3) Transfer desired gcode files from the pregenerated, regenerated, or custom folder onto the sd card (depending on which route you took). For example, if you plan on using just pregenerated routines (recommended) on 4" and 6" wafers, just upload '4_inch_wafer_scan_pre_generated.gcode' and '6_inch_wafer_scan_pre_generated.gcode' to the SD card.
4) Eject the sd card from your computer and plug it into the micro sd port on the front, bottom, left black controller box (underneath the scan bed).

The GCODE routines are now loaded on the printer and ready to run.

### Running Routines

To execute a routine that's been uploaded to the SD card:
1) **Turn on the scanner** (i.e. 3D printer) using the red power switch on the right side of its frame.
2) **Wait for the LCD to finish loading**. After a few loading screens the front LCD should show a home with some miscellanous information. This is all a remanant of the previous 3D printer operating system and is not relevant for the scanner. 
3) **Pull up the action menu** by pressing into the selection knob. It should click when pressed.
4) **Select "Print from SD"** by rotating the selection knob so the selection highlight is over "Print from SD." Press the knob again to select
5) **Select the desired scan routine to run** from the list of routines saved to the SD card. Use the same rotate and press selection method from above.

The scanner should begin the routine within a few seconds of selecting it.

## Step 4: Characterization

At this point, the scanner is ready to

*TODO: Explain how to perform a leach test. Explain our results*

*TODO: Explain how to perform a recovery test*

*TODO: Explain our recovery results*

## Step 5: Standard Operation

*Information about installment in a fumehood*

*How we process, store, and run tests with the SIGMA lab*

*Connecting to NEMO*

## Step 6: Misc

### License

This project is licensed under the MIT License. See the LICENSE file for more details.