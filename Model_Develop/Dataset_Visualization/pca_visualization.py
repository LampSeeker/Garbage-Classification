from torch.utils.data import Dataset ,DataLoader
import os
import numpy as np
import tqdm
import cv2
import matplotlib
import matplotlib.pyplot as plt
import mplcursors
from IPython.display import clear_output
import matplotlib.image as mpimg

# 좋은 후보 예시 -10,-40의 스티로폼과 종이(비닐)
alpha = 0.3

train_x = np.load('pca_vec.npy')
x_label = np.load('label_sequence.npy')
image_paths_list = np.load('image_paths_list.npy')
x_label.shape , train_x.shape , image_paths_list.shape

k_label = { 0 : '종이' , 1 : '종이팩' ,2 : '종이컵' , 3 : '캔' ,
           4 : '유리병' , 5 : '페트' ,6 : '플라스틱' , 7 : '비닐',
           8 : '유리(포장재)' , 9 : '페트(포장재)' ,10 : '스티로폼' , 11 : '건전지'}

plt.rcParams['font.family'] = 'NanumGothic' 
matplotlib.rcParams['axes.unicode_minus'] = False

def draw_scatter_with_tooltips(train_x, x_label, image_paths_list):
    # 색상 맵 설정
    cmap = plt.cm.get_cmap('rainbow', len(np.unique(x_label)))

    fig, ax = plt.subplots()
    scatter = ax.scatter(train_x[:, 0], train_x[:, 1], c=x_label, cmap=cmap , alpha=alpha)

    # 저장된 이미지 폴더
    root_img_path = './crop_img_save'

    clicked_image_paths = []
    click_cnt = 0

    # 툴팁
    tooltip = ax.text(0, 0, '', alpha=0.7, bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='grey'))
    tooltip.set_visible(False)

    threshold_distance = 10


    # 각 점에 대한 label 정보를 툴팁으로 보여줄 함수
    def on_hover(event):
        if event.inaxes == ax:
            x, y = event.xdata, event.ydata
            distances = np.sqrt((train_x[:, 0] - x) ** 2 + (train_x[:, 1] - y) ** 2)
            ind = np.argmin(distances)
            min_distance = distances[ind]
    

            if min_distance <= threshold_distance:
                label = int(x_label[ind, 0])

                # Update the position and text of the tooltip
                tooltip.set_text(f"{k_label[label]}")
                tooltip.set_position((x+2, y+2))
                tooltip.set_visible(True)
                fig.canvas.draw_idle()
            else:
                # Hide the tooltip if the mouse is far from any data point
                tooltip.set_visible(False)
                fig.canvas.draw_idle()




    # 마우스를 올렸을 때의 이벤트 처리
    fig.canvas.mpl_connect("motion_notify_event", on_hover)

    # 점을 클릭했을 때의 이벤트 처리
    def on_click(event):
        nonlocal clicked_image_paths, click_cnt

        if event.inaxes == ax:
            x, y = event.xdata, event.ydata
            distances = np.sqrt((train_x[:, 0] - x) ** 2 + (train_x[:, 1] - y) ** 2)
            ind = np.argmin(distances)
            image_path = f"{image_paths_list[ind, 0]}.jpg"
            min_distance = distances[ind]
            threshold_distance = 10

            if min_distance <= threshold_distance:
                clicked_image_paths.append((ind, image_path))
            else:
                clear_output(wait=True)  # 이미지를 지우고 대기 상태로 유지

            click_cnt += 1

            if click_cnt % 2 == 0 and len(clicked_image_paths) >= 2:
                # Display the two most recently clicked images with their labels
                fig, axes = plt.subplots(1, 2, figsize=(10, 5))

                for i, (clicked_ind, img_path) in enumerate(clicked_image_paths[-2:]):
                    img = mpimg.imread(os.path.join(root_img_path, img_path))
                    label = k_label[int(x_label[clicked_ind, 0])]
                    axes[i].imshow(img)
                    axes[i].set_title(f"Label {i+1} : {label}")
                    axes[i].axis('off')

                plt.show()
    # 클릭 이벤트 처리 함수를 연결합니다.
    fig.canvas.mpl_connect("button_press_event", on_click)

    # 색상 막대 직접 생성하여 라벨 표시
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_ticks(np.arange(len(np.unique(x_label))) + 0.0)
    cbar.set_ticklabels([k_label[int(l)] for l in np.unique(x_label)])

    plt.xlabel('X 좌표')
    plt.ylabel('Y 좌표')
    plt.title('PCA : 객체 이미지 벡터 시각화',fontsize=20)
    plt.show()

draw_scatter_with_tooltips(train_x, x_label, image_paths_list)

