# ROM Flasher Tool v1.4.0 - ⚡ 1-Click AOSP Auto Flasher & BCB Direct Sideload 🚀

**ROM Flasher Tool v1.4.0 is here!** This release introduces the revolutionary **1-Click AOSP Auto Flasher** — an end-to-end hands-free flashing pipeline for AOSP Custom ROMs (PixelOS, Evolution X, crDroid, LineageOS, PixelExperience, etc.) right from your phone over USB-OTG! No PC. No Termux. Zero manual recovery steps. 🛠️

---

## 🌟 What's New in v1.4.0

### 1. ⚡ 1-Click AOSP Auto Flasher (Option 2: ADB Sideload Card)
- **Hands-Free Flashing Pipeline:** Simply pick any AOSP ROM zip file and tap **⚡ AUTO FLASHER**. The tool handles the rest automatically!
- **Auto Device Mode Transition:** If target device is booted in Android (ADB), the engine automatically issues `adb reboot bootloader` and waits for Fastboot re-enumeration.
- **High-Speed Targeted Payload Extraction:** Extracts only essential boot partitions (`boot.img`, `vendor_boot.img`, `init_boot.img`) directly from `payload.bin` into `Download/RomFlasher/Auto_Flasher/<ROM_Name>/` using our zero-overhead native Payload Dumper.
- **Dual-Slot Flashing (A & B):** Automatically flashes all extracted images to both `_a` and `_b` slots (`boot_a`/`boot_b`, `vendor_boot_a`/`vendor_boot_b`, `init_boot_a`/`init_boot_b`) and switches active slot to A.
- **Fastboot Clean Data Wipe:** Automatically performs a clean wipe (`erase userdata` & `erase metadata`) via Fastboot before entering recovery mode.
- **BCB Direct-Sideload Injection (`misc` partition):** Injects a 2048-byte Bootloader Control Block (`boot-recovery` + `recovery\n--sideload\n`) directly into the `misc` partition.
- **Zero-Touch Sideload Streaming:** Device bypasses recovery menus and boots straight into ADB Sideload listening mode. ROM Flasher Tool's Smart USB Daemon detects the connection instantaneously and streams `adb sideload <rom.zip>` until 100% complete!

### 2. 🛡️ Safety Confirmation & Real-Time Console
- Safety confirmation prompt detailing all partitions to be flashed before executing.
- Live real-time console with 60/120 FPS log streaming so you can watch every stage of the pipeline as it executes.

---

## ✨ Full Feature Overview
- **Fastboot ROM Flashing:** Android-to-Android over USB-OTG. No PC. No Termux.
- **1-Click AOSP Auto Flasher:** Targeted extract + Dual Slot flash + Format + Direct Sideload.
- **AOSP ADB Sideload:** PixelExperience, LineageOS, GApps & Magisk.
- **Single & Custom Image Flashing:** Boot, Vendor Boot, Recovery, Super 9.2GB RAW, etc.
- **Dual Slot A/B Engine & Slot Switcher**
- **Hardware EFS / IMEI Backup & Restore (Qualcomm + MediaTek)**
- **AnyKernel3 Kernel Flashing & Bootloop Rescue**
- **Root Wizard:** Guided Magisk & KernelSU rooting
- **Remote Debloater & File Manager**
