import { BaseService } from "@/services/baseService";
import createAxiosInstance from "../utils";

class LastFMService extends BaseService {}

const lastFMService = new LastFMService(
    createAxiosInstance("http://ws.audioscrobbler.com/2.0/")
);

export default lastFMService;
