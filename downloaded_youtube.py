import os

def download_youtube_video(url, output_path, video_filename):
    video_output = os.path.join(output_path, f'{video_filename}.mp4')
    
    # 映像のみダウンロード
    os.system(f'yt-dlp --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" -f "bestvideo" {url} -o "{video_output}"')
    return video_output

video_url = input("保存したいYouTubeのURLを入力: ")
output_path = input("保存先のディレクトリパスを入力: ")
video_filename = input("保存するファイル名の指定: ")

if not os.path.exists(output_path):
    os.makedirs(output_path)

video_output = download_youtube_video(video_url, output_path, video_filename)
print(f"映像ダウンロード完了: {video_output}")
