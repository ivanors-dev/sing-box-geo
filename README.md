# Clash Rules Auto Builder (geosite + geoip)

Repo ini otomatis:
1. Ambil `geosite.db` & `geoip.db` dari [malikshi/sing-box-geo](https://github.com/malikshi/sing-box-geo)
2. Convert ke JSON (via sing-box)
3. Convert ke YAML (untuk Clash rule-providers)
4. Publish hasil ke branch `gh-pages`

## Cara pakai di Clash
```yaml
rule-providers:
  geosite:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/USERNAME/clash-rules/gh-pages/geosite.yaml
    path: ./ruleset/geosite.yaml
    interval: 86400

  geoip:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/USERNAME/clash-rules/gh-pages/geoip.yaml
    path: ./ruleset/geoip.yaml
    interval: 86400
```
⚡ Ganti `USERNAME` dengan username GitHub kamu.
