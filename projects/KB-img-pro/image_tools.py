"""
Image Data Tools - Data Augmentation and Processing Utilities

This module provides tools for image data augmentation, loading, saving,
batch processing, and dataset analysis.

Dependencies:
    pip install pillow numpy opencv-python
"""

import os
import random
from typing import List, Tuple, Union

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

# =============================================================================
# Image I/O Utilities
# =============================================================================


def load_image(path: str, mode: str = "RGB") -> Image.Image:
    """
    Load an image from file.

    Args:
        path: Path to the image file
        mode: Color mode ('RGB', 'L' for grayscale, 'RGBA')

    Returns:
        PIL Image object
    """
    img = Image.open(path)
    if mode:
        img = img.convert(mode)
    return img


def save_image(img: Image.Image, path: str, quality: int = 95) -> None:
    """
    Save an image to file.

    Args:
        img: PIL Image object
        path: Output path
        quality: JPEG quality (1-100)
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    img.save(path, quality=quality)


def load_images_from_directory(
    directory: str,
    extensions: Tuple[str, ...] = (".jpg", ".jpeg", ".png", ".bmp", ".gif"),
    mode: str = "RGB",
) -> List[Tuple[str, Image.Image]]:
    """
    Load all images from a directory.

    Args:
        directory: Path to directory
        extensions: Valid file extensions
        mode: Color mode

    Returns:
        List of (filename, image) tuples
    """
    images = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(extensions):
            path = os.path.join(directory, filename)
            img = load_image(path, mode)
            images.append((filename, img))
    return images


# =============================================================================
# Geometric Augmentations
# =============================================================================


def rotate(img: Image.Image, angle: float, expand: bool = False) -> Image.Image:
    """
    Rotate image by specified angle.

    Args:
        img: Input image
        angle: Rotation angle in degrees (positive = counter-clockwise)
        expand: If True, expand output to fit entire rotated image

    Returns:
        Rotated image
    """
    return img.rotate(angle, expand=expand, resample=Image.BICUBIC)


def random_rotate(img: Image.Image, max_angle: float = 30) -> Image.Image:
    """
    Randomly rotate image within range [-max_angle, max_angle].
    """
    angle = random.uniform(-max_angle, max_angle)
    return rotate(img, angle)


def flip_horizontal(img: Image.Image) -> Image.Image:
    """Flip image horizontally (left-right)."""
    return ImageOps.mirror(img)


def flip_vertical(img: Image.Image) -> Image.Image:
    """Flip image vertically (top-bottom)."""
    return ImageOps.flip(img)


def random_flip(
    img: Image.Image, horizontal: bool = True, vertical: bool = False
) -> Image.Image:
    """
    Randomly flip image.

    Args:
        img: Input image
        horizontal: Allow horizontal flip
        vertical: Allow vertical flip

    Returns:
        Possibly flipped image
    """
    if horizontal and random.random() > 0.5:
        img = flip_horizontal(img)
    if vertical and random.random() > 0.5:
        img = flip_vertical(img)
    return img


def resize(img: Image.Image, size: Tuple[int, int]) -> Image.Image:
    """
    Resize image to specified size.

    Args:
        img: Input image
        size: (width, height)

    Returns:
        Resized image
    """
    return img.resize(size, Image.BICUBIC)


def crop(img: Image.Image, box: Tuple[int, int, int, int]) -> Image.Image:
    """
    Crop image to specified box.

    Args:
        img: Input image
        box: (left, top, right, bottom)

    Returns:
        Cropped image
    """
    return img.crop(box)


def center_crop(img: Image.Image, size: Tuple[int, int]) -> Image.Image:
    """
    Crop image from center.

    Args:
        img: Input image
        size: (width, height) of crop

    Returns:
        Center-cropped image
    """
    w, h = img.size
    new_w, new_h = size
    left = (w - new_w) // 2
    top = (h - new_h) // 2
    return img.crop((left, top, left + new_w, top + new_h))


def random_crop(img: Image.Image, size: Tuple[int, int]) -> Image.Image:
    """
    Randomly crop image.

    Args:
        img: Input image
        size: (width, height) of crop

    Returns:
        Randomly cropped image
    """
    w, h = img.size
    new_w, new_h = size
    if new_w > w or new_h > h:
        raise ValueError(f"Crop size {size} larger than image size {(w, h)}")
    left = random.randint(0, w - new_w)
    top = random.randint(0, h - new_h)
    return img.crop((left, top, left + new_w, top + new_h))


def scale(img: Image.Image, factor: float) -> Image.Image:
    """
    Scale image by factor.

    Args:
        img: Input image
        factor: Scale factor (>1 enlarges, <1 shrinks)

    Returns:
        Scaled image
    """
    w, h = img.size
    new_size = (int(w * factor), int(h * factor))
    return img.resize(new_size, Image.BICUBIC)


def random_scale(
    img: Image.Image, min_factor: float = 0.8, max_factor: float = 1.2
) -> Image.Image:
    """Randomly scale image within range."""
    factor = random.uniform(min_factor, max_factor)
    return scale(img, factor)


def translate(img: Image.Image, offset: Tuple[int, int], fill: int = 0) -> Image.Image:
    """
    Translate (shift) image.

    Args:
        img: Input image
        offset: (x, y) offset in pixels
        fill: Fill value for empty areas

    Returns:
        Translated image
    """
    if img.mode == "RGB":
        fill_color = (fill, fill, fill)
    else:
        fill_color = fill

    # Create offset image
    result = Image.new(img.mode, img.size, fill_color)
    result.paste(img, offset)
    return result


def random_translate(
    img: Image.Image, max_offset: Tuple[int, int] = (20, 20), fill: int = 0
) -> Image.Image:
    """Randomly translate image."""
    x_offset = random.randint(-max_offset[0], max_offset[0])
    y_offset = random.randint(-max_offset[1], max_offset[1])
    return translate(img, (x_offset, y_offset), fill)


# =============================================================================
# Color Augmentations
# =============================================================================


def adjust_brightness(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjust image brightness.

    Args:
        img: Input image
        factor: Brightness factor (1.0 = original, >1 brighter, <1 darker)

    Returns:
        Adjusted image
    """
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)


def random_brightness(
    img: Image.Image, min_factor: float = 0.7, max_factor: float = 1.3
) -> Image.Image:
    """Randomly adjust brightness."""
    factor = random.uniform(min_factor, max_factor)
    return adjust_brightness(img, factor)


def adjust_contrast(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjust image contrast.

    Args:
        img: Input image
        factor: Contrast factor (1.0 = original, >1 more contrast)

    Returns:
        Adjusted image
    """
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)


def random_contrast(
    img: Image.Image, min_factor: float = 0.7, max_factor: float = 1.3
) -> Image.Image:
    """Randomly adjust contrast."""
    factor = random.uniform(min_factor, max_factor)
    return adjust_contrast(img, factor)


def adjust_saturation(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjust image saturation.

    Args:
        img: Input image
        factor: Saturation factor (1.0 = original, 0 = grayscale)

    Returns:
        Adjusted image
    """
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(factor)


def random_saturation(
    img: Image.Image, min_factor: float = 0.7, max_factor: float = 1.3
) -> Image.Image:
    """Randomly adjust saturation."""
    factor = random.uniform(min_factor, max_factor)
    return adjust_saturation(img, factor)


def adjust_sharpness(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjust image sharpness.

    Args:
        img: Input image
        factor: Sharpness factor (1.0 = original, >1 sharper, <1 blurrier)

    Returns:
        Adjusted image
    """
    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)


def to_grayscale(img: Image.Image) -> Image.Image:
    """Convert image to grayscale."""
    return img.convert("L").convert("RGB")


def random_grayscale(img: Image.Image, probability: float = 0.1) -> Image.Image:
    """Randomly convert to grayscale."""
    if random.random() < probability:
        return to_grayscale(img)
    return img


def invert_colors(img: Image.Image) -> Image.Image:
    """Invert image colors."""
    return ImageOps.invert(img.convert("RGB"))


def adjust_gamma(img: Image.Image, gamma: float) -> Image.Image:
    """
    Adjust image gamma.

    Args:
        img: Input image
        gamma: Gamma value (>1 darkens midtones, <1 lightens)

    Returns:
        Gamma-adjusted image
    """
    img_array = np.array(img).astype(np.float32) / 255.0
    img_array = np.power(img_array, gamma)
    img_array = (img_array * 255).astype(np.uint8)
    return Image.fromarray(img_array)


# =============================================================================
# Noise and Blur Augmentations
# =============================================================================


def add_gaussian_noise(
    img: Image.Image, mean: float = 0, std: float = 25
) -> Image.Image:
    """
    Add Gaussian noise to image.

    Args:
        img: Input image
        mean: Noise mean
        std: Noise standard deviation

    Returns:
        Noisy image
    """
    img_array = np.array(img).astype(np.float32)
    noise = np.random.normal(mean, std, img_array.shape)
    noisy = np.clip(img_array + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy)


def add_salt_pepper_noise(img: Image.Image, amount: float = 0.02) -> Image.Image:
    """
    Add salt and pepper noise.

    Args:
        img: Input image
        amount: Proportion of pixels to affect

    Returns:
        Noisy image
    """
    img_array = np.array(img).copy()
    h, w = img_array.shape[:2]
    n_pixels = int(h * w * amount)

    # Salt (white)
    for _ in range(n_pixels // 2):
        y = random.randint(0, h - 1)
        x = random.randint(0, w - 1)
        img_array[y, x] = 255

    # Pepper (black)
    for _ in range(n_pixels // 2):
        y = random.randint(0, h - 1)
        x = random.randint(0, w - 1)
        img_array[y, x] = 0

    return Image.fromarray(img_array)


def gaussian_blur(img: Image.Image, radius: float = 2) -> Image.Image:
    """
    Apply Gaussian blur.

    Args:
        img: Input image
        radius: Blur radius

    Returns:
        Blurred image
    """
    return img.filter(ImageFilter.GaussianBlur(radius))


def random_blur(img: Image.Image, max_radius: float = 3) -> Image.Image:
    """Randomly apply Gaussian blur."""
    radius = random.uniform(0, max_radius)
    return gaussian_blur(img, radius)


def motion_blur(img: Image.Image, size: int = 15, angle: float = 0) -> Image.Image:
    """
    Apply motion blur effect.

    Args:
        img: Input image
        size: Kernel size
        angle: Blur angle in degrees

    Returns:
        Motion-blurred image
    """
    # Create motion blur kernel
    kernel = np.zeros((size, size))
    kernel[size // 2, :] = 1
    kernel = kernel / size

    # Rotate kernel
    from scipy.ndimage import rotate as scipy_rotate

    try:
        kernel = scipy_rotate(kernel, angle, reshape=False)
    except ImportError:
        pass  # Use unrotated kernel if scipy not available

    # Apply convolution
    img_array = np.array(img)
    from PIL import ImageFilter

    # Simple approximation using PIL
    return img.filter(ImageFilter.MotionBlur(size))


# =============================================================================
# Advanced Augmentations
# =============================================================================


def random_erasing(
    img: Image.Image,
    probability: float = 0.5,
    scale: Tuple[float, float] = (0.02, 0.33),
    ratio: Tuple[float, float] = (0.3, 3.3),
    fill: Union[int, Tuple[int, int, int]] = 128,
) -> Image.Image:
    """
    Random erasing augmentation (cutout).

    Args:
        img: Input image
        probability: Probability of applying
        scale: Range of proportion of image to erase
        ratio: Range of aspect ratio of erased area
        fill: Fill value

    Returns:
        Augmented image
    """
    if random.random() > probability:
        return img

    img = img.copy()
    w, h = img.size
    area = w * h

    for _ in range(10):  # Try 10 times
        target_area = random.uniform(scale[0], scale[1]) * area
        aspect_ratio = random.uniform(ratio[0], ratio[1])

        erase_w = int(round((target_area * aspect_ratio) ** 0.5))
        erase_h = int(round((target_area / aspect_ratio) ** 0.5))

        if erase_w < w and erase_h < h:
            x = random.randint(0, w - erase_w)
            y = random.randint(0, h - erase_h)

            from PIL import ImageDraw

            draw = ImageDraw.Draw(img)
            draw.rectangle([x, y, x + erase_w, y + erase_h], fill=fill)
            return img

    return img


def color_jitter(
    img: Image.Image,
    brightness: float = 0.2,
    contrast: float = 0.2,
    saturation: float = 0.2,
) -> Image.Image:
    """
    Apply random color jittering.

    Args:
        img: Input image
        brightness: Max brightness change
        contrast: Max contrast change
        saturation: Max saturation change

    Returns:
        Color-jittered image
    """
    transforms = [
        lambda x: random_brightness(x, 1 - brightness, 1 + brightness),
        lambda x: random_contrast(x, 1 - contrast, 1 + contrast),
        lambda x: random_saturation(x, 1 - saturation, 1 + saturation),
    ]
    random.shuffle(transforms)
    for transform in transforms:
        img = transform(img)
    return img


# =============================================================================
# Augmentation Pipeline
# =============================================================================


class AugmentationPipeline:
    """
    Pipeline for chaining multiple augmentations.

    Usage:
        pipeline = AugmentationPipeline([
            ('random_flip', {'horizontal': True}),
            ('random_rotate', {'max_angle': 15}),
            ('color_jitter', {'brightness': 0.2}),
        ])
        augmented = pipeline(image)
    """

    # Map of augmentation names to functions
    AUGMENTATIONS = {
        "rotate": rotate,
        "random_rotate": random_rotate,
        "flip_horizontal": flip_horizontal,
        "flip_vertical": flip_vertical,
        "random_flip": random_flip,
        "resize": resize,
        "crop": crop,
        "center_crop": center_crop,
        "random_crop": random_crop,
        "scale": scale,
        "random_scale": random_scale,
        "translate": translate,
        "random_translate": random_translate,
        "adjust_brightness": adjust_brightness,
        "random_brightness": random_brightness,
        "adjust_contrast": adjust_contrast,
        "random_contrast": random_contrast,
        "adjust_saturation": adjust_saturation,
        "random_saturation": random_saturation,
        "adjust_sharpness": adjust_sharpness,
        "to_grayscale": to_grayscale,
        "random_grayscale": random_grayscale,
        "invert_colors": invert_colors,
        "adjust_gamma": adjust_gamma,
        "add_gaussian_noise": add_gaussian_noise,
        "add_salt_pepper_noise": add_salt_pepper_noise,
        "gaussian_blur": gaussian_blur,
        "random_blur": random_blur,
        "random_erasing": random_erasing,
        "color_jitter": color_jitter,
    }

    def __init__(self, transforms: List[Tuple[str, dict]]):
        """
        Initialize pipeline.

        Args:
            transforms: List of (augmentation_name, kwargs) tuples
        """
        self.transforms = transforms

    def __call__(self, img: Image.Image) -> Image.Image:
        """Apply all transforms to image."""
        for name, kwargs in self.transforms:
            if name not in self.AUGMENTATIONS:
                raise ValueError(f"Unknown augmentation: {name}")
            func = self.AUGMENTATIONS[name]
            img = func(img, **kwargs)
        return img


# =============================================================================
# Batch Processing
# =============================================================================


def augment_directory(
    input_dir: str,
    output_dir: str,
    pipeline: AugmentationPipeline,
    num_augmentations: int = 5,
    prefix: str = "aug_",
) -> int:
    """
    Apply augmentations to all images in a directory.

    Args:
        input_dir: Input directory path
        output_dir: Output directory path
        pipeline: Augmentation pipeline
        num_augmentations: Number of augmented versions per image
        prefix: Prefix for augmented filenames

    Returns:
        Number of images created
    """
    os.makedirs(output_dir, exist_ok=True)
    images = load_images_from_directory(input_dir)
    count = 0

    for filename, img in images:
        name, ext = os.path.splitext(filename)

        # Save original
        save_image(img, os.path.join(output_dir, filename))
        count += 1

        # Generate augmentations
        for i in range(num_augmentations):
            augmented = pipeline(img)
            aug_filename = f"{prefix}{name}_{i}{ext}"
            save_image(augmented, os.path.join(output_dir, aug_filename))
            count += 1

    return count


def process_batch(
    images: List[Image.Image], pipeline: AugmentationPipeline
) -> List[Image.Image]:
    """
    Apply pipeline to a batch of images.

    Args:
        images: List of images
        pipeline: Augmentation pipeline

    Returns:
        List of augmented images
    """
    return [pipeline(img) for img in images]


# =============================================================================
# Dataset Analysis
# =============================================================================


def get_image_stats(img: Image.Image) -> dict:
    """
    Get statistics for a single image.

    Args:
        img: Input image

    Returns:
        Dictionary with image statistics
    """
    img_array = np.array(img)
    stats = {
        "width": img.size[0],
        "height": img.size[1],
        "mode": img.mode,
        "channels": len(img.getbands()),
        "mean": img_array.mean(),
        "std": img_array.std(),
        "min": img_array.min(),
        "max": img_array.max(),
    }

    if len(img_array.shape) == 3:
        stats["channel_means"] = img_array.mean(axis=(0, 1)).tolist()
        stats["channel_stds"] = img_array.std(axis=(0, 1)).tolist()

    return stats


def analyze_dataset(directory: str) -> dict:
    """
    Analyze all images in a directory.

    Args:
        directory: Path to image directory

    Returns:
        Dictionary with dataset statistics
    """
    images = load_images_from_directory(directory)

    if not images:
        return {"error": "No images found"}

    widths = []
    heights = []
    means = []
    stds = []

    for filename, img in images:
        stats = get_image_stats(img)
        widths.append(stats["width"])
        heights.append(stats["height"])
        means.append(stats["mean"])
        stds.append(stats["std"])

    return {
        "num_images": len(images),
        "width": {
            "min": min(widths),
            "max": max(widths),
            "mean": np.mean(widths),
        },
        "height": {
            "min": min(heights),
            "max": max(heights),
            "mean": np.mean(heights),
        },
        "pixel_mean": np.mean(means),
        "pixel_std": np.mean(stds),
        "filenames": [f for f, _ in images],
    }


def print_dataset_summary(directory: str) -> None:
    """Print a formatted summary of the dataset."""
    stats = analyze_dataset(directory)

    if "error" in stats:
        print(f"Error: {stats['error']}")
        return

    print(f"\n{'=' * 50}")
    print(f"Dataset Summary: {directory}")
    print(f"{'=' * 50}")
    print(f"Number of images: {stats['num_images']}")
    print("\nImage dimensions:")
    print(
        f"  Width:  min={stats['width']['min']}, max={stats['width']['max']}, mean={stats['width']['mean']:.1f}"
    )
    print(
        f"  Height: min={stats['height']['min']}, max={stats['height']['max']}, mean={stats['height']['mean']:.1f}"
    )
    print("\nPixel statistics:")
    print(f"  Mean: {stats['pixel_mean']:.2f}")
    print(f"  Std:  {stats['pixel_std']:.2f}")
    print(f"{'=' * 50}\n")


# =============================================================================
# Preset Pipelines
# =============================================================================


def get_light_augmentation() -> AugmentationPipeline:
    """Get a light augmentation pipeline for fine-tuning."""
    return AugmentationPipeline(
        [
            ("random_flip", {"horizontal": True}),
            ("random_brightness", {"min_factor": 0.9, "max_factor": 1.1}),
        ]
    )


def get_medium_augmentation() -> AugmentationPipeline:
    """Get a medium augmentation pipeline."""
    return AugmentationPipeline(
        [
            ("random_flip", {"horizontal": True}),
            ("random_rotate", {"max_angle": 15}),
            ("color_jitter", {"brightness": 0.2, "contrast": 0.2, "saturation": 0.2}),
        ]
    )


def get_heavy_augmentation() -> AugmentationPipeline:
    """Get a heavy augmentation pipeline for training with limited data."""
    return AugmentationPipeline(
        [
            ("random_flip", {"horizontal": True, "vertical": True}),
            ("random_rotate", {"max_angle": 30}),
            ("random_scale", {"min_factor": 0.8, "max_factor": 1.2}),
            ("color_jitter", {"brightness": 0.3, "contrast": 0.3, "saturation": 0.3}),
            ("random_blur", {"max_radius": 2}),
            ("random_erasing", {"probability": 0.3}),
        ]
    )


# =============================================================================
# Main / Demo
# =============================================================================

if __name__ == "__main__":
    # Demo usage
    print("Image Data Tools - Demo")
    print("-" * 40)

    # Check if we have a test image
    test_dir = "data/raw/can"
    if os.path.exists(test_dir):
        print(f"\nAnalyzing dataset in: {test_dir}")
        print_dataset_summary(test_dir)

        # Load and augment a sample image
        images = load_images_from_directory(test_dir)
        if images:
            filename, img = images[0]
            print(f"\nDemonstrating augmentations on: {filename}")

            # Create output directory
            output_dir = "data/augmented"
            os.makedirs(output_dir, exist_ok=True)

            # Apply different augmentations
            augmentations = [
                ("original", img),
                ("rotated_15", rotate(img, 15)),
                ("flipped_h", flip_horizontal(img)),
                ("brightness_up", adjust_brightness(img, 1.3)),
                ("contrast_up", adjust_contrast(img, 1.5)),
                ("gaussian_noise", add_gaussian_noise(img, std=30)),
                ("blurred", gaussian_blur(img, 3)),
                ("color_jitter", color_jitter(img)),
            ]

            for name, aug_img in augmentations:
                output_path = os.path.join(output_dir, f"{name}.jpg")
                save_image(aug_img, output_path)
                print(f"  Saved: {output_path}")

            print(f"\nDemo complete! Check {output_dir} for results.")
    else:
        print(f"\nNo test directory found at: {test_dir}")
        print("Place images in 'data/raw/can' to test the augmentation tools.")

    print("\n" + "=" * 40)
    print("Available functions:")
    print("-" * 40)
    for name in sorted(AugmentationPipeline.AUGMENTATIONS.keys()):
        print(f"  - {name}")
    print("\nPreset pipelines:")
    print("  - get_light_augmentation()")
    print("  - get_medium_augmentation()")
    print("  - get_heavy_augmentation()")
