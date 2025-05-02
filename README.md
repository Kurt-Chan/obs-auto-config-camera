# 📄 OBS Auto Configuration Tool

This tool helps automatically apply the correct camera settings when you launch OBS. It’s useful if your webcam settings reset after a restart or when OBS crashes. 

This utilizes the WebCameraConfig.exe from [SuslikV](https://github.com/SuslikV).
Download the WebCameraConfig on the [release page](https://github.com/SuslikV/cfg-cam/releases)

---

## 📁 Files Included

- ✅ **`run.py`** — Double-click this to automatically:
  - Launch OBS
  - Apply saved webcam settings  
- ✅ **`Apply Configuration.bat`** — Use this **if the camera settings don’t apply** after OBS opens.
- ✅ **`Save Configuration.bat`** — Use this to **save new webcam settings** after you adjust them in OBS.
- ✅ **`WebCameraConfig.exe`** — The tool that applies or saves your webcam settings (do not delete this).
- ✅ **`vcredist_x86 & vcredist_x64`** — This might be needed if **Microsoft Redist 2013 ++** is not yet installed in the PC. Download it vcredist_x86 [here](https://aka.ms/highdpimfc2013x86enu) and vcredist_x64 [here](https://aka.ms/highdpimfc2013x64enu)
---
### REMINDER: Make sure vcredist_x86 & vcredist_x64 are installed in the PC before using.

## 🚀 How to Use

### 1. ✅ To Open OBS with Correct Settings
- Double-click `run.py`  
- Wait a few seconds — OBS will open and your webcam settings should apply automatically.

### 2. 🛠️ If Settings Don’t Apply
- After OBS is open, **double-click `Apply Configuration.bat`**  
- Your saved webcam settings will be applied instantly.

### 3. 💾 To Save New Camera Settings
> Use this **only if you change webcam settings** inside OBS.

- Open OBS and adjust your camera settings (e.g. resolution, FPS).
- When done, **double-click `Save Configuration.bat`**  
- It will save the current settings for future use (filename: cam_sett.cfg).

---

## 📌 Reminders

- Keep **all files in the same folder** — don’t move them separately.
- vcredist_x86 & vcredist_x64 is installed.
- The tool is tested on Windows 11 and assumes OBS is installed at:
  ```
  C:\Program Files\obs-studio\bin\64bit\obs64.exe
  ```
- Make sure the OBS path is the same.
- If anything breaks, restart the PC and try again.
