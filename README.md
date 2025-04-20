# Fancy File Mover

## 🎯 Goal

Move main files and their matching sidecars together, but:

* ❌ Don’t overwrite existing files
* 🔄 Keep the relationship intact (e.g., movie.mp4 with movie.srt)
* ✨ Optionally skip or rename on conflict

## 🧠 Logic Outline

For each file in the source:

* 💡 Identify if it’s a "main" file (e.g., .mp4, .exe, .jpg)
* 🔍 Look for any files with the same name prefix (file.*) that are companions (e.g., .srt, .xmp, .sfv)
* ✅ Check if the destination already has those files
  - If yes: skip or rename (e.g., add -copy or timestamp)
  - If no: move them
* ⚙️ Repeat for all files

## ⚠️ If only the main file exists:

* 🛠️ Option A: Skip just the main file
You’d still move the sidecar files (e.g., .srt, .xmp).

  Risk: You end up with a .srt file in the destination without its corresponding video — possibly messy.

* 🛠️ Option B: Skip the whole group (main + all matching sidecars)
Safer and cleaner

  If the main file exists in the destination, you skip the entire set, including .srt, .xmp, .sfv, etc.

## ✅ Recommended Approach:

Skip the whole set if any main file already exists at the destination.

## 🌟 Example Behavior:
Say you have this in source/:
```css
video.mp4
video.srt
video.xmp
```
And video.mp4 already exists in destination/.

Then with the smart "group skip" logic, nothing from that set gets moved.

That way, everything stays in sync — no orphan sidecar files lying around.

## 📃 License

This repository is licensed under [GNU General Public License v3.0](https://github.com/almarshenwan/fancy-file-mover/blob/main/LICENSE). If you don’t want to read the whole license, here’s a summary without legal force:
* ⚖️ You are allowed to download, use, copy, publish and distribute.
* ✍️ You are allowed to create modified versions but you may only distribute them on same license.
* 🛡️ Repository comes with absolutely no warranty.
