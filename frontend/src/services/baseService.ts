import { AxiosInstance } from "axios";

export class BaseService {
    protected readonly axiosInstance: AxiosInstance;

    constructor(axiosInstance: AxiosInstance) {
        this.axiosInstance = axiosInstance;
    }
}
