# Raspberry Pi Pico Usage Guide

[![YouTube Video](https://img.youtube.com/vi/lGAiZ7O3Xu8/0.jpg)](https://youtube.com/shorts/lGAiZ7O3Xu8?feature=share)

## Introduction
This guide provides instructions and examples for using the Raspberry Pi Pico development board with the latest version of Thonny IDE. The steps include firmware updates, uploading font files, and the ST7789 driver, as well as downloading example programs.

---

## Steps

### 1. Using the Raspberry Pi Pico Development Board
Ensure you have a Raspberry Pi Pico hardware device and a USB cable to connect it to your computer.

---

### 2. Install the Latest Thonny IDE
1. Go to the [Thonny official website](https://thonny.org/) to download the latest version.
2. After installation, launch Thonny IDE and set the Python interpreter to MicroPython for Raspberry Pi Pico.

---

### 3. Update the Latest Pico Firmware
1. Visit the [Raspberry Pi MicroPython firmware download page](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) to get the latest firmware.
2. Press and hold the **BOOTSEL button** on the Pico, then connect it to your computer.
3. The Pico will appear as a USB drive on your computer. Drag and drop the downloaded `.uf2` firmware file into the drive. The Pico will reboot automatically after the process.

---

### 4. Upload Font Files to the Development Board
1. Ensure you have the required font files (e.g., `.ttf` or converted binary font files).
2. Open Thonny IDE and use the file manager feature to upload the font files to the Pico's file system.

---

### 5. Upload the ST7789 Driver to the Development Board
1. Download the ST7789 MicroPython driver, such as [this driver](https://github.com/russhughes/st7789py_mpy).
2. Use Thonny to upload the driver files to the Pico's file system.

---

### 6. Download Example Programs
1. In this project, you can find example programs in the `examples/` folder.
2. Use Thonny to upload the example programs to the Pico and run them.

---

## Notes
To display BMP images, convert the images to a resolution of 240x240 and save them in a compatible format. You can use the following tool: [Online Image Conversion Tool](https://resizeimage.net/).

---

## Additional References
- [Raspberry Pi Pico Official Documentation](https://www.raspberrypi.com/documentation/microcontrollers/)  
- [MicroPython Official Documentation](https://docs.micropython.org/en/latest/)

If you have any questions, please submit an issue or contact the maintainer!

---

## License
This project is licensed under the terms of the [MIT License](LICENSE).
