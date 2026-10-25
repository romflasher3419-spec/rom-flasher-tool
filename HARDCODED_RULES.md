# ⚡ ROM FLASHER AUTOMATED CONTENT DISTRIBUTION — HARDCODED BINDING RULES

> **SYSTEM INSTRUCTION FOR AGENT (ANTIGRAVITY / GEMINI):**
> Ye rules user (Rohit bhai / @Rom_Flasher) ke dwara strictly mandate kiye gaye hain. Jab bhi user bole **"new video upload krdi"**, **"nayi video aa gayi hai"**, **"video schedule kar di hai"** ya similar trigger, agent ko ye complete 4-in-1 automated workflow **ZERO-TO-HERO** execute karna hai bina baar-baar sawaal pooche ya rules bhule.

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
   - ✅ **Sirf Official Rom Flasher Links:**
     - Tool download: `https://romflasher.in/download.html`
     - Dedicated ROM guide: `https://romflasher.in/rom/<slug>.html`
     - Instagram: `https://instagram.com/romflasheryt`
4. **Title & Tags:**
   - Title high-CTR clickbait + search optimized + 1-2 emojis (e.g. `🔥`, `⚡`, `📲`).
   - 15-20 top ranking fastboot/custom ROM tags.
5. **Thumbnail:**
   - User dwara provide ki gayi custom thumbnail ko video par upload karo.

---

## 2. 🌐 WEBSITE (romflasher.in) PUBLISHING RULES
1. **Content Generation (`romflasher-site/content/<video_id>.json`):**
   - YouTube video ka detailed technical article generate karo (Requirements, Device compatibility table, Transcript se live steps, FAQ, aur official download buttons).
   - ❌ No Telegram links.
2. **Responsive Cyber-Glass Comparison Table/Chart Standard (MANDATORY):**
   - Har article me jab bhi comparison ya technical breakdown table aaye, usko strictly `pro-table` standards par format karo:
     - **Column Alignment:** First column (Features/Requirements) strictly left-aligned (`:---`), jabki comparison metrics, status aur checkmarks strictly center-aligned (`:---:`).
     - **Visual Icons & High Contrast:** Plain boring text ki jagah visual icons, green checkmarks (`✅`), red cross warnings (`❌`), lightning badges (`⚡`) lagao taaki dekhte hi clear visual contrast mile.
     - **Native HTML Wrapping:** Engine me table hamesha `<div class="tablewrap"><table class="pro-table">` me compile ho jisse mobile screens par responsive touch-scroll smoothly kaam kare bina text bikhre.
3. **Static Build:**
   - Run: `python build.py` inside `C:\Users\vrohi\romflasher-site\`.
4. **MANDATORY LIVE DEPLOY (DO NOT FORGET):**
   - Sirf locally build karna kaafi nahi hai.
   - Mandatory Git push execute karo:
     ```bash
     git add .
     git commit -m "Publish guide for <title>"
     git push origin main
     ```
   - Make sure article live deploy ho jaye GitHub Pages / production par.

---

## 3. 📘 FACEBOOK PAGE (`Rom Flasher` — ID: `1449977448193123`)
1. **Original 1080p Video Download:**
   - YouTube se full original 1080p video download karke save karo: `C:\Users\vrohi\Documents\Social_Media_Assets\rom_flasher_video.mp4`.
2. **Resumable Upload Protocol (MANDATORY):**
   - Non-resumable upload se 413 Payload Too Large error aata hai.
   - Hamesha Resumable Upload API use karo:
     - `upload_phase=start` (file_size specify karo)
     - `upload_phase=transfer` (1MB - 2MB chunks me upload karo)
     - `upload_phase=finish` (Title, Boxed description, aur `thumb` attach karo)
3. **Credentials:**
   - Use `facebook_page_token` stored in `C:\Users\vrohi\Documents\Instagram_Automation\config.json`.
4. **Description & Viral Tags (MANDATORY):**
   - Same boxed description + exact transcript sequence + zero Telegram + zero GitHub.
   - 🏷️ **25-30 High-Volume Viral Hashtags Bundle:** Description ke end me compulsory boxed `🏷️ VIRAL TAGS & KEYWORDS` section hoga:
     - Niche tags: `#RomFlasher #PlayIntegrity #StrongIntegrity #PlayStoreCertified #Magisk #DeviceCertified #BankingApps #RootHide #NoPC #KernelSU #APatch #AndroidMod #CustomROM #FlashWithoutPC`
     - Broad viral tags: `#AndroidTricks #TechViral #TrendingTech #Technology #AndroidHacks #TechReels #AndroidTips #PlayProtect #PhoneRoot #Zygisk #GPayFix #PhonePeFix #ExploreTech #Gadgets`
     - Ye tags Facebook Video algorithm aur search feed (Facebook Watch) me video ko boost karte hain.

---

## 4. 📸 INSTAGRAM REELS (`@romflasheryt`)
1. **Video Slicing (9:16 Vertical):**
   - Video ko `ffmpeg` se 60-75 second ke vertical slices me cut karo:
     ```bash
     ffmpeg -y -i rom_flasher_video.mp4 -ss <start> -t <duration> -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1" -c:v libx264 -pix_fmt yuv420p -preset fast -crf 22 -c:a aac -ar 44100 -b:a 128k -movflags +faststart <output_file>
     ```
2. **Custom Eye-Catching Reel Covers with Sequential Badges (MANDATORY):**
   - ❌ Kabhi bhi Instagram ko default random frame cover mat choose karne do.
   - 🖼️ **Base Canvas:** Agar user ne dedicated 9:16 vertical poster/thumbnail provide kiya hai, toh usko base canvas use karo. Warna 16:9 thumbnail ko 1080x1920 blurred-backdrop ke sath format karo.
   - 🏷️ **Prominent Sequential Part Badges (MANDATORY):**
     - Har part cover par top ribbon me ultra-bold, high-contrast, neon glowing badge stamp karo: **`PART 1`**, **`PART 2`**, **`PART 3`**, **`PART 4`** in sequential order!
     - Subtitle pill: Part-specific topic (e.g. `STEP 1: FAILED CHECKS`, `STEP 2: 1-CLICK INJECTION`, `STEP 3: ALL 3 PASSED`, `STEP 4: PLAY CERTIFIED & BANKING APPS`).
     - Bottom bar branding: `@Rom_Flasher • romflasher.in • NO PC`.
3. **Rich, Aesthetic, Multi-Section Long Captions (MANDATORY — ZERO 1-LINERS):**
   - ❌ **KABHI BHI CHOTA YA 1-LINE KA CAPTION NA DAALO.**
   - Har reel me top tech creator jaisa aesthetic, structured description hona chahiye:
     - 🚀 **Catchy Hook:** Problem / hook with emojis (Device not certified, banking apps crashing, etc.)
     - 📱 **Part & Series Info:** `(PART X/4: Detailed Step Name)`
     - ━━━━━━━━━━━━━━━━━━━━━━━━━━ Boxed sections
     - 🚨 **The Problem / Solution Breakdown:** Detailed explanation.
     - ⚡ **Rom Flasher Tool Highlights:** Key USPs (No PC, Zero Termux, 1-Click OTG, Universal).
     - 👉 **Next Part Teaser:** What to expect in the next part.
     - 📥 **Call to Action (CTA):** Download link in bio (`@romflasheryt`), website `romflasher.in`.
     - 💾 **Engagement Prompts:** *"SAVE THIS REEL for later! 📲 Share with Android root lovers!"*
     - 🏷️ **20-25 Targeted Viral Hashtags:** `#romflasher #playintegrity #magisk #customrom #rootandroid #techreels #explorepage ...`
4. **Publishing with Cover URL:**
   - Cloudflare Quick Tunnel / CDN se host karo.
   - Meta Container creation `POST /me/media` me `video_url` ke saath `cover_url` mandatory pass karo:
     ```python
     media_data = {
         "media_type": "REELS",
         "video_url": video_url,
         "cover_url": cover_url,
         "caption": caption,
         "access_token": token
     }
     ```
   - Har slice ko sequentially publish karke live permalink verify karo.

---

## 5. 🎯 FINAL DELIVERY
Har run ke baad user ko saare live links structured format me provide karo:
- 🔴 **YouTube Video Link:** `https://youtu.be/<id>`
- 🌐 **Website Article Link:** `https://romflasher.in/rom/<slug>.html`
- 📘 **Facebook Page Video Link:** `https://www.facebook.com/1449977448193123/videos/<video_id>/`
- 📸 **Instagram Reels Links:**
  - Part 1: `https://www.instagram.com/reel/<id>/`
  - Part 2: `https://www.instagram.com/reel/<id>/`
  - Part 3: `https://www.instagram.com/reel/<id>/`
  - Part 4: `https://www.instagram.com/reel/<id>/`

---

## 6. 📦 REPO HOME SCREEN (`README.md`) & RELEASE SYNC RULE (MANDATORY)
1. **Real-Time Feature Showcase on Landing Page:**
   - Jab bhi app build me koi naya feature add ho ya nayi release banayi jaye (e.g. 1-Click Auto Flasher, Play Integrity fix, Multi-slot bypass), **repo ki home screen (`README.md`) ko sath ke sath update karna mandatory hai**.
   - Top comparison table, `Features Breakdown` section, aur badges me naye feature ko prominently spotlight karo taaki repository visit karne wale kisi bhi user ko home screen se hi pata chal jaye ki tool me kya kya latest material aur capabilities hain.
2. **Real-Time Simultaneous GitHub Push:**
   - Har modification ke baad `rom-flasher-tool`, `romflasher-site` aur `romflasher-master-private` (Private Master Vault) teeno repos par real-time sath ke sath commit aur push karna mandatory hai.

---

## 7. 🛡️ BACKGROUND SECURITY GUARD & AUTO RESTORE PROTOCOL (MANDATORY)
1. **Daily Silent Credential Guard (11:30 AM):**
   - Windows Task Scheduler me `RomFlasher Secret Guard` task hamesha registered rahega.
   - **Mode:** Strictly Silent Background mode using `pythonw.exe` (`C:\Python315\pythonw.exe C:\Users\vrohi\.romflasher\guard_daily.py`).
   - ❌ **ZERO CMD POPUPS:** Kabhi bhi `python.exe` (console mode) use nahi hoga taaki Rohit bhai ki screen par koi black CMD window pop-up na ho.
   - **Purpose:** Automatically scans `Downloads`, `Desktop`, aur `Documents` for exposed API keys, private tokens, or secrets before they can leak in video recordings.
2. **Nayi Windows / PC Migration Auto-Restore:**
   - Agar Rohit bhai Windows reinstall ya upgrade karte hain, toh Master Backup folder me shamil `RESTORE_ALL.ps1` ya `credentials_and_tools/install_guard_task_silent.ps1` se ye automated silent guard automatically dobara install aur configure ho jayega.
   - Agent ko prompt milte hi (`maine master backup paste kar diya hai`), agent automatically task scheduler me silent guard restore kar dega bina user ke kahe.


