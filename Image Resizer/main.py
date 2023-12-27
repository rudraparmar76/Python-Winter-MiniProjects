import cv2
import pyttsx3

engine = pyttsx3.init()
print("----------- Welcome to Image Resizer 1.1 - Created By Rudra -----------".center(80))
engine.say("Welcome to Image Resizer 1.1 - Created By Rudra")
engine.runAndWait()
engine.say("Enter the location of the image")
engine.runAndWait()
loc = input("- Enter the location of the image:")

src = cv2.imread(f"{loc}", cv2.IMREAD_UNCHANGED)


#percent by which the image is resized
engine.say("Please enter the desired resize percentage for the image")
engine.runAndWait()
scale_percent = int(input("- Please enter the desired resize percentage for the image:"))

#calculate the 50 percent of the original dimension
new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)


#resize image
#resize function takes second parameter as a tuple in which we have new height and new width
output = cv2.resize(src, (new_width,new_height))
cv2.imwrite('resized.png',output)
engine.say("Resized Image is stored in the file name resized.png. Thank you for using Image Resizer")
engine.runAndWait()
print("- Thank you for using Image Resizer :)")
cv2.waitKey(0)