import { ArtistSearchResponse } from "@/schemas/artist";
import { BaseService } from "@/services/baseService";

import createAxiosInstance, { handleMusicApiError } from "../utils";
import { ISearchArtist } from "./serviceInterfaces";

class MusicService extends BaseService implements ISearchArtist {
    search = async (query: string) => {
        return this.axiosInstance
            .get<ArtistSearchResponse>(
                `/?method=artist.search&artist=${query}&api_key=${process.env.NEXT_PUBLIC_LAST_FM_API_KEY}&format=json`
            )
            .then((response) => response.data)
            .catch(handleMusicApiError);
    };
}

const musicService = new MusicService(
    createAxiosInstance("http://ws.audioscrobbler.com/2.0/")
);

export default musicService;
