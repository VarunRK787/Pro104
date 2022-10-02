import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,  
           "Sun",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1.5,  
           color=(00,00,00)
           )

cv2.putText(img,  
           "Mercury",
           (120, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Venus",
           (190, 215),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=.7,  
           color=(00,00,00)
           ) 

cv2.putText(img,  
           "Earth",
           (285, 215),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=.8,  
           color=(255,255,255)
           )  

cv2.putText(img,  
           "Mars",
           (385, 215),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Jupiter",
           (485, 215),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(00,00,00)
           )

cv2.putText(img,  
           "Saturn",
           (745, 215),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(00,00,00)
           )

cv2.putText(img,  
           "Uranus",
           (945, 215),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(00,00,00)
           )  

cv2.putText(img,  
           "Neptune",
           (1095, 215),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(00,00,00)
           )                                                              
           
cv2.imshow("output",img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)




