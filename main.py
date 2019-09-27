import sys

sys.path.insert(0, './src')
sys.path.insert(0, './algorithms')

import DSPEngine
import Algorithm

f = open('./test/data.txt', "r")
data = []

if f.mode == "r":
    file = f.readlines()

    for line in file:
        data.append(int(line))

DSP = DSPEngine.DSPEngine()
RMS = Algorithm.Algorithm("RMS")
Kurtosis = Algorithm.Algorithm("Kurtosis")

DSP.add(RMS)
DSP.add(Kurtosis)

DSP.run(data)
