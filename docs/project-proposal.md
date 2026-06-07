# Project Proposal — Bluetooth Audio Adapter for 2008 Infiniti G37

**Prepared for:** (contractor — PCB design / fab / firmware / install)
**Prepared by:** project owner
**Date:** 2026-06-07
**Companion document:** [`bluetooth-ipod-adapter-design.md`](bluetooth-ipod-adapter-design.md) — full
technical feasibility analysis, pinouts, prior art, and phasing. Read it
alongside this proposal; this document is the scope/handoff, that one is the
engineering detail.

---

## 1. Summary

Design, build, and install a small custom electronic adapter that replaces the
obsolete 30-pin iPod connection in a **2008 Infiniti G37** with a modern
**Bluetooth** link to a current (USB-C) iPhone. The adapter emulates an iPod to
the car's factory head unit so that, from the driver's seat, the car behaves
exactly as it did with an iPod — but audio, track info, and controls now flow
to/from the phone wirelessly.

**Engagement type:** turnkey — the contractor owns hardware design, firmware,
fabrication/assembly, and final in-vehicle installation and commissioning.

## 2. Background & objective

The car's center console has a Nissan-proprietary connector that breaks out to a
**30-pin Apple dock connector** (factory cable P/N 284H2-1BA0B). The head unit
talks to a connected iPod over Apple's **iPod Accessory Protocol v1 (iAP1)** and
pulls **analog line-level audio**. The 30-pin standard is obsolete; adapting a
modern iPhone is impractical, and the old commercial "fake iPod → Bluetooth"
dongles (e.g. Bovee 1000) are discontinued and use outdated Bluetooth.

**Objective:** a clean, reliable, reversible one-off adapter that:
1. Streams audio from the iPhone to the car over modern Bluetooth (A2DP, AAC).
2. Shows **track metadata** (title / artist / album / elapsed) on the dash.
3. Accepts **transport controls** (play/pause/next/prev) from the **dash and
   steering wheel** and relays them to the phone.
4. Powers itself from the car connector; auto-connects on ignition.

## 3. How it works (architecture)

A single MCU bridges two interfaces:

```
                 Bluetooth 5.x                         30-pin dock
  ┌─────────┐  A2DP audio (AAC)   ┌──────────────┐   analog L/R out   ┌──────────┐
  │ iPhone  │ ──────────────────► │   Adapter    │ ─────────────────► │  Car     │
  │ (USB-C) │  AVRCP metadata ──► │  (ESP32 +    │   iAP1 serial      │  head    │
  │         │ ◄── AVRCP controls  │   DAC)       │ ◄────────────────► │  unit    │
  └─────────┘                     └──────────────┘   (UART, 3.3V TTL)  └──────────┘
```

- **Audio:** iPhone → A2DP/AAC → MCU decode → I²S → DAC → analog line-out to the
  car's audio pins.
- **Metadata:** iPhone AVRCP now-playing → MCU → reformatted as iAP1 responses →
  dash display.
- **Control:** car/steering-wheel button → iAP1 command → MCU → AVRCP command →
  iPhone.

**Why no Apple MFi license is needed:** Apple's authentication coprocessor only
matters when an *accessory* must prove itself to an *Apple device*. Here the roles
are reversed — the adapter **emulates the iPod** (the trusted device) and the car
is the accessory. Older head units do not demand auth from the iPod. (Confirmed
empirically during Phase 1; see §6.) The phone-side link uses only standard,
open Bluetooth profiles (A2DP/AVRCP), which also require no MFi.

**Reference platform:** the proven approach is an **ESP32-WROVER** (Bluetooth
Classic + PSRAM for AAC) running the `pschatzmann/ESP32-A2DP` stack, plus a
**PCM5102 I²S DAC** for clean analog out. A near-identical open-source project
exists for BMW Minis (`martinroger/ipodesp32`) and is the primary firmware
reference. The contractor may propose an alternative MCU/BT module (e.g.
Microchip BM83, Qualcomm QCC30xx/51xx) if it improves audio quality, cost, or
manufacturability — see §7.

## 4. Scope of work (turnkey)

The contractor is responsible for:

**A. Hardware**
- Schematic capture and PCB layout (2- or 4-layer as needed).
- Power supply from the car connector rail to board rails, with automotive
  transient protection (see §6).
- 30-pin connector interface (female receptacle — see §6 connector-gender note).
- Audio output stage (DAC → AC-coupled line-level to car pins 3/4).
- Configurable accessory-ID network on pin 21 (value finalized from capture).
- Fabrication and assembly of working prototype(s); revise to a final board.
- Enclosure (3D-printed or off-the-shelf) sized to fit the console location.

**B. Firmware**
- Bluetooth A2DP sink (AAC) + AVRCP (metadata + controls).
- iAP1 device-side emulation that satisfies the G37 head unit's handshake,
  metadata requests, and transport commands (built against the Phase 1 capture).
- Control translation both directions (iAP1 ↔ AVRCP).
- Ignition-aware behavior: auto-connect/resume on power-up, graceful sleep on
  power-down; persistent phone pairing.

**C. Installation**
- Final fit and in-vehicle commissioning in the G37; verify all functions from
  the driver's seat; tidy, reversible install (no cutting the factory harness).

## 5. Responsibility split

| Provided by owner | Delivered by contractor |
|---|---|
| The vehicle (G37) for capture, bring-up, and install | All hardware design + fab + assembly |
| A junk 30-pin iPod + the Phase 1 **capture transcript** (see §6) | All firmware |
| The factory iPod cable (284H2-1BA0B) for fit/test | Enclosure |
| Access for the install appointment(s) | Documentation + sources (see §8) |
| Budget per agreed terms (§10) | Final installed, working unit |

**Owner runs the Phase 1 handshake capture** (it requires the car + iPod) and
hands over a decoded byte-level transcript before firmware work begins. The
capture procedure, tooling, and parts list are in the companion design doc
(§7a, §10) — the owner already has the iPod and will acquire the ~$35 capture kit
(eLabGuy 30-pin pass-through breakout + USB logic analyzer).

## 6. Technical requirements & design constraints

**Car-side electrical (target — confirm against capture):**
- **Audio out:** analog line-level on 30-pin **pins 3 (R+) / 4 (L+)**, ground
  pins 1/2. AC-couple the DAC output; match nominal iPod line-out level so the
  head unit's gain staging is correct.
- **Control serial:** iAP1 over **UART, pins 12 (iPod→car Tx) / 13 (car→iPod Rx)**,
  3.3 V TTL, expected 19200 8N1. ESP32 is 3.3 V native — direct connect with
  series resistors + ESD protection recommended.
- **Accessory ID:** resistor-to-GND on **pin 21** selects the iPod mode. **Make
  this configurable on the prototype** (jumper-selectable resistor options) until
  the capture confirms the exact value the car expects.
- **Power:** the car energizes a rail on the connector (2008 G37 historically used
  **12 V Firewire** charging; some pins may carry 5 V). Design a **wide-input
  buck** (handle ~6–16 V) to the board rails, with **reverse-polarity protection**
  and a **TVS / load-dump clamp** suitable for automotive 12 V. Confirm the actual
  energized pin(s) and voltage during capture.

**Connector gender:** an iPod's port is female, so the factory cable's iPod-end is
a **male** plug → the adapter most likely needs a **female 30-pin receptacle** to
"become the iPod." Confirm with the cable in hand. (eLabGuy `APPLE-30F-BO-V1A` is
a candidate prototyping receptacle; a raw JAE-type / clone connector is the
production option.)

**Bluetooth:** target **AAC over A2DP on Bluetooth 5.x** (the practical ceiling
for iPhone, and the meaningful upgrade over the old SBC/BT-2.x dongles). AVRCP
≥ 1.4 for metadata + transport.

**Mechanical / environmental:** must fit the console iPod-cable location; tolerate
automotive temperature swings; secure, rattle-free, fully reversible install.

## 7. Open technical items (resolved by the Phase 1 capture)

The owner's capture transcript will confirm, before firmware/PCB finalization:
1. **Serial vs. USB iAP transport** (analog line-out strongly implies serial — if
   confirmed, no USB descriptor spoofing needed; this is the main risk retired).
2. **Exact accessory-ID resistor value** (pin 21).
3. **Whether the head unit demands authentication** (expected: no).
4. **Which iPod model to emulate** for full metadata/control coverage (BMW
   reference emulates an iPod Classic 5G).
5. **Energized power pin(s) and voltage.**

The contractor should treat the prototype as **configurable** around these
(jumperable ID resistor, headroom in the power input) so the capture can be
folded in without a respin.

## 8. Milestones & deliverables

| Phase | Milestone | Deliverable |
|------|-----------|-------------|
| 0 | Kickoff | Reviewed scope, agreed terms, BOM/architecture sign-off |
| 1 | (owner) Capture | Decoded iAP1 transcript handed to contractor |
| 2 | Audio proof | Breadboard: A2DP→DAC→car audio confirmed in the vehicle |
| 3 | Handshake | Car recognizes the device and selects the iPod source |
| 4 | Metadata + controls | Dash text + dash/steering-wheel controls working both ways |
| 5 | PCB + enclosure | Fabricated/assembled board in enclosure; bench-validated |
| 6 | Install | Commissioned in the G37; acceptance test passed |

**Final deliverables:**
- Working, installed adapter in the vehicle.
- **KiCad (or equivalent) source** — schematic + layout — plus **Gerbers**,
  drill files, and assembly drawings.
- **Finalized BOM** with sourcing.
- **Firmware source** (repo) with build/flash instructions.
- Brief **as-built doc**: pinout used, ID-resistor value, pairing/reset
  procedure, and how to re-flash.
- At least one **spare assembled board** (optional — see terms).

## 9. Acceptance criteria

Tested from the driver's seat in the G37:
1. Phone auto-connects on ignition; audio plays through the car system with no
   objectionable noise/hum and correct volume staging.
2. Track title/artist/album and elapsed time display on the dash and update on
   track change.
3. Play/pause/next/prev work from **both** the dash and steering wheel and are
   reflected on the phone.
4. Clean power-down on ignition off; reliable reconnect on next start.
5. Install is tidy and fully reversible (factory cable/harness uncut).

## 10. Commercial terms (to be completed by owner)

- **Budget / payment:** _[TBD — e.g., fixed price vs. hourly + parts; milestone
  payments tied to §8]_
- **Timeline:** _[TBD — target start and completion]_
- **Parts/fab costs:** _[TBD — reimbursed at cost vs. included]_
- **IP / ownership:** design files, firmware, and documentation transfer to the
  owner on final payment. _[Confirm.]_
- **Revisions / warranty:** _[TBD — e.g., bug-fix window after install]_
- **Spares:** _[TBD — quantity of extra assembled boards, if any]_

## 11. Risk register (summary; full version in design doc §11)

| Risk | Mitigation |
|------|------------|
| Car uses USB-mode iAP (would need descriptor spoofing) | Capture confirms first; BMW project's CP210x approach available as fallback |
| Head unit demands iPod auth | Capture confirms; emulate the exact iPod identity the car trusts |
| iAP1 device-side framing harder than expected | Lean on `xtensa/PodEmu` + `martinroger/ipodesp32` command tables |
| ESP32 onboard BT audio quality | Fall back to dedicated BM83/QCC module |
| Automotive power transients | Wide-input buck + reverse-polarity + TVS/load-dump protection |

## 12. References

- **Companion design doc:** [`bluetooth-ipod-adapter-design.md`](bluetooth-ipod-adapter-design.md)
- **Prior art:** `martinroger/ipodesp32`, `chemicstry/A2DP_iPod`, `xtensa/PodEmu`,
  `pschatzmann/ESP32-A2DP`
- **Pinout / protocol:** irq5.io 30-pin dock connector writeup; PinoutGuide;
  The Apple Wiki 30-pin connector page (links in the design doc).
