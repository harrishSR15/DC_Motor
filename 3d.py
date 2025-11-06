import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# STEP 1: Create a 3D scene
# ---------------------------
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X*2 + Y*2))  # Simulated depth surface

# ---------------------------
# STEP 2: Generate stereo views
# ---------------------------
eye_separation = 0.2
left_view = np.sin(np.sqrt((X + eye_separation)*2 + Y*2))
right_view = np.sin(np.sqrt((X - eye_separation)*2 + Y*2))

# Normalize for display
def normalize(img):
    img = img - np.min(img)
    return img / np.max(img)

left_view = normalize(left_view)
right_view = normalize(right_view)

# ---------------------------
# STEP 3: Assign polarization
# ---------------------------
# Left = Horizontal (R channel), Right = Vertical (B channel)
left_polarized = np.zeros((left_view.shape[0], left_view.shape[1], 3))
right_polarized = np.zeros_like(left_polarized)

left_polarized[..., 0] = left_view
right_polarized[..., 2] = right_view

# ---------------------------
# STEP 4: Combine both views
# ---------------------------
combined_display = 0.5 * (left_polarized + right_polarized)

# ---------------------------
# STEP 5: Simulate glasses filtering
# ---------------------------
# Adding slight crosstalk
crosstalk_factor = 0.05
left_eye_seen = left_polarized + crosstalk_factor * right_polarized
right_eye_seen = right_polarized + crosstalk_factor * left_polarized

# ---------------------------
# STEP 6: Stereo fusion (approximate)
# ---------------------------
stereo_fused = 0.5 * (left_eye_seen + right_eye_seen)

# ---------------------------
# STEP 7: Display results
# ---------------------------
fig, axs = plt.subplots(2, 3, figsize=(12, 7))
axs = axs.ravel()

axs[0].imshow(left_view, cmap='gray')
axs[0].set_title("Left Eye Image (Perspective)")

axs[1].imshow(right_view, cmap='gray')
axs[1].set_title("Right Eye Image (Perspective)")

axs[2].imshow(combined_display)
axs[2].set_title("Combined Polarization Display")

axs[3].imshow(left_eye_seen)
axs[3].set_title("Left Eye Through Glasses")

axs[4].imshow(right_eye_seen)
axs[4].set_title("Right Eye Through Glasses")

axs[5].imshow(stereo_fused)
axs[5].set_title("Fused Stereo (3D Perception)")

for ax in axs:
    ax.axis('off')

plt.tight_layout()
plt.show()

# ---------------------------
# STEP 8: Explore characteristics
# ---------------------------
crosstalk = np.mean(np.abs(left_eye_seen - left_polarized))
brightness_loss = np.mean(combined_display) / np.mean(left_polarized + right_polarized)

print("=== 3D Display Characteristics ===")
print(f"Crosstalk (leakage ratio): {crosstalk:.3f}")
print(f"Relative Brightness (after polarization): {brightness_loss:.3f}")
print("Depth perception simulated via horizontal parallax between left/right views.")