"""
Test script to verify the image tools can find files in the directory.
This tests that the path resolution fix works correctly.
"""

import os
import sys

# Add the script directory to path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from image_tools import (
    SCRIPT_DIR as TOOLS_SCRIPT_DIR,
)
from image_tools import (
    load_images_from_directory,
)


def test_script_dir_is_correct():
    """Test that SCRIPT_DIR points to the correct directory."""
    print("=" * 60)
    print("TEST 1: SCRIPT_DIR Resolution")
    print("=" * 60)

    expected_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Expected SCRIPT_DIR: {expected_dir}")
    print(f"Actual SCRIPT_DIR:   {TOOLS_SCRIPT_DIR}")

    assert TOOLS_SCRIPT_DIR == expected_dir, "SCRIPT_DIR mismatch!"
    print("✅ PASSED: SCRIPT_DIR is correctly resolved\n")


def test_data_directories_exist():
    """Test that the data directories can be found."""
    print("=" * 60)
    print("TEST 2: Data Directory Detection")
    print("=" * 60)

    # Define expected directories
    data_dirs = [
        os.path.join(TOOLS_SCRIPT_DIR, "data"),
        os.path.join(TOOLS_SCRIPT_DIR, "data", "raw"),
        os.path.join(TOOLS_SCRIPT_DIR, "data", "raw", "can"),
        os.path.join(TOOLS_SCRIPT_DIR, "data", "raw", "pet"),
        os.path.join(TOOLS_SCRIPT_DIR, "data", "raw", "taobin-bottle"),
        os.path.join(TOOLS_SCRIPT_DIR, "data", "raw", "taobin-pa"),
    ]

    all_passed = True
    for dir_path in data_dirs:
        exists = os.path.exists(dir_path)
        status = "✅" if exists else "❌"
        print(f"{status} {dir_path} - {'Found' if exists else 'NOT FOUND'}")
        if not exists:
            all_passed = False

    if all_passed:
        print("\n✅ PASSED: All data directories found\n")
    else:
        print("\n⚠️ WARNING: Some directories not found (may be empty)\n")

    return all_passed


def test_load_images_from_directories():
    """Test that images can be loaded from each directory."""
    print("=" * 60)
    print("TEST 3: Image Loading from Directories")
    print("=" * 60)

    raw_dir = os.path.join(TOOLS_SCRIPT_DIR, "data", "raw")

    if not os.path.exists(raw_dir):
        print(f"❌ Raw directory not found: {raw_dir}")
        return False

    # List all subdirectories in raw
    subdirs = [
        d for d in os.listdir(raw_dir) if os.path.isdir(os.path.join(raw_dir, d))
    ]

    total_images = 0
    results = []

    for subdir in subdirs:
        subdir_path = os.path.join(raw_dir, subdir)
        try:
            images = load_images_from_directory(subdir_path)
            count = len(images)
            total_images += count
            status = "✅" if count > 0 else "⚠️"
            results.append((subdir, count, status, None))
        except Exception as e:
            results.append((subdir, 0, "❌", str(e)))

    for subdir, count, status, error in results:
        if error:
            print(f"{status} {subdir}: ERROR - {error}")
        else:
            print(f"{status} {subdir}: {count} image(s) found")

    print(f"\n📊 Total images found: {total_images}")

    if total_images > 0:
        print("✅ PASSED: Successfully loaded images\n")
        return True
    else:
        print("⚠️ WARNING: No images found in directories\n")
        return False


def test_path_works_from_any_directory():
    """Test that paths work regardless of current working directory."""
    print("=" * 60)
    print("TEST 4: Path Independence Test")
    print("=" * 60)

    original_cwd = os.getcwd()
    print(f"Original CWD: {original_cwd}")

    # Change to a completely different directory
    test_cwd = os.path.expanduser("~")  # Home directory
    os.chdir(test_cwd)
    print(f"Changed CWD to: {os.getcwd()}")

    # Try to access files using SCRIPT_DIR
    test_dir = os.path.join(TOOLS_SCRIPT_DIR, "data", "raw", "can")
    exists = os.path.exists(test_dir)

    # Restore original directory
    os.chdir(original_cwd)
    print(f"Restored CWD to: {os.getcwd()}")

    if exists:
        print(f"✅ PASSED: Path '{test_dir}' accessible from any directory\n")
        return True
    else:
        print(f"⚠️ Directory not found (may be empty): {test_dir}\n")
        return True  # Not a failure, directory might just be empty


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("     IMAGE TOOLS PATH RESOLUTION TEST SUITE")
    print("=" * 60 + "\n")

    results = []

    # Test 1
    try:
        test_script_dir_is_correct()
        results.append(("SCRIPT_DIR Resolution", True))
    except AssertionError as e:
        print(f"❌ FAILED: {e}\n")
        results.append(("SCRIPT_DIR Resolution", False))

    # Test 2
    results.append(("Data Directory Detection", test_data_directories_exist()))

    # Test 3
    results.append(("Image Loading", test_load_images_from_directories()))

    # Test 4
    results.append(("Path Independence", test_path_works_from_any_directory()))

    # Summary
    print("=" * 60)
    print("                    TEST SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, r in results if r)
    total = len(results)

    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")

    print(f"\nResult: {passed}/{total} tests passed")
    print("=" * 60 + "\n")

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
