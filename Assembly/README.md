# Assembly

Printing, assembling and wiring the box. For the parts list and prices see the
[Bill of materials](../README.md#bill-of-materials); for wiring see [Wiring](Wiring.md).

The STL contains six printed parts:

- Behaviour box body
- Lid — the tapered tower that carries the camera above the arena. It is 240 mm tall, so it doubles
  the assembled height to 460 mm; allow for that on the bench and in the printer
- Camera holder
- Running wheel
- Two screws

Everything else is bought off the shelf, as listed in the [Bill of materials](../README.md#bill-of-materials).
Assembly takes 20-30 minutes.

<p align="center">
  <img src="Pictures/Setup.jpg" width="52%" alt="Assembly overview: the camera slides into the camera holder, the holder into the top of the lid, the lid onto the box body; the encoder mounts through the side wall and the wheel onto its shaft; the Harp Behaviour Board sits outside">
</p>

<p align="center"><em>How the parts go together. The Harp Behaviour Board sits outside the box; see
<a href="Wiring.md">Wiring</a>.</em></p>

## Tools required

- 2 mm Allen key, for the M3 screws
- Flat-head screwdriver

## Step 1 - Print the components

Print all six parts from [`Behaviour_Box_Mini.stl`](Behaviour_Box_Mini.stl).

| Setting | Value |
|---|---|
| Material | PLA |
| Infill | 15% |
| Supports | None needed |
| Build volume | At least 210 x 210 x 245 mm |
| Printer | Standard Bambu Lab or equivalent |

The two largest parts set the build volume: the box body is 207 mm square and 220 mm tall, and the
lid is 199 mm square and 240 mm tall. Both fit an X1 or P1 series printer, but not an A1 mini.

The STL holds all six parts in their assembled positions, so they arrive spread out and at
different heights. **Split to objects** in the slicer, drop everything to the plate and arrange it
yourself. They will not fit on one plate: budget three, and closer to two or three days of printing
than one.

Print the box in a darker colour if you plan to record white or light-coloured mice, for contrast.

## Step 2 - Install the rotary encoder

Secure the encoder to the side wall of the box with three M3 x 8 mm screws, with the shaft facing
inwards. See [Wiring](Wiring.md) for the encoder connections.

## Step 3 - Install the running wheel

1. Turn the shaft until the flat of the D faces the matching flat inside the wheel hub.
2. Push the wheel home. It should slide on smoothly; if it needs force, the flats are not aligned.

## Step 4 - Install the camera

1. Remove the lens from the camera body.
2. Insert the camera through the camera holder from the rear.
3. Reattach the lens from the front, clamping the holder between the camera body and the lens so it
   cannot move.
4. Slide the holder into the square opening at the top of the lid and lock it with the two printed
   screws. Either screw goes in either hole.

See [Wiring](Wiring.md) for the camera power and trigger connections.

## Step 5 - Fit the infrared illumination

The 850 nm strip lights the arena for the camera without being visible to the mouse.

1. Cut about 600 mm from the 2 m reel — the interior is 200 mm square and three walls are lined.
   Cut **only on the marked cut points**, which on a 12 V strip fall every few LEDs. Cut anywhere
   else and the segment will not light.
2. Peel the backing and run the strip along **three of the four walls, leaving the wheel wall
   dark**. Three sides give even light across the floor, and keeping the strip off the wheel wall
   avoids both the encoder mount and the shadow the wheel would throw across the arena.
3. Connect the strip to its own 12 V supply, not to the Harp board.
