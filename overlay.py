import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

# Define the XPM colormap mapping
color_map = {
    "A": 0.00, "B": 0.533, "C": 1.07, "D": 1.6, "E": 2.13, "F": 2.66, "G": 3.2, "H": 3.73, "I": 4.26, "J": 4.79, 
    "K": 5.33, "L": 5.86, "M": 6.39, "N": 6.92, "O": 7.46, "P": 7.99, "Q": 8.52, "R": 9.06, "S": 9.59, "T": 10.1, 
    "U": 10.7, "V": 11.2, "W": 11.7, "X": 12.3, "Y": 12.8
}

# Define the XPM data
data = [
"YYYYYYYYYYYYYYWYYYWYYYYYYYYYYYYY",
"YYYYYYYYYYYYYYWWYTYYYYYYYYYYYYYY",
"YYYYYYYYYYYYYYWWTWYWYYYYYYYYYYYY",
"YYYYYYYYYYYYWWWRYWTWYYYYYYWYYYYY",
"YYYYYYYYYYYYTTTQRRTQWYYYYYWYYYYY",
"YYYYYYYYYYWWTNNNLJLWRRRWYWYYYTYY",
"YYYYYYYYYRWRQMJJKKMQMTTYYYWRRYYY",
"YYYYYYWYWYWPKIJKJIKQLORTRTQRTYYW",
"YYYYYTWYTLLJKHHJIJIKOWLOMMMOPPYT",
"YYYYYWYTOMLLHHFIHLILLNLKLJLPQWRY",
"YYYYYTTMKJIIFGIIGIHMLLMIIILJNQWW",
"YYYYWQQKIKIFFIHFIILMPLJIGGGILQQY",
"YYWWRMLHHGHHGFIIIKKMQLJGGFFIJPYY",
"YYYRNIIFGGHGIIKJJNNMLIGGDDEHINYY",
"YYYTLIGGGGGIHKHJMKMRLHGDDBDGJTYY",
"YYWPLHEEEGHIHILIMNLKJGFDCCDGJMYY",
"YTWQKFEEGGHJIIJLLPMMKHDCBBCHKTYY",
"YWQIHFFEGIKHJILLOTTMKHDCACEGNRWW",
"YWTJFFFFGGIIIKLWRWTMJFEBBCDGOTYY",
"WWMKHFFFHIIKLNQWWWOLGEDCBCFKQYYY",
"WTQIIGFHIKLKPROTPQOLHEDCCEFKNYYY",
"YTMMIHGJHIKLRPTWYTKKHFECFFIQWYYY",
"WRLKMIIKJLMOTYWTTQOIGFFFHILPYYYY",
"YTMMKMMKLOQQYWYWRPNJHHGHKLQTYYYY",
"YTOWOTPPWRTYYWYYTTPIJHJKJTRRYYYY",
"YTTPQRRQTTYYYYYYTNQMLLNNQTYYYYYY",
"YYRWWTWPWYYYYYYYYWONMNPQRYYYYYYY",
"YYYWYRWWYYYYYYYYWWRMPPNQYYYYYYYY",
"YYTWYWYYWYYYYYYYYTRWRWWYYYYYYYYY",
"YYYYYYWYYYYYYYYYYWYWYRYWYYYYYYYY",
"YYYWYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
"YYYYYYYYYYYYYYYYYTYYYYYYYYYYYYYY"
]

# Convert XPM characters to numerical values
Z = np.array([[color_map[char] for char in row] for row in data])

# Define x and y axis values
x_values = np.linspace(-17.8061, 14.3904, Z.shape[1])
y_values = np.linspace(-14.2613, 14.7793, Z.shape[0])
X, Y = np.meshgrid(x_values, y_values)

# Interpolation for smooth contours
xi = np.linspace(X.min(), X.max(), 100)
yi = np.linspace(Y.min(), Y.max(), 100)
Xi, Yi = np.meshgrid(xi, yi)
Zi = griddata((X.flatten(), Y.flatten()), Z.flatten(), (Xi, Yi), method='cubic')

# Set global color scale limits
vmin = Z.min()
vmax = Z.max()

# Plot Contour with smooth interpolation
plt.figure(figsize=(8, 6))
contour = plt.contourf(Xi, Yi, Zi, levels=20, cmap="rainbow", vmin=vmin, vmax=vmax)
plt.contour(Xi, Yi, Zi, levels=10, colors='black', linewidths=0.5)  # Contour lines
plt.colorbar(contour, label="Free Energy (kJ/mol)")
plt.title("Contour Plot of Gibbs Energy")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

# 3D Surface Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap="rainbow", edgecolor="k", vmin=vmin, vmax=vmax)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("Free Energy (kJ/mol)")
ax.set_title("3D Energy Surface with 2D Contour")

# Overlay contour plot on 3D surface at the bottom
ax.contourf(Xi, Yi, Zi, zdir='z', offset=Z.min(), cmap="rainbow", vmin=vmin, vmax=vmax)

plt.show()
