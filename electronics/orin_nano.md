How does cooling work on a GPU?

Card: Orin Nano

Under `/sys/devices/virtual/thermal` this card separates thermal concepts by either a) thermal zones, or, b) cooling devices.  

Thermal zones are a management unit that includes a sensor, trip points thresholds classified by types, a governor that executes some policy, and a pointer to the device it should act on to shed heat. 

Cooling devices (also referred as cdev) are what shed heat like CPU frequency, GPU frequency, DLA frequency, and Fans.

A special thermal zone is Junction Temperature. This is a virtual concept determines the maximum across all thermal zones. 

The energy balance is Q_generated = Q_rejected

Q_generated: P ∝ C·V²·f where C is effective capacitance, V is voltage and f freqency.

Capacitance is the cumulative charge on the gates flipped by code so it's software dependent.
Freqency and Voltage are lively controllable. Since there's the squared term, cutting frequency drops heat super linearly, eg. 20% reduction could be 40% reduction on heat. 

Q_rejected: It's best understood by what happens at the boundary between the heatsink and fluid (convection), and then the ability of the fluid do move it (advection).

Convection

Q = h · A_eff · (T_s − T_air) This measures heat at the boundary between the heat sink and air, Ts is the fin surface temp. 

Advection

Q = m_air * cp_air * (Tair,out - Tair_in)

At steady state these 2 Qs are the same.
