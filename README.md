# Low-Cost Vapor Phase Decomposition (VPD) Scanner for Trace Metal Detection on Surface of Wafers

*Insert GIF of the scanner operating*

## Introduction
Vapor phase decomposition (VPD) is a common technique used in the semiconductor industry to collect trace contaiminates on the surface of wafers into a droplet. When paired with an ICP-MS (a common instrument for measuring low concentrations of chemicals in liquid solutions), a 'VPD-ICP-MS' enables users to quantify the chemical impurities on the surface of their wafers.

However, no low-cost VPD systems exist for academic institutions interested in characterizing their own wafers' contaiminatints. This project provides the end-to-end manufcturing, programming, installation, and standard operating procedure for anyone to create their own VPD scanner.

This project was created and now maintained at the Stanford Nanofabrication Facility (SNF) by Alex Denton, Trevor, and Thomas Rimer. 

*Add small SNF logo*

## Overview

*Insert image of the scanner sitting inside its box in a fume hood*

The VPD scanner is based on a modified Ender 3s 3D printer. Using the provided STLs, Python scripts, and ordering sheet outlined below, the entire VPD scanner can be built and installed in just ~6 hours of work for $4,000. In addition to the written instructions on this doc, there are also accompanying video tutorials for certain steps, going in depth on different parts of the project. 

**Analysis Note**: This project assumes you have access to an ICP-MS or similarly sensitive tool to analyze the samples. The VPD scanner itself has no capacity to analyze the droplets it collects. Some work arounds are noted below if an ICP-MS is not availible. 

**Safety Note**: This project relies on hydrofluoric acid (HF) for the collection solution. HF is an unbelievably toxic chemical; if you need to google why, this project is *not* for you.

All aspects of the manufacturing process are designed to be as accessble as possible. Below are a list of tools you're assumed to already have. There are workarounds to every tool:

- 3D printer
- Laser cutter 
- Phillips screw driver
- Metric allen keys
- Soldering iron
- Scissors
- Tape

## Operating Principle

To collect a sample, the scanner (modified 3D printer) has a syringe in place of its original hot-end allowing the syringe to be positioned anywhere around the target wafer. First, the syringe automatically aspirates ~200 uL of an HF/H2O2/Water solution, moves to ~0.2 mm above the center of the wafer, and then dispenses the solution. This forms a droplet on the surface of the wafer that remains attached to the tip of the syringe. Over the course of 5-15 minutes (depending on wafer size), the scanner slowly moves the syringe head in a series of expanding concentric rings, dragging the droplet across the entire surface of the wafer. The HF in the scan solution attacks the ~2nm native oxide on the wafer's surface, dissolving any contaminants on the surface or within the first few layers of SiO2. Finally, the scanner sucks up the droplet from the surface and dispenses it in a collection cuvette, for analysis by an ICP-MS.

This droplet-dragging technique is similar to what's found in commercial VPD machines. However, there are a few differences worth noting:

**Full Automation:** A human user is needed for setup and sample transfer for the VPD outlined in this repo. Most commercial VPDs have fully automated, load-lock-compatible setups which allow seamless integration into their production lines.

**Vapor Etching:** As the name "Vapor Phase Decomposition" might suggest, commerical VPDs use an HF vapor to etch the entire surface of the wafer at once, before the droplet scan commences. This VPD scanner relies on HF within the scan solution to etch and collect the contaminants at the same time. 

**Speed:** While our machine takes ~20+ minutes to process a wafer, a commercial machine can often complete a scan in <60 seconds.

## Table of Contents

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


### Scanner Components
| Item | Price per Unit | Units | Subcost | Link | Use
|----------|----------|----------|----------|----------|----------|
| Ender 3 S1 3D Printer    | $249     | 1     | $249 | [Amazon](https://www.amazon.com/Creality-Ender-S1-Precision-8-6X8-6X10-6in/dp/B0BXPQD3KB/) | Sacrifical 3D printer converted into the scanner
| Filament    | $25     | 1     | $25 | [Amazon](https://www.amazon.com/HATCHBOX-Printer-Filament-Dimensional-Accuracy/dp/B09G85F1CC/?th=1) | Material used to print the necessary Ender modifications

Scanner Components Subtotal: **~$275**

<details>
  <summary> Click here for details about Scanner Components, alternatives to certain items, and other comments</summary>
   
  ### Ender 3 S1 3D Printer
  The Ender 3 is a super popular, low cost, easily modifiable 3D printer chosen for its large support community and easily accessible components.

  **Ordering notes**: Feel free to purchase the Ender 3 from any website you see fit. Note that there are different versions of the Ender 3 (Ender 3, Ender 3s, Ender 3 pro, etc...) Make sure you purchase the Ender 3s to ensure components fit the gantry. 
  
  **Alternatives**: Using any other 3D printer will almost certainly mean a complete redesign of all mechanical components, including the clean enclosure (unless the alternative printer is smaller). Additionally, the scan programs would no longer work, meaning you'd need to generate your own (which should be easy using the program builder script included in this repo, but is still worth noting). If there were one component in this build we'd suggest not replacing, it's the Ender 3s printer. 

  ### Filament
  **Ordering notes**: Any brand of 3D printer filament will work just fine. Because the 3D prints will never come in contact with the scan solution, it does matter what plastic you use. We recommend PLA for its ease of printing. 
  
  **Alternatives**: If yo're feeling ambitious, some/all 3D printed components can be machined out of blocks of teflon. This will provide excellent chemical resistance and durability. Stanford actually has a previous version of the scanner with custom machined teflon components.

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


## Manufacturing and Assembly

The VPD scanner has two manufacturing tasks; building the scanner and building its enclosure. Each can be built independently of the other, making it convienent to split up amongst multiple people or parallelize work if you're waiting on parts to finish printing.

### Scanner Manufacturing

*Insert image of finished scanenr*

**Step 1: Assembling the Ender 3s**

The Ender 3s comes partially assembled from the factory. There are several high-quality YouTube tutorials already made outlining exactly how to assemble an Ender 3. Here's a well made one from [3D Printing Canada](https://www.youtube.com/watch?v=dQ0q9zLygTY) (https://www.youtube.com/watch?v=dQ0q9zLygTY).

While most of the build proceeds as normal, there are a few steps you should <ins>not</ins> do:

- Do not mount the extruder stepper motor on the bracket designed for it. However, you should still wire it as if you were going to mount it. The extruder stepper motor will be used later on to control the syringe.
- Similarly, do not install the spring-loaded extruder gear assembly. This is not needed for the VPD.
- 


**Step 2: 3D Print Required Components** 

**Step 3: Install 3D Printed Components**

**Step 4: Level Bed**

### Enclosure Manufacturing

*Insert CAD rendering of finished enclosure*

The enclosure is predominantly built from laser-cut acrylic panels. A  fan mounted on top of a ULPA filter blows clean air into the top of the enclosure. Slots cut into the bottom of the enclosure allow the clean air to escape out the bottom. A power supply mounted on the back of the 

**Step 1: Cutting Acrylic Panels**

**Step 2: Acrylic Enclosure Welding**

**Step 3: Mounting Magnets**

**Step 4: ULPA Filter Installation**

**Step 5: Blower Fan Installation**

**Step 6: LED Light Installation**

**Step 7: Power Switch Installation**

**Step 8: Power Supply Mounting and Wiring**

**Step 9: Teflon Base Installation**

## Scripting

## Calibration

## Standard Operation

## Misc

### Contact

Please reach out if you're thinking about building a scanner, we're excited to see these get into as many labs as possible! We ask you use the "Issues" tab to ask questions, this will allow other people thinking of building a VPD to see what is and isn't going well. 

### License

This project is licensed under the MIT License. See the LICENSE file for more details.