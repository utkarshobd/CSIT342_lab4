import numpy as np
import matplotlib.pyplot as plt

def generate_2d_dft_basis(N=8):
    """Generate 2D DFT basis functions for NxN grid"""
    basis = np.zeros((N*N, N, N), dtype=complex)
    idx = 0
    for u in range(N):
        for v in range(N):
            for x in range(N):
                for y in range(N):
                    basis[idx, x, y] = np.exp(-2j * np.pi * (u*x + v*y) / N)
            idx += 1
    return basis

def display_dft_basis():
    """Display 8x8 2D DFT basis as 64x64 image"""
    basis = generate_2d_dft_basis(8)
    
    # Create 64x64 display grid (8x8 basis functions arranged in 8x8 grid)
    display_grid = np.zeros((64, 64))
    
    for i in range(64):
        row = i // 8
        col = i % 8
        # Use real part for visualization
        basis_real = np.real(basis[i])
        # Normalize to [0,1]
        basis_norm = (basis_real - basis_real.min()) / (basis_real.max() - basis_real.min())
        
        display_grid[row*8:(row+1)*8, col*8:(col+1)*8] = basis_norm
    
    plt.figure(figsize=(10, 10))
    plt.imshow(display_grid, cmap='gray')
    plt.title('8x8 2D DFT Basis Functions (64x64 Display)')
    plt.axis('off')
    plt.show()

def create_rectangle_image():
    """Create binary 64x64 image with rectangle"""
    print("Enter rectangle parameters:")
    top_left_x = int(input("Top-left corner X position (0-63): "))
    top_left_y = int(input("Top-left corner Y position (0-63): "))
    width = int(input("Rectangle width (pixels): "))
    height = int(input("Rectangle height (pixels): "))
    
    # Create binary image
    image = np.zeros((64, 64))
    
    # Ensure rectangle stays within bounds
    end_x = min(top_left_x + width, 64)
    end_y = min(top_left_y + height, 64)
    
    image[top_left_y:end_y, top_left_x:end_x] = 1
    
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='gray')
    plt.title(f'Binary Rectangle Image (64x64)\nPosition: ({top_left_x},{top_left_y}), Size: {width}x{height}')
    plt.axis('off')
    plt.show()
    
    return image

def compute_2d_dft(image):
    """Compute 2D DFT without using ready-made DFT/FFT functions"""
    M, N = image.shape
    dft_result = np.zeros((M, N), dtype=complex)
    
    print("Computing 2D DFT...")
    for u in range(M):
        for v in range(N):
            sum_val = 0
            for x in range(M):
                for y in range(N):
                    sum_val += image[x, y] * np.exp(-2j * np.pi * (u*x/M + v*y/N))
            dft_result[u, v] = sum_val
        if u % 10 == 0:
            print(f"Progress: {u}/{M} rows completed")
    
    return dft_result

def plot_dft_results(dft_result, title_prefix=""):
    """Plot magnitude and phase of DFT results"""
    magnitude = np.abs(dft_result)
    phase = np.angle(dft_result)
    
    # Log scale for better visualization
    magnitude_log = np.log(magnitude + 1)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Magnitude plot
    im1 = ax1.imshow(magnitude_log, cmap='hot')
    ax1.set_title(f'{title_prefix}DFT Magnitude (Log Scale)')
    ax1.axis('off')
    plt.colorbar(im1, ax=ax1)
    
    # Phase plot
    im2 = ax2.imshow(phase, cmap='hsv')
    ax2.set_title(f'{title_prefix}DFT Phase')
    ax2.axis('off')
    plt.colorbar(im2, ax=ax2)
    
    plt.tight_layout()
    plt.show()

def create_centered_image(image):
    """Create centered image by multiplying with (-1)^(x+y)"""
    M, N = image.shape
    centered_image = np.zeros_like(image)
    
    for x in range(M):
        for y in range(N):
            centered_image[x, y] = image[x, y] * ((-1) ** (x + y))
    
    plt.figure(figsize=(8, 8))
    plt.imshow(centered_image, cmap='gray')
    plt.title('Centered Image (multiplied by (-1)^(x+y))')
    plt.axis('off')
    plt.show()
    
    return centered_image

def main():
    print("2D DFT Implementation Lab")
    print("=" * 30)
    
    # Step 1: Generate and display 2D DFT basis
    print("\n1. Generating 8x8 2D DFT basis...")
    display_dft_basis()
    
    # Step 2: Create binary rectangle image
    print("\n2. Creating binary rectangle image...")
    rectangle_image = create_rectangle_image()
    
    # Step 3: Compute 2D DFT for rectangle image
    print("\n3. Computing 2D DFT for rectangle image...")
    dft_rectangle = compute_2d_dft(rectangle_image)
    plot_dft_results(dft_rectangle, "Rectangle Image ")
    
    # Step 4: Compute 2D DFT for centered image
    print("\n4. Creating centered image and computing its 2D DFT...")
    centered_image = create_centered_image(rectangle_image)
    dft_centered = compute_2d_dft(centered_image)
    plot_dft_results(dft_centered, "Centered Image ")
    
    print("\nAll steps completed successfully!")

if __name__ == "__main__":
    main()