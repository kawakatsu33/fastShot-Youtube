import cv2
import os

def take_screenshots(video_path, output_base_dir, start_time_str, end_time_str, interval):
    # 動画ファイルの読み込み
    video = cv2.VideoCapture(video_path)

    # 動画のfpsを取得
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # 指定した時間範囲をミリ秒に変換
    start_time = time_to_seconds(start_time_str) * 1000
    end_time = time_to_seconds(end_time_str) * 1000

    # 現在の時間を指定した開始時間に設定
    current_time = start_time

    # フォルダ名
    video_filename = os.path.basename(video_path).split('.')[0]
    folder_name = f"{video_filename}_{start_time_str.replace(':', '-')}_to_{end_time_str.replace(':', '-')}"
    output_dir = os.path.join(output_base_dir, folder_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    while current_time <= end_time:
        # 指定した時間にフレームを移動
        video.set(cv2.CAP_PROP_POS_MSEC, current_time)
        ret, frame = video.read()
        if not ret:
            break

        # スクリーンショットの保存処理
        screenshot_path = os.path.join(output_dir, f'screenshot_{int(current_time / 1000)}_{int((current_time % 1000) / 10)}.png')
        cv2.imwrite(screenshot_path, frame)
        print(f'ScreenShot完了: {screenshot_path}')
        current_time += interval

    video.release()

def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

if __name__ == "__main__":
    video_path = input("動画ファイルのパスを入力: ")
    output_base_dir = input("スクリーンショットの保存先ディレクトリパスを入力: ")
    start_time_str = input("開始時間を入力し<分:秒>（例|0:00）: ")
    end_time_str = input("終了時間を入力<分:秒>（例|1:30）: ")

    # インターバルの入力（秒単位でミリ秒に変換）
    interval_seconds = float(input("スクリーンショット間隔をミリ秒単位で入力（例|0.5 = 500ミリ秒）: "))
    interval = int(interval_seconds * 1000)

    take_screenshots(video_path, output_base_dir, start_time_str, end_time_str, interval)
