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
    <td align="center"><img src="docs/screenshots/screenshot-1.jpg" width="260"/></td>
    <td align="center"><img src="docs/screenshots/screenshot-2.jpg" width="260"/></td>
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
