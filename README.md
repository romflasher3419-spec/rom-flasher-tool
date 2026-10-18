<div align="center">

<img src="docs/logo.png" width="128" alt="ROM Flasher Tool"/>

# ROM Flasher Tool

**Flash Fastboot & custom ROMs — Android → Android, over USB-OTG. No PC. No Termux.**

[![Platform](https://img.shields.io/badge/Platform-Android%208.0%2B-3DDC84?logo=android&logoColor=white)](#)
[![Kotlin](https://img.shields.io/badge/Kotlin-1.9-7F52FF?logo=kotlin&logoColor=white)](#)
[![UI](https://img.shields.io/badge/UI-Jetpack%20Compose-4285F4?logo=jetpackcompose&logoColor=white)](#)
[![Build](https://img.shields.io/badge/Build-Unlocked-brightgreen)](https://www.youtube.com/channel/UC-Oc7NNVa0oW3nHI1L-3oKQ)
[![YouTube](https://img.shields.io/badge/YouTube-Rom%20Flasher-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/channel/UC-Oc7NNVa0oW3nHI1L-3oKQ)

</div>

---

## 🎉 Unlocked for Everyone

> **The 2,000-subscriber milestone is COMPLETE! 🎉**
> The **[Rom Flasher YouTube channel](https://www.youtube.com/channel/UC-Oc7NNVa0oW3nHI1L-3oKQ)** crossed **2,000 subscribers**, so the app is now **fully unlocked for everyone** — no lock screen, no unlock code, nothing to enter.

A huge thank you to every single subscriber who made this happen. ❤️ Download the latest release and enjoy the full tool. Subscribing (and sharing the tool) still helps the channel a lot.

---

## 📺 YouTube

<!-- YT-SUBS:START -->
[![YouTube Subscribers](https://img.shields.io/badge/YouTube%20Subscribers-2.03K-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/@Rom_Flasher)
<!-- YT-SUBS:END -->

<!-- YT-VIDEO:START -->
<a href="https://www.youtube.com/watch?v=pxp_m6uAgug"><img src="https://i.ytimg.com/vi/pxp_m6uAgug/mqdefault.jpg" width="150" align="left" alt="🔥 Backup &amp; Flash ANY Android Kernel in 1 CLICK?! 😱 No APK, No Commands!"/></a>
<a href="https://www.youtube.com/watch?v=pxp_m6uAgug"><b>🔥 Backup &amp; Flash ANY Android Kernel in 1 CLICK?! 😱 No APK, No Commands!</b></a><br/>
<sub>🔥 LATEST&nbsp;&nbsp;·&nbsp;&nbsp;📅 17 Oct 2026</sub>
<br clear="all"/>
<br/>
<a href="https://www.youtube.com/watch?v=v5adFI2we2M"><img src="https://i.ytimg.com/vi/v5adFI2we2M/mqdefault.jpg" width="150" align="left" alt="PixelExperience Plus For MI PAD 5 | Android 13 |"/></a>
<a href="https://www.youtube.com/watch?v=v5adFI2we2M"><b>PixelExperience Plus For MI PAD 5 | Android 13 |</b></a><br/>
<sub>🏆 MOST WATCHED&nbsp;&nbsp;·&nbsp;&nbsp;👀 19,002 views</sub>
<br clear="all"/>
<br/>
<a href="https://www.youtube.com/watch?v=NUjIiqviMd0"><img src="https://i.ytimg.com/vi/NUjIiqviMd0/mqdefault.jpg" width="150" align="left" alt="Flash TWRP on Xiaomi 11T PRO  Best Recovery"/></a>
<a href="https://www.youtube.com/watch?v=NUjIiqviMd0"><b>Flash TWRP on Xiaomi 11T PRO  Best Recovery</b></a><br/>
<sub>❤️ MOST LIKED&nbsp;&nbsp;·&nbsp;&nbsp;♥ 110 likes</sub>
<br clear="all"/>
<!-- YT-VIDEO:END -->

> 🤖 This block keeps itself up to date — the subscriber count, the newest video and the all-time top videos refresh on their own.

---

## 📖 What is ROM Flasher Tool?

An **Apple/iOS-grade Jetpack Compose** app that turns one Android phone into a complete flashing station. Plug the target device into the host phone over **USB-OTG** and flash Fastboot ROMs, sideload packages, back up EFS/IMEI, rescue boot loops and much more — all from one clean, dark, glassmorphic UI.

Everything runs **on the device**. No PC, no Termux, no root required for the flashing flows (only an unlocked bootloader).

---

## ✨ Features

<details open>
<summary><b>🚀 Flashing</b></summary>

- **Flash Fastboot ROMs** — full `.bat` / `.sh` flash-script parsing with Windows → Unix path normalisation
- **Sideload ROM / GApps / Magisk** — recovery sideload over USB
- **Flash Custom Images** — `boot`, `init_boot`, `super`, `vbmeta` and more
- **Sparse Chunking Engine** — streams huge partitions (4–8 GB `super.img`) safely
- **A/B Slot Manager** — read and switch active slots
- **Confirm before every risky flash / reboot**

</details>

<details open>
<summary><b>🛠️ Tools & Recovery</b></summary>

- **IMEI / EFS Backup & Restore**
- **Kernel Backup, Restore & Flash**
- **Boot-loop Rescue** — automatic fastboot restore path
- **Root Wizard** — KernelSU / Magisk, straight from the app
- **App Installer** — `.apk` / `.xapk` / `.apkm`
- **Debloater** — remove system bloat
- **File Manager** — upload / download between the two phones
- **Full Device Info**
- **Live CMD Terminal + Logs**

</details>

<details open>
<summary><b>⬇️ Stock ROM Downloader</b></summary>

- **Live, region-wise stock ROM index** — Xiaomi, POCO, OnePlus, OPPO, realme, vivo / iQOO, Google Pixel
- **Clean one-screen ROM picker** — no console, no clutter
- **Recovery + Fastboot ROMs both listed**
- **Search any device by name** (no phone needed)
- **Parallel multi-segment fast download** with automatic **fastest-mirror selection**
- **IDM-style download popup** that keeps running in the background
- **Mirror failover** if speed drops mid-download

</details>

<details open>
<summary><b>🧩 More</b></summary>

- **Payload Dumper + SHA-256 verify**
- **ROM-wise Backup Picker** for safe restores
- **Video guides inside the app**
- **Parallel multi-segment downloads**
- **Buttons stay off until a phone is connected**
- **Cancel a running ROM extraction anytime**
- **Change language anytime** (English / Hinglish) from the 🌐 button

</details>

---

## 📱 Screenshots

<div align="center">

<table>
  <tr>
    <td align="center"><img src="docs/screenshots/screenshot-1.jpg" width="260" alt="ROM Flasher Tool - fastboot ROM flashing from an Android phone over USB-OTG"/></td>
    <td align="center"><img src="docs/screenshots/screenshot-2.jpg" width="260" alt="ROM Flasher Tool - stock ROM downloader, EFS/IMEI backup and device tools"/></td>
  </tr>
</table>

</div>

> More screenshots welcome — drop PNGs/JPGs into [`docs/screenshots/`](docs/screenshots/) and add a row above.

---

## 📲 Install

1. Download the latest **`app-release.apk`** from the [Releases](../../releases) page.
2. On your Android phone, allow **Install unknown apps** for your browser / file manager.
3. Install, open the app, and connect the target phone over a **USB-OTG cable**.

> **Requirements:** Android 8.0 (API 26) or newer · OTG cable · unlocked bootloader for flashing.

---

## ❓ FAQ

<details>
<summary><b>Can I flash a ROM without a PC?</b></summary>

Yes. ROM Flasher Tool is a complete **PC-free flashing station** — it runs on one Android phone and talks to the target phone over **USB-OTG**. No laptop, no Termux, no ADB or fastboot scripts on a computer.
</details>

<details>
<summary><b>Do I need root or a custom recovery?</b></summary>

No. The flashing flows need only an **unlocked bootloader** on the target device. Root is optional — the built-in Root Wizard installs **KernelSU / Magisk** if you want it.
</details>

<details>
<summary><b>Which phones are supported?</b></summary>

Any device with **fastboot** can be flashed. The built-in **Stock ROM Downloader** has a live, region-wise index for **Xiaomi, POCO, OnePlus, OPPO, realme, vivo / iQOO and Google Pixel**.
</details>

<details>
<summary><b>Does it work on Samsung?</b></summary>

Samsung phones do not expose a standard **fastboot** path, so the flashing flows do not apply to them. Other brands work normally over fastboot.
</details>

<details>
<summary><b>Is it free?</b></summary>

Yes — **100% free** to download and use. No account, no ads, no unlock code.
</details>

<details>
<summary><b>Which Android version do I need?</b></summary>

**Android 8.0 (API 26)** or newer on the host phone, plus a **USB-OTG cable**.
</details>

<details>
<summary><b>Is it safe? Can it brick my phone?</b></summary>

Every risky action asks for **confirmation first**, and the app keeps a fastboot **boot-loop rescue** path. That said, flashing is inherently risky — always back up, and only flash ROMs built for your **exact device codename**.
</details>

---

## 🐞 Found a bug? Have an idea?

Open an **[Issue](../../issues/new/choose)** — bug reports and feature requests both land **directly in my notifications**, and I'll reply right there.

Please include your **app version**, your **phone model**, and what you were doing. Screenshots or the app's terminal log speed things up a lot.

For general questions and chat, use **[Discussions](../../discussions)**.

---

## 🧱 About this repository

This is a **distribution repository** — it hosts the documentation, screenshots and the compiled **release APKs**. The application source code is private and is not published here.

Every release is built from source and signed with a private release key, then R8-obfuscated before publishing.

---

## ▶️ YouTube · ❤️ Support

- 📺 **YouTube:** [Rom Flasher](https://www.youtube.com/channel/UC-Oc7NNVa0oW3nHI1L-3oKQ)
- ⭐ **Star** this repo if the tool helped you
- 💰 **Donate:** UPI QR is inside the app (*Donate* button)

---

## ⚠️ Disclaimer

Flashing firmware is **risky**. Always back up first. You alone are responsible for what happens to your device — the developer is not liable for bricked phones, lost data, or voided warranties. Only flash ROMs meant for **your exact device codename**.

---

<div align="center">
<sub>© 2026 ROM Flasher Tool · Made with ❤️ in India</sub>
</div>
