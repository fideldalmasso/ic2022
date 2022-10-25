import cv2

HEIGHT = 299
WIDTH = 299

# for type in ['Viral Pneumonia']:
for type in ['COVID','Normal','Viral Pneumonia']:
    for i in range(1,1001):
        
        IMAGE_FILENAME = f'./dataset/{type}/images/{type}-{i}.png'
        MASK_FILENAME = f'./dataset/{type}/masks/{type}-{i}.png'
        OUTPUT_FILENAME = f'./dataset/{type}/images_with_mask/{type}-{i}.png'
        
        img = cv2.imread(IMAGE_FILENAME)
        mask = cv2.imread(MASK_FILENAME,0)
        resized_mask = cv2.resize(mask, (HEIGHT,WIDTH), interpolation= cv2.INTER_LINEAR)
        res = cv2.bitwise_and(img,img,mask = resized_mask)
        cv2.imwrite(OUTPUT_FILENAME,res)
        print(OUTPUT_FILENAME)
        





def display(img):
    cv2.imshow("Image with mask", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()