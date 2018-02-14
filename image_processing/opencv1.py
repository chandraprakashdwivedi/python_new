import cv2


img=cv2.imread("galaxy.jpg",1)

print(img)
print(img.shape)
print(img.ndim)


resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("galaxy_resize.jpg",resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()


