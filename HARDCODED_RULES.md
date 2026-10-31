# ⚡ ROM FLASHER AUTOMATED WORKFLOWS — HARDCODED BINDING RULES

> **SYSTEM INSTRUCTION FOR AGENT (ANTIGRAVITY / GEMINI):**
> Ye rules user (Rohit bhai / @Rom_Flasher) ke dwara strictly mandate kiye gaye hain:
> 1. Jab bhi user bole **"new video upload krdi"**, **"nayi video aa gayi hai"**, **"video schedule kar di hai"** ya similar trigger → Run **2-in-1 automated distribution pipeline (YouTube + Website romflasher.in)** ZERO-TO-HERO.
> 2. **FACEBOOK & INSTAGRAM ARE PERMANENTLY REMOVED:** Ab se Facebook aur Instagram par koi video ya reels upload nahi karni hai. Website top bar, articles, aur YouTube description me se bhi Facebook aur Instagram ke saare links aur mentions permanently ban hain.
> 3. Jab bhi user bole **"bhai maine new windows dal li"**, **"windows change kari hai"**, **"pc format kiya hai"** ya similar trigger → **Bina koi sawaal pooche 100% Zero-Click Full System Auto-Restore execute karo.**
> 4. **SACRED HOST PHONE RULE (STRICT MANDATE):** Wireless ADB se jo device (rodin) connected hai wo Rohit bhai ka HOST PHONE hai (jisme Rom Flasher Tool run hota hai). Us par kabhi bhi direct ADB shell se root, fastboot, flash, reboot ya system modification test nahi karni! Target phone host phone se USB-OTG ke through judta hai aur saara operation APP KE ANDAR se hota hai. Wireless ADB sirf APK install aur app logcat dekhne ke liye use hoga.
> 5. **THE 4-STAGE PEAK-HARDENING RULE (ZERO BOOTLOOP MANDATE):** Jab bhi Rohit bhai kisi bhi feature, upgrade ya modification ka bolen, agent ko KABHI BHI superficial / happy-path code nahi likhna hai. Agent ko 4 compulsory stages (Hardware/SoC matrix for Qualcomm/MediaTek/Exynos/Tensor, Partition & Super space calculations, Binary magic & archive input validation, aur Zero-touch auto-reconnection USB lifecycles) par feature ko peak level par harden karke hi deliver karna hai taaki kisi ka phone kabhi bootloop na ho!

---

## 0. 🛡️ THE 4-STAGE PEAK-HARDENING & HARDWARE CALCULATION PROTOCOL (ZERO BOOTLOOP MANDATE)

> **STRICT BINDING INSTRUCTION:** Jab bhi Rohit bhai koi feature request ya upgrade demand karein, agent ko us feature ko deliver karne se pehle **4 COMPULSORY HARDENING STAGES** se guzaarna mandatory hai. Rohit bhai ko dobara bolne ya yaad dilane ki zaroorat nahi padni chahiye — pehli baar mein hi feature peak level of safety par ready hona chahiye!

### 🔹 STAGE 1: HARDWARE & SOC COMPATIBILITY MATRIX
Har feature ko sabhi major mobile SoCs ke context mein verify aur calculate karna hai:
- **Qualcomm (Snapdragon):** Standard fastbootd, dynamic partitions, dual-slot A/B, EDL fail-safes.
- **MediaTek (Dimensity & Helio):** Chained AVB 2.0/3.0 verification (`vbmeta`, `vbmeta_system`, `vbmeta_vendor`). Generic blank 4KB vbmeta flash ko **strictly block** karna hai taaki "Red State" bootloop na aaye. Genuine stock vbmeta patching support karna hai.
- **Samsung (Exynos & Knox):** Fastboot limitations (Odin vs TWRP fastbootd), Knox bootloader verification, VaultKeeper protections.
- **Google Tensor & Unisoc (Spreadtrum):** GKI (Generic Kernel Image) boot boundaries, USB chunk sizes, Unisoc partition naming conventions.

### 🔹 STAGE 2: PARTITION ARCHITECTURE & MEMORY BOUNDARIES
Har Android version (Android 9 se Android 15+) ke partition schemes ke against stress-test:
- **Legacy Non-A/B vs A/B:** Correct active slot detection (`getvar:current-slot`) aur slot-specific fallback (`system_a` vs `system`).
- **Dynamic Partitions ('super'):** Fastbootd Userspace mode is strictly mandatory for dynamic partitions. Agar space kam ho (`Not enough space`), unneeded stock `product` aur `system_ext` partitions ko auto-free karke space create karna.
- **Virtual A/B Snapshots:** Flashing se pehle pending background OTA snapshots check karna (`snapshot-update-status: merging / snapshotted`) aur safely `snapshot-update:cancel` execute karna.

### 🔹 STAGE 3: BINARY INTEGRITY & USER INPUT SANITIZATION
User dwara select ki gayi kisi bhi file par blindly trust nahi karna:
- **Magic Header Inspection:** First 64 bytes inspect karna (`BOOT_MAGIC`, `AVB0`, Sparse `0xed26ff3a`, Ext4 `0x53ef`, EROFS `0xe2f56a42`).
- **GKI Split Inspection:** Android 13+ devices mein `kernel_size == 0L` check karke `init_boot` aur `boot` ko strictly separate aur lock karna.
- **Archive Compression Guard:** File extensions aur magic bytes (`.xz`, `.zip`, `.gz`, `.7z`, `.rar`) check karke compressed archives ko reject karna aur user ko extraction guidance dena taaki partition raw bytes se corrupt na ho.
- **Original Filename Preservation:** SAF se real `DISPLAY_NAME` lena, generic names se partition confuse hone se bachana.

### 🔹 STAGE 4: ZERO-TOUCH AUTOMATION & RESILIENT USB LIFECYCLE
User experience seamless aur zero-manual intervention hona chahiye:
- **Resilient USB Reconnection:** Jab phone Fastbootd, bootloader, ya recovery mein reboot ho, purana USB session terminate karke background polling (`waitForDevice`) se naye USB endpoint ko auto-capture karna.
- **Automatic Resume:** Fastbootd detect hote hi operation bina user ko dobara tap karwaye automatically execute karna.
- **Clean First Boot Wipe:** FBE (File-Based Encryption) keystore panics se bachne ke liye `erase:userdata`, `format:userdata`, `erase:metadata` execute karna taaki first boot 100% clean ho.

---

## 🛑 THE 2-INPUT INTAKE RULE (ZERO REDUNDANT QUESTIONS)
Jab user nayi video announce kare:
1. **Sirf 2 cheezein check karni hain:**
   - **Thumbnail Image:** Agar user ne image upload nahi ki, toh bas ek baar poocho: *"Bhai thumbnail bhej do"*. Agar user ne de di, toh dobara mat poocho.
   - **Additional Details:** Poocho: *"Koi additional details ya specific highlights hain to bata do (warna enter/skip kardo, baki sab automatic ho jayega)"*.
2. **Details milte hi:**
   - Desktop batch file / existing YouTube OAuth tokens se latest scheduled/uploaded video ka data automatically fetch karo.
   - **KOI BHI BAAR-BAAR PERMISSION YA TOKENS KA SAWAAL NA POOCHO** — directly background me pura pipeline execute karo.

---

## 1. 🔴 YOUTUBE METADATA & SEO RULES
1. **Audio Transcript & Live Flashing Sequence (MANDATORY):**
   - Video ki live transcript automatically fetch/download karo.
   - Rohit bhai ne video me target phone par jo EXACT sequence of actions perform kiye hain (OTG connect, ROM zip select, Auto Flasher tap, vendor_boot skip, reboot, etc.), unko description ke `📖 STEP-BY-STEP FLASHING SEQUENCE` section me numbered list me detail me likho.
2. **Boxed Headings (MANDATORY):**
   - Description ki har heading double box bars ke andar pack honi chahiye:
     ```text
     ━━━━━━━━━━━━━━━━━━━━━━━━━━
     📱 DEVICE & TOOL DETAILS
     ━━━━━━━━━━━━━━━━━━━━━━━━━━
     ```
3. **STRICT LINK RESTRICTIONS (ZERO TOLERANCE):**
   - ❌ **BILKUL ZERO TELEGRAM LINKS:** Description me kahin par bhi koi Telegram link ya mention nahi aayega.
   - ❌ **BILKUL ZERO GITHUB LINKS:** Description me koi bhi GitHub repository ya raw file link nahi aayega.
   - ❌ **BILKUL ZERO FACEBOOK & INSTAGRAM LINKS:** Description me koi bhi Facebook ya Instagram profile/post link nahi aayega.
   - ✅ **Sirf Official Rom Flasher Links:**
     - Tool download: `https://romflasher.in/download.html`
     - Dedicated ROM guide: `https://romflasher.in/rom/<slug>.html`
4. **Title & Tags:**
   - Title high-CTR clickbait + search optimized + 1-2 emojis (e.g. `🔥`, `⚡`, `📲`).
   - 15-20 top ranking fastboot/custom ROM tags.
5. **Thumbnail:**
   - User dwara provide ki gayi custom thumbnail ko video par upload karo.
6. **Mandatory YouTube API Embedding Status Check:**
   - Video publish karte waqt verify karo ki `status.embeddable == True` ho taaki website player par playback block na ho.

---

## 2. 🌐 WEBSITE (romflasher.in) PUBLISHING RULES
1. **Content Generation (`romflasher-site/content/<video_id>.json`):**
   - YouTube video ka detailed technical article generate karo (Requirements, Device compatibility table, Transcript se live steps, FAQ, aur official download buttons).
   - ❌ No Telegram links, No GitHub links, No Facebook/Instagram links.
2. **Responsive Cyber-Glass Comparison Table/Chart Standard (MANDATORY):**
   - ❌ **STRICT BAN ON RAW HTML IN JSON BODY:** JSON ke `body` field me KABHI BHI raw `<div class="tablewrap"><table class="pro-table">...</table></div>` mat daalna! `build.py` ka engine `body` ko `html.escape()` se sanitize karta hai, jisse raw HTML tags `&lt;div class=...` me badal jaate hain aur screen par unrendered ugly code text print hota hai!
   - ✅ **MANDATORY PURE MARKDOWN TABLE SYNTAX:** Hamesha pure Markdown table syntax (`| Feature | Traditional | Tool |` with `:---` aur `:---:`) use karo. `build.py` ka built-in `_render_md_table()` engine automatically isko `<div class="tablewrap"><table class="pro-table">` me compile kar deta hai!
   - **Column Alignment:** First column (Features/Requirements) strictly left-aligned (`:---`), jabki comparison metrics, status aur checkmarks strictly center-aligned (`:---:`).
   - **Visual Icons & High Contrast:** Plain boring text ki jagah visual icons, green checkmarks (`✅`), red cross warnings (`❌`), lightning badges (`⚡`), gold strong tags (`**...**`) lagao taaki dekhte hi clear visual contrast aur cyber-glass look mile.
3. **Interactive FAQ Accordions Standard (MANDATORY):**
   - ❌ **FAQ KABHI BHI `body` TEXT ME NAHI AAYEGA:** FAQ ko markdown list ya headings ki tarah `body` me dump karna strictly prohibited hai.
   - ✅ **TOP-LEVEL `"faq"` ARRAY:** FAQ ko hamesha JSON ke root level par `"faq": [ {"q": "...", "a": "..."}, ... ]` array me 4-5 high-search query pairs ke roop me provide karo. `build.py` automatically isko interactive expandable Obsidian accordion cards (`<details class="faq"><summary>...</summary>`) me compile karta hai.
4. **Code Blocks & Formatting (MANDATORY):**
   - ❌ **NO TRIPLE-BACKTICK BLOCKS (```):** `build.py` markdown engine triple-backtick code fences ko parse nahi karta aur unhe plain paragraph me convert kar deta hai. Commands, error codes aur logs ke liye hamesha single backticks (`code`) ya blockquotes (`> text`) use karo.
5. **Voice & Writing Quality (`WRITER.md` Standard):**
   - **Rohit Verma (@Rom_Flasher) Authentic Voice:** Modder talking to a friend. No AI robotic tone, no generic Wikipedia summaries, no hype words.
   - **Mandatory Sections in Body:**
     - Hook (2–4 lines describing the real reader's pain point).
     - Highlights bullet list (`## ⚡ Key Highlights...`).
     - Cyber-glass Comparison Table (`## 📊 ...`).
     - Requirements list (`## 🛠️ What You Need...`).
     - Step-by-Step Sequence (`## Step 1 — ...`, `## Step 2 — ...`).
     - Failure modes (`## ⚠️ Where People Get Stuck`).
     - Honest detail / reboot behavior (`## 💡 One Honest Thing to Know`).
6. **Universal Obsidian Red & Gold Theme & Typography (MANDATORY DEFAULTS):**
   - **Theme Identity:** Deep rich obsidian black background (`#070709`, `#0d0d12`), Imperial Red accents (`#e50914`, `#ff2a3b`), Warm Metallic Gold (`#d4af37`, `#f3e5ab`), Crisp snow white (`#f8fafc`).
   - **Typography Standard:** `Plus Jakarta Sans` (weights 400, 500, 600, 700, 800) Google Font preconnect ke through har page ke `<head>` me inject rahega. Zero local font mismatch between PC and mobile browsers.
   - **Rohit Verma Author Avatar:** Circular avatar (`border-radius: 50% !important; aspect-ratio: 1/1; object-fit: cover;`) with animated warm gold glowing pulse (`@keyframes goldGlowPulse`) aur E-E-A-T profile schema.
   - **Header Navbar Standard:** Sirf YouTube (`yt-round`), GitHub (`gh-round`), aur Coffee (`coffee-round`) icons honge. Facebook aur Instagram icons completely removed hain.
7. **Zero-Autoplay Click-to-Play Video Facade (MANDATORY AD-SENSE & UX STANDARD):**
   - ❌ **KABHI BHI RAW IFRAME YA AUTOPLAY EMBED MAT DAALO:** Initial page load par koi `<iframe>` render nahi hoga jisse zero initial bandwidth drain, zero layout shift (CLS = 0), aur zero AdSense intrusive video playback violations hon.
   - ✅ **Click-to-Play Facade Engine (`.yt-facade`):** Har guide page par high-res poster image (`https://i.ytimg.com/vi/<id>/hqdefault.jpg`) + animated hover-lift YouTube red play button display hoga. Jab user play button par tap ya click karega, tabhi lightweight `youtube-nocookie.com` iframe dynamically inject hoke video stream hogi.
   - **Standalone YouTube Toolbar:** Video player ke neeche prominent red button `Watch on YouTube (@Rom_Flasher)` hamesha present rahega taaki kisi bhi browser restriction ya ad-blocker par user 1-click me direct channel par video dekh sake.
8. **Static Build & Verification:**
   - Run: `python build.py` inside `romflasher-site\`.
   - Verification checks: `python _seocheck.py` aur `python qa.py --links`.
9. **MANDATORY LIVE DEPLOY (DO NOT FORGET):**
   - Sirf locally build karna kaafi nahi hai.
   - Mandatory Git push execute karo:
     ```bash
     git add .
     git commit -m "Publish guide for <title>"
     git push origin main
     ```
   - Make sure article live deploy ho jaye GitHub Pages / production par.

---

## 3. 🎯 FINAL DELIVERY REPORT
Har nayi video ke baad user ko saare live links structured format me provide karo:
- 🔴 **YouTube Video Link:** `https://youtu.be/<id>`
- 🌐 **Website Article Link:** `https://romflasher.in/rom/<slug>.html`

---

## 4. 📦 REPO HOME SCREEN (`README.md`) & RELEASE SYNC RULE (MANDATORY)
1. **Real-Time Feature Showcase on Landing Page:**
   - Jab bhi app build me koi naya feature add ho ya nayi release banayi jaye (e.g. 1-Click Auto Flasher, Play Integrity fix, Multi-slot bypass), **repo ki home screen (`README.md`) ko sath ke sath update karna mandatory hai**.
   - Top comparison table, `Features Breakdown` section, aur badges me naye feature ko prominently spotlight karo taaki repository visit karne wale kisi bhi user ko home screen se hi pata chal jaye ki tool me kya kya latest material aur capabilities hain.
2. **Real-Time Simultaneous GitHub Push:**
   - Har modification ke baad `rom-flasher-tool`, `romflasher-site` aur `romflasher-master-private` (Private Master Vault) teeno repos par real-time sath ke sath commit aur push karna mandatory hai.

---

## 5. 🛡️ BACKGROUND SECURITY GUARD & AUTO RESTORE PROTOCOL (MANDATORY)
1. **Daily Silent Credential Guard (11:30 AM):**
   - Windows Task Scheduler me `RomFlasher Secret Guard` task hamesha registered rahega.
   - **Mode:** Strictly Silent Background mode using `pythonw.exe`.
   - ❌ **ZERO CMD POPUPS:** Kabhi bhi `python.exe` (console mode) use nahi hoga taaki Rohit bhai ki screen par koi black CMD window pop-up na ho.
   - **Purpose:** Automatically scans `Downloads`, `Desktop`, aur `Documents` for exposed API keys, private tokens, or secrets before they can leak in video recordings.
2. **Nayi Windows / PC Migration Auto-Restore:**
   - Agar Rohit bhai Windows reinstall ya upgrade karte hain, toh Master Backup folder me shamil `RESTORE_ALL.ps1` ya `credentials_and_tools/install_guard_task_silent.ps1` se ye automated silent guard automatically dobara install aur configure ho jayega.
   - Agent ko prompt milte hi (`maine master backup paste kar diya hai`), agent automatically task scheduler me silent guard restore kar dega bina user ke kahe.

---

## 6. 🔄 "WINDOWS CHANGE KARI HAI" / "NEW WINDOWS DAL LI" — ZERO-CLICK FULL AUTO RESTORE (MANDATORY)
Jab Rohit bhai bole *"bhai maine new windows dal li"*, *"windows change kari hai"*, *"pc format kiya hai"*, ya *"backup se sab restore kardo"*:
- **KOI BHI SAWAAL NA POOCHO.**
- Background me ye 4 steps immediately execute karo:
  1. **Locate Backup Vault:** Master Backup folder (`romflasher-master-backup` / `ROM_FLASHER_MASTER_BACKUP`) locate karo.
  2. **Run Restore Script:** `RESTORE_ALL.ps1` execute karo jo:
     - `.romflasher` config, `yt_credentials.json`, `guard_daily.py`, `secret_guard.py` ko `$HOME\.romflasher\` me inject karega.
     - Git `.gitconfig` aur credentials restore karega.
     - Task Scheduler me `RomFlasher Secret Guard` ko **strictly invisible (`pythonw.exe`) mode me 11:30 AM** daily trigger ke sath register karega.
  3. **Verify All 3 Repositories:**
     - `rom-flasher-tool` (`Documents\ROM_Flasher_Tool`)
     - `romflasher-site` (`romflasher-site`)
     - `romflasher-master-private` (`romflasher-master-backup`)
     Ensure branches origin/main par sync hain.
  4. **Final Clean Delivery Report:** Rohit bhai ko single reassuring message me deliver karo:
     *"Bhai nayi Windows par aapka poora setup (App Keystore, Website, YouTube API, aur Daily 11:30 AM Silent Security Guard) 100% restore aur active ho chuka hai! Kuch bhi dobara setup karne ki zaroorat nahi hai."*
