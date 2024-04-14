from totk_audio_classes import Bwav
import sys

# pyinstaller --onefile --add-binary "C:\Python312\Lib\site-packages\pyogg\libs\win_amd64\opus.dll;." --add-binary "C:\Python312\Lib\site-packages\pyogg\libs\win_amd64\ogg.dll;." bwav2opus.py

if len(sys.argv) > 1:
    path = sys.argv[1]
    bwav = Bwav(path)
    
    bwav.convert_to_opus()
    bwav.write(path)
else:
    print("Provide a path to a BWAV file!")