import axios, { AxiosError,AxiosInstance } from "axios";

export default function createAxiosInstance(baseURL: string): AxiosInstance {
    const client = axios.create({
        baseURL: baseURL,
    });

    return client;
}

export const handleBackendError = (error: AxiosError) => {
    console.error(error);
    throw error;
};

export const handleMusicApiError = (error: AxiosError) => {
    console.error(error);
    throw error;
};
