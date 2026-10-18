# Privacy Policy — Rom Flasher Tool

**Last updated: 18 October 2026**

Rom Flasher Tool ("the App") is a free Android utility that helps you find the right
firmware / ROM download and the correct flashing procedure for your device.

This page explains what the App does with your information.

---

## Short version

> **The App collects nothing.** There is no account, no sign-up, no analytics and no
> advertising SDK. Nothing about you leaves your phone.

---

## What the App does NOT collect

- Personal details (name, email address, phone number, postal address)
- Location data of any kind
- Contacts, photos, videos, or other files on your device
- Advertising identifiers or device fingerprints
- Usage tracking, telemetry, or crash reports sent to us
- Nothing is sold, rented, or shared — because nothing is collected

## What stays on your device

The App stores a small amount of data **locally, on your phone only**:

- Your app settings (theme, language preference)
- Cached firmware / device information so the App opens faster

This data never leaves your device, and uninstalling the App removes it.

## Permissions and why they are needed

| Permission | Why the App asks for it |
|---|---|
| **Internet** | To fetch device details, firmware information and download links |
| **Storage / files** | To read the firmware or recovery image you choose, and to save downloads |
| **USB (ADB / fastboot)** | To send the flashing commands to your device over the USB cable |

The App only uses these permissions for the feature you have just started.

## Third-party services

The App opens links to third-party websites — for example GitHub, manufacturer
firmware portals, and ROM mirrors such as `roms.danielspringer.at`. Those websites
have their own privacy policies and are not controlled by us. Please read their
policies before using them.

## YouTube channel management (developer tooling, not the App)

The maintainer of this project uses Google's **YouTube Data API** to:

- keep the public README page of this repository updated (subscriber count and a few
  featured videos), and
- manage the project's **own** YouTube channel metadata.

Details of that access:

- The **only** Google Account accessed is this project's own channel account.
- Access is limited to the `youtube.force-ssl` scope (channel read / write).
- The OAuth refresh token is stored as an **encrypted secret** in the project's private
  GitHub Actions configuration. It is never published in the repository, never shared,
  and never sold.
- **No third-party Google user data is ever read, stored, or processed.**

## Children's privacy

The App is not directed at children and collects no data from anyone.

## Data retention and deletion

Because the App collects no data, there is nothing for us to retain or delete.
To remove the locally stored settings and cache, simply uninstall the App.

## Changes to this policy

If this policy changes, the "Last updated" date above will change and the new version
will be published in this repository.

## Contact

Questions about this policy? Open an issue:

<https://github.com/romflasher3419-spec/rom-flasher-tool/issues>
