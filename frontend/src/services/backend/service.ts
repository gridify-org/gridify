import { BaseService } from "@/services/baseService";
import createAxiosInstance from "../utils";

class BackendService extends BaseService {}

const backendService = new BackendService(
    createAxiosInstance(process.env.NEXT_PUBLIC_BACKEND_URL!)
);

export default backendService;
