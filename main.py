import DSPEngine
import Algorithm

DSP = DSPEngine.DSPEngine()
RMS = Algorithm.Algorithm("RMS")

DSP.add(RMS)

while(1):
    DSP.run()
