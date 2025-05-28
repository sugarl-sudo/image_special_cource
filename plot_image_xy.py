import cv2
import csv

IMG = "box.JPG"  # キャリブ画像
OUT = "coords.csv"  # 出力先
points = []  # 応答配列


def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        idx = len(points) + 1
        points.append((idx, x, y))
        print(f"{idx}: ({x}, {y})")
        cv2.circle(img, (x, y), 4, (0, 0, 255), -1)
        cv2.imshow("pick", img)
        if idx == 12:  # 12点揃ったら保存
            with open(OUT, "w", newline="") as f:
                csv.writer(f).writerows(points)
            print("saved ->", OUT)
            cv2.destroyAllWindows()


img = cv2.imread(IMG)
cv2.namedWindow("pick"), cv2.setMouseCallback("pick", on_click)
cv2.imshow("pick", img)
cv2.waitKey(0)
