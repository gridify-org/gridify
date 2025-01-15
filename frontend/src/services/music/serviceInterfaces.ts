import { ArtistSearchResponse } from "@/schemas/artist";

export interface ISearchArtist {
    search: (_query: string) => Promise<ArtistSearchResponse>;
}
