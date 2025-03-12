# Projects in Data Science_Group_I (2025)

We ran the file main.py on the example image to test various results when changing the threshold and kernel size parameters in img_util.py.


The example picture we all agreed on a rating of 2 (a lot of hair) and looked to see how main.py performed on segmenting the image. Common consensus on the success of the program was if the hair surrounding the melanoma was fully removed, as the one on top of the melanoma would be harder to remove without affecting the quality of the melanoma itself.

---

## Hair in Skin Disease Pictures

Hair can make it hard to see skin problems in pictures. We checked each image and gave it a score: 

0 (no hair), 1 (some hair), or 2 (a lot of hair). 0 means no hair is in the way. 1 means there is some hair, but you can still see the skin. 2 means there is a lot of hair, making it hard to see the skin. 

This helps us know which images are clear and which are not. It also helps with removing hair from images. Clear images make it easier to study skin diseases.

---

## On changing the threshold numbers: 

We performed 4 different tests on the example image 

The lowest threshold we tested was 0: the threshold mask changed a lot compared to the original one, however the hair seemed fully removed. 

![Picture 1 on the Images_example file](https://github.com/luca-itu/2025-FYP-Assignment-Group-I/blob/main/result/Images_Example/Picture1.png?raw=true)

For threshold of 3, it did remove some quality out of the melanoma (more pixelated), but removed the hair out of the picture. 

![Picture 2 on the Images_example file](https://github.com/luca-itu/2025-FYP-Assignment-Group-I/blob/main/result/Images_Example/Picture2.png?raw=true)


For a value of 20, it removed a fair amount of hair, however, could be better. 

![Picture 3 on the Images_example file](https://github.com/luca-itu/2025-FYP-Assignment-Group-I/blob/main/result/Images_Example/Picture3.png?raw=true)

As for a threshold of value 50, the hair was not removed and the image appeared unchanged. 

![Picture 4 on the Images_example file](https://github.com/luca-itu/2025-FYP-Assignment-Group-I/blob/main/result/Images_Example/Picture4.png?raw=true)

Bottom line: the higher the threshold, the lower quality of hair segmentation. 

---

## On changing the kernel size (5 original)

Here, we again looked to see differences in 5 different kernel size values on hair segmentation. 

If kernel size is set to 1, the image is unchanged. 

![Picture 5 on the Images_example file](https://github.com/luca-itu/2025-FYP-Assignment-Group-I/blob/main/result/Images_Example/Picture5.png?raw=true)

Kernel size 7, the melanoma is unaffected, however, the hair appears like clusters. 

![Picture 6 on the Images_example file](https://github.com/luca-itu/2025-FYP-Assignment-Group-I/blob/main/result/Images_Example/Picture6.png?raw=true)

Kernel size 10, it cuts an insignificant amount out of the melanoma's surface and the hair looks blurry in the image. 

![Picture 7 on the Images_example file](https://github.com/luca-itu/2025-FYP-Assignment-Group-I/blob/main/result/Images_Example/Picture7.png?raw=true)

Kernel size 20, the hair is fully removed but the melanoma surface is affected 

![Picture 8 on the Images_example file](https://github.com/luca-itu/2025-FYP-Assignment-Group-I/blob/main/result/Images_Example/Picture8.png?raw=true)

While a kernel size of 50, the hair is completely gone, but the melanoma as well

![Picture 9 on the Images_example file](https://github.com/luca-itu/2025-FYP-Assignment-Group-I/blob/main/result/Images_Example/Picture9.png?raw=true)

Bottom line: Increased kernel size performs better on removing the hair, however affects melanoma surface quality.

---

As such, combining observations for both threshold and kernel values, a combination of both is needed to ensure effective hair segmentation with a higher kernel value, while maintaining the melanoma surface's quality with the threshold.