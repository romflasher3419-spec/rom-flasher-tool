<div align="center">

<img src="docs/logo.png" width="130" alt="ROM Flasher Tool Logo"/>

# ROM Flasher Tool ⚡

### The Ultimate Android-to-Android Flashing Station over USB-OTG
**Flash Fastboot ROMs, Unbrick Devices, Download Stock ROMs & Root — No PC. No Termux. No Root Required.**

<br/>

[![Latest Release](https://img.shields.io/github/v/release/romflasher3419-spec/rom-flasher-tool?style=for-the-badge&logo=android&logoColor=white&color=10b981)](https://github.com/romflasher3419-spec/rom-flasher-tool/releases/latest)
[![Total Downloads](https://img.shields.io/github/downloads/romflasher3419-spec/rom-flasher-tool/total?style=for-the-badge&logo=github&logoColor=white&color=0284c7)](https://github.com/romflasher3419-spec/rom-flasher-tool/releases)
[![GitHub Stars](https://img.shields.io/github/stars/romflasher3419-spec/rom-flasher-tool?style=for-the-badge&logo=star&logoColor=white&color=facc15)](https://github.com/romflasher3419-spec/rom-flasher-tool/stargazers)
[![Official Website](https://img.shields.io/badge/Official_Website-romflasher.in-7c3aed?style=for-the-badge&logo=googlechrome&logoColor=white)](https://romflasher.in/)
[![Platform](https://img.shields.io/badge/Platform-Android_8.0+-3DDC84?style=for-the-badge&logo=android&logoColor=white)](#)
[![UI](https://img.shields.io/badge/UI-Jetpack_Compose-4285F4?style=for-the-badge&logo=jetpackcompose&logoColor=white)](#)

<br/>

[📥 **Download Latest APK**](https://github.com/romflasher3419-spec/rom-flasher-tool/releases/latest) • [🌐 **Official Guides & ROMs**](https://romflasher.in/) • [💬 **Join Discussions**](../../discussions) • [🐛 **Report Bug**](../../issues)

</div>

---

> ⭐ **Support Open Source:** If ROM Flasher Tool helped you flash, unbrick, or upgrade your Android device without a computer, please **give this repository a Star**! It helps the project reach more Android enthusiasts worldwide.

---

## ⚡ Why ROM Flasher Tool?

Traditional Android flashing requires a PC, ADB/Fastboot drivers, platform-tools, and command-line knowledge. **ROM Flasher Tool** eliminates all of that by turning your spare Android phone into a high-speed, portable flashing deck:

| Feature | ⚡ ROM Flasher Tool | 💻 PC (Windows / Linux) | 📟 Termux / OTG CLI |
| :--- | :---: | :---: | :---: |
| **1-Click Auto Flasher** | ✅ **1-Tap Flash (No PC/Termux)** | ❌ Multiple manual steps | ❌ None |
| **Native Rust Payload Dumper** | ✅ **Extract payload.bin on phone** | ⚠️ Heavy Python/Go scripts | ❌ Resource intensive/slow |
| **No PC Required** | ✅ **100% Mobile (USB-OTG)** | ❌ Computer Needed | ⚠️ Complex command setup |
| **No Host Root Required** | ✅ **Works on any stock phone** | N/A | ❌ Usually requires root |
| **Fastboot Script Runner** | ✅ **Auto-runs `.bat` / `.sh`** | ⚠️ Manual CMD commands | ❌ No native script parser |
| **Built-in ROM Downloader** | ✅ **Multi-segment Fast Download** | ❌ Manual web search | ❌ None |
| **Super Partition Sparse Chunking** | ✅ **Streams 4–8 GB images safely** | ⚠️ Driver/Buffer sensitive | ❌ Prone to buffer crash |
| **Touchscreen UI** | ✅ **Apple-grade Dark Glassmorphism** | ❌ Boring command prompt | ❌ Pure terminal |
| **EFS & Baseband Backup** | ✅ **1-Tap IMEI/Modem Safety** | ⚠️ Complex QFIL / QPST tools | ❌ None |

---

## 📱 Device Compatibility & Supported Brands

ROM Flasher Tool supports any Android phone with a standard Fastboot interface:

| Brand / Ecosystem | Supported Interfaces | Supported Features & Capabilities |
| :--- | :---: | :--- |
| **Xiaomi / Redmi / POCO** | Fastboot, Recovery Sideload | Official HyperOS & MIUI Fastboot scripts, `super.img` sparse chunking, TWRP/OrangeFox flashing, A/B slot switching |
| **OnePlus** | Fastboot, Recovery Sideload | OxygenOS & ColorOS flashing, `init_boot` / `boot` KernelSU & Magisk root patching |
| **realme / OPPO** | Fastboot, Sideload | Official stock firmware restore, custom recovery installation, partition flashing |
| **Google Pixel** | Fastboot | Factory image flashing, bootloader status verification, `vbmeta` flags management |
| **vivo / iQOO** | Fastboot | Stock firmware updates, system app debloater, fast app installer |
| **Motorola, Nothing & Others** | Fastboot, Sideload | Custom ROM sideloading, recovery flashing, fastboot reboot options |

---

## 📚 Written guides for every video

> Every video on the channel has its own written page — the same steps in text, with the full description, the download links and the questions people ask. There are **brand**, **ROM**, **year** and **topic** indexes too, so you can find the guide for your exact phone without scrolling a channel.
>
> 👉 **[Open the Rom Flasher guides](https://romflasher.in/)**

---

## 🎉 Unlocked for Everyone

> **The 2,000-subscriber milestone is COMPLETE! 🎉**
> The **[Rom Flasher YouTube channel](https://www.youtube.com/channel/UC-Oc7NNVa0oW3nHI1L-3oKQ)** crossed **2,000 subscribers**, so the app is now **fully unlocked for everyone** — no lock screen, no unlock code, nothing to enter.

A huge thank you to every single subscriber who made this happen. ❤️ Download the latest release and enjoy the full tool. Subscribing (and sharing the tool) still helps the channel a lot.

---

## 📺 YouTube

<!-- YT-SUBS:START -->
[![YouTube Subscribers](https://img.shields.io/badge/YouTube%20Subscribers-1.72K-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/@Rom_Flasher)
<!-- YT-SUBS:END -->

<!-- YT-VIDEO:START -->
<a href="https://www.youtube.com/watch?v=MPSwx3y1ipA"><img src="https://i.ytimg.com/vi/MPSwx3y1ipA/mqdefault.jpg" width="150" align="left" alt="Pass Basic, Device &amp; Strong Integrity in 30 Seconds! 🔥 Device Certified [No Modules, No PC]"/></a>
<a href="https://www.youtube.com/watch?v=MPSwx3y1ipA"><b>Pass Basic, Device &amp; Strong Integrity in 30 Seconds! 🔥 Device Certified [No Modules, No PC]</b></a><br/>
<sub>🔥 LATEST&nbsp;&nbsp;·&nbsp;&nbsp;📅 25 Oct 2026</sub>
<br clear="all"/>
<br/>
<a href="https://www.youtube.com/watch?v=v5adFI2we2M"><img src="https://i.ytimg.com/vi/v5adFI2we2M/mqdefault.jpg" width="150" align="left" alt="PixelExperience Plus on Mi Pad 5 📱 Android 13 Sideload Guide"/></a>
<a href="https://www.youtube.com/watch?v=v5adFI2we2M"><b>PixelExperience Plus on Mi Pad 5 📱 Android 13 Sideload Guide</b></a><br/>
<sub>🏆 MOST WATCHED&nbsp;&nbsp;·&nbsp;&nbsp;19,014 views</sub>
<br clear="all"/>
<br/>
<a href="https://www.youtube.com/watch?v=NUjIiqviMd0"><img src="https://i.ytimg.com/vi/NUjIiqviMd0/mqdefault.jpg" width="150" align="left" alt="TWRP on Xiaomi 11T Pro 🧡 Flash Recovery With One Fastboot Command"/></a>
<a href="https://www.youtube.com/watch?v=NUjIiqviMd0"><b>TWRP on Xiaomi 11T Pro 🧡 Flash Recovery With One Fastboot Command</b></a><br/>
<sub>❤️ FAN FAVOURITE&nbsp;&nbsp;·&nbsp;&nbsp;110 likes</sub>
<br clear="all"/>
<!-- YT-VIDEO:END -->

> 🤖 This block keeps itself up to date — the subscriber count, the newest video and the all-time top videos refresh on their own.

---

## ✨ Features Breakdown

<details open>
<summary><b>🛡️ 1-Click Play Integrity & Device Certification Bypass (NEW)</b></summary>

- **Pass All 3 Integrity Levels** — Instant green checks on **Basic Integrity**, **Device Integrity**, and **Strong Integrity** in under 30 seconds!
- **Fix "Device is not certified"** — Automatically restores official Google Play Protect device certification in Google Play Store settings.
- **Zero Manual Downloads & Zero Modules** — No hunting for broken PIF modules or keybox files on Telegram/forums; auto-detects Android OS and auto-injects verified patches.
- **Automated Banking App Cloak** — Seamlessly sets up Zygisk root cloaking for Google Pay, PhonePe, Paytm, and corporate banking apps with zero detection.
- **100% Phone-to-Phone (No PC Needed)** — Injected directly over USB-OTG from host phone without typing a single terminal command.

</details>

<details open>
<summary><b>🔥 1-Click Auto Flasher Engine</b></summary>

- **True 1-Tap ROM Flashing** — Flash ANY AOSP Custom ROM (Project Infinity X, PixelOS, LineageOS, Evolution X) with just ONE tap over USB-OTG!
- **Zero PC & Zero Termux** — No commands, no scripts, no desktop dependencies whatsoever.
- **No Vendor_Boot Pre-Flashing Needed** — Automated recovery sideloading eliminates manual partition prep.
- **Intelligent A/B Slot Manager** — Seamless slot switching, verification, and automated direct boot to system upon completion.

</details>

<details open>
<summary><b>🚀 Flashing Engine</b></summary>

- **Flash Fastboot ROMs** — full `.bat` / `.sh` flash-script parsing with Windows → Unix path normalisation
- **Sideload ROM / GApps / Magisk** — recovery sideload over USB
- **Flash Custom Images** — `boot`, `init_boot`, `super`, `vbmeta`, `recovery` and more
- **Sparse Chunking Engine** — streams huge partitions (4–8 GB `super.img`) safely without running out of RAM
- **A/B Slot Manager** — read and switch active boot slots (`_a` / `_b`)
- **Safety Prompts** — confirm before every risky flash or reboot operation

</details>

<details open>
<summary><b>🛠️ Tools & Recovery Deck</b></summary>

- **IMEI / EFS Backup & Restore** — guard against radio/NVRAM corruption
- **Kernel Backup, Restore & Flash** — flash AnyKernel3 zip files directly
- **Boot-loop Rescue** — automatic fastboot rescue path
- **Root Wizard** — 1-click download and patch for KernelSU / Magisk
- **App Installer** — install `.apk`, `.xapk`, `.apkm` directly to target device
- **Debloater** — safely freeze and uninstall bloatware
- **File Manager** — browse and transfer files between both phones over OTG
- **Hardware Diagnostics** — read bootloader lock state, CPU, serial number, and battery
- **Live Terminal & Real-Time Console Logs**

</details>

<details open>
<summary><b>⬇️ Built-In Stock ROM Downloader</b></summary>

- **Official Region-Wise Firmware** — Xiaomi, POCO, OnePlus, OPPO, realme, vivo, Google Pixel
- **Search Any Device** by commercial name or codename
- **Fast Multi-Threaded Engine** with automatic fastest mirror selection
- **Background Downloads** with progress notification
- **Automatic Resume & Mirror Failover**

</details>

<details open>
<summary><b>🧩 Power Tools</b></summary>

- **Payload Dumper** — extract `.bin` images directly from `payload.bin` with SHA-256 verification
- **ROM-wise Backup Picker** for easy restoration
- **Integrated Video Tutorials** inside the app
- **Dual Language UI** — switch between English and Hinglish seamlessly with 1 tap

</details>

---

## 📱 Screenshots

<div align="center">

<table>
  <tr>
    <td align="center"><img src="docs/screenshots/screenshot-1.jpg" width="280" alt="ROM Flasher Tool - fastboot ROM flashing from an Android phone over USB-OTG"/></td>
    <td align="center"><img src="docs/screenshots/screenshot-2.jpg" width="280" alt="ROM Flasher Tool - stock ROM downloader, EFS/IMEI backup and device tools"/></td>
  </tr>
</table>

</div>

---

## 📲 How to Install & Use

1. Download the latest **`app-release.apk`** from [Releases](https://github.com/romflasher3419-spec/rom-flasher-tool/releases/latest).
2. Install the APK on your host phone (allow *Install unknown apps* if prompted).
3. Connect your host phone to the target phone using a **USB-OTG Cable / Adapter**.
4. Put the target phone in **Fastboot Mode** (`Power + Volume Down`) or **Recovery Mode**.
5. Accept the USB permission prompt and start flashing!

> **Requirements:** Host phone running Android 8.0 (API 26) or newer · OTG Adapter/Cable · Target device with unlocked bootloader.

---

## ❓ Frequently Asked Questions (FAQ)

<details>
<summary><b>Can I really flash a custom ROM without any PC?</b></summary>

Yes! ROM Flasher Tool communicates directly with the target device's fastboot and recovery endpoints over the Android USB Host API. No computer, laptop, or Termux is needed.
</details>

<details>
<summary><b>Do I need to root my host phone?</b></summary>

No! The host phone that runs the app does **NOT** require root. It uses native Android USB host permissions.
</details>

<details>
<summary><b>Does it work on Samsung devices?</b></summary>

Samsung devices use proprietary Odin/Download protocol instead of standard fastboot protocol. Fastboot flashing requires a standard fastboot interface (Xiaomi, POCO, OnePlus, realme, Pixel, Motorola, etc.).
</details>

<details>
<summary><b>Is the app free?</b></summary>

Yes, **100% free and unlocked**. No subscriptions, no ads, no paywalls.
</details>

<details>
<summary><b>Can I brick my phone?</b></summary>

The app features confirmation safety guards and boot-loop rescue. However, flashing custom firmware always carries risk. Always create an EFS/IMEI backup and ensure firmware files match your exact device codename.
</details>

---

## 📊 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=romflasher3419-spec/rom-flasher-tool&type=Date)](https://star-history.com/#romflasher3419-spec/rom-flasher-tool&Date)

---

## 🐞 Issues & Community

- 🐛 **Found a bug?** Open an [Issue](../../issues/new/choose) with your device model and log.
- 💬 **Questions or Discussions?** Join the community in [GitHub Discussions](../../discussions).
- 📺 **YouTube Channel:** [Rom Flasher](https://www.youtube.com/@Rom_Flasher)
- 🌐 **Official Website & Guides:** [romflasher.in](https://romflasher.in/)

---

<div align="center">
<sub>© 2026 ROM Flasher Tool · Made with ❤️ in India · <a href="PRIVACY.md">Privacy Policy</a> · <a href="TERMS.md">Terms of Service</a></sub>
</div>
