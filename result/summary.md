# Projects in Data Science_Group_I (2025)
We ran the file main.py on the example image to test various results when changing the treshold and kernel size parameters in img_util.py.The example picture we all agreed on a rating of 2 (a lot of hair) and looked to see how main.py performed on segmenting the image. Common consensus on the success of the program was if the hair surrounding the melanoma was fully removed, as the one on top of the melanoma would be harder to remove without affecting the quality of the melanoma itself.

---
On changing the treshold numbers: 

We performed 4 different tests on the example image, the lowest treshold being 0: the treshold mask changed a lot compared to the original one, however the hair seemed fully removed. For treshold of 3, it did remove some quality out of the melanoma (more pixelated), but removed the hair out of the picture. For a value of 20, it removed a fair amount of hair, however, could be better. As for a treshold of value 50, the hair was not removed and the image appeared unchanged. 

Bottom line: the higher the treshold, the lower quality of hair segmentation. 

---

On changing the kernel size (5 original)

Here, we again looked to see differences in 5different kernel size values on hair segmentation. If kernel size is set to 1, the image is unchanged. For a vlue of 7, the melanoma is unaffected, hoever, the hair appears like clusters. Kernel sie 10, it cuts an insignificant amount out of the melanoma's surface and the hair looks blurry in the image. For a kernel size of 20, the hair is fully removed but the melanoma surface is affected, while a kernel size of 50, the hair is completely gone, but the melanoma as well :p

Bottom line: Increased kernel size performs better on removing the hair, however affects melanoma surface quality.

As such, combining observations for both treshold and kernel values, a combination of both is needed to ensure effective hair segmentation with a higher treshold, while maintaining the melanoma surface's quality with the treshold.










