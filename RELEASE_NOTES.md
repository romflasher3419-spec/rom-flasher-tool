# ROM Flasher Tool v1.2.7 - Flash Control Overhaul. Stop It Whenever You Want. 🚨

**The flashing console finally has real control buttons.** In this build the live flash console gets a
**STOP button in its header**, **closing the console actually stops the running flash**, and the
**Reboot section only reboots** - it never kicks off a flash script by accident. On top of that every
option card now opens and closes with a **proper smooth animation** instead of snapping. 🚀

---

## 🔧 What changed in this build

### Flash console
- **STOP button added to the console header** - the header now shows *Save / Copy / Share / Stop flash / Close*
  while a flash is running. One tap stops the flash script where it is.
- **Closing the console now really stops the flash.** Previously closing the window only hid the UI and the
  flash script kept running in the background. Now the flash job is cancelled and the script is terminated.
- The flash notification switches to **"Flash stopped" / "Stopped by the user"** the moment you stop it.

### Reboot section
- **The reboot section ONLY reboots.** It stops any running flash first and then reboots via
  ADB -> fastboot -> ADB -> local fallback. It never starts a flash script.

### Option cards
- **Every option card now expands and collapses smoothly.** The old `animateContentSize()` approach re-measured
  the whole expanded content on every animation frame and stuttered. It now uses `AnimatedVisibility` with an
  explicit vertical expand/shrink (280 ms, FastOutSlowInEasing) plus a short fade (190 ms).
- Measured on a POCO F5 (120 Hz panel): **102 frames in 833 ms, frame gap p50 = 8.3 ms, p90 = 9.9 ms,
  0 frames over 16 ms** - every frame lands inside the refresh budget.

### Cleanup
- **No more "resume interrupted flash" anywhere** in the app.
- Removed leftover QA/testing hooks from the release build (verified: zero QA strings inside the APK).

---

## ✨ Full feature list

**Flashing**
- Flash Fastboot ROMs (`.bat` / `.sh` flash-script parsing)
- Sideload ROM / GApps / Magisk
- Flash custom images (`boot`, `init_boot`, `super`, `vbmeta`)
- Sparse-chunking engine for huge partitions (4-8 GB)
- A/B Slot Manager
- Confirm before every risky flash / reboot

**Tools & Recovery**
- IMEI / EFS Backup & Restore
- Kernel Backup, Restore & Flash + Boot-loop Rescue
- Root Wizard (KernelSU / Magisk)
- App Installer (`.apk` / `.xapk` / `.apkm`)
- Debloater - File Manager - Full Device Info - Live CMD Terminal

**Stock ROM Downloader**
- Live, region-wise ROMs - Xiaomi, POCO, OnePlus, OPPO, realme, vivo / iQOO, Google Pixel
- Clean one-screen picker - Recovery + fastboot ROMs - Search any device by name
- Parallel multi-segment downloads with fastest-mirror selection + mirror failover
- IDM-style background download popup

**More**
- Payload Dumper + SHA-256 verify - ROM-wise backup picker
- Video guides inside the app - English / Hinglish - Cancel extraction anytime

---

## 📲 Install

1. Download **`app-release.apk`** below.
2. Allow **Install unknown apps** for your browser / file manager.
3. Install and open the app.
4. Connect the target phone with a **USB-OTG cable**.

> **Requirements:** Android 8.0+ - USB-OTG cable - unlocked bootloader for flashing.

> **Already on v1.2.6 or older?** Just install this over it - it is signed with the same key, so your data
> and settings stay exactly where they are.

---

## 🔐 Integrity

```
File    : app-release.apk
Size    : 8654006 bytes
SHA-256 : 2C887EF5D0B48608060FC9E30E82906EACC0DD053C57BF42C6FB43801A628BB0
```

---

## ⚠️ Disclaimer

Flashing firmware is risky. Always back up first. You alone are responsible for your device - only flash ROMs
built for **your exact device codename**.
