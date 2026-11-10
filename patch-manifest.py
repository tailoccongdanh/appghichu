import re

path = "android/app/src/main/AndroidManifest.xml"
s = open(path, encoding="utf-8").read()

if 'android:scheme="com.binmosa.ghichu"' in s:
    print("Intent-filter da co, bo qua")
else:
    block = """
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="com.binmosa.ghichu" android:host="oauth" />
            </intent-filter>
"""
    idx = s.find("</activity>")
    if idx == -1:
        raise SystemExit("Khong tim thay </activity> trong AndroidManifest.xml")
    s = s[:idx] + block + "        " + s[idx:]
    open(path, "w", encoding="utf-8").write(s)
    print("Da them intent-filter OAuth")
