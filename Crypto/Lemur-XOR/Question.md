## The Challenge

I've hidden two cool images by XOR with the same secret key so you can't see them!

This challenge requires performing a visual XOR between the RGB bytes of the two images - not an XOR of all the data bytes of the files.


Challenge files:
  - lemur.png
  - flag.png

---

## The Explanation:

XOR has several important properties:
- Commutative: A ⊕ B = B ⊕ A
- Associative: (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C)
- Self-inverse: A ⊕ A = 0 and A ⊕ 0 = A
- Cancellation: If A ⊕ B = C, then A ⊕ C = B (and B ⊕ C = A)

Ok, so we have two images, and we need to perform a visual XOR between the RGB bytes of the two images.
Why is that?
A xor B = x1
C xor B = x2
SO x1 xor x2 = A xor C
This is because:
  x1 xor x2 = (A xor B) xor (C xor B)
  = A xor B xor C xor B (associative property)
  = A xor (B xor B) xor C (rearranging)
  = A xor 0 xor C (B xor B = 0)
  = A xor C
Conclusion:
XORing the two given images (lemur.png and flag.png) will reveal a new image that is the XOR of the two original, unencrypted images.
The challenge is to identify the secret key used for the XOR operation.
So this new image will likely reveal visual information from both original images, potentially making the flag visible.
But the secret key used for encryption remains unknown, preserving its security.
---

## The Solution:


1. Understanding the Challenge:
   - We have two images (lemur.png and flag.png) that have been XORed with the same secret key.
   - Our task is to perform a visual XOR between these two images to reveal the hidden information.

2. Conceptual Approach:
   - When we XOR the two encrypted images, the secret key cancels out, leaving us with the XOR of the original images.
   - This is because (A ⊕ Key) ⊕ (B ⊕ Key) = A ⊕ B ⊕ (Key ⊕ Key) = A ⊕ B

3. Image Processing Concept:
   - Images are composed of pixels, and each pixel has RGB (Red, Green, Blue) values.
   - We need to XOR the RGB values of corresponding pixels from both images.

4. Implementation Steps:
   a. Open both input images (lemur.png and flag.png).
   b. Ensure both images are in RGB mode and have the same dimensions.
   c. Create a new blank image to store the result.
   d. Iterate through each pixel position in both images:
      - Get the RGB values of the pixel from both images.
      - XOR the corresponding R, G, and B values.
      - Set the resulting RGB values in the new image at the same position.
   e. Save the resulting image.

5. Key Points for Implementation:
   - Use an image processing library that can handle PNG files and allow pixel-level manipulation.
   - Remember that XOR is performed on individual color channels, not on the entire pixel value.
   - Ensure proper error handling for file operations and potential image size mismatches.

6. Expected Outcome:
   - The resulting image should reveal visual information from both original images.
   - The flag or hidden message should become visible in this new image.

7. Verification:
   - Open the resulting image and visually inspect it for the flag or hidden message.
   - If the result isn't clear, try adjusting the contrast or brightness of the output image.

---