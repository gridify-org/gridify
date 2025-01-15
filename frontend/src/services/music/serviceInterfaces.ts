import { ArtistSearchResponse } from "@/schemas/artist";

export interface ISearchArtist {
    search: (query: string) => Promise<ArtistSearchResponse>;
}
