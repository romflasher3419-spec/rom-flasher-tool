# ROM Flasher Tool v1.2.0 — No PIN Screen. Nothing To Enter. 🔓

**The VIP / unlock-code screen is gone from the app itself.** 🎉

In v1.1.0 the lock was only switched *off* — the code was still inside the APK. This build takes it out completely: the lock screen, the PIN verifier and the native unlock library are all **deleted**, so there is nothing left to show and nothing left to type. Install it and use it. 🚀

---

## 🔓 What changed in this build

- **VIP / PIN lock screen REMOVED from the app** — not disabled, deleted. No unlock code, no "locked preview", no device code, no hidden gate.
- **~1.3 MB lighter download** — the native unlock-code library that shipped in v1.0.0 / v1.1.0 is no longer bundled (release APK: **9.94 MB → 8.69 MB**).
- **Cleaner & better protected** — the release is still fully obfuscated (R8 + custom renaming dictionary + stripped logging), and every native debug symbol is stripped.
- Everything else is the same app you already know: flashing, tools, ROM downloader, backups, debloater and more.

> Subscribing (and sharing the tool with friends) still helps the channel a lot. ❤️

---

## ✨ Full feature list

**Flashing**
- Flash Fastboot ROMs (`.bat` / `.sh` flash-script parsing)
- Sideload ROM / GApps / Magisk
- Flash custom images (`boot`, `init_boot`, `super`, `vbmeta`)
- Sparse-chunking engine for huge partitions (4–8 GB)
- A/B Slot Manager
- Confirm before every risky flash / reboot

**Tools & Recovery**
- IMEI / EFS Backup & Restore
- Kernel Backup, Restore & Flash + Boot-loop Rescue
- Root Wizard (KernelSU / Magisk)
- App Installer (`.apk` / `.xapk` / `.apkm`)
- Debloater · File Manager · Full Device Info · Live CMD Terminal

**Stock ROM Downloader**
- Live, region-wise ROMs — Xiaomi, POCO, OnePlus, OPPO, realme, vivo / iQOO, Google Pixel
- Clean one-screen picker · Recovery + fastboot ROMs · Search any device by name
- Parallel multi-segment downloads with fastest-mirror selection + mirror failover
- IDM-style background download popup

**More**
- Payload Dumper + SHA-256 verify · ROM-wise backup picker
- Video guides inside the app · English / Hinglish · Cancel extraction anytime

---

## 📲 Install

1. Download **`app-release.apk`** below.
2. Allow **Install unknown apps** for your browser / file manager.
3. Install and open the app.
4. Connect the target phone with a **USB-OTG cable**.

> **Requirements:** Android 8.0+ · USB-OTG cable · unlocked bootloader for flashing.

**Already on v1.0.0 / v1.1.0?** Just install this over it — it is signed with the same key, so your data and settings stay.

---

## 🔐 Integrity

```
File    : app-release.apk
Size    : __SIZE__ bytes
SHA-256 : __SHA__
```

---

## ⚠️ Disclaimer

Flashing firmware is risky. Always back up first. You alone are responsible for your device — only flash ROMs built for **your exact device codename**.
