# TOTK_BWAV2Opus
A tool to re-encode existing TOTK BWAV files with an Opus encoder.

## Requirements
- PyOGG >= 0.7 - `pip install git+https://github.com/TeamPyOgg/PyOgg`

## Usage
- Run in a terminal providing a path to your BWAV, e.g. `python bwav2opus.py path_to_bwav.bwav`.
- Alternative way, drag-and-drop your BWAV onto the bwav2opus.py script, cosidering you've associated Python with the .py file format in your OS.

Beware, the script will **overwrite** the provied BWAV file, consider making a copy.

## Notes
When modding any BWAVs, remember about patching your BARS files: https://github.com/MediaMoots/TOTK_BARS_Tool

More information on sound modding and more can be found on Zelda TOTK Modding Hub discord server: https://discord.gg/nEFVf8A
