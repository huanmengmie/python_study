# -*- coding:UTF-8 -*-
import cv2
import numpy as np


def moving_object_detection():
    camera = cv2.VideoCapture("10.mp4")
    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 4))
    background = None

    while True:
        # 读取视频流
        grabbed, frame_lwp_cv = camera.read()
        # 对帧进行预处理，先转灰度图，再进行高斯滤波。
        # 用高斯滤波进行模糊处理，进行处理的原因：每个输入的视频都会因自然震动、光照变化或者摄像头本身等原因而产生噪声。对噪声进行平滑是为了避免在运动和跟踪时将其检测出来。
        if grabbed:

            gray_lwp_cv = cv2.cvtColor(frame_lwp_cv, cv2.COLOR_BGR2GRAY)
            gray_lwp_cv = cv2.GaussianBlur(gray_lwp_cv, (21, 21), 0)

            # 将第一帧设置为整个输入的背景
            if background is None:
                background = gray_lwp_cv
                continue
            # 对于每个从背景之后读取的帧都会计算其与背景之间的差异，并得到一个差分图（different map）。
            # 还需要应用阈值来得到一幅黑白图像，并通过下面代码来膨胀（dilate）图像，从而对孔（hole）和缺陷（imperfection）进行归一化处理
            diff = cv2.absdiff(background, gray_lwp_cv)
            diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]  # 二值化阈值处理
            diff = cv2.dilate(diff, es, iterations=2)  # 形态学膨胀

            # 显示矩形框
            contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL,
                                                   cv2.CHAIN_APPROX_SIMPLE)  # 该函数计算一幅图像中目标的轮廓
            for c in contours:
                if cv2.contourArea(c) < 1500:  # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
                    continue
                (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
                cv2.rectangle(frame_lwp_cv, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow('contours', frame_lwp_cv)
            cv2.imshow('dis', diff)

            key = cv2.waitKey(5) & 0xFF
            if key == ord('q'):
                print('完成1')
                break
        else:
            print('完成2')
            break

    camera.release()
    cv2.destroyAllWindows()


def calc_time():
    cap = cv2.VideoCapture("10.mp4")  # 参数0表示第一个摄像头
    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 4))
    # 获取视频宽高
    frame_width, frame_height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    background, frame_list, second_list = None, [], [],

    while True:
        grabbed, frame = cap.read()
        if grabbed:
            frame_lwp_cv = np.copy(frame)
            # 遮盖下方时间
            cv2.rectangle(frame_lwp_cv, (0, frame_height - 10), (frame_width, frame_height), (0, 0, 0), 30)
            # 对帧进行预处理，先转灰度图，再进行高斯滤波。
            gray_lwp_cv = cv2.cvtColor(frame_lwp_cv, cv2.COLOR_BGR2GRAY)
            # 用高斯滤波进行模糊处理，进行处理的原因：每个输入的视频都会因自然震动、光照变化或者摄像头本身
            # 等原因而产生噪声。对噪声进行平滑是为了避免在运动和跟踪时将其检测出来。
            gray_lwp_cv = cv2.GaussianBlur(gray_lwp_cv, (21, 21), 0)

            # 将第一帧设置为整个输入的背景
            if background is None:
                background = gray_lwp_cv
                continue
            # 对于每个从背景之后读取的帧都会计算其与背景之间的差异，并得到一个差分图（different map）。
            # 还需要应用阈值来得到一幅黑白图像，并通过下面代码来膨胀（dilate）图像，从而对孔（hole）和缺陷（imperfection）进行归一化处理
            diff = cv2.absdiff(background, gray_lwp_cv)
            diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]  # 二值化阈值处理
            diff = cv2.dilate(diff, es, iterations=2)  # 形态学膨胀

            if not np.all(diff == 0):
                frame_list.append(frame)
                second_list.append(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0)
        else:
            break

    cap.release()
    cv2.imwrite("start.jpg", frame_list[0])
    cv2.imwrite("end.jpg", frame_list[-1])
    m_start, m_end = second_list[0], second_list[-1]
    print("第{}秒出现，第{}秒消失，总时长{}秒".format(m_start, m_end, m_end - m_start))


if __name__ == '__main__':
    calc_time()
    pass
