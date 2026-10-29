# ⚡ ROM FLASHER TOOL — CORE AGENT MANDATES & RULES

## 🛡️ THE 4-STAGE PEAK-HARDENING RULE (ZERO BOOTLOOP MANDATE)
> **STRICT BINDING INSTRUCTION:** Whenever Rohit (@Rom_Flasher) requests ANY feature, upgrade, or modification to the ROM Flasher Tool, NEVER write superficial, single-scenario, or happy-path code. The feature MUST undergo and pass the following **4 Compulsory Verification Layers at Peak Engineering Standards** before delivery. Rohit must NEVER have to remind or ask for deeper checks!

### 1. HARDWARE & SOC COMPATIBILITY MATRIX
Evaluate and implement explicit logic for all major Android SoCs:
- **Qualcomm Snapdragon:** Fastbootd userspace compatibility, dynamic partition bundling, slotted A/B logic, EDL protection.
- **MediaTek (Dimensity & Helio):** Chained AVB 2.0/3.0 validation. Generic blank 4KB VBMeta flashing is STRICTLY BLOCKED on MediaTek devices to prevent the infamous "Red State: Your device has failed verification" bootloop. Always support patching user's genuine stock vbmeta flags (offset 120-123, flags |= 0x03).
- **Samsung (Exynos & Knox):** Fastboot limitations (Odin vs TWRP fastbootd), Knox bootloader flags, VaultKeeper checks.
- **Google Tensor & Unisoc (Spreadtrum):** GKI (Generic Kernel Image) constraints, Unisoc USB gadget chunk limitations.

### 2. PARTITION ARCHITECTURE & MEMORY BOUNDARIES
Ensure rock-solid handling across all Android partition generations (Android 9 to Android 15+):
- **Legacy Non-A/B vs A/B:** Active slot verification (`current-slot`) and automatic fallback to slotted naming (`system_a` vs `system`).
- **Dynamic Partitions ('super'):** Fastbootd is strictly required for dynamic partitions. If partition resize fails due to constrained super space, automatically free unneeded stock `product` and `system_ext` logical partitions inside `super` before retrying.
- **Virtual A/B Snapshots:** Pre-flight check on `snapshot-update-status`. If `merging` or `snapshotted`, safely execute `snapshot-update:cancel` to prevent permanent partition merge corruption.

### 3. BINARY INTEGRITY & USER INPUT SANITIZATION
Never trust user file inputs blindly; inspect binary magic:
- **Magic Header Inspection:** First 64 bytes inspection (`BOOT_MAGIC`, `AVB0`, Sparse `0xed26ff3a`, Ext4 `0x53ef`, EROFS `0xe2f56a42`).
- **GKI Split Inspection:** Android 13+ devices check `kernel_size == 0L` to strictly distinguish `init_boot` from `boot`. Never overwrite boot with an empty-kernel image.
- **Archive Compression Guard:** Rejects compressed files (`.xz`, `.zip`, `.gz`, `.7z`, `.rar`) by checking extensions and magic bytes (`\xFD7zXZ\x00`, `PK\x03\x04`), giving clear extraction guidance to prevent raw partition byte corruption.
- **Original Filename Preservation:** Query real SAF `DISPLAY_NAME` instead of using generic placeholder filenames.

### 4. ZERO-TOUCH AUTOMATION & RESILIENT USB LIFECYCLE
Provide a flawless, zero-friction user experience:
- **Resilient USB Reconnection:** If an action reboots the target device (e.g. into Fastbootd or bootloader), cleanly close the terminated USB session, poll for the newly enumerated USB endpoint via `waitForDevice`, and acquire a fresh session.
- **Automatic Resume:** Once re-enumerated, continue execution seamlessly without requiring the user to re-tap buttons.
- **Clean First Boot Wipe:** Always execute `erase:userdata`, `format:userdata`, `erase:metadata` after major flashing to prevent old File-Based Encryption (FBE) Keystore keys from triggering recovery bootloops.

---

## 🛑 SACRED HOST PHONE RULE (STRICT MANDATE)
- The device connected via Wireless ADB (`rodin` / `2412DPC0AI`) is Rohit's **HOST PHONE**.
- NEVER run shell root, reboot, fastboot, flash, or partition modification commands on this host phone!
- Target phones connect to the host phone via **USB-OTG cable**.
- Wireless ADB is strictly reserved for APK installation, logcat viewing, and non-destructive screencaps.
