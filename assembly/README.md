# Assembly

Printing, assembling and wiring the box. For the parts list and prices see the
[bill of materials](../README.md#bill-of-materials); for wiring see [wiring.md](wiring.md).

The STL contains six printed parts:

- Behaviour box body
- Lid
- Camera holder
- Running wheel
- Two screws

Everything else is bought off the shelf, as listed in the [bill of materials](../README.md#bill-of-materials).
Assembly takes 20-30 minutes.

<p align="center">
  <img src="Pictures/Setup.jpg" width="68%" alt="Assembled behaviour box">
</p>

## Tools required

- 2 mm Allen key, for the M3 screws
- Flat-head screwdriver

## Step 1 - Print the components

Print all six parts from [`Behaviour_box_Mini.stl`](Behaviour_box_Mini.stl).

| Setting | Value |
|---|---|
| Material | PLA |
| Infill | 15% |
| Supports | None needed |
| Printer | Standard Bambu Lab or equivalent |

Print the box in a darker colour if you plan to record white or light-coloured mice, for contrast.

## Step 2 - Install the rotary encoder

Secure the encoder to the side wall of the box with three M3 x 8 mm screws, with the shaft facing
inwards. See [wiring](wiring.md) for the encoder connections.

## Step 3 - Install the running wheel

Slide the wheel onto the encoder shaft. The hub is designed to mate with the D-shaped shaft, so
align the flat of the shaft with the matching flat inside the hub before pushing the wheel home. It
should slide on smoothly, without excessive force.

## Step 4 - Install the camera

1. Remove the lens from the camera body.
2. Insert the camera through the camera holder from the rear.
3. Reattach the lens from the front, clamping the holder between the camera body and the lens so it
   cannot move.

See [wiring](wiring.md) for the camera power and trigger connections.

## Step 5 - Fit the infrared illumination

The 850 nm strip lights the arena for the camera without being visible to the mouse. Run it along
**three of the four walls, leaving the wheel wall dark**. Three sides give even light across the
floor, and keeping the strip off the wheel wall avoids both the encoder mount and the shadow the
wheel would throw across the arena.

The interior is 200 mm square, so three runs need about 600 mm. Buy the 2 m reel and cut it to
length: the strip is adhesive-backed and cuts with scissors, but **only on the marked cut points**,
which on a 12 V strip fall every few LEDs. Cut anywhere else and the segment will not light.

The strip runs from its own 12 V supply, not from the Harp board.
