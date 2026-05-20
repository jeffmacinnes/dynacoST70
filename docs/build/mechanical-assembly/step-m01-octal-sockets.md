---
title: M1 — Octal sockets
---

# M1: Mount the seven octal sockets

> *Mount the seven octal sockets with 4/40 hardware (the smallest screws supplied). Note that there is a small slot or keyway in the center hole of each socket; be sure in each instance that this keyway is properly oriented as shown in the pictorial diagram. Insert screw from the top of the chassis and mount the sockets from the bottom. Fasten with the kep nuts provided.* — manual page 4

## Why seven octal sockets

The ST-70 chassis has positions for seven octal sockets:

| Socket | Role | Holds a tube? |
|---|---|---|
| V1 | GZ-34 rectifier | Yes |
| V2 | EL-34 output | Yes |
| V3 | EL-34 output | Yes |
| V4 | Left Biaset socket / preamp power take-off | **No** — meter probe point only |
| V5 | Right Biaset socket / preamp power take-off | **No** — meter probe point only |
| V6 | EL-34 output | Yes |
| V7 | EL-34 output | Yes |

V4 and V5 hold no tubes — they're front-panel sockets where you stick a meter probe to read bias voltage. Don't be surprised when those two sockets stay empty for the life of the amp.

## What you're doing physically

Each socket has two #4 mounting holes on either side. The socket sits on the TOP of the chassis with the contacts hanging down through the chassis hole. Insert a #4-40 screw from above (through the chassis top, through the socket's mounting tab), then thread a kep nut on from below.

Eight sockets × 2 screws = 16 screws and 16 kep nuts for this step. Don't fully tighten any socket until all seven are placed — you may want to rotate one slightly to keep keyways aligned.

## Why the keyway orientation matters

Each socket has a small slot or keyway in its center hole. This indicates the "12 o'clock" position relative to the pinout. When you wire pin #2 of V2 (for example), you need pin #2 to be in a known physical location — and that's determined by keyway orientation.

The wiring pictorial on page 22 of the manual shows the keyway position for each socket, viewed from the underside. Match each socket to the pictorial as you mount them.

If you get keyways wrong, every "pin #N" instruction in the wiring procedure will land on the wrong pin. The amp won't work and troubleshooting is a nightmare.

## Why kep nuts

The kep nut has a built-in conical lock washer that bites into the chassis when tightened. This prevents the nut from vibrating loose over decades of thermal cycling (the chassis gets warm from the tubes; the nut + screw + chassis all expand and contract slightly at every power-on / cool-down).

A plain hex nut would slowly back out over 10-20 years; a kep nut stays put.

## Common mistakes

- **Cross-threading the kep nut**: #4-40 threads are fragile. If the nut doesn't start easily by hand, back it off and re-align. Forcing it strips the threads and you'll need to replace the screw.
- **Mounting the socket upside-down**: the socket has a "front" (pin entry) and a "back" (solder side). Pin entry faces TOP of chassis; solder lugs face the underside. Easy to mess up if you're not paying attention.
- **Forgetting to align keyways**: see above. Hardest mistake to recover from.

## See also

- [Tube pinouts](../../appendices/tube-pinouts.md) — what each pin does on each tube type
- [PA-060 power transformer](../../components/pa-060-power-transformer.md) — what V1 socket will eventually connect to
