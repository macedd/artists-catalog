import type { AxiosError } from 'axios';
import type { ApiError } from './types';

export function axiosApiError(error: AxiosError): ApiError {
  return {
    message: error.message,
    code: error.code as string,
    status: error.response?.status as Number,
    data: error.response?.data as Object
  };
}

export function apiUrl(uri: String): string {
  const host = (import.meta.env.VITE_API_HOST as String).replace(/\/+$/, '');
  const path = uri.replace(/^\/+/, '').replace(/\/+$/, '');
  return `${host}/api/${path}/`;
}

// from silent-box
export const isLocalVideo = (itemSrc: string): boolean => {
  const supportedVideoFormats: string[] = [
    '.mp4', '.ogg', '.webm', '.mov', '.flv', '.wmv', '.mkv'
  ]
  return supportedVideoFormats.some(service => {
    return itemSrc.toLowerCase().includes(service)
  })
}

// from: https://stackoverflow.com/a/63474748/667927
function getVideoCover(file: string, seekTo = 0.0): Promise<string | null> {
  console.log("getting video cover for file: ", file);
  return new Promise((resolve, reject) => {
      // load the file to a video player
      const videoPlayer = document.createElement('video');
      videoPlayer.setAttribute('src', file);
      videoPlayer.load();
      videoPlayer.addEventListener('error', (ex) => {
          reject("error when loading video file: " + ex);
      });
      // load metadata of the video to get video duration and dimensions
      videoPlayer.addEventListener('loadedmetadata', () => {
          // seek to user defined timestamp (in seconds) if possible
          if (videoPlayer.duration < seekTo) {
              reject("video is too short.");
              return;
          }
          // delay seeking or else 'seeked' event won't fire on Safari
          setTimeout(() => {
            videoPlayer.currentTime = seekTo;
          }, 200);
          setTimeout(() => {
            reject('timeout');
          }, 2000);
          // extract video thumbnail once seeking is complete
          videoPlayer.addEventListener('seeked', () => {
              console.log('video is now paused at %ss.', seekTo);
              // define a canvas to have the same dimension as the video
              const canvas = document.createElement("canvas");
              canvas.width = videoPlayer.videoWidth;
              canvas.height = videoPlayer.videoHeight;
              // draw the video frame to canvas
              const ctx = canvas.getContext("2d");
              ctx.drawImage(videoPlayer, 0, 0, canvas.width, canvas.height);
              // return the canvas image as a blob
              ctx.canvas.toBlob(
                  blob => {
                      resolve(blob);
                  },
                  "image/jpeg",
                  0.75 /* quality */
              );
          });
      });
  });
}

export async function getCachedVideoCover(fileUrl: string): Promise<string | null | undefined> {
  const key = `videothumbnail_${fileUrl}`;
  try {
    // try from cache
    let thumbnail = localStorage.getItem(key);
    if (thumbnail) {
      return Promise.resolve(thumbnail);
    }

    // render video cover
    thumbnail = await getVideoCover(fileUrl);
    if (thumbnail) {
      localStorage.setItem(key, thumbnail);
      return Promise.resolve(thumbnail);
    }
  } catch {
  }
}
