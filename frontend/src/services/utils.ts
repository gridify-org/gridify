import axios, { AxiosInstance } from "axios";

export default function createAxiosInstance(baseURL: string): AxiosInstance {
    const client = axios.create({
        baseURL: baseURL,
    });

    return client;
}
