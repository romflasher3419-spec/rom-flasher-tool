# ROM Flasher Tool v1.2.8 - One Icon, One Splash, No More Flicker 🔄

**The launch screen is fixed.** The app used to show the app icon **twice** while opening - first the big
Android 12+ system splash icon, then a second smaller copy of the same artwork from the window background,
and only then the dashboard. This build shows the icon **exactly once**, masked exactly like the launcher
icon, and the background never jumps between two different colours. 🚀

---

## 🔄 What changed in this build

### Launch screen (the double-icon fix)
- **The app icon now appears only ONCE.** Previously the platform splash screen drew the raw icon artwork
  and the window background drew a second, differently sized copy of it - which is exactly the
  "big icon, then small icon" you saw on launch.
- **The splash icon is now the real adaptive launcher icon** (`@mipmap/ic_launcher`), so the system masks it
  with the same shape it uses on the launcher instead of showing a floating, background-less logo.
- **One continuous background.** The splash background and the launch window background are now the same
  dark gradient, so there is no colour flash between the splash and the dashboard.
- **Android 8 - 11 keep their branded launch frame** (gradient + centred logo) - those versions have no
  platform splash screen, so the logo is still shown there, still only once.

### Carried over from v1.2.7
- **STOP button in the flash console header** - *Save / Copy / Share / Stop flash / Close* while flashing.
  One tap stops the flash script where it is.
- **Closing the console now really stops the flash** instead of only hiding the UI.
- **The reboot section only reboots** - it never starts a flash script by accident.
- **Every option card expands and collapses smoothly** (`AnimatedVisibility`, 280 ms expand/shrink + 190 ms
  fade). Measured on a 120 Hz panel: 102 frames in 833 ms, frame gap p50 = 8.3 ms, p90 = 9.9 ms,
  **0 frames over 16 ms**.
- No "resume interrupted flash" anywhere in the app.

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

> **Already on v1.2.7 or older?** Just install this over it - it is signed with the same key, so your data
> and settings stay exactly where they are.

---

## 🔐 Integrity

```
File    : app-release.apk
Size    : 8654581 bytes
SHA-256 : 5D91ED789998467AF54072FA05C95EF7C5408ED371BBE55C8385CA76FB7C0712
```

---

## ⚠️ Disclaimer

Flashing firmware is risky. Always back up first. You alone are responsible for your device - only flash ROMs
built for **your exact device codename**.
