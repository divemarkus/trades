# NVIDIA RTX Spark

Yes — the new NVIDIA Arm/Blackwell “superchip” for Windows laptops. And as of **September 5, 2026**, this has become much more concrete than it was when NVIDIA announced it in June.

The important point: **128GB unified-memory RTX Spark laptops are real, but they are not broadly shipping yet.** The first systems are expected in **October 2026**. ([The Verge][1])

![Image](https://images.openai.com/static-rsc-4/YEuc1E2X1wAkdv5VmhiGjfT65MDOGdriolTj5wh0YJYbYab1dJRHIOxT1YZf5pTU7938AQWi56MAr8tU5xvttvJVkxNkl7lxrJtnAk6x0Z_6TZsMRWiUEu1JRqEnMlRzLtvsUtojyi6nZNhVsc6Q8vHop1xq6bsDU3VaPX5Z2LZGyriiv59eKlM0iPIghdEz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/QXT7Vez6XelM9fC8LHEtlLn3C4gh2QjNum3N4fyR5FXS6u6tWoxSrcadRhlY3Px1_PRoZcK9zUpON1ILhHGVVxbLw7JQ9xpN_VEGFM88dhyT6L3Q49BEDr2W4ltaqMSi-UNy6nuYexaMUDMGYrssM_sl5y0rCKLgj7B3htzpgocNboIPVVIhf2pyB_f_2Ifm?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/YOrlMybfHG56U2cGm905m2luYchi_kVEifJ8VseS4Ks---932ThDRWz-dQywngNXoZjlRH-b86MfwWg-eoQhYF7ncPhQ-Ra7B66jgMSV0nbzkccX8ytcS2arafqnx4NSkz3TLQBTr3bSpYZU6jFNUKkYJbbpoN6UVFi2eTXDAs4MIJJYg2sKuuHXocPZvWwV?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/z09fojyKR8RFSaKIHM-xwIu7GVB3WGue7nWntdpSZ5ElRbQAOJ8txViT9ImojzfhYknEEsDMtfw1tYX3xhM0kz9yMZJbvuytSXbZ8lgPjx2oCnzqKdnlvUZe7YGRNXO1XXnrd2-lFbJlKeBf2Y_6Tr8owaFFernH060RJrrzTRZrZlMXYwrwFciz1J3xErOC?purpose=fullsize)

## The 128GB RTX Spark laptops

The most interesting manufacturers/models currently announced are:

| Manufacturer  | Model                           |                    128GB? | Screen       | Status        |
| ------------- | ------------------------------- | ------------------------: | ------------ | ------------- |
| **ASUS**      | **ProArt P16**                  |                         ✅ | 16" 4K OLED  | October class |
| **ASUS**      | **ProArt P14**                  |                         ✅ | 14" 3K OLED  | October class |
| **Lenovo**    | **Yoga Pro 9n**                 |                         ✅ | 15.3" OLED   | October       |
| **Microsoft** | **Surface Laptop Ultra**        |                         ✅ | 15" mini-LED | Expected fall |
| Dell          | XPS/Precision RTX Spark systems | Some 128GB configurations | 16" class    | Fall          |
| HP            | OmniBook/RTX Spark systems      |                TBD by SKU | Various      | Fall          |
| MSI           | Prestige RTX Spark systems      |                TBD by SKU | Various      | Fall          |

ASUS has now explicitly listed both the **ProArt P16 and P14** with up to **128GB unified memory**. ([ASUS Global][2])

Lenovo's newly detailed **Yoga Pro 9n** is also confirmed for up to 128GB, while the Yoga 9n 2-in-1 tops out at 64GB. ([Tom's Hardware][3])

### My early favorite: ASUS ProArt P16

For **your use case — local LLMs, CUDA, development, agents, ComfyUI, etc. — I'd put the ProArt P16 very high on the list.**

Its important configuration is:

* NVIDIA RTX Spark
* 20-core Grace CPU
* Blackwell GPU
* **6,144 CUDA cores**
* **128GB LPDDR5X unified memory**
* 16" 4K OLED
* USB4
* up to 2TB SSD
* Windows 11 Pro

ASUS has officially published those specifications. ([ASUS Global][4])

---

# What exactly is RTX Spark?

This is what makes it interesting compared with a normal RTX laptop.

It's essentially NVIDIA doing an **Apple Silicon-style architecture**, but with CUDA/Blackwell.

**CPU + GPU + memory are one tightly integrated system:**

```text
              RTX SPARK N1X
        ┌─────────────────────────┐
        │                         │
        │  20-core Grace CPU      │
        │          │              │
        │          │ NVLink-C2C   │
        │          ▼              │
        │  Blackwell RTX GPU      │
        │  6,144 CUDA cores       │
        │                         │
        │  Tensor Cores / RT      │
        │                         │
        └──────────┬──────────────┘
                   │
             128GB LPDDR5X
             UNIFIED MEMORY
                   │
        ┌──────────┴──────────┐
        │                     │
       CPU                   GPU
```

Instead of:

```text
CPU → system RAM
GPU → 16/24/32GB VRAM
```

you effectively get:

```text
              128GB
         ┌─────────────┐
         │ Unified RAM │
         └─────────────┘
           ↑         ↑
          CPU       GPU
```

That's **very interesting for local AI**.

NVIDIA specifically says the platform is designed to run models up to roughly **120B parameters locally**, depending on quantization and workload. ([NVIDIA Newsroom][5])

---

# But there's a VERY important catch

The 128GB version isn't the same as the lower-end RTX Spark laptop chip.

NVIDIA has now clarified that there are **two N1X configurations**.

### High-end N1X

**20-core Grace + 6,144 Blackwell CUDA cores**

Memory:

**24GB → 128GB unified**

This is the one you want.

### Lower laptop N1X

**18-core Grace + 5,120 CUDA cores**

Memory:

**24GB → 32GB**

This is more of a conventional premium laptop.

The distinction was confirmed by NVIDIA this week. ([Tom's Hardware][6])

So don't simply buy something advertised as an **"RTX Spark laptop."**

You want:

> **20-core / 6,144 CUDA / 128GB N1X**

---

# What will it cost?

This is where things get murky.

**The manufacturers have not yet published definitive US retail pricing for the 128GB models.**

And I would *not* trust many of the prices circulating online right now.

There are estimates around:

### $3,000–$5,000+

for the high-end 128GB machines.

That is consistent with the economics of the platform.

For comparison, NVIDIA's existing **DGX Spark**, which uses closely related Grace/Blackwell architecture and 128GB unified memory, has been positioned around the **$3,499–$4,699** range depending on configuration. ([Ars Technica][7])

There is also an independent RTX Spark registry currently listing a purported 128GB Dell Precision Spark at **$3,499**, but I'd treat that as **provisional/unverified retail information**, because the actual OEM launch pricing isn't fully established yet. ([RTXsparks][8])

### My estimate

I'd budget roughly:

| Configuration              |       Expected price |
| -------------------------- | -------------------: |
| RTX Spark 32GB             |        ~$1,800–2,500 |
| RTX Spark 64GB             |        ~$2,500–3,500 |
| **RTX Spark 128GB**        |    **~$3,500–5,000** |
| Fully loaded premium 128GB | **Possibly $5,000+** |

I would **not buy one based on a rumored price yet**.

---

# Has anyone benchmarked it?

### Yes — but this is where things get REALLY interesting.

There are three different categories of benchmark data.

## 1. Engineering sample CPU benchmark

An N1X engineering system produced approximately:

**Geekbench 6**

| CPU                    |    Single |      Multi |
| ---------------------- | --------: | ---------: |
| N1X engineering sample | **3,096** | **18,837** |
| M3 Max                 |     3,124 |     18,920 |
| M5                     |    ~4,224 |    ~17,465 |
| M5 Pro                 |    ~4,242 |    ~25,800 |

So the early N1X looks roughly:

**M3 Max-class multicore performance**

but substantially behind M5 Pro in multicore and behind Apple in single-core. ([CpuTronic.com][9])

However:

> **These are engineering samples, not final production hardware.**

That's extremely important.

---

# And then there's the concerning benchmark

A leaked **Surface Laptop Ultra engineering sample** was reportedly tested for roughly a month.

The results weren't universally fantastic.

The prototype reportedly reached approximately:

**100°C CPU temperature**

under sustained workloads.

Cinebench 2024:

**123 single / 1,386 multi**

with sustained CPU power around 38–50W in some configurations. ([Hardware Busters][10])

That's the biggest red flag I've seen so far.

Not because it proves the final product will run hot — it doesn't — but because **this is exactly the kind of thing I'd want to see independently tested before spending $4K+ on one.**

---

# Local LLM performance is much more interesting

There are already early tests of RTX Spark systems.

One independent benchmark set reports approximately:

### Gemma 3 27B Q4

**~40 tokens/sec**

at 4K context.

At 32K context:

**~22 tok/s**

because KV-cache pressure starts eating into the memory system. ([RTXsparks][11])

Another benchmark dataset reports:

### Llama 3.1 70B Q4

roughly:

**18–24 tok/sec**

on Grace-Blackwell systems. ([RTXsparks][8])

Those numbers are **much more relevant to you** than Geekbench.

---

# And this is why the 128GB is compelling

Think about your current local-LLM environment.

Your RTX 3090 Ti:

**24GB VRAM**

RTX 5090:

**32GB VRAM**

RTX Spark:

**128GB unified memory**

That's a completely different class of local-model capability.

For example:

| Model              | 24GB GPU | 32GB GPU | 128GB Spark |
| ------------------ | -------: | -------: | ----------: |
| 7–14B              |      🟢 |       🟢 |          🟢 |
| 32B                |      🟢 |       🟢 |          🟢 |
| 70B Q4             |   🔴/⚠️ |       ⚠️ |          🟢 |
| 70B Q8             |      🔴 |    🔴/⚠️ |          🟢 |
| 120B-ish quantized |      🔴 |       🔴 |         🟢* |
| Large MoE          |      ⚠️ |       ⚠️ |          🟢 |

*Depending heavily on quantization, context length and inference stack.

That's the real attraction.

---

# Reception so far

I'd characterize the reception as:

### **Technically extremely interesting**

### **Commercially unproven**

### **Software compatibility is the big question**

### **Thermals need validation**

### **128GB is genuinely compelling for local AI**

The early hands-on reaction is generally positive.

For example, reviewers who have handled the Surface Laptop Ultra have praised the hardware, display, keyboard and overall concept. ([Tom's Guide][12])

The ASUS ProArt machines are also getting attention because NVIDIA managed to put this architecture into relatively thin machines. ASUS says the P16 is only around **12.9mm** thick. ([ASUS Global][13])

But there is an important counterpoint:

### CUDA/Windows ARM is still the elephant in the room.

A recent report specifically tested pre-production ASUS hardware and found that CUDA workloads weren't working under the tested driver versions. That is **pre-production hardware**, so I wouldn't conclude that RTX Spark lacks CUDA — NVIDIA explicitly intends it to have the CUDA ecosystem — but it demonstrates exactly why we need independent production testing before buying. ([Tech Times][14])

---

# For YOU, I would wait

Given the hardware you're already running, I **wouldn't preorder the first 128GB Spark laptop**.

I'd wait for approximately **30–60 days after launch**.

What I want to see:

1. **llama.cpp**
2. **Ollama**
3. **vLLM**
4. **TensorRT-LLM**
5. **PyTorch CUDA**
6. **ComfyUI**
7. **Qwen**
8. **Qwen3-Coder**
9. **70B/120B inference**
10. **long-context performance**
11. **GPU memory bandwidth**
12. **sustained thermals**
13. **battery life**
14. **Windows ARM compatibility**
15. **Linux support**

And particularly:

> **128GB Spark vs RTX 5090 32GB vs Apple M5 Pro/Max/Ultra vs Ryzen AI Max+ 395 128GB**

That is the comparison I think would actually tell us whether Spark is revolutionary or simply an expensive curiosity.

### My current prediction

For **gaming**, I don't think RTX Spark is going to replace your 5090-class desktop.

For **general productivity**, I don't think it beats Apple Silicon's efficiency story.

But for:

**portable local AI + CUDA + 128GB unified memory + reasonable gaming + development**

I think RTX Spark could become **one of the most interesting laptops for local-LLM users we've seen**.

And given that you're specifically interested in making **local LLM the default AI environment**, the 128GB Spark machines are *much more relevant to you than a normal 64GB/96GB laptop*. ([NVIDIA Newsroom][5])

**My current shortlist would be:**

**#1 ASUS ProArt P16 128GB** → most interesting overall
**#2 Lenovo Yoga Pro 9n 128GB** → potentially better balanced workstation
**#3 Surface Laptop Ultra 128GB** → most interesting Windows reference/design
**#4 ASUS ProArt P14 128GB** → potentially the killer portable AI machine

I'd wait for **real production benchmarks before putting $4K+ down.**

[1]: https://www.theverge.com/news/989133/nvidia-rtx-spark-laptops-n1x-specifications "Nvidia's new RTX Spark laptops launch in October with two different configs"
[2]: https://www.asus.com/proart/laptops-home/ "ProArt Laptops | AI Laptops for Creators"
[3]: https://www.tomshardware.com/laptops/lenovo-details-its-rtx-spark-laptops-yoga-pro-9n-and-yoga-9n-2-in-1-get-full-specs-stylus-support "Lenovo details its RTX Spark laptops — Yoga Pro 9n and Yoga 9n 2-in-1 get full specs, stylus support | Tom's Hardware"
[4]: https://www.asus.com/laptops/for-creators/proart/proart-p16-h7607/techspec/ "ProArt P16 (H7607) - Tech Specs｜Laptops For Creators｜ASUS Global"
[5]: https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark "NVIDIA and Microsoft Reinvent Windows PCs for the Age of Personal AI | NVIDIA Newsroom"
[6]: https://www.tomshardware.com/laptops/nvidias-rtx-spark-n1x-launches-in-october-for-laptops-and-desktops-18-or-20-cpu-cores-paired-with-5-120-or-6-144-cuda-cores-up-to-128gb-of-unified-memory "Nvidia's RTX Spark N1X launches in October for laptops and desktops — 18 or 20 CPU cores, paired with 5,120 or 6,144 CUDA cores, up to 128GB of unified memory | Tom's Hardware"
[7]: https://arstechnica.com/gadgets/2026/06/nvidia-gets-into-the-arm-pc-business-with-new-high-end-rtx-spark-processor/ "Nvidia RTX Spark comes to Windows PCs with Arm CPU, RTX GPU, and unified memory - Ars Technica"
[8]: https://rtxsparks.com/ "RTXsparks — The independent registry for RTX Spark AI PCs"
[9]: https://cputronic.com/cpu/nvidia-rtx-spark-n1x "NVIDIA RTX Spark N1X: Detailed Specifications and Benchmark Ratings - CpuTronic"
[10]: https://hwbusters.com/news/an-unreleased-rtx-spark-laptop-got-a-month-of-testing-and-the-cpu-lives-at-100c/ "An Unreleased RTX Spark Laptop Got a Month of Testing — and the CPU Lives at 100°C - Hardware Busters"
[11]: https://rtxsparks.com/guides/benchmark-gemma-3-27b-rtx-spark "Gemma 3 27B benchmarks on RTX Spark — RTX Spark | RTXsparks"
[12]: https://www.tomsguide.com/computing/laptops/microsoft-surface-laptop-ultra-rtx-spark-hands-on-review "I just tested Microsoft Surface Laptop Ultra - Nvidia RTX Spark brings life to one of the best laptops I've ever tried"
[13]: https://www.asus.com/blog/what-s-driving-the-buzz-media-s-first-impressions-of-asus-proart-laptops-at-computex-2026/ "Why the buzz? ASUS ProArt & NVIDIA RTX Spark at Computex｜ASUS Global"
[14]: https://www.techtimes.com/articles/326553/20260903/asus-proart-rtx-spark-debut-thinner-lighter-128gb-cuda-ai-unverified.htm "ASUS ProArt RTX Spark Debut: Thinner, Lighter, 128GB, But CUDA AI Unverified"
