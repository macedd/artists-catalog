import type { AxiosError } from 'axios';
import type { ApiError } from './types';

export function axiosApiError(error: AxiosError): ApiError {
  return {
    message: error.message,
    code: error.code as String,
    status: error.response?.status as Number,
    data: error.response?.data as Object
  };
}

export function apiUrl(uri: String): string {
  const host = (import.meta.env.VITE_API_HOST as String).replace(/\/+$/, '');
  const path = uri.replace(/^\/+/, '').replace(/\/+$/, '');
  return `${host}/api/${path}/`;
}