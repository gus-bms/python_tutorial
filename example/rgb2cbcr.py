import cv2

img = cv2.imread('images.jpeg', cv2.IMREAD_COLOR)
cv2.imshow("rgb", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow("ycbcr", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

y, cr, cb = cv2.split(img2)

new = cv2.add(cr, cb)
cv2.imshow("y", y)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("cr", cr)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("cb", cb)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("bgr채널 x10, y10 값 :", img[10,20])
print("Ycbcr - Y x10, y10 값 :", y[10,20])
print("Ycbcr - cb x10, y10 값 :", cb[10,20])
print("Ycbcr - cr x10, y10 값 :", cr[10,20])