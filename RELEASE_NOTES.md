# ROM Flasher Tool v1.3.0 - Major Core Upgrade & Fastboot Power Features 🚀

**ROM Flasher Tool v1.3.0 is a major upgrade** bringing temporary image booting, universal Qualcomm + MediaTek EFS backup support, instant payload dumper inspection, new reboot modes, and critical bootloader fixes! 🛠️

---

## 🌟 What's New in v1.3.0

### 1. ⚡ Custom Image Flasher — Temporary Boot & Custom Partitions
- **New `BOOT (RAM)` Feature:** Test custom recoveries (TWRP / OrangeFox) or kernels temporarily via `fastboot boot` without overwriting on-device flash partitions.
- **Custom Partition Input:** Added support for `vendor_dlkm`, `system_dlkm`, `modem`, `persist`, or any user-defined partition name.
- **OOM Protection:** Added safeguards against memory allocation crashes on large partition files.

### 2. 🔄 Advanced Reboot — Complete 2x2 Modes
- Added **`ADB -> System`** (Normal reboot into Android).
- Added **`ADB -> FastbootD`** (Userspace fastboot mode for dynamic partitions).
- Added **`Fastboot -> Bootloader`** and **`Fastboot -> FastbootD`**.

### 3. 🛡️ Universal EFS & IMEI Backup/Restore (Qualcomm + MediaTek)
- Dynamic `/dev/block/by-name` detection now scans and backs up both **Qualcomm** (`modemst1`, `modemst2`, `fsg`, `fsc`, `persist`) and **MediaTek** (`nvram`, `nvdata`, `nvcfg`, `protect1`, `protect2`, `seccfg`) partitions.
- Restore engine automatically restores whatever matching partition images exist in the backup.

### 4. 🔁 A/B Slot Manager Standard Compliance
- Fixed slot switcher to send standard AOSP fastboot command `set_active:a` / `set_active:b` (preventing bootloader rejections caused by underscore prefixes).
- UI now displays clean `SLOT A` and `SLOT B`.

### 5. 📦 High-Speed Payload Dumper (Zero-Disk Overhead)
- Partition manifest is now streamed directly from the ROM zip header in `< 100ms` without extracting 4GB–8GB of data to phone storage.

### 6. 🧠 AnyKernel3 (AK3) Target ABI Detection
- ADB automatically probes the connected phone's real CPU ABI (`ro.product.cpu.abi`) to select the exact matching shell architecture (`arm64`, `arm`, etc.).

### 7. 📁 Remote File Manager
- Added quick **"New Folder"** 1-tap shortcut directly in the directory path bar.

### 8. 💻 Zero-Lag Terminal Console
- Replaced frame-by-frame log scroll animation with instant scrolling, delivering smooth 60/120 FPS rendering even during high-speed partition flashes.

---

## ✨ Full Feature Overview
- **Fastboot ROM Flashing:** Android-to-Android over USB-OTG. No PC. No Termux.
- **AOSP ADB Sideload:** PixelExperience, LineageOS, GApps & Magisk.
- **Single & Custom Image Flashing:** Boot, Vendor Boot, Recovery, Super 9.2GB RAW, etc.
- **Dual Slot A/B Engine & Slot Switcher**
- **Hardware EFS / IMEI Backup & Restore**
- **AnyKernel3 Kernel Flashing & Bootloop Rescue**
- **Root Wizard:** Guided Magisk & KernelSU rooting
- **Remote Debloater & File Manager**
