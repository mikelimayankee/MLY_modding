# Bluetooth Audio Adapter for 2008 Infiniti G37 (30-pin iPod Interface)

**Status:** Concept / feasibility — design draft
**Target vehicle:** 2008 Infiniti G37 with factory navigation/audio and the
center-console iPod interface (Nissan proprietary connector → 30-pin Apple dock).
**Goal:** Replace the obsolete 30-pin iPod connection with a modern Bluetooth
link to a current iPhone (USB-C), preserving track metadata on the dash and
two-way transport control (dash + steering wheel).

---

## 1. Problem statement

The car's center console exposes a Nissan-proprietary connector that breaks out
to a **30-pin Apple dock connector** (factory cable P/N **284H2-1BA0B**). The
30-pin standard is ~15 years obsolete; adapting a modern USB-C iPhone would
require stacking multiple adapters, and even then the car's iPod integration
expects an actual iPod to be present.

Commercial "fake iPod → Bluetooth" dongles (e.g. the **Bovee 1000**) solved this
years ago but are now hard to source and rely on old Bluetooth standards
(SBC over Bluetooth 2.x). This project builds a modern one-off replacement.

## 2. What the car expects (the iPod side)

The car's head unit is the **host**; it expects to talk to an **iPod** as the
device. On the 30-pin connector the relevant signals are:

| Pin(s) | Signal | Notes |
|--------|--------|-------|
| 1, 2   | Ground / Audio GND | |
| 3      | Right line-out (R+) | **Analog** line-level audio to the car amp |
| 4      | Left line-out (L+)  | **Analog** line-level audio to the car amp |
| 11     | Serial GND | |
| 12     | Serial TxD (iPod → car) | UART, 3.3V TTL |
| 13     | Serial RxD (car → iPod) | UART, 3.3V TTL |
| 21     | Accessory identify | Resistor-to-GND selects accessory mode (e.g. ~500 kΩ = serial comms, 1 kΩ = dock) |
| 19/20, 23/25/27 | USB / power | See power note below |

**Protocol:** The serial control link is the **iPod Accessory Protocol v1
(iAP1)** — 8N1, typically **19200 baud** (higher rates possible). Over it the
car: identifies the device, queries capabilities, sends transport commands
(play/pause/next/prev), and requests **track metadata** (title / artist / album /
elapsed time) for the dash display.

**Audio is analog line-out** (pins 3/4) for this 30-pin/classic-iPod-era
integration — good news, because we only need a clean DAC, not a digital audio
link into the head unit.

### Authentication — why MFi is *not* required
Apple's authentication coprocessor exists so an **accessory** can prove itself to
an **Apple device**. Here the roles are reversed: **we emulate the iPod**, and the
car is the accessory. Older car head units trusted the iPod and did not demand
cryptographic auth from it. So **no Apple MFi license and no auth chip are
needed** — this is the elegant core of the whole approach. (Flagged below as a
must-verify, but it almost certainly holds for a 2008 head unit.)

## 3. What the phone provides (the Bluetooth side)

Standard, open Bluetooth profiles — no MFi:

- **A2DP (sink):** receive audio from the iPhone. iPhone's best codec is **AAC**
  over A2DP; targeting AAC on **Bluetooth 5.x** is the meaningful upgrade over the
  old Bovee's SBC/BT-2.x. (aptX/LDAC aren't relevant — iPhone doesn't support them.)
- **AVRCP:** receive **now-playing metadata** (title/artist/album/position) and
  send/receive **transport controls** (play/pause/next/prev).

## 4. System architecture

Two bridges meet in the middle of one MCU:

```
                 Bluetooth 5.x                         30-pin dock
  ┌─────────┐  A2DP audio (AAC)   ┌──────────────┐   analog L/R out   ┌──────────┐
  │ iPhone  │ ──────────────────► │   Adapter    │ ─────────────────► │  Car     │
  │ (USB-C) │  AVRCP metadata ──► │  (ESP32 +    │   iAP1 serial      │  head    │
  │         │ ◄── AVRCP controls  │   DAC)       │ ◄────────────────► │  unit    │
  └─────────┘                     └──────────────┘   (UART 19200)     └──────────┘
```

- **Audio path:** iPhone → A2DP/AAC → ESP32 decode → I²S → external DAC →
  analog line-out → car audio pins (3/4).
- **Metadata path:** iPhone → AVRCP now-playing → ESP32 → reformat as iAP1
  responses → car dash display.
- **Control path:** car / steering-wheel buttons → iAP1 command → ESP32 →
  AVRCP command → iPhone.

### Why ESP32
A single ESP32 (classic Bluetooth variant, **not** S3 if using classic BT — see
below) can host all of it: Bluetooth Classic **A2DP sink + AVRCP**, **I²S** to a
DAC, a spare **UART** for iAP1, and a **GPIO/resistor** for the accessory-ID pin.
The `pschatzmann/ESP32-A2DP` library already exposes AVRCP metadata callbacks.

> **Note on ESP32 variants:** Classic Bluetooth A2DP needs an ESP32 with
> Bluetooth Classic/EDR (original ESP32, ESP32-WROVER). ESP32-S3 is BLE-only and
> cannot do Classic A2DP — relevant when picking the module. AAC decode needs
> PSRAM (WROVER-class part).

## 5. Prior art (strong references)

- **`martinroger/ipodesp32`** — ESP32 iPod emulator for 2006–2013 BMW Minis that
  need Bluetooth. Does almost exactly this project: streams BT audio, **keeps
  track metadata on the display**, supports **steering-wheel controls**, auto-
  reconnect on ignition. Uses a UDA1334/PCM5102 DAC for analog out. **Key
  difference:** the Mini uses **USB-mode** iAP, so that project must spoof a
  PL2303 USB descriptor on a CP210x chip — its single biggest pain point
  (broken on newer CP2102N/GM parts). **If the G37 uses serial-mode iAP1
  (likely, given analog line-out), we skip USB spoofing entirely** and drive the
  UART directly — a major de-risk.
- **`chemicstry/A2DP_iPod`** — ESP32 A2DP-sink iPod emulator (PCM5102 I²S DAC),
  good reference for the audio half.
- **`xtensa/PodEmu`** — Android app that emulates an iPod over the 30-pin serial
  interface; useful reference for **iAP1 serial message framing** in the
  iPod-device direction.

## 6. Physical interface — plug into the factory cable

The adapter mates directly with the existing factory Nissan→30-pin cable
(284H2-1BA0B), rather than tapping the Nissan-proprietary harness. Rationale:

- Fully reversible, no cutting into the Nissan harness.
- No need to reverse-engineer the Nissan-proprietary console pinout.
- 30-pin connectors/breakouts are still sourceable.

**Connector gender (confirm with cable in hand):** an iPod's port is *female*,
so the factory cable's iPod-end is almost certainly a **male** plug. To "become
the iPod," the adapter therefore likely needs a **female 30-pin receptacle** —
not a male plug. Confirm visually when the cable is on the bench; the inline
breakout used for capture (§7a) is dual-gender so it sidesteps this for recon.

Trade-off vs. tapping the Nissan harness directly: slightly less "hidden," but
far lower risk and effort for a one-off. Revisit only if a cleaner permanent
install is wanted later.

## 7. Bill of materials

### 7a. Phase 1 — recon / handshake-capture tooling

Everything needed to passively tap a real iPod ↔ car session and capture the
handshake (see procedure in §10, Phase 1). Buy this set first.

| Item | Suggested part | ~Cost | Purpose |
|------|----------------|-------|---------|
| Reference iPod | Any junk **30-pin iPod** (nano 1–3G / classic / touch); broken screen / dead battery OK as long as it boots | $15–30 | Known-good device to capture real iAP1 traffic |
| Inline 30-pin breakout | 30-pin **male↔female pass-through / dock extender** with pins broken out to pads/header | $5–15 | Insert between car cable and iPod so both talk normally while you probe |
| Logic analyzer | 8-ch USB analyzer (Saleae clone), 3.3 V logic threshold | $10–15 | **Critical** — sniff iAP1 on pins 12/13; decode with PulseView/sigrok |
| Multimeter | any | — | Measure pin-21 ID resistor, verify power-rail voltages, confirm pin-1 orientation |
| Dupont/jumper leads | — | — | Tap breakout pads → analyzer |

> If no breakout is sold for your needs, cut a cheap 30-pin male-to-female
> extender cable and tap the wires, or wire one male + one female 30-pin
> connector pin-to-pin on protoboard and probe the middle.

### 7b. Prototype build BOM (Phases 2+)

| Item | Suggested part | Purpose |
|------|----------------|---------|
| MCU + Bluetooth | ESP32-WROVER (Classic BT + PSRAM, for AAC) | A2DP/AVRCP + iAP1 + control logic |
| Audio DAC | PCM5102 I²S DAC board | Clean analog line-out to car pins 3/4 |
| 30-pin connector | **Female** 30-pin receptacle (see §6) to mate with the factory cable's male plug | Physical iPod-side interface |
| Accessory-ID | Resistor (value TBD by capture) on pin 21 | Sense/set the iPod mode the car wants |
| Power | Buck regulator from car-supplied rail to 3.3V/5V | Run adapter from the dock connector |

If the ESP32's onboard BT audio quality disappoints, fall back to a dedicated
A2DP module (Microchip **BM83**, Qualcomm **QCC30xx/51xx**) and use the ESP32
only for iAP1 + control bridging.

## 8. Power note (verify)
2008 Infiniti models were wired to charge the iPod via the **12 V Firewire** pin
(Apple dropped Firewire charging with the iPhone 3GS in 2009). Since our phone
connects over Bluetooth and isn't physically charged here, we only need to power
the *adapter*. Confirm which rail the car energizes on the connector (12 V
Firewire vs. 5 V USB) and regulate from whatever is present.

## 9. Critical unknowns to verify (in priority order)

1. **Serial vs. USB iAP transport.** Does the G37 head unit talk iAP1 over the
   **UART (pins 12/13)** or over **USB**? Analog line-out strongly implies
   serial mode — but confirm with a logic analyzer / continuity before
   committing. This single answer determines whether we avoid the BMW project's
   USB-spoofing nightmare.
2. **Accessory-ID resistor value** on pin 21 that selects the mode the car wants.
3. **Authentication:** confirm the head unit does **not** demand iPod auth
   (expected: it doesn't).
4. **Which iPod model to emulate** for full metadata/control feature set (the
   BMW project emulates an *iPod Classic 5G U2*). Capture what the car probes for.
5. **Power rail present** on the connector and its voltage.

The logic-analyzer capture of a known-good iPod (or Bovee) session answers
1–5 at once and is the highest-value first bench task.

## 10. Phased plan

1. **Recon / capture** (tooling in §7a). Passively tap a real iPod ↔ car session
   and capture the handshake — answers all of §9 at once. Procedure:
   1. **Insert the breakout inline:** car cable ↔ breakout ↔ iPod, so both talk
      normally while you probe. Confirm **pin-1 orientation** with a continuity
      check before trusting the channel map.
   2. **Wire the analyzer** (UART is single-ended — listen each line to GND):
      CH0 → pin 12 (iPod→car Tx), CH1 → pin 13 (car→iPod Tx), GND → pin 11.
      Set the analyzer to a **3.3 V** logic threshold.
   3. **Capture the cold-boot handshake:** start the capture *first*, then key to
      ACC / insert the iPod, and select iPod as the head-unit source. The opening
      bytes are the car's identify request + the iPod's reply. Grab several
      power-on cycles (cold boot can differ from warm reconnect).
   4. **Capture controls + metadata:** press play/pause/next/prev on the **dash**
      and **steering wheel** one at a time (note timestamps); with a track
      playing, capture how the car requests and the iPod returns title / artist /
      album / elapsed time.
   5. **Measure pin 21 → GND** on the car-cable side (everything unplugged) to
      read the accessory-ID resistor the car presents; **measure the power-pin
      voltages** with the car on.
   6. **Decode in PulseView/sigrok:** add a UART decoder per channel, **8N1,
      try 19200** (if garbage, measure narrowest pulse → baud = 1/width).
      iAP1 packets start with sync header **`0xFF 0x55`** → seeing it confirms
      serial-mode iAP1. Map command IDs against `xtensa/PodEmu`'s tables; watch
      for an auth challenge (auth lingo `0x02`) — its absence confirms no auth.
   *Output: a labeled byte-level transcript the firmware can replay against.*
2. **Audio first.** ESP32 A2DP sink → PCM5102 → into the car's analog pins.
   Prove clean audio + stable Bluetooth (AAC). Low risk, validates half the system.
3. **Handshake.** Implement iAP1 device emulation so the car **recognizes** the
   device and selects the iPod source.
4. **Metadata + controls.** Bridge AVRCP ↔ iAP1 both directions (dash display +
   steering-wheel/dash buttons).
5. **Integrate + PCB.** Fold the breadboard design into a single PCB with the
   30-pin plug, regulator, and DAC; sort enclosure / install.

## 11. Risk register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| G37 uses USB-mode iAP (needs descriptor spoofing) | Low–Med | High | Capture first (phase 1); reuse BMW project's CP210x approach if needed |
| Head unit demands iPod authentication | Low | High | Capture confirms; emulate exact iPod model the car trusts |
| iAP1 device-side framing harder than expected | Med | Med | Lean on PodEmu / ipodesp32 message tables; iterate against capture |
| ESP32 onboard BT audio quality/latency | Med | Med | Fall back to BM83/QCC module |
| Sourcing male 30-pin connector | Low | Low | Still available; or harvest from a cheap dock cable |

## 12. References

- 2008 G37 iPod interface, factory cable 284H2-1BA0B, 12 V Firewire charging:
  [MyG37 forum](https://www.myg37.com/forums/audio-video-and-electronics/274262-ipod-cable.html),
  [Nissan/Infiniti OEM iPod cable (Amazon)](https://www.amazon.com/Infiniti-Genuine-Original-INTEGRATION-CONNECTOR/dp/B008B8OJAU),
  [Eastar 284H2-1BA0B adapter](https://www.amazon.com/Adapter-iPhone-Infiniti-2007-2013-284H2-1BA0B/dp/B082TM8HHB)
- 30-pin dock pinout, serial 19200 8N1 (pins 12/13), accessory-ID resistor (pin 21),
  line-out (pins 3/4):
  [irq5.io — The Apple 30-pin Dock Connector](https://irq5.io/2012/06/25/the-apple-30-pin-dock-connector/),
  [PinoutGuide — iPod dock](https://pinoutguide.com/PortableDevices/ipod_pinout.shtml),
  [The Apple Wiki — 30-pin Connector](https://theapplewiki.com/wiki/30-pin_Connector)
- iPod-emulation prior art:
  [martinroger/ipodesp32](https://github.com/martinroger/ipodesp32),
  [chemicstry/A2DP_iPod](https://github.com/chemicstry/A2DP_iPod),
  [xtensa/PodEmu](https://github.com/xtensa/PodEmu)
- ESP32 Bluetooth audio:
  [pschatzmann/ESP32-A2DP](https://github.com/pschatzmann/ESP32-A2DP),
  [ESP-IDF A2DP API](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/esp_a2dp.html)
