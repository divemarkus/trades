# Pila Energy (bidirectional electrical path)

Based on Pila's current documentation, the **Battery Mesh Network is a communication network, not an energy-sharing network**. Batteries coordinate schedules, monitoring, and optimization, but **they do not transfer stored electricity between each other.** ([Pila Energy][1])

### Example

Suppose you have:

```
      400W Solar Panel
             │
             ▼
        Pila #1 (Living Room)
             │
         TV + Router


Pila #2 (Kitchen)
      │
 Refrigerator

Pila #3 (Office)
      │
 Desktop + NAS
```

Today:

* ✅ Pila #1 can charge directly from the solar panel (once the plug-in solar accessory is available).
* ✅ Pila #2 and #3 communicate with #1 for coordinated energy management.
* ❌ Pila #1 does **not** send its stored energy over the mesh to recharge #2 or #3. ([Pila Energy][1])

---

## What the mesh actually does

The mesh network allows batteries to:

* Coordinate charging/discharging schedules.
* Present a unified view in the app.
* Share energy usage information.
* Continue communicating even if Wi-Fi is unavailable. ([Pila Energy][1])

Think of it like:

```
Tesla vehicles
      │
     Wi-Fi
      │
Communicate?   YES

Share battery energy?
NO
```

The mesh is for **data and coordination**, not for moving electrical power.

---

## Could this change?

Potentially, yes.

Pila has already indicated that some hardware was designed with future capabilities in mind. For example, they state the hardware is built for future bidirectional functionality, although that refers to grid interaction rather than battery-to-battery charging. ([Pila Energy][1])

In theory, a future system could support something like:

```
Solar
   │
Pila #1
   │
 AC house wiring
   │
Pila #2
```

where batteries intelligently coordinate charging over the home's wiring. However, **Pila has not announced such a feature**, and current documentation does not describe battery-to-battery energy transfer. ([Pila Energy][1])

---

## What I'd like to see

As an engineer, the feature I'd be most excited about is:

```
Solar Panel
     │
 Pila Garage
     │
Stores excess
     │
House AC wiring
     │
Automatically charges:
    • Kitchen Pila
    • Office Pila
    • Bedroom Pila
```

This would let one large solar array serve multiple Pila units without running dedicated solar cables to each battery. It's technically possible in principle, but implementing it safely would require sophisticated inverter synchronization, anti-islanding protection, and regulatory approvals.

### My guess

Pila's roadmap appears to be evolving from a smart UPS toward a distributed home energy platform. If they eventually add **AC energy sharing over existing household wiring**, it would become a very compelling alternative to a traditional Powerwall for many homes.

At present, though, you should plan on **each Pila charging itself**—from the grid, rooftop solar integration, or its own direct plug-in solar input—not from another Pila. ([Pila Energy][1])

[1]: https://www.pilaenergy.com/pages/faqs "FAQs: Setup, Safety & Support | Pila"
