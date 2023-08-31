import numpy as np
import cv2
import os

# frame_resize 为一帧的图片size，比如 （512,512）; deep_resize 为帧的数量，比如：80
def resize_video_1channel(sample_dir, result_sample_dir, deep_resize, frame_resize):
    sample_list = os.listdir(sample_dir)
    sample_list = sorted(sample_list, key=lambda x: str(x.split('.')[0].split('-')[-1]))
    sample_list = sorted(sample_list, key=lambda x: len(x.split('.')[0].split('-')[-1]))

    file_example = sample_list[0]
    file_name = file_example.split('-')[0]
    file_example_path = os.path.join(sample_dir, file_example)
    img_1 = cv2.imread(file_example_path)
    h, w, c = img_1.shape

    stack = np.zeros((len(sample_list), h, w), np.uint8)
    for num, img in enumerate(sample_list):
        img_dir = os.path.join(sample_dir, img)
        stack[num, :, :] = cv2.imread(img_dir)[:,:,2]
    print('stack.shape: ', stack.shape)

    stack_resize = np.zeros((deep_resize, h, w), np.uint8)
    for h_index in range(h):
        coronal_plane = stack[:, h_index, :]
        coronal_plane_resize = cv2.resize(coronal_plane, (w, deep_resize))
        stack_resize[:, h_index, :] = coronal_plane_resize
    print('stack_resize shape: ', stack_resize.shape)

    for deep_index in range(deep_resize):
        frame = stack_resize[deep_index]
        frame = frame[:, :, np.newaxis]
        resize_frame = cv2.resize(frame, frame_resize)
        resize_frame = resize_frame[:, :, np.newaxis]
        # print(resize_frame.shape, type(resize_frame))
        cv2.imwrite(result_sample_dir + f'{file_name}-{deep_index}.png', resize_frame)

if __name__ == '__main__':
    sample_dir = r'E:\B_station\13\a4c_png\ES0001_4CH_1/'
    result_sample_dir = r'E:\B_station\13\a4c_png\ES0001_4CH_1_resize/'
    resize_video_1channel(sample_dir, result_sample_dir, deep_resize=80, frame_resize=(512,512))
