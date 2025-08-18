# ```Electronics```

How does one go at building a programmable microcontroller that reads information from the world and controls a device using I/O pins? 

**Theory**: voltage, current, resistance, capacitance, inductance, laws and theorems

**Passive components**: resistors, capacitors, inductors, transformers

**Discrete passive circuits**: current limiters, voltage, dividers, filter circuits, attenuators

**Discrete active devices**: built with semiconductors. Diodes (one-way current gates), transistors (electrically controlled switches)

**Discrete active/passive devices**: rectifiers (AC to DC), amplifiers, oscillators, modulators, voltage regulators

Integrated circuits are convenient combinations of these components. 

ICs that respond and produce varying degrees of Voltage are `Analog Devices`.

Whereas ICs that work with only 2 states (5V or 0V) are digital.

Digital ICs: logic gates, flip-flops, shift registers, counters, memories, processors, microcontrollers, etc. Most of these are designed to perform logical operations on input information. 

**Electric current**   

Total charge passing through a cross-sectional area `A` per unit time. 

$\displaystyle I_{\text{avg}} = \frac{\Delta Q}{\Delta t}$

1 A = 1 C/s (Coulombs per second)

| Device | Current Draw |
|--------|--------------|
| Low-powered microchip | μA or even pA |
| LED light | 20mA |
| Smartphone | 200mA |
| Current to induce cardiac arrest | 100mA to 1A |
| 100-W lightbulb | 1A |
| Electric fan | ~1A |
| Laptop | ~3A |
| Microwave | ~13A |
| Automobile starter | 200A |
| Lightning strike | 1000A |

**Voltage**

A voltage across a conductor creates an eletromotive force (EMF) that gives `free electrons` withing the conductor a push.

Direct Current voltage source (DC voltage source): A device that maintains a constant voltage across its terminals. 

> A battery generates EMF by chemical reactions that yield a buildup of free electrons in the negative terminal region, they repel each other and generate electrical pressure.
> By placing a load between the terminals, electrons attemp to alleviate the pressure by dispersing into the circuit.
> Even a small concentration gives rise to great repulsive forces between free electrons.
> The chain reaction or pulse when there's a release in tension travels down the conductor at near the speed of light.
> The physical movement is much slower though. 

You can create EMF in different ways: chemical reactions (batteries), magnetic induction, photovoltaic effect, piezoelectric, thermoelectric, static effect. The latter 3 produce rather small forces so we mostly use the first 3.

Relationship between Voltage and potential energy difference gives us:

$\displaystyle V = \frac{U}{q}$

where 1 volt = 1 joule / coulomb, ie. two points with a voltage of 1 V between them have enough "electrical pressure" to perform 1 J worth of work while moving 1 C worth of charge.

