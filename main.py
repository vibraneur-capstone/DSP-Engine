import DSPEngine
import Algorithm

DSP = DSPEngine.DSPEngine()
RMS = Algorithm.Algorithm("RMS")

DSP.add(RMS)

DSP.run()

DSP.remove(RMS)

DSP.run()

DSP.add(RMS)

while(1):
    DSP.run()
