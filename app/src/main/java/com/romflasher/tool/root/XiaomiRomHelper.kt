package com.romflasher.tool.root

import java.io.File
import java.net.HttpURLConnection
import java.net.URL
import javax.xml.parsers.DocumentBuilderFactory
import org.w3c.dom.Element

/**
 * Resolves official Xiaomi, Redmi, and POCO stock firmware from global tracking servers
 * (XiaomiFirmwareUpdater / miui-updates-tracker official RSS & GitHub database).
 */
object XiaomiRomHelper {

    data class XiaomiRomInfo(
        val codename: String,
        val version: String,
        val region: String,
        val fastbootUrl: String?,
        val recoveryUrl: String?
    )

    fun isXiaomiDevice(brand: String?, manufacturer: String?, codename: String?): Boolean {
        val b = (brand ?: "").lowercase()
        val m = (manufacturer ?: "").lowercase()
        val c = (codename ?: "").lowercase()
        return b.contains("xiaomi") || b.contains("redmi") || b.contains("poco") ||
               m.contains("xiaomi") || m.contains("redmi") || m.contains("poco") ||
               c == "rodin" || c.startsWith("redmi") || c.startsWith("poco")
    }

    /**
     * Queries online Xiaomi OTA tracker for the target codename and matches version & region.
     */
    fun findMatchingRom(
        codename: String,
        buildVersion: String,
        region: String,
        onLog: (String) -> Unit = {}
    ): XiaomiRomInfo? {
        val cleanCode = codename.lowercase().trim()
        val rssUrl = "https://raw.githubusercontent.com/XiaomiFirmwareUpdater/miui-updates-tracker/master/rss/$cleanCode.xml"

        return try {
            onLog("→ Querying official Xiaomi cloud server for '$cleanCode' (v$buildVersion · $region)…")
            val conn = URL(rssUrl).openConnection() as HttpURLConnection
            conn.connectTimeout = 8000
            conn.readTimeout = 8000
            conn.setRequestProperty("User-Agent", "ROM-Flasher-Patcher/2.0")
            if (conn.responseCode != 200) {
                onLog("[i] Codename '$cleanCode' cloud repository not indexed (HTTP ${conn.responseCode}).")
                return null
            }

            val factory = DocumentBuilderFactory.newInstance()
            val builder = factory.newDocumentBuilder()
            val doc = builder.parse(conn.inputStream)
            val items = doc.getElementsByTagName("item")

            var bestFastboot: String? = null
            var bestRecovery: String? = null
            var matchedVer = buildVersion

            for (i in 0 until items.length) {
                val item = items.item(i) as? Element ?: continue
                val title = item.getElementsByTagName("title").item(0)?.textContent ?: ""
                val link = item.getElementsByTagName("link").item(0)?.textContent ?: ""

                val isFastboot = title.contains("Fastboot", ignoreCase = true) || link.endsWith(".tgz")
                val isRecovery = title.contains("Recovery", ignoreCase = true) || link.endsWith(".zip")

                // Check version match
                val isVerMatch = buildVersion.isNotBlank() && (title.contains(buildVersion, ignoreCase = true) || link.contains(buildVersion, ignoreCase = true))
                val isRegionMatch = region.isNotBlank() && (title.contains(region, ignoreCase = true) || link.contains("_${region.lowercase()}_"))

                if (isVerMatch || (isRegionMatch && bestRecovery == null && bestFastboot == null)) {
                    if (isFastboot && bestFastboot == null) bestFastboot = link
                    if (isRecovery && bestRecovery == null) bestRecovery = link
                    matchedVer = extractVersion(title) ?: buildVersion
                }
            }

            if (bestFastboot != null || bestRecovery != null) {
                val info = XiaomiRomInfo(cleanCode, matchedVer, region, bestFastboot, bestRecovery)
                onLog("[+] Matched Official Xiaomi Firmware: $matchedVer ($region)")
                bestFastboot?.let { onLog("  [Fastboot TGZ]: $it") }
                bestRecovery?.let { onLog("  [Recovery ZIP]: $it") }
                info
            } else {
                onLog("[i] No exact cloud ROM package match found for $cleanCode $buildVersion.")
                null
            }
        } catch (e: Exception) {
            onLog("[i] Xiaomi cloud lookup note: ${e.message}")
            null
        }
    }

    private fun extractVersion(text: String): String? {
        val regex = Regex("""(OS\d+\.[\d\.]+\.[A-Z0-9]+|V\d+\.[\d\.]+\.[A-Z0-9]+)""")
        return regex.find(text)?.value
    }
}
