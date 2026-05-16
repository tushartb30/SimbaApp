
[app]
title = Simba Assistant
package.name = simba_assistant
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy==2.3.0, requests, urllib3, charset-normalizer, idna, certifi

orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
