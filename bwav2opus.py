from totk_audio_classes import Bwav
import sys

if len(sys.argv) > 1:
    path = sys.argv[1]
    bwav = Bwav(path)
    
    bwav.convert_to_opus()
    bwav.write(path)
else:
    print("Provide a path to a BWAV file!")