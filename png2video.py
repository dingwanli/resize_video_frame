import cv2
import os


def video2png(video_path, png_folder_path):
    cap = cv2.VideoCapture(video_path)
    video_name = os.path.split(video_path)[1]
    video_name_nofix = os.path.splitext(video_name)[0]
    count = 1
    while True:
        success, frame = cap.read()
        if success == False:
            break
        print(frame.shape)
        cv2.imwrite(png_folder_path + '\\'+ video_name_nofix + "-%d.png" % count, frame)
        count += 1

def png2video(png_load_path, video_save_path):

    files = os.listdir(png_load_path)
    files = sorted(files, key=lambda x: str(x.split('.')[0].split('-')[-1]))
    files = sorted(files, key=lambda x: len(x.split('.')[0].split('-')[-1]))
    video_file_name = os.path.splitext(files[0])[0].split('-')[0]

    h, w, _ = cv2.imread(png_load_path + files[0]).shape
    fps = 30
    vid = []

    #     设置要保存的格式:   mp4: mp4v; avi: xvid, i420
    video_file_path = video_save_path + video_file_name + '.mp4'
    if os.path.exists(video_file_path) is True:
        return 0
    #     save_path = "video/video.avi"		# 保存视频路径和名称 av格式

    vid = cv2.VideoWriter(video_file_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    # vid = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'xvid'), fps, (w, h))
    # vid = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'i420'), fps, (w, h))

    for file in files:
        img = cv2.imread(png_load_path + file)
        vid.write(img)

def png2video_subfolder(sequence_png_path, video_save_path):
    for each_subFolder in os.listdir(sequence_png_path):
        each_subFolder_path = os.path.join(sequence_png_path, each_subFolder) + '/'
#         print(each_subFolder_path)
        png2video(each_subFolder_path, video_save_path)

def video2png_subfolder(video_folder_path, sequence_png_path):
    for videofile_name in os.listdir(video_folder_path):
        videofile_path = os.path.join(video_folder_path, videofile_name)

        videofile_name_nofix = os.path.splitext(videofile_name)[0]
        png_subfolder_path = os.path.join(sequence_png_path, videofile_name_nofix)
        if not os.path.exists(png_subfolder_path):
            os.mkdir(png_subfolder_path)

        video2png(videofile_path, png_subfolder_path)

if __name__ == '__main__':
    # video_folder_path = r'E:\B_station\13\a4c_video'
    # sequence_png_path = r'E:\B_station\13\a4c_png'
    # video2png_subfolder(video_folder_path, sequence_png_path)

    png_load_path = r'E:\B_station\13\a4c_png\ES0001_4CH_1_resize/'
    video_save_path = r'E:\B_station\13\a4c_png\ES0001_4CH_1_resize_video/'
    png2video(png_load_path, video_save_path)

