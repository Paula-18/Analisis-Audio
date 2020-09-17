import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave

import thinkplot

waveTelefono = read_wave("telefono.wav")
waveTelefono.plot()
decorate(xlabel="Tiempo (s)")
thinkplot.show()

#espectro = waveTelefono.make_spectrum()
#espectro.plot()
#decorate(xlabel="Frecuencia (Hz)")
#thinkplot.show()

wavePrimerDigito = waveTelefono.segment(start=0,duration=0.5)
#waveTelefono.plot()
#decorate(xlabel="Tiempo (s)")
#thinkplot.show()

#Telefono: 2-2-4-5-3-2

espectroPrimerDigito = wavePrimerDigito.make_spectrum()
espectroPrimerDigito.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()

waveSegundoDigito = waveTelefono.segment(start=0.5, duration=0.5)
espectroSegundorDigito = waveSegundoDigito.make_spectrum()
espectroSegundorDigito.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()

waveTercerDigito = waveTelefono.segment(start=1, duration=0.5)
espectroTercerDigito = waveTercerDigito.make_spectrum()
espectroTercerDigito.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()

waveCuartoDigito = waveTelefono.segment(start=1.5, duration=0.5)
espectroCuartoDigito = waveCuartoDigito.make_spectrum()
espectroCuartoDigito.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()

waveQuintoDigito = waveTelefono.segment(start=2, duration=0.5)
espectroQuintoDigito = waveQuintoDigito.make_spectrum()
espectroQuintoDigito.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()

waveSextoDigito = waveTelefono.segment(start=2.5, duration=0.5)
espectroSextoDigito = waveSextoDigito.make_spectrum()
espectroSextoDigito.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()