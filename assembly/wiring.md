# Wiring

The Mini Behaviour Box consists of three hardware connections:

1. Camera
2. Rotary Encoder
3. Harp Behaviour Board

Refer to the wiring diagrams below for the complete connection layout.

---

## Camera

The camera requires two connections:

- **Locking USB 3.0 Micro-B cable**
- **GPIO trigger cable**

The Locking USB 3.0 Micro-B cable is connected directly to the computer for image acquisition.

The GPIO trigger cable is connected to the **Output** port of the Harp Behaviour Board to enable hardware triggering.

For the **FLIR Blackfly S (BFS-U3-16S2M-CS)** listed in the Bill of Materials:

| Camera Wire | Connect To |
|-------------|------------|
| Blue (Opto GND) | GND |
| Black (OPTO IN) | Trigger |

> **Insert camera wiring diagram here**

Camera software configuration is described in the **Software** section.

---

## Rotary Encoder

The rotary encoder connects to the Harp Behaviour Board through an RJ45 cable (default **Port P0**).

To simplify assembly and replacement, we recommend terminating the encoder wires using a **5-way screw terminal block** before connecting them to the Harp Behaviour Board.

The encoder provides five wires, of which four are used:

| Encoder Connection | Harp Pin |
|--------------------|----------|
| Black (Channel A) | DI (Input A) |
| White (Channel B) | DIO (Input B) |
| *(Leave empty)* | Pin 3 |
| +5 V | Pin 4 |
| GND | Pin 5 |

> **Insert rotary encoder wiring diagram here**

---

## Harp Behaviour Board

The Harp Behaviour Board serves as the central interface between the camera, rotary encoder and computer.

The following connections are required:

- USB connection to the computer
- 12 V DC power input
- GPIO output connected to the camera trigger cable
- RJ45 connection to the rotary encoder (default **Port P0**)

Once all hardware connections are complete, proceed to the **Software** section for device configuration and data acquisition.
