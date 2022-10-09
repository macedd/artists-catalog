import type { AxiosError } from 'axios';

export function axiosErrorObject(error: AxiosError) {
  return {
    message: error.message,
    code: error.code,
    status: error.response?.status,
    data: error.response?.data
  };
}