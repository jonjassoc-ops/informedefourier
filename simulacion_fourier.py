"""Señales elementales y propiedades de la Transformada de Fourier.
Requisitos: Python 3.10+, NumPy y Matplotlib. Ejecuta python simulacion_fourier.py.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
OUT = Path(__file__).resolve().parent / "figuras"
OUT.mkdir(exist_ok=True)
fs, T = 1000.0, 1.0
N = int(fs*T); dt = 1/fs
t = (np.arange(N)-N/2)*dt
pulso = ((t >= -.10) & (t < .10)).astype(float)
pulso_comprimido = ((2*t >= -.10) & (2*t < .10)).astype(float)
escalon = (t >= 0).astype(float)
seno = np.sin(2*np.pi*5*t)

def espectro(x):
    X = dt*np.fft.fftshift(np.fft.fft(np.fft.ifftshift(x)))
    f = np.fft.fftshift(np.fft.fftfreq(len(x), d=dt))
    mag = np.abs(X); fase = np.angle(X)
    fase[mag < mag.max()*1e-3] = np.nan
    return f, mag, fase

def guardar(nombre, x, titulo):
    f, mag, fase = espectro(x)
    fig, ax = plt.subplots(3, 1, figsize=(10, 8), constrained_layout=True)
    ax[0].plot(t,x,color="#147D92",lw=1.8); ax[0].set(title=f"{titulo}: dominio del tiempo",xlabel="Tiempo (s)",ylabel="Amplitud"); ax[0].grid(alpha=.25)
    ax[1].plot(f,mag,color="#D47732",lw=1.5); ax[1].set(title="Magnitud de la CTFT aproximada",xlabel="Frecuencia (Hz)",ylabel="|X(f)|"); ax[1].set_xlim(-20,20); ax[1].grid(alpha=.25)
    ax[2].plot(f,fase,color="#5B6C9E",lw=1.3); ax[2].set(title="Fase (rad), donde la magnitud es significativa",xlabel="Frecuencia (Hz)",ylabel="∠X(f)"); ax[2].set_xlim(-20,20); ax[2].set_ylim(-np.pi,np.pi); ax[2].grid(alpha=.25)
    fig.savefig(OUT/f"{nombre}.png",dpi=170); plt.close(fig)
for nombre,x,titulo in [("pulso_rectangular",pulso,"Pulso rectangular de 0.20 s"),("escalon_unitario",escalon,"Escalón unitario observado durante 1 s"),("senoidal_5_hz",seno,"Seno de 5 Hz")]: guardar(nombre,x,titulo)
# Verificación de linealidad y desplazamiento circular en la DFT.
x,z=pulso,np.roll(seno,70); a,b=1.7,-.4
err_lin=np.max(np.abs(np.fft.fft(a*x+b*z)-(a*np.fft.fft(x)+b*np.fft.fft(z))))
d=80; X=np.fft.fft(pulso); k=np.arange(N)
err_shift=np.max(np.abs(np.fft.fft(np.roll(pulso,d))-X*np.exp(-2j*np.pi*k*d/N)))
# Verificación de escala: al comprimir a la mitad, el pulso mide 0.10 s y su CTFT es 0.10*sinc(0.10*f).
f, mag_comp, _ = espectro(pulso_comprimido)
referencia = .10*np.abs(np.sinc(.10*f))
mask = np.abs(f) <= 200
err_scale=np.max(np.abs(mag_comp[mask]-referencia[mask]))
print(f"Muestras: {N}; fs={fs:.0f} Hz; resolución={fs/N:.1f} Hz")
print(f"Error máximo de linealidad (DFT): {err_lin:.3e}")
print(f"Error máximo de desplazamiento circular (DFT): {err_shift:.3e}")
print(f"Error máximo de escalamiento vs CTFT analítica (|f|<=200 Hz): {err_scale:.3e}")
print(f"Duración del pulso: {pulso.sum()*dt:.3f} s; comprimido: {pulso_comprimido.sum()*dt:.3f} s")
print(f"Gráficas guardadas en: {OUT}")

